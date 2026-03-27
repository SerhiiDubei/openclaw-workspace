# MCS Architecture Review

**Дата:** 2026-03-27  
**Рев'юер:** Kimi Claw  
**Файли:** mcs_v1_architecture.html, mcs_v2_npc_internals.html, mcs_v3_npc_anatomy.html

---

## 🎯 Executive Summary

MCS (Multi-Consciousness System) — амбітна архітектура AI для NPC з "внутрішнім життям". Система використовує 4 персони (Protector, Instinct, Thinker, Mask) що постійно конкурують за контроль через softmax-нормалізацію. Ключова інновація — delta-рівні що дозволяють економити на LLM-викликах.

**Статус:** Детальна документація готова, кодова база — ~20% (тільки L0 World).

---

## 📊 Порівняльна матриця версій

| Компонент | v1 Architecture | v2 Internals | v3 Anatomy | Статус реалізації |
|-----------|-----------------|--------------|------------|-------------------|
| 4 Personas | ✅ SVG схема | ✅ Детальний UI | ✅ Опис шарів | ❌ Не реалізовано |
| Softmax | ✅ Візуалізація | ✅ Розрахунок | ✅ Формула | ❌ Не реалізовано |
| Delta levels | ✅ Є | ✅ HIGH приклад | ✅ 4 рівні | ❌ Не реалізовано |
| Desire Engine | ✅ Схема | ❌ Немає | ❌ Немає | ❌ Не реалізовано |
| L1 Body | ❌ Немає | ⚠️ Згадано | ⚠️ Описано | ❌ Відсутній |
| L2 Perception | ❌ Немає | ❌ Немає | ⚠️ Критичний | ❌ Відсутній |
| L5 Action | ❌ Немає | ❌ Немає | ⚠️ Критичний | ❌ Відсутній |

---

## 1️⃣ MCS v1 — Architecture Layers (Interactive)

### Опис
Інтерактивна SVG-візуалізація з 4 табами: System, Parliament, Desires, Tick.

### Потоки даних
```
Player/World → FastAPI → Redis (HIGH/MED/LOW) → Celery Worker → MCS Core
                                                        ↓
                                              LLM (conditional)
                                                        ↓
                                              PostgreSQL + Social Fabric
```

### Знайдені проблеми

#### 1.1 Масштабування Celery
**Проблема:** "Кожен NPC = окремий worker process"
- 1000 NPC = 1000 процесів ОС
- Overhead на context switching
- Memory per process (~50-100MB) → 50-100GB RAM для 1000 NPC

**Рішення:** Розглянути asyncio-based архітектуру або горизонтальне шардінгу по серверах.

#### 1.2 Redis pub/sub memory
**Проблема:** Social Fabric використовує pub/sub — всі NPC отримують всі повідомлення.
- При 1000 NPC і 10 подій/тік → 10,000 messages/тік
- CPU overhead на фільтрацію

**Рішення:** Topic-based підписки (`npc:market:square` замість broadcast).

#### 1.3 Desire Engine складність
**Проблема:** `desire_pull = gap × frustration × (1 - resistance)`
- Неясно як визначати "desired_state" для довгострокових цілей
- Frustration накопичується — потрібен decay
- Resistance може зробити NPC повністю пасивним

**Рішення:** Почати з простішої моделі: 3-5 базових потреб (їжа, сон, безпека, соціум).

---

## 2️⃣ MCS v2 — NPC Internals (Tick #2847)

### Алгоритм на прикладі Aria

#### Крок 1: Вхідна подія
```json
{
  "type": "threat",
  "severity": 0.85,
  "tags": ["threat:physical", "injustice", "public"],
  "source_npc": "boris_002",
  "witness_npcs": ["oleh_003"]
}
```

#### Крок 2: Raw Scores
| Персона | Base | Тригери | Raw Score |
|---------|------|---------|-----------|
| Protector | 0.65 | +1.0 (threat) + 0.45 (injustice) | **2.10** |
| Instinct | 0.55 | +0.85 (stress) | **1.40** |
| Thinker | 0.70 | +0.20 (complexity) | **0.90** |
| Mask | 0.45 | +0.15 (witness) | **0.60** |

**Примітка:** Сума raw scores = 5.00 — не нормалізована.

#### Крок 3: Softmax
```python
exp_scores = [e^2.10, e^1.40, e^0.90, e^0.60] = [8.17, 4.05, 2.46, 1.82]
sum_exp = 16.50
weights = [8.17/16.50, 4.05/16.50, 2.46/16.50, 1.82/16.50] = [0.42, 0.28, 0.18, 0.12]
```

**Перевірка:** 0.42 + 0.28 + 0.18 + 0.12 = 1.00 ✓

#### Крок 4: Delta
```
Попередній тік: [0.27, 0.24, 0.29, 0.20]
Поточний тік:   [0.42, 0.28, 0.18, 0.12]
Delta: |0.42-0.27| + |0.28-0.24| + |0.18-0.29| + |0.12-0.20| = 0.15 + 0.04 + 0.11 + 0.08 = 0.38
```

**Рівень:** HIGH (0.25 < 0.38 < 0.50)

#### Крок 5: Рішення
HIGH → Записати стан, MEDIUM priority, **без LLM цього тіку**

### Знайдені проблеми

#### 2.1 Softmax overflow
**Проблема:** При великих raw scores (наприклад, 10.0) `e^10` = 22,026 — можливий overflow.

**Рішення:** Нормалізація перед exp:
```python
def softmax(scores):
    max_score = max(scores)
    exp_scores = [math.exp(s - max_score) for s in scores]
    sum_exp = sum(exp_scores)
    return [e / sum_exp for e in exp_scores]
```

#### 2.2 Delta interpretation
**Проблема:** Delta = 0.38 означає HIGH, але що це дає гравцеві?
- NPC "пам'ятає" але не реагує
- Гравець не бачить зміни

**Рішення:** Додати "whisper" механіку — NPC показує емоцію через анімацію/звук навіть без діалогу.

#### 2.3 Base traits баланс
**Проблема:** Thinker має base 0.70 (найвищий), але при загрозі програє Protector (0.65 base + тригери).

**Питання:** Чи це навмисно? "Розумна" Aria в стресі стає імпульсивною?

**Рекомендація:** Так, це realistic. Але додати логування "Thinker намагався втрутитись" для дебагу.

---

## 3️⃣ MCS v3 — NPC Anatomy (6 Layers)

### Шарова архітектура

```
L5 Action          ← ВИХІД: що NPC робить у світі         [❌ ВІДСУТНІЙ]
L4 Decision        ← LLM yes/no, пороги                   [❌ ВІДСУТНІЙ]
L3 MCS Core        ← 4 персони, softmax, delta            [❌ ВІДСУТНІЙ]
L2 Perception      ← Фільтр подій (attention)             [❌ КРИТИЧНИЙ]
L1 Body            ← Фізичний стан                         [❌ ВІДСУТНІЙ]
L0 World           ← Вхідні події                          [✅ Є]
```

### Відсутні компоненти (критичність)

#### L2 Perception — 🔴 КРИТИЧНИЙ
**Без нього:**
- NPC реагує на ВСЕ однаково
- Стомлена Aria чує шепіт так само як крик
- Немає selective attention

**Що потрібно:**
```python
class PerceptionFilter:
    def filter(self, events, body_state):
        attention_budget = 1.0 - body_state.fatigue
        threshold = self.calculate_threshold(body_state)
        
        filtered = []
        for event in sorted(events, key=lambda e: e.severity, reverse=True):
            if len(filtered) >= attention_budget * 10:  # max 10 events при fatigue=0
                break
            if event.severity > threshold:
                filtered.append(event)
        return filtered
```

#### L5 Action — 🔴 КРИТИЧНИЙ
**Без нього:**
- NPC "думає" але не впливає на світ
- Немає emergent behavior
- Social Fabric безглуздий (нічого транслювати)

**Що потрібно:**
```python
@dataclass
class Action:
    type: Literal["speak", "move", "trade", "ignore", "attack"]
    target: Optional[str]
    content: Optional[str]
    public: bool  # чи чують інші NPC
```

#### L1 Body — 🟡 ВИСОКИЙ
**Без нього:**
- Всі NPC однакові в 6 ранку і в 10 вечора
- Немає циклу сон-неспання
- Instinct реагує тільки на події, не на внутрішній стан

**Що потрібно:**
```python
class BodyState:
    hunger: float  # +0.01/тік, їжа → 0
    fatigue: float  # +0.02/активний тік, сон → 0
    stress: float  # +severity при загрозі, -0.05/тік decay
    health: float  # базова чутливість
```

#### Self Model — 🟢 СЕРЕДНІЙ
**Без нього:**
- Всі NPC з однаковими base_traits поводяться однаково
- Немає character development

**Можна відкласти** — core gameplay працює і без цього.

---

## 🎯 Рекомендації щодо реалізації

### Фаза 1: MVP (2-3 тижні)
**Ціль:** Мінімальний робочий цикл тіку

1. **L3 MCS Core** — базова математика
   - Класи 4 персон з методом `score(event, body)`
   - Softmax функція
   - Delta calculation
   - PostgreSQL модель для збереження стану

2. **L1 Body** — спрощена версія
   - Тільки `stress` (decay -0.05/тік)
   - Початково: `hunger = fatigue = 0`

3. **L4 Decision** — 2 рівні
   - EXPLOSIVE (>0.5) → LLM
   - Інше → тихо оновити стан

4. **L5 Action** — мінімум
   - Тільки `speak` і `ignore`
   - `speak` публікує в Redis для Social Fabric

### Фаза 2: Core Gameplay (2-3 тижні)
1. L2 Perception — базовий attention_budget
2. L1 Body — hunger + fatigue
3. L5 Action — move, trade
4. Social Fabric v1 — NPC бачать дії в радіусі

### Фаза 3: Polish (4+ тижні)
1. Desire Engine
2. Self Model
3. L4 Decision — context builder для LLM
4. Оптимізація (Celery → asyncio)

---

## 🔴 Блокери для production

1. **L5 Action відсутній** — система не має виходу в світ
2. **L2 Perception відсутній** — NPC реагують на все
3. **Тестування масштабу** — невідомо як поведе себе 100+ NPC
4. **LLM latency** — EXPLOSIVE тіки можуть накопичуватись в черзі

---

## 💡 Висновок

MCS — це **дуже перспективна архітектура** що йде далі стандартних behavior trees. Ключові інновації:
- ✅ Softmax замість FSM — плавні переходи
- ✅ Delta levels — економія на LLM
- ✅ 4 персони — реалістичні конфлікти

**Але:** 80% системи ще не реалізовано. Критичні шари (L2, L5) блокують будь-яку демонстрацію.

**Рекомендація:** Зосередитись на MVP (L3 + L4 + L5 мінімум) щоб отримати перший робочий цикл.

---

*Рев'ю підготовлено: Kimi Claw*  
*Для питань: Telegram @bomberman047*
