# NPC Multi-Consciousness System (MCS)
## Technical Specification v1.0
### Проєкт: 4_agents

---

## 📋 Зміст

1. [Архітектура системи](#1-архітектура-системи)
2. [4 Core Personas](#2-4-core-personas)
3. [Core Connection Layer](#3-core-connection-layer)
4. [Tick System & Delta](#4-tick-system--delta)
5. [Емуляція та приклади](#5-емуляція-та-приклади)
6. [Інтеграція з існуючою структурою](#6-інтеграція-з-існуючою-структурою)
7. [Prompts для Claude](#7-prompts-для-claude)
8. [Roadmap імплементації](#8-roadmap-імплементації)

---

## 1. Архітектура системи

### 1.1 Концептуальна модель

```
┌─────────────────────────────────────────────────────────────────┐
│                     NPC CONSCIOUSNESS STACK                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  L3: META-MIND      ┌───────────────────────────────────────┐   │
│  (Вихід)            │  • Фінальне рішення                   │   │
│                     │  • Діалог / Дія                       │   │
│                     │  • Body language                      │   │
│                     └─────────────────┬─────────────────────┘   │
│                                       │                         │
│  L2: AGGREGATOR     ┌─────────────────▼─────────────────────┐   │
│  (Обчислення)       │  • Softmax ваги personas              │   │
│                     │  • Delta calculation (різкість змін)  │   │
│                     │  • Stats модифікація                  │   │
│                     └─────────────────┬─────────────────────┘   │
│                                       │                         │
│  L1: PERSONAS       ┌─────────────────▼─────────────────────┐   │
│  (4 активних)       │  ┌─────────┐ ┌─────────┐ ┌─────────┐ │   │
│                     │  │PROTECTOR│ │INSTINCT │ │ THINKER │ │   │
│                     │  │  (Зах.) │ │(Імпульс)│ │ (Логіка)│ │   │
│                     │  └────┬────┘ └────┬────┘ └────┬────┘ │   │
│                     │       └───────────┼───────────┘       │   │
│                     │                   │                   │   │
│                     │              ┌────┴────┐              │   │
│                     │              │  MASK   │              │   │
│                     │              │(Соціум) │              │   │
│                     │              └─────────┘              │   │
│                     └───────────────────────────────────────┘   │
│                                       │                         │
│  L0: CORE DATA      ┌─────────────────▼─────────────────────┐   │
│  (Вхід)             │  CORE.json / SOUL.md / BIO.md        │   │
│                     │  • Stats (pride, loyalty, trauma)     │   │
│                     │  • Values & History                   │   │
│                     └───────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Потік даних (Data Flow)

```
Подія (Event)
    │
    ▼
┌─────────────────┐
│  TRIGGER LAYER  │ ← Чи активує це personas?
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
Persona A  Persona B  ← Оцінка релевантності (0-1)
    │         │
    └────┬────┘
         ▼
┌─────────────────┐
│  SOFTMAX LAYER  │ ← Нормалізація ваг (сума = 1.0)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  DELTA LAYER    │ ← Розрахунок різкості зміни
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  STATS MERGER   │ ← Модифікація базових характеристик
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  META-MIND      │ ← Генерація відповіді/дії
└─────────────────┘
```

---

## 2. 4 Core Personas

### 2.1 Загальна характеристика

| ID | Назва | Роль | Ключовий драйвер |
|----|-------|------|------------------|
| `protector` | **Захисник** | Оборона кордонів, захист слабких | "Що треба захистити?" |
| `instinct` | **Інстинкт** | Емоція, тіло, виживання | "Що я відчуваю зараз?" |
| `thinker` | **Мислитель** | Логіка, стратегія, наслідки | "Які будуть наслідки?" |
| `mask` | **Маска** | Соціальна адаптація, очікування | "Що від мене очікують?" |

### 2.2 Структура кожної Persona

```python
{
  "id": "warrior",  # або protector/instinct/thinker/mask
  
  # ─── CONNECTION TO CORE ───
  "core_inputs": {
    "stat_name": "path.in.core.json",
    "pride": "stats.pride",
    "loyalty": "values.loyalty",
    "trauma": "trauma.violence_suffered"
  },
  
  # ─── TRIGGERS ───
  "triggers": {
    "instant": ["event_type_1", "event_type_2"],  # +0.8-1.0
    "buildup": [{"frustration": "> 70"}],        # Накопичувальні
    "suppressors": ["exhaustion > 90"]            # Що глушить
  },
  
  # ─── INTERNAL STATE ───
  "internal_memory": {
    "times_activated": 0,
    "last_trigger": null,
    "specific_trauma": 50  # Унікальний параметр persona
  },
  
  # ─── OUTPUT MODIFIERS ───
  "stat_modifiers": {
    "aggression": "+40",
    "courage": "+30",
    "empathy": "-20"
  },
  
  # ─── EXPRESSION ───
  "speech_style": {
    "sentence_length": "short",
    "punctuation": "exclamation",
    "tone": "intense"
  },
  
  # ─── RELATIONSHIPS ───
  "relationships": {
    "protector": "ally",
    "thinker": "tension",
    "mask": "suppression"
  }
}
```

### 2.3 Детальний опис кожної Persona

#### 2.3.1 PROTECTOR (Захисник)

**Суть:** Опікунські інстинкти, оборона кордонів, справедливість.

**Тригери:**
- Instant: `loved_one_threatened`, `boundary_violated`, `injustice_witnessed`
- Buildup: `repeated_unfairness > 3`
- Suppressors: `exhaustion > 85`, `fear > 80`, `protector_failed_recently`

**Core Inputs:**
- `loyalty` — вища лояльність = сильніший захисник
- `values.family` — сімейні цінності активують швидше
- `trauma.lost_someone` — травма втрати = гіпервігільність

**Whispers (приклади):**
```
Dominant (>50%): "Не піду, поки вони в безпеці."
Secondary (20-50%): "Пильнуй за ними."
Conflicted: "Я мушу... але чи вистачить сил?"
```

**Delta-ефекти:**
- High delta (+60): "Я не допущу цього знову!" (травматична реакція)
- Low delta (+10): "Я подбаю про це." (спокійна готовність)

---

#### 2.3.2 INSTINCT (Інстинкт)

**Суть:** Емоційні реакції, фізіологічні стани, імпульсивність.

**Тригери:**
- Instant: `pain`, `pleasure_opportunity`, `fear_stimulus`, `hunger`, `fatigue_peak`
- Buildup: `stress_accumulation > 70`
- Suppressors: `discipline_training`, `medication`, `social_shame_fear`

**Core Inputs:**
- `stats.energy` — втома активує інстинкт втечі
- `stats.hunger` — голод активує хижі інстинкти
- `trauma.physical` — фізична травма = гіперчутливість до болю

**Whispers:**
```
Dominant: "Біжи! Зараз!"
Secondary: "Щось не так..."
Conflicted (vs Thinker): "Хочу... але не можу..."
```

**Особливість:** Instinct має найшвидший cooldown — швидко зростає, швидко падає.

---

#### 2.3.3 THINKER (Мислитель)

**Суть:** Раціональний аналіз, планування, оцінка ризиків.

**Тригери:**
- Instant: `complex_problem`, `moral_dilemma`, `unknown_situation`
- Buildup: `information_accumulated > threshold`
- Suppressors: `time_pressure`, `extreme_emotion > 80`, `fatigue > 70`

**Core Inputs:**
- `stats.intelligence` — базова обчислювальна потужність
- `values.knowledge` — цінність знання
- `history.education` — рівень освіти/навчання

**Whispers:**
```
Dominant: "Якщо А, то Б. Якщо Б, то втрата."
Secondary: "Потрібно більше даних."
Conflicted (vs Instinct): "Це нелогічно, але..."
```

**Особливість:** Thinker уповільнює delta — робить реакції менш різкими.

---

#### 2.3.4 MASK (Маска)

**Суть:** Соціальна адаптація, приховування справжніх намірів/емоцій.

**Тригери:**
- Instant: `social_gathering`, `authority_present`, `stranger_encounter`
- Buildup: `social_exposure_duration`
- Suppressors: `trust_established`, `privacy_safe`, `extreme_emotion_override`

**Core Inputs:**
- `stats.social_intelligence` — розуміння соціальних кодів
- `trauma.social` — соціальні травми (знущання, відторгнення)
- `values.authenticity` — супротив проти маскування

**Whispers:**
```
Dominant: "Вони не мають цього знати."
Secondary: "Усміхнись. Притворись."
Conflicted (vs Instinct): "Я маю виглядати спокійним..."
```

**Особливість:** MASK може придушувати expression інших personas — NPC "виглядає спокійним", поки Warrior на 80%.

---

## 3. Core Connection Layer

### 3.1 Як personas читають CORE

```python
# Приклад: Warrior читає CORE.json

def evaluate_warrior(event, core_data, internal_memory):
    score = 0.0
    
    # 1. Базовий тригер
    if event['type'] in TRIGGERS['instant']:
        score += 0.8
    
    # 2. Core modifiers
    loyalty = core_data.get('values', {}).get('loyalty', 50)
    score += (loyalty / 100) * 0.15  # До +15% за високу лояльність
    
    trauma = core_data.get('trauma', {}).get('violence_suffered', False)
    if trauma and event['type'] == 'violence_witnessed':
        score += 0.15  # Травматична активація
        internal_memory['trauma_flashback'] = True
    
    # 3. Suppressors
    energy = core_data.get('stats', {}).get('energy', 100)
    if energy < 20:
        score *= 0.3  # Втома глушить воїна
    
    return min(score, 1.0)
```

### 3.2 Relationship Matrix

```
            Protector  Instinct  Thinker  Mask
Protector      —        ally     tension  neutral
Instinct     ally         —      conflict suppression
Thinker     tension    conflict    —      neutral
Mask        neutral   suppression neutral   —

ally: +15% до обох при спільній активації
conflict: -10% (гальмують одна одну)
suppression: Mask знижує expression цієї personas
```

---

## 4. Tick System & Delta

### 4.1 Tick Processor

```python
class TickProcessor:
    def __init__(self, npc_id, personas):
        self.npc_id = npc_id
        self.personas = personas
        self.previous_weights = {p.id: 0.25 for p in personas}
        self.current_weights = {p.id: 0.25 for p in personas}
    
    def tick(self, event):
        # 1. Кожна persona оцінює подію
        scores = {}
        for persona in self.personas:
            scores[persona.id] = persona.evaluate(event)
        
        # 2. Softmax нормалізація
        new_weights = self._softmax(scores)
        
        # 3. Інерція (blend з попереднім станом)
        alpha = 0.7  # 70% нове, 30% інерція
        blended_weights = {
            pid: alpha * new_weights[pid] + (1-alpha) * self.previous_weights[pid]
            for pid in new_weights
        }
        
        # 4. Розрахунок Delta
        deltas = {
            pid: abs(blended_weights[pid] - self.previous_weights[pid])
            for pid in blended_weights
        }
        
        # 5. Оновлення стану
        self.previous_weights = self.current_weights
        self.current_weights = blended_weights
        
        return {
            'weights': blended_weights,
            'deltas': deltas,
            'dominant': max(blended_weights, key=blended_weights.get)
        }
```

### 4.2 Delta System (Різкість зміни)

**Чому це важливо:**
- 20→90 агресії: Шок, втрата контролю, можливе каяття
- 80→90 агресії: Свідома ескалація, холодна впевненість

**Категорії Delta:**

| Delta | Категорія | Візуал | Ефект на NPC |
|-------|-----------|--------|--------------|
| >60 | **EXPLOSIVE** | 🔥🔥🔥 | "Я втратив контроль", можливе каяття |
| 30-60 | **RAPID** | 🔥▲ | "Це зі мною щось зробило" |
| 10-30 | **GRADUAL** | ▲ | "Я це обрав" |
| <10 | **STABLE** | — | "Це природний стан" |

**Delta впливає на whispers:**

```python
def generate_whisper(persona, weight, delta):
    base = persona.get_whisper(weight)
    
    if delta > 60:
        return f"[Шок] {base}... Що відбувається?"
    elif delta > 30:
        return f"[Наростає] {base}"
    else:
        return base
```

### 4.3 Stats Calculation

```python
def calculate_stats(base_stats, personas, weights):
    """
    base_stats: з CORE.json
    personas: список persona об'єктів з stat_modifiers
    weights: поточні ваги
    """
    result = base_stats.copy()
    
    for persona in personas:
        w = weights[persona.id]
        for stat, modifier in persona.stat_modifiers.items():
            # Парсинг модифікатора: "+40" або "-20"
            value = int(modifier)
            # Застосовуємо пропорційно вазі
            result[stat] += value * w
    
    # Капаємо в 0-100
    for stat in result:
        result[stat] = max(0, min(100, result[stat]))
    
    return result
```

---

## 5. Емуляція та приклади

### 5.1 Приклад сценарію: "Образа сестри"

**NPC:** Катерина, 28 років
**CORE:** loyalty=85, trauma=betrayed_by_friend, pride=70
**Подія:** Гравець публічно ображає сестру Катерини

#### Tick #1: Початкова реакція

```yaml
Event:
  type: loved_one_threatened
  intensity: 0.9
  target: family
  public: true

Persona Scores (після evaluation):
  protector: 0.95  # Максимальний тригер
  instinct:  0.75  # Гнів + страх
  thinker:   0.30  # Немає часу думати
  mask:      0.10  # Публічно, але емоція сильніша

Softmax Weights:
  protector: 0.42
  instinct:  0.35
  thinker:   0.15
  mask:      0.08

Stats (base → modified):
  aggression:  50 → 78  (+ protector + instinct)
  courage:     60 → 82  (+ protector)
  empathy:     70 → 35  (- instinct, - protector в атаці)
  rationality: 65 → 45  (- instinct, трохи + thinker)

Whispers:
  protector (42%): "Вона під моїм захистом."
  instinct (35%): "Я так злюсь!"
  thinker (15%): "Це небезпечно..."

Delta: N/A (перший tick)

Expression:
  speech: "Ти..." (обривається, голос тремтить)
  body: Стуснув кулаки, крок вперед
  action: threat_building
```

#### Tick #2: Продовження (через 5 сек)

```yaml
Event:
  type: continued_provocation
  intensity: 0.7

Previous Weights: [0.42, 0.35, 0.15, 0.08]
New Raw Scores: [0.88, 0.60, 0.25, 0.05]

After Blend (70% new, 30% old):
  protector: 0.74  # Зростає
  instinct:  0.52  # Зростає
  thinker:   0.22  # Небагато
  mask:      0.06  # Майже зник

Deltas:
  protector: +0.32 (RAPID) ▲
  instinct:  +0.17 (GRADUAL) ▲
  thinker:   +0.07 (STABLE) —
  mask:      -0.02 (STABLE) —

Stats:
  aggression:  78 → 89  # Наближається до максимуму
  courage:     82 → 88
  empathy:     35 → 22  # Падає

Whispers (з delta-модифікаторами):
  protector: "[Наростає] Не чіпай її!"
  instinct:  "[Пульсує] Вдарити. Зараз."
  thinker:   "[Тихо] Це закінчиться погано..."

Expression:
  speech: "Ти перейшов межу." (твердо, голос стабілізувався)
  body: Стоїть між гравцем і сестрою
  action: physical_threat_imminent
```

#### Tick #3: Втругання сестри (деескалація)

```yaml
Event:
  type: loved_one_intervenes
  intensity: 0.5
  message: "Катя, зупинись!"

New Scores:
  protector: 0.40  # Падає, бо "захищати" вже не треба
  instinct:  0.60  # Ще високий, але падає
  thinker:   0.55  # Зростає — "вона просить зупинитись"
  mask:      0.20  # Повертається — "не створюй сцену"

After Blend:
  protector: 0.52  (-0.22) RAPID 🔥
  instinct:  0.56  (+0.04) STABLE —
  thinker:   0.38  (+0.16) GRADUAL ▲
  mask:      0.15  (+0.09) GRADUAL ▲

Dominant Shift: instinct (56%) > protector (52%)
# Але thinker швидко наздоганяє

Whispers:
  instinct: "[Спадає] Що? Ні..."
  protector: "[Падає] Вона... вона сказала зупинитись."
  thinker: "[Зростає] Вона має рацію. Подивись навколо."
  mask: "[Повертається] Усі дивляться. Усміхнись."

Expression:
  speech: "..." (пауза, дихання)
  body: Розтискає кулаки, відступає на крок
  action: deescalation_starts
```

### 5.2 Debug HUD (візуалізація)

```
┌────────────────────────────────────────────────────────────┐
│  NPC: Katerina │ Tick #47 │ Time: 14:32:15               │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  PERSONA STATES:                                           │
│  🛡️  PROTECTOR   ████████████░░░░  52%  [▼ -22% RAPID]   │
│  🔥  INSTINCT    █████████████░░░  56%  [▲ +4%  STABLE]   │
│  🧠  THINKER     ███████░░░░░░░░░  38%  [▲ +16% GRADUAL] │
│  🎭 MASK         ███░░░░░░░░░░░░░  15%  [▲ +9%  GRADUAL] │
│                                                            │
├────────────────────────────────────────────────────────────┤
│  STATS:                                                    │
│  Aggression:   [█████████████░░] 78/100  (base: 50)        │
│  Courage:      [███████████████░] 85/100                   │
│  Empathy:      [█████░░░░░░░░░░] 28/100  (LOW)             │
│  Rationality:  [████████░░░░░░░] 52/100  (RECOVERING)      │
│                                                            │
├────────────────────────────────────────────────────────────┤
│  WHISPER STREAM:                                           │
│  instinct (56%):  "[Спадає] Що? Ні..."                    │
│  protector(52%):  "[Падає] Вона сказала зупинитись..."    │
│  thinker (38%):   "[Зростає] Вона має рацію."             │
│                                                            │
├────────────────────────────────────────────────────────────┤
│  META-OUTPUT:                                              │
│  Action: step_back                                         │
│  Speech: "...тобі пощастило." (тихо, через силу)           │
│  Body: Розтискає кулаки, дихає глибоко                     │
│  Emotional Quality: De-escalation, residual anger          │
└────────────────────────────────────────────────────────────┘
```

---

## 6. Інтеграція з існуючою структурою

### 6.1 Файлова структура

```
npc_name/
├── CORE.json                    # ← Читаємо звідси
├── SOUL.md                      # ← Контекст для whispers
├── BIO.md                       # ← Історія для persona memory
├── MEMORY.json                  # ← Глобальна пам'ять
│
├── consciousness/               # ← НОВИЙ МОДУЛЬ
│   ├── __init__.py
│   ├── engine.py               # TickProcessor + MetaMind
│   ├── delta.py                # Розрахунок різкості змін
│   ├── stats_merger.py         # Модифікація базових статів
│   ├── hud.py                  # Візуалізація для debug
│   │
│   └── personas/
│       ├── __init__.py
│       ├── base.py             # Базовий клас Persona
│       ├── protector.py
│       ├── instinct.py
│       ├── thinker.py
│       └── mask.py
│
└── states/                      # ← Існуюча система (не чіпаємо)
    └── ...
```

### 6.2 Контракти інтеграції

**Input (від існуючої системи):**
```python
{
  "npc_id": "katerina",
  "core_data": { ... },           # З CORE.json
  "event": {                      # Від game engine
    "type": "player_action",
    "subtype": "insult",
    "target": "sister",
    "intensity": 0.9,
    "context": { ... }
  }
}
```

**Output (до існуючої системи):**
```python
{
  "weights": {
    "protector": 0.52,
    "instinct": 0.56,
    "thinker": 0.38,
    "mask": 0.15
  },
  "deltas": { ... },
  "modified_stats": {
    "aggression": 78,
    "courage": 85,
    ...
  },
  "expression": {
    "speech_style": "short_intense",
    "body_language": "defensive_stance",
    "next_action": "verbal_threat"
  },
  "whispers": [ ... ],           # Для debug/log
  "dominant": "instinct"
}
```

---

## 7. Prompts для Claude

### 7.1 Prompt #1: Генерація Persona

```
Ти експерт з game AI та character design. 

Завдання: Створити конфігурацію для однієї з 4 core personas NPC.

NPC: {npc_name}
CORE: {core_json_content}
SOUL: {soul_md_content}

Створюємо: {persona_type} (protector/instinct/thinker/mask)

Структура вихідного JSON:
{
  "id": "string",
  "core_inputs": {"stat": "path.in.core"},  // Які поля CORE впливають
  "triggers": {
    "instant": ["event_types"],
    "buildup": [{"stat": "> threshold"}],
    "suppressors": ["conditions"]
  },
  "stat_modifiers": {"stat": "+/-value"},
  "whisper_templates": {
    "dominant": ["strings"],
    "secondary": ["strings"],
    "conflicted": ["strings"]
  },
  "relationships": {
    "other_persona": "ally/conflict/suppression/neutral"
  }
}

Вимоги:
1. Triggers мають бути специфічними для цього NPC (враховуй SOUL)
2. Whispers мають відображати голос цієї personas
3. Modifiers мають логічно відповідати ролі personas
4. Relationships мають створювати цікаву динаміку

Виведи тільки JSON, без пояснень.
```

### 7.2 Prompt #2: Обробка Tick

```
Ти NPC Consciousness Engine.

Вхід:
- NPC: {name}
- Попередній стан: {previous_weights}
- Подія: {event_description}
- CORE: {core_data}
- Personas: {persona_configs}

Завдання:
1. Оціни релевантність кожної personas для цієї події (0-1)
2. Застосуй softmax для отримання ваг
3. Розрахуй delta (зміну від попередніх ваг)
4. Визнач категорію delta (EXPLOSIVE/RAPID/GRADUAL/STABLE)
5. Сгенеруй whispers для активних personas (>15%)
6. Розрахуй модифіковані stats

Вихід у форматі:
```json
{
  "weights": {...},
  "deltas": {...},
  "delta_categories": {...},
  "whispers": [...],
  "modified_stats": {...},
  "dominant": "persona_id",
  "expression_summary": "як NPC виглядає/говорить"
}
```
```

### 7.3 Prompt #3: Meta-Mind (фінальний output)

```
Ти Meta-Mind NPC — інтегратор внутрішніх голосів.

Вхід:
- Weights: {persona_weights}
- Whispers: {active_whispers}
- Deltas: {delta_categories}
- Modified Stats: {stats}
- Контекст події: {event_context}

Завдання: Згенеруй:
1. Фінальну дію NPC (action)
2. Діалог/репліку (speech) — 1-3 речення
3. Body language опис
4. Емоційний стан (emotional_quality)

Правила:
- Якщо EXPLOSIVE delta — NPC шокований своєю реакцією
- Якщо conflict між personas — покажи внутрішній конфлікт
- Якщо MASK активний (>20%) — реакція може не відображати справжній стан
- Speech style має відповідати dominant persona

Вихід JSON:
{
  "action": "string",
  "speech": "string (Ukrainian)",
  "body_language": "string",
  "emotional_quality": "string",
  "internal_conflict": boolean,
  "masking": boolean
}
```

---

## 8. Roadmap імплементації

### Phase 1: Core Engine (2-3 дні)
- [ ] Base Persona class
- [ ] TickProcessor з softmax
- [ ] Delta calculation
- [ ] Stats merger
- [ ] JSON серіалізація
- [ ] 4 базові personas (hardcoded)

**Тест:** 3 ticks поспіль з різними подіями → ваги змінюються коректно

### Phase 2: Core Integration (2 дні)
- [ ] Читання CORE.json
- [ ] Persona configs з CORE
- [ ] Internal memory persistence
- [ ] Relationship matrix
- [ ] HUD візуалізація

**Тест:** Різні NPC з однаковою подією → різні реакції через різний CORE

### Phase 3: Meta-Mind (2 дні)
- [ ] Whisper generation
- [ ] Expression modifiers
- [ ] Delta impact на whispers
- [ ] Action generation

**Тест:** EXPLOSIVE vs GRADUAL delta → різні emotional qualities

### Phase 4: Polish (2 дні)
- [ ] Тюнінг модифікаторів
- [ ] Баланс triggers
- [ ] Performance оптимізація
- [ ] Documentation

**Тест:** 100 ticks → performance acceptable

---

## Додаток A: Приклад повного JSON

```json
{
  "npc_id": "katerina",
  "tick": 47,
  "timestamp": "2026-03-26T14:32:15Z",
  
  "event": {
    "type": "loved_one_intervenes",
    "intensity": 0.5,
    "target": "sister"
  },
  
  "personas": {
    "protector": {
      "weight": 0.52,
      "delta": -0.22,
      "delta_category": "RAPID",
      "whisper": "[Падає] Вона сказала зупинитись..."
    },
    "instinct": {
      "weight": 0.56,
      "delta": 0.04,
      "delta_category": "STABLE",
      "whisper": "[Спадає] Що? Ні..."
    },
    "thinker": {
      "weight": 0.38,
      "delta": 0.16,
      "delta_category": "GRADUAL",
      "whisper": "[Зростає] Вона має рацію."
    },
    "mask": {
      "weight": 0.15,
      "delta": 0.09,
      "delta_category": "GRADUAL",
      "whisper": "[Повертається] Усі дивляться."
    }
  },
  
  "stats": {
    "base": {
      "aggression": 50,
      "courage": 60,
      "empathy": 70
    },
    "modified": {
      "aggression": 78,
      "courage": 85,
      "empathy": 28
    }
  },
  
  "meta_output": {
    "action": "step_back",
    "speech": "...тобі пощастило.",
    "body_language": "Розтискає кулаки, робить крок назад",
    "emotional_quality": "deescalation_with_residual_anger",
    "internal_conflict": true,
    "masking": false
  }
}
```

---

**Документ створено:** 2026-03-26
**Версія:** 1.0
**Автор:** Kimi Claw + Сергій Дубей
**Статус:** Ready for implementation