# 4_agents × TIMER: Merge Concept — "The Convergence"

> **Концепція:** Агенти розкидані по локаціях, таймер веде до фінальної зустрічі  
> **Ресурс:** Час (з TIMER) + Очки (з 4_agents)  
> **Механіка:** Локації + Переміщення + Коди-дії  

---

## Частина 1: Філософія Мерджу

### Що беремо з TIMER:
- ⏱️ **Серверний таймер** — єдине джерело правди
- 🎫 **Одноразові коди** — дії як "коди" з ефектами
- 🏠 **Лобі/Кімнати** — сесії гри
- ⚡ **Realtime** — Supabase для миттєвих оновлень
- 💀 **Вибуття** — час = 0 → агент "вмирає"

### Що беремо з 4_agents:
- 🧠 **Персонажі** — CORE, SOUL, MEMORY
- 🤝 **Соціальні дії** — Trust, Betray, Influence
- 🎲 **Ймовірнісна механіка** — d20, outcome tables
- 📊 **Payoff matrix** — розрахунок очок
- 🧬 **Розвиток** — cross-game memory

### Нове — Локації:
- 🗺️ **Ізометрична карта** — агенти фізично переміщаються
- 🏛️ **Точки інтересу** — місця для зустрічей/дій
- ⏳ **Сценарій зведення** — таймер веде до "The Convergence"

---

## Частина 2: Архітектура Локацій

### Карта — Гекси (Hex Grid)

```
         [Ліс]────[Річка]
        /    \      /
    [Печера] [Центр] [Ферма]
        \      /      \
         [Руїни]────[Озеро]
```

Кожен гекс має:
- **Тип:** Безпечний / Небезпечний / Ресурсний
- **Вмістість:** max N агентів одночасно
- **Події:** локальні події (шторм, скарб, засада)

### Стан Агента (розширений)

```json
{
  "agent_id": "marta",
  "location": "forest_hex_3",
  "time_remaining": 1200,
  "points": 150,
  "energy": 80,
  "inventory": ["code_steal_001", "code_heal_002"],
  "visible_agents": ["pavlo", "void"],
  "status": "hidden" // visible, hidden, trapped
}
```

---

## Частина 3: Таймер як Сценарій (The Convergence)

### Фази Гри (залежно від часу)

| Час | Фаза | Опис | Механіка |
|-----|------|------|----------|
| **20:00** | Розосередження | Агенти в різних кутках | Кожен в своїй локації, бачить тільки сусідів |
| **15:00** | Перші контакти | Можливі зустрічі | Діапазон бачення +1 гекс |
| **10:00** | 🚨 Convergence Alert | Всі мусить йти до Центру | Штраф за перебування на периферії |
| **5:00** | Final Approach | Центр відкривається | Можливість зустрітися всі разом |
| **0:00** | 💀 Deadline | Хто не в Центрі — вибуває | Фінальний payoff розрахунок |

### Зведення через Карту

```
Фаза 1 (20:00)           Фаза 3 (10:00)           Фаза 5 (0:00)
    
    A    B                    A  B                    
      \  /                      \/                       
       X                        X ← CENTER (відкрито)      [A,B,C,D
      / \                      /\                             всі тут]
     C    D                   C  D
   
   Розкидані             Всі йдуть до центру           Фінальна зустріч
```

---

## Частина 4: Дії як "Коди" (TIMER-style)

### Структура Коду-Дії

```json
{
  "code_id": "act_marta_001",
  "issuer": "marta",
  "category": "INFLUENCE",
  "cost": {
    "time": -30,
    "energy": 20
  },
  "target_location": "forest_hex_3",
  "effect": {
    "type": "persuade",
    "payload": {
      "target_agent": "pavlo",
      "change": "trust +0.2",
      "duration": "2 rounds"
    }
  },
  "conditions": {
    "range": 1,
    "visibility": "line_of_sight",
    "cooldown": 3
  }
}
```

### Генерація Кодів

Агент НЕ просто говорить "я переконую". Він:
1. **Вибирає дію** (Learn/Influence/Alter/Pact)
2. **LLM генерує "код"** — конкретну пропозицію
3. **Система валідує** — чи вистачає ресурсів
4. **Код активується** — ефект застосовується

**Приклад:**
```
Марта хоче: Influence → Павло
LLM генерує код: "Павле, у мене є інформація про Вождя"
Система перевіряє: Марта бачить Павла? Так. Energy ≥ 20? Так.
Код активовано: Павло отримує повідомлення, може відреагувати
```

---

## Частина 5: Переміщення та TU

### Movement System

```
TU на раунд: 6 (як в ACTION_CORE)

Дії:
├── Move (1 TU за гекс) — переміщення
├── Sprint (2 TU) — +1 гекс, але -10 energy  
├── Hide (2 TU) — стати невидимим на 1 раунд
├── Search (1 TU) — сканування сусідніх гексів
│
└── Action (2-3 TU) — Learn/Influence/Alter/Pact
```

### Fog of War

```
Агент бачить:
- Свій гекс: повна інформація
- Сусідні гекси: тип місцевості, чи є хтось (але не хто)
- Далі: невідомо

Розвідка:
- Піднятись на висоту (вежа, пагорб) → бачиш +2 гекси
- Дрон/розвідник (якщо є) → бачиш конкретних агентів
```

---

## Частина 6: Ресурси (Merge TIMER + 4_agents)

### Два Паралельних Ресурси

| Ресурс | З TIMER | З 4_agents | Взаємодія |
|--------|---------|------------|-----------|
| **⏱️ Час** | Серверний таймер | — | Час = 0 → вибуття |
| **💎 Очки** | — | Payoff matrix | Фінальний рейтинг |
| **⚡ Energy** | Нове | Нове | Відновлюється, витрачається на дії |
| **🎫 Коди** | Одноразові | Дії агентів | Коди = "закарбовані дії" |

### Економіка

```
Кожен раунд:
├── Час: -30 секунд (від таймера)
├── Energy: +10 (відновлення)
├── Очки: від Payoff (cooperate/betray)
└── Коди: можливість згенерувати 1 код
```

---

## Частина 7: Сценарії Зведення (Приклади)

### Сценарій A: "Острів"

```
[Північ]     [Схід]      [Південь]     [Захід]
   A            B            C            D
   |            |            |            |
   └────────────┴────[Центр]────┴────────────┘

Фаза 1: Агенти на берегах, між ними вода (треба човен або обхід)
Фаза 2: Відливи — відкриваються проходи
Фаза 3: Цунамі — хто не в Центрі, отримує урон
Фаза 4: Фінал в Центрі
```

### Сценарій B: "Метро"

```
Лінія 1: A ── B ──[HUB]── C ── D
Лінія 2: E ── F ──[HUB]── G ── H

Фаза 1: Поїзди ходять, можна пересісти
Фаза 2: Аварія на Лінії 1 — тільки Лінія 2 працює
Фаза 3: HUB закривається — треба встигнути
Фаза 4: Тунелі як локації для засідок
```

### Сценарій C: "Космічна Станція"

```
[Модуль A]──[Коридор 1]──[Центр]──[Коридор 2]──[Модуль B]
      |                        |
[Модуль C]──[Коридор 3]──[Модуль D]

Фаза 1: Гравці в різних модулях
Фаза 2: Розгерметизація — модулі закриваються
Фаза 3: Тільки Центр з киснем
Фаза 4: Фінал — хто встиг в Центр
```

---

## Частина 8: Технічна Імплементація

### База Даних (Supabase)

```sql
-- Агенти в грі
CREATE TABLE game_agents (
  id uuid PRIMARY KEY,
  game_session_id uuid,
  agent_id text,
  location_hex text,
  time_remaining int,
  points int,
  energy int,
  status text -- active, eliminated, winner
);

-- Гекси карти
CREATE TABLE hex_map (
  hex_id text PRIMARY KEY,
  game_session_id uuid,
  type text, -- forest, river, center, etc.
  capacity int,
  agents_present text[]
);

-- Дії-коди (з TIMER)
CREATE TABLE action_codes (
  code_hash text PRIMARY KEY,
  issuer_id uuid,
  category text,
  target_hex text,
  effect jsonb,
  used boolean DEFAULT false
);

-- Івенти (realtime)
CREATE TABLE game_events (
  id uuid PRIMARY KEY,
  game_session_id uuid,
  agent_id text,
  event_type text, -- move, action, meet
  payload jsonb,
  created_at timestamp
);
```

### API Endpoints

```
POST /game/move          -- переміщення
POST /game/action        -- дія (генерує код)
POST /game/redeem        -- використати код (з TIMER)
GET  /game/state         -- повний стан (location, time, agents)
POST /game/convergence   -- перевірка фази таймера
```

---

## Частина 9: Game Loop (Повний)

```python
def game_loop():
    while time_remaining > 0:
        # 1. Оновлення фази (залежно від часу)
        phase = update_convergence_phase(time_remaining)
        apply_phase_effects(phase)
        
        # 2. Агенти роблять ходи (паралельно)
        for agent in active_agents:
            # Movement phase
            if agent.wants_to_move():
                move_agent(agent, target_hex)
            
            # Action phase (генерує код)
            if agent.wants_to_act():
                code = generate_action_code(agent)
                broadcast_code(code)
            
            # Redeem codes (від TIMER)
            for code in agent.inventory:
                if agent.wants_to_redeem(code):
                    apply_code_effect(code)
        
        # 3. Перевірка зустрічей
        for hex in hex_map:
            if len(hex.agents) > 1:
                trigger_meeting(hex)
        
        # 4. Payoff calculation (для зустрівшихся)
        for meeting in active_meetings:
            calculate_payoff(meeting.agents)
        
        # 5. Оновлення таймера
        time_remaining -= ROUND_DURATION
        
        # 6. Перевірка вибуття (з TIMER)
        check_eliminations()
```

---

## Частина 10: Приклад Гри

### Раунд 5, Час: 12:30

```
📍 Локації:
├── Марта: forest_hex_3 (бачить: ???)
├── Павло: forest_hex_3 (бачить: Марта)
├── Вождь: center_hex (бачить: всіх хто поруч)
└── Сергій: lake_hex (бачить: нікого)

⏱️ Час до Convergence: 2:30
⚡ Energy: Марта 60, Павло 80

🎲 Марта вирішує:
1. Move → center_hex (2 гекси, 2 TU)
2. Action → Influence Павло (2 TU, генерує код)
3. Залишок: 2 TU → Sprint (швидше дійде)

💬 Код згенеровано:
"Павле, я знаю де скарб. Йди зі мною до Центру."

🎯 Павло отримує код, може:
- Прийняти (Trust +0.3, йде з Мартою)
- Відхилити (нічого)
- Використати код проти Марти (Expose: "Марта шукає союзників")
```

---

## Частина 11: Roadmap Мерджу

### Phase 1: Core Integration
- [ ] Додати `location` до агентів
- [ ] Імплементувати таймер (з TIMER)
- [ ] Базова карта (3-5 гексів)

### Phase 2: Movement
- [ ] Move/Sprint дії
- [ ] Fog of War
- [ ] Сценарій "Острів" (MVP)

### Phase 3: Action Codes
- [ ] Генерація кодів з LLM
- [ ] Redeem система (з TIMER)
- [ ] Realtime оновлення

### Phase 4: Convergence
- [ ] Фази зведення
- [ ] Deadline механіка
- [ ] Фінальний payoff

---

*Концепція: "The Convergence"*  
*TIMER × 4_agents Merge*
