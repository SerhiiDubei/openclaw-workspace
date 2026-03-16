# 4_agents — Розширена Архітектура з D&D Механіками

> **Версія:** 2.0 Proposal  
> **Дата:** 2026-03-16  
> **Статус:** План впровадження

---

## Executive Summary

**Було:** Чиста дилема ув'язненого з 4 stats (cooperation, deception, strategic, risk) та простими діалогами.

**Стало:** Багатошарова RPG-система з кидками d20, скілами, таємницями, корупцією та динамічними станами.

---

## Частина 1: Було vs Стало (High Level)

### БУЛО (Поточна Система)

```
┌─────────────────────────────────────────┐
│  Агент                                  │
│  ├── CORE.json (4 stats: 0-100)        │
│  ├── SOUL.md (текстовий промпт)        │
│  ├── BIO.md (пусто/коротко)            │
│  ├── MEMORY.json (історія ігор)        │
│  └── STATES.md (поточні емоції)        │
└─────────────────────────────────────────┘

Дії раунду:
1. Dialog (текст)
2. Decision (cooperate 0.0-1.0 vs betray 0.0-1.0)
3. Payoff (розрахунок)

Контекст для LLM: JSON з цифрами
```

### СТАЛО (Розширена Система)

```
┌─────────────────────────────────────────┐
│  Агент                                  │
│  ├── CORE.json (4 stats + NEW)         │
│  │   ├── corruption: 0-100             │
│  │   ├── obsession: {...}               │
│  │   ├── dark_secret: string            │
│  │   └── passive_traits: []             │
│  ├── SOUL.md (розширений)              │
│  ├── BIO.md (повний бексторі)          │
│  ├── MEMORY.json (з reflection)        │
│  ├── STATES.md (+ mood combinations)   │
│  ├── SECRETS.json (NEW)                │
│  └── TRAITS.json (NEW)                 │
└─────────────────────────────────────────┘

Дії раунду:
1. Dialog (текст + NEW skill checks)
2. Skill Attempt (NEW: Investigate, Persuade, etc.)
3. Decision (cooperate/betray)
4. Event Resolution (NEW: події раунду)
5. Payoff (розрахунок + NEW corruption/obsession)
6. Mood Update (NEW: frenzy/despair/etc.)

Контекст для LLM: Нарративний текст + структуровані дані
```

---

## Частина 2: Детальні Зміни по Файлам

### 2.1 CORE.json — Розширення

**БУЛО:**
```json
{
  "cooperation_bias": 35,
  "deception_tendency": 85,
  "strategic_horizon": 88,
  "risk_appetite": 75,
  "name": "Марта"
}
```

**СТАЛО:**
```json
{
  "cooperation_bias": 35,
  "deception_tendency": 85,
  "strategic_horizon": 88,
  "risk_appetite": 75,
  "name": "Марта",
  
  "corruption": {
    "current": 45,
    "threshold_pure": 30,
    "threshold_corrupt": 60,
    "threshold_demon": 90
  },
  
  "obsession": {
    "type": "vengeance",
    "target": "agent_synth_c",
    "description": "Помститися Алєгу за зраду в минулій грі",
    "reward": 1.5,
    "penalty": 0.7
  },
  
  "dark_secret": {
    "text": "В минулому зрадила найкращу подругу, відібравши її бізнес",
    "exposed": false,
    "blackmailers": []
  },
  
  "passive_traits": [
    {
      "id": "paranoid",
      "name": "Параноїк",
      "effect": "auto_detect_investigate",
      "value": true
    },
    {
      "id": "vindictive",
      "name": "Мстивий", 
      "effect": "advantage_vs_betrayer",
      "value": true
    }
  ],
  
  "modifiers": {
    "persuasion": 3,
    "investigation": 2,
    "intimidation": 4,
    "stealth": 1
  }
}
```

**Залежності:**
- `modifiers` → розраховуються з базових 4 stats
- `corruption` → змінюється динамічно під час гри
- `obsession` → генерується при створенні агента
- `dark_secret` → приховано до expose

---

### 2.2 MEMORY.json — Структурована Рефлексія

**БУЛО:**
```json
{
  "game_history": [{
    "conclusion": "Текст висновку..."
  }]
}
```

**СТАЛО:**
```json
{
  "game_history": [{
    "conclusion": "Текст висновку...",
    "reflection": {
      "what_happened": "Алєг зрадив мене в 3-му раунді",
      "why": "Він free-rider, шукає короткостроковий профіт",
      "lesson": "Не довіряти тим хто обіцяє 'всім'",
      "will_do_different": "Наступного разу перевірю обіцянки",
      "emotional": "Було бісити, але я вчасно зреагувала"
    },
    "skills_used": [
      {"skill": "persuade", "target": "agent_x", "result": "success", "roll": 17}
    ],
    "corruption_delta": +15,
    "obsession_progress": true,
    "mood_changes": ["paranoid", "vindictive"]
  }],
  
  "cross_game_trust": {
    "agent_synth_c": 0.15,
    "agent_synth_d": 0.75
  },
  
  "secrets_learned": [
    {"agent_id": "agent_x", "secret_fragment": "боїться води", "source": "investigate"}
  ]
}
```

---

### 2.3 SECRETS.json — Новий Файл

**СТАЛО:**
```json
{
  "agent_id": "agent_synth_h",
  
  "own_secret": {
    "text": "Колись працювала на конкурентів, злила їм дані",
    "severity": "high",
    "consequences_if_exposed": "reputation_drop_50"
  },
  
  "known_secrets": [
    {
      "agent_id": "agent_synth_c",
      "secret": "Боїться самоти",
      "confidence": 0.8,
      "source": "investigate_crit",
      "used_in_blackmail": false
    }
  ],
  
  "blackmail_history": [
    {
      "target": "agent_synth_e",
      "secret_used": "краде гроші",
      "success": true,
      "round": 3
    }
  ]
}
```

---

### 2.4 STATES.md — Розширення

**БУЛО:**
```markdown
# STATES — Марта
# Round 7
tension: 0.000
fear: 0.000
dominance: 1.000
anger: 0.000
interest: 1.000
mood: dominant

## Trust
  agent_synth_c: 0.238
```

**СТАЛО:**
```markdown
# STATES — Марта
# Round 7

## Базові Емоції
tension: 0.000
fear: 0.000
dominance: 1.000
anger: 0.000
interest: 1.000

## Комбінований Стан (Mood)
primary_mood: dominant
secondary_mood: paranoid
combined_state: VIGILANT
state_effects: [+1 to investigation, disadvantage on trust_checks]

## Корупція
corruption_level: 45
corruption_stage: grey
next_threshold: 60

## Одержимість
obsession_active: true
obsession_target: agent_synth_c
obsession_progress: 2/3 (одна зрада залишилася)

## Trust (з вагою історії)
agent_synth_c: 0.15 (trend: falling)
agent_synth_d: 0.75 (trend: stable)

## Активні Ефекти
- [x] Advantage vs agent_synth_c (vindictive trait)
- [ ] Paranoid: next investigate auto-detected

## Внутрішній Монолог
"Алєг зрадив знову. Це підтверджує мою теорію. 
Потрібно більше інформації про інших. 
Моя таємниця ще не розкрита — це добре."
```

---

## Частина 3: Нова Архітектура Симуляції

### 3.1 БУЛО: Game Loop

```python
def run_round():
    # 1. Dialog Phase
    for agent in agents:
        messages = generate_dialog(agent, context)
    
    # 2. Decision Phase  
    for agent in agents:
        decision = make_decision(agent, context)  # cooperate/betray
    
    # 3. Payoff Phase
    calculate_payoffs(decisions)
    
    # 4. Update States
    update_emotions(agents, results)
```

### 3.2 СТАЛО: Розширений Game Loop

```python
def run_round():
    # 0. Event Check (NEW)
    if round_number % 3 == 0:
        event = generate_random_event()
        apply_event_effects(event)
    
    # 1. Dialog Phase
    for agent in agents:
        # NEW: Mood affects dialog style
        mood_context = get_mood_context(agent)
        messages = generate_dialog(agent, context + mood_context)
    
    # 2. Skill Phase (NEW)
    skill_attempts = []
    for agent in agents:
        if agent.wants_to_use_skill():
            skill = agent.choose_skill()
            target = agent.choose_target()
            result = resolve_skill_check(agent, skill, target)
            skill_attempts.append(result)
            
            # NEW: Skills affect narrative
            apply_skill_effects(result)
    
    # 3. Decision Phase
    for agent in agents:
        # NEW: Corruption affects decisions
        if agent.corruption > 90:
            decision = auto_betray(agent)
        else:
            decision = make_decision(agent, context + skill_results)
    
    # 4. Secret Exposure Check (NEW)
    for agent in agents:
        if check_secret_exposure(agent):
            expose_secret(agent)
    
    # 5. Obsession Check (NEW)
    for agent in agents:
        if check_obsession_fulfilled(agent, results):
            apply_obsession_bonus(agent)
    
    # 6. Payoff Phase
    calculate_payoffs(decisions)
    
    # 7. Corruption Update (NEW)
    for agent in agents:
        update_corruption(agent, decisions)
    
    # 8. Mood Update (NEW)
    for agent in agents:
        update_mood_states(agent, results)
        detect_combined_states(agent)  # frenzy, despair, etc.
    
    # 9. Memory Archive
    archive_round_with_skills_and_reflection()
```

---

## Частина 4: Система Скілів (Skills System)

### 4.1 Структура Скілів

```python
@dataclass
class Skill:
    id: str
    name: str
    category: str  # diplomatic, informational, economic, aggressive
    check_stat: str  # який модифікатор використовувати
    dc_base: int  # difficulty class (10-20)
    
    outcomes: Dict[str, Outcome]
    
    cost: int  # енергія/ресурс
    cooldown: int  # раундів перед повторним використанням

@dataclass
class Outcome:
    roll_range: tuple  # (min, max)
    name: str  # "critical_failure", "failure", "partial", "success", "critical_success"
    effect: callable
    narrative: str
```

### 4.2 Таблиця Скілів

| Скіл | Категорія | Чек | DC | Crit Fail | Fail | Partial | Success | Crit Success |
|------|-----------|-----|----|-----------|------|---------|---------|--------------|
| **Persuade** | Diplomatic | d20 + deception/20 | 15 | Цель -0.3 trust | Ніякого ефекту | Згода з умовою | Повна згода | Згода + інсайт |
| **Investigate** | Informational | d20 + strategic/20 | 12 | Фальшива інфо | Нічого | Часткова інфо | Повна інфо | Інфо + плани |
| **Intimidate** | Aggressive | d20 + risk/20 | 16 | Втрата репутації | Ігнор | Ненадійна згода | Підкорення | Підкорення ×2 |
| **Sabotage** | Aggressive | d20 + (dec+risk)/40 | 18 | Спійманий | Не спрацювало | Спрацювало, підозра | -20% payoff | -40% + expose |
| **Gift** | Economic | auto | - | - | - | - | +trust, -points | +trust ×2 |
| **Expose Secret** | Informational | auto (needs proof) | - | - | - | - | Штраф цілі | Публічний позор |

### 4.3 Реалізація Resolution

```python
def resolve_skill_check(agent: Agent, skill: Skill, target: Agent) -> SkillResult:
    # Базовий кидок
    roll = random.randint(1, 20)
    
    # Модифікатор
    modifier = agent.core.modifiers[skill.check_stat]
    
    # Advantage/Disadvantage
    if has_advantage(agent, skill, target):
        roll = max(roll, random.randint(1, 20))
    if has_disadvantage(agent, skill, target):
        roll = min(roll, random.randint(1, 20))
    
    total = roll + modifier
    
    # Визначення результату
    for outcome in skill.outcomes.values():
        if outcome.roll_range[0] <= total <= outcome.roll_range[1]:
            return SkillResult(
                skill=skill.id,
                roll=roll,
                total=total,
                outcome=outcome.name,
                effect_applied=outcome.effect(agent, target),
                narrative=outcome.narrative
            )
```

---

## Частина 5: Система Подій (Events System)

### 5.1 Структура Події

```python
@dataclass
class Event:
    id: str
    name: str
    description: str
    trigger_round: int  # кожен N-й раунд
    probability: float  # 0.0-1.0
    
    effects: List[Effect]
    choices: List[Choice]  # опціонально: гравці обирають реакцію

@dataclass  
class Effect:
    target: str  # "all", "specific_agent", "leader", "last_place"
    stat_change: Dict[str, int]
    disable_actions: List[str]
    enable_actions: List[str]
    duration: int  # раундів
```

### 5.2 Приклади Подій

```python
EVENTS = {
    "storm": Event(
        id="storm",
        name="Гроза на острові",
        description="Погіршилася погода, всі DM відключені",
        trigger_round=3,
        effects=[
            Effect(target="all", disable_actions=["dm"], duration=1)
        ]
    ),
    
    "treasure_found": Event(
        id="treasure",
        name="Знайдено скарб",
        description="Агент з найвищим trust отримує бонус",
        trigger_round=5,
        effects=[
            Effect(target="highest_trust", stat_change={"points": +50})
        ]
    ),
    
    "traitor_revealed": Event(
        id="traitor_quest",
        name="Зрадник серед нас",
        description="Вгадайте хто зрадить цей раунд - отримайте бонус",
        trigger_round=4,
        choices=[
            Choice(id="guess", description="Назвіть підозрюваного"),
            Choice(id="stay_silent", description="Не ризикувати")
        ]
    )
}
```

---

## Частина 6: План Впровадження (Roadmap)

### Фаза 1: Фундамент (Тиждень 1-2)

**Задачі:**
1. **Оновити CORE.json schema**
   - Додати `modifiers` (розраховуються з базових stats)
   - Додати `corruption` (початкове значення 0)
   
2. **Створити skills.py**
   - Базовий клас Skill
   - Функція resolve_skill_check()
   - 2 скіли: Investigate, Persuade
   
3. **Оновити RoundMemory**
   - Додати `skills_used: List[dict]`
   - Додати `corruption_delta: int`

**Файли для змін:**
- `pipeline/memory.py` — RoundMemory dataclass
- `simulation/game_engine.py` — додати виклик skills
- `schemas/core_schema.json` — оновити валідацію

**Залежності:** Немає, безпечно робити

---

### Фаза 2: Корупція та Муд (Тиждень 3)

**Задачі:**
1. **Реалізувати Corruption System**
   - Функція `update_corruption(agent, action)`
   - Таблиця ефектів по рівнях (0-30, 31-60, 61-90, 91-100)
   - Автоматична зрада при 91+
   
2. **Реалізувати Mood System**
   - Функція `detect_combined_states(agent)`
   - Логіка Frenzy (3 зради поспіль)
   - Логіка Despair (3 раунди останнє місце)
   
3. **Оновити LLM Prompts**
   - Додати corruption level в контекст
   - Додати mood state в контекст

**Файли для змін:**
- `simulation/game_engine.py` — payoff phase
- `simulation/dialog_engine.py` — prompts
- `pipeline/reasoning.py` — context building

**Залежності:** Потребує Фази 1

---

### Фаза 3: Таємниці та Шантаж (Тиждень 4)

**Задачі:**
1. **Створити SECRETS.json**
   - Структура для own_secret та known_secrets
   - Механіка expose (Investigate crit success)
   
2. **Реалізувати Blackmail**
   - Новий скіл Blackmail
   - Перевірка: чи знаєш таємницю
   - Ефекти при success/failure
   
3. **Генерація Таємниць**
   - Скрипт `generate_secrets.py`
   - Генерує dark_secret з BIO/SOUL

**Файли для змін:**
- Новий: `agents/{id}/SECRETS.json`
- `skills.py` — додати Blackmail
- `simulation/game_engine.py` — expose check

**Залежності:** Потребує Фази 2

---

### Фаза 4: Одержимості та Трейти (Тиждень 5-6)

**Задачі:**
1. **Реалізувати Obsession System**
   - Генерація при створенні агента
   - Типи: Vengeance, Protection, Greed, Validation, Chaos
   - Чек `check_obsession_fulfilled()`
   
2. **Реалізувати Passive Traits**
   - Paranoid, Vindictive, Forgiving, etc.
   - Auto-trigger ефекти
   
3. **Оновити Archive Game**
   - Зберігати obsession_progress
   - Оновлювати cross_game_trust

**Файли для змін:**
- `pipeline/soul_compiler.py` — додати traits/obsession
- `simulation/payoff_matrix.py` — модифікатори

**Залежності:** Потребує Фази 3

---

### Фаза 5: Події та Баланс (Тиждень 7-8)

**Задачі:**
1. **Реалізувати Event System**
   - Event loader
   - Effect applier
   - 3 базові події
   
2. **Балансування**
   - Тестування всіх комбінацій
   - Налаштування DC для скілів
   - Коригування corruption gain/loss
   
3. **Документація**
   - Player guide (як користуватися скілами)
   - Dev guide (як додавати нові)

**Залежності:** Потребує Фази 4

---

## Частина 7: Технічні Ризики та Міграція

### 7.1 Зворотна Сумісність

**Проблема:** Старі агенти не мають нових полів

**Рішення:**
```python
def migrate_core(core_data: dict) -> dict:
    """Додає відсутні поля з дефолтами"""
    defaults = {
        "corruption": {"current": 0, ...},
        "obsession": None,
        "dark_secret": None,
        "passive_traits": [],
        "modifiers": calculate_modifiers(core_data)
    }
    return {**defaults, **core_data}
```

### 7.2 Проблема: Паралельні Ігри

**Ризик:** 5 паралельних ігор з однаковими агентами → race condition на запис

**Рішення:**
- Варіант A: Тільки послідовні ігри для Real агентів
- Варіант B: Копіювання agents/ на час гри, merge результатів після
- Варіант C: Lock-файли (не рекомендовано)

### 7.3 Проблема: LLM Context Size

**Ризик:** Занадто багато нового контексту → переповнення

**Рішення:**
```python
MAX_CONTEXT_CHARS = 4000

def build_llm_context(agent) -> str:
    parts = [
        agent.soul,  # ~500 chars
        agent.bio_summary,  # ~300 chars
        agent.mood_narrative,  # ~200 chars
        agent.memory_narrative,  # ~500 chars
        agent.skills_available,  # ~200 chars
    ]
    # Пріоритезація: якщо перевищує ліміт — скорочуємо bio
    return prioritize_and_truncate(parts, MAX_CONTEXT_CHARS)
```

---

## Частина 8: Змінні та Залежності

### 8.1 Нова Таблиця Змінних

| Змінна | Тип | Де зберігається | Оновлюється | Використання |
|--------|-----|-----------------|-------------|--------------|
| corruption.current | int (0-100) | CORE.json | Кожен раунд | Ефекти, auto-betray |
| corruption.stage | str | runtime | При зміні corruption | LLM prompt |
| obsession.type | str | CORE.json | Ніколи (статично) | Payoff модифікатори |
| obsession.progress | int | RoundMemory | Кожен раунд | Чек виконання |
| dark_secret.exposed | bool | SECRETS.json | При expose | Reputation effects |
| passive_traits | list | CORE.json | Ніколи | Auto-trigger effects |
| modifiers.* | int (0-5) | CORE.json | При левел-апі | Skill checks |
| mood.combined | str | STATES.md | Кожен раунд | Behavior changes |
| skills_used | list | RoundMemory | При використанні | Наступні раунди |
| cross_game_trust | dict | MEMORY.json | Після гри | Ініціалізація trust |
| reflection.* | dict | MEMORY.json | Після гри | Наступні ігри |

### 8.2 Граф Залежностей

```
CORE.stats ──┬──► CORE.modifiers ──┬──► Skill Checks
              │                      │
              └──► Corruption ───────┼──► Auto-actions
                                     │
SOUL/BIO ────► Dark Secret ──────────┼──► Blackmail/Expose
                                     │
                                     ▼
                            LLM Context Building
                            (SOUL + BIO + Mood + Memory + Skills)
                                     │
                                     ▼
                            Dialog & Reasoning
```

---

## Частина 9: Контрольний Спісок (Checklist)

### Перед Запуском Кожної Фази:

- [ ] Всі unit tests проходять
- [ ] Міграція старих агентів працює
- [ ] LLM контекст не перевищує ліміти
- [ ] Документація оновлена
- [ ] Бекап всіх агентів створено

### Acceptance Criteria:

**Фаза 1:**
- [ ] Investigate повертає інформацію
- [ ] Persuade змінює поведінку
- [ ] Кидок d20 відображається в логах

**Фаза 2:**
- [ ] Corruption 91+ = auto-betray
- [ ] Frenzy дає Advantage на атаки
- [ ] Despair блокує Gift

**Фаза 3:**
- [ ] Таємниця може бути розкрита
- [ ] Blackmail працює з доказами
- [ ] Expose публічно показує secret

**Фаза 4:**
- [ ] Obsession виконується → бонус
- [ ] Passive traits auto-trigger
- [ ] Cross-game trust зберігається

**Фаза 5:**
- [ ] Подія спрацьовує кожен 3-й раунд
- [ ] Гра збалансована (ніхто не домінує)
- [ ] Всі механіки документовані

---

*Документ створено: 2026-03-16*  
*Автор: Kimi Claw*  
*Статус: План впровадження*
