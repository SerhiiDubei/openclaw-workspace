# ТЗ: Node-Based Architecture Visualization — For Agents / 4_agents

> **Проєкт:** Island Simulation (4_agents) + TimeWars  
> **Мета:** Інтерактивна node-based карта архітектури  
> **Дата ТЗ:** 2026-04-10 (переробка з урахуванням реальних файлів)

---

## 1. Контекст (Що Реально Існує)

### 1.1 Проєкти в Workspace

| Проєкт | Статус | Файл |
|--------|--------|------|
| **Island Simulation** (4_agents) | Основний | TZ.md |
| **TimeWars** | Окремий | TIME_WARS.md |
| **Convergence Merge** | План | CONVERGENCE_MERGE.md |

### 1.2 Реальна Файлова Структура

```
projects/for-agents/
├── TZ.md                      # План розробки UI/UX (9 модулів)
├── ARCHITECTURE_V2.md         # D&D механіки (d20, corruption, secrets)
├── SYSTEMS-ARCHITECTURE.md    # 9 Core Systems
├── ACTION_CORE.md             # 4 категорії дій + TU
├── DODECAHEDRON_SYSTEM.md     # 12 параметрів × 12 під-параметрів
├── ARCHITECTURE_ANALYSIS.md   # Аналіз + покращений пайплайн
├── CONVERGENCE_MERGE.md       # Merge TIMER + 4_agents
├── TIME_WARS.md               # Спрощена концепція з часом
└── node-architecture-TZ.md    # Цей файл
```

---

## 2. Node-Based Карта — Структура

### 2.1 Легенда Фаз (4 кольори)

| Фаза | Колір | Опис | Приклади |
|------|-------|------|----------|
| **Legacy** | 🟤 Сірий | Попередні версії, застарілі підходи | Перші архітектури, прототипи |
| **Planned** | 🔵 Синій | Заплановано, але не реалізовано | Convergence Merge, factions |
| **Current** | 🟢 Зелений | Працює зараз, можливо з "білими дірками" | 9 Core Systems, SOUL generation |
| **Future** | 🟠 Помаранчевий | Планується додати/розширити | Multiplayer, advanced AI |

### 2.2 Типи Нод

```
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   ПРОСТА НОДА   │  │ СКЛАДНА НОДА    │  │   ІНТЕРФЕЙС     │
│                 │  │  (Container)    │  │                 │
│  • Одна функція │  │                 │  │  • API endpoint │
│  • Не має       │  │  • Має внутрішні│  │  • UI компонент │
│    під-нод      │  │    під-ноди     │  │  • Event        │
│                 │  │  • Можна        │  │                 │
│                 │  │    розгорнути   │  │                 │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

### 2.3 Типи Зв'язків (Edges)

| Тип | Стиль | Опис |
|-----|-------|------|
| **Data Flow** | Суцільна стрілка | Дані передаються (JSON, events) |
| **Dependency** | Пунктирна стрілка | Необхідно для роботи |
| **Trigger** | Зигзаг лінія | Подія активує іншу систему |
| **Planned** | Синя пунктирна | Ще не реалізовано |
| **Broken** | Червона з хрестом | Не працює/треба фікс |

---

## 3. Ноди — Детальний Опис

### 3.1 ШАР 1: Entity Layer (Персонажі)

#### SOUL Generation System [Current 🟢]
```yaml
Нода: soul-generation
Тип: Complex
Фаза: Current
Статус: MVP працює

ЩО РОБИТЬ:
  Ритуал ініціалізації — 12 питань → генерація агента

ВНУТРІШНІ ПІД-НОДИ:
  - seed-generator: Генерація початкового сіда
  - question-engine: 7 контекстів × 4 варіанти відповідей
  - soul-compiler: Перетворення відповідей у SOUL.md
  - core-calculator: Розрахунок 4 stats з інтервью
  - bio-expander: Розширення короткого брифу → повна біографія

ВХОДИ:
  - user-input: Короткий бриф (ім'я, вік, трейти)
  - interview-answers: Відповіді на 12 питань

ВИХОДИ:
  - agent-files: SOUL.md, CORE.json, BIO.md, AVATAR.json
  - session-data: session_id, seed

БІЛІ ДІРКИ:
  - BIO.md іноді пустий (треба backfill)
  - AVATAR.json не у всіх агентів
  - Немає reflection в MEMORY після гри
```

#### Agent Storage [Current 🟢]
```yaml
Нода: agent-storage
Тип: Container
Фаза: Current

ЩО ВСЕРЕДИНІ (файли агента):
  agents/{agent_id}/
  ├── BIO.md          # Біографія (розгорнута) [⚠️ часто пустий]
  ├── CORE.json       # 4 stats + corruption + traits
  ├── MEMORY.json     # Історія ігор + рефлексія [⚠️ не повністю]
  ├── SOUL.md         # Персональний промпт LLM
  ├── STATES.md       # Поточний стан (емоції, trust)
  └── AVATAR.json     # Візуальний опис [⚠️ не всі мають]

ЗВ'ЯЗКИ:
  → soul-generation (отримує нові агенти)
  → game-emulation-engine (надає дані агентів)
  → memory-system (оновлює після ігор)
```

---

### 3.2 ШАР 2: Game Layer (Ігровий цикл)

#### Game Emulation Engine [Current 🟢]
```yaml
Нода: game-emulation-engine
Тип: Complex
Фаза: Current
Статус: MVP працює, але базовий

ЩО РОБИТЬ:
  Управління ігровими сесіями — від ініціалізації до фіналу

ВНУТРІШНІ ПІД-НОДИ:
  - lobby-manager: Створення лоббі, вибір 4 агентів
  - round-controller: Управління 10 раундами
  - phase-switcher: Перемикання фаз (dialog → decision → reveal → narrative)
  - timer-manager: Таймери для кожної фази
  - payoff-calculator: Розрахунок очок за дилемою

ФАЗИ РАУНДУ:
  1. Dialog Phase — публічні повідомлення + DM
  2. Decision Phase — Trust/Betray sliders 0.0-1.0
  3. Reveal Phase — розкриття рішень, матриця результатів
  4. Narrative Phase — сторітелінг між раундами

ВХОДИ:
  - selected-agents: 4 агента з agent-storage
  - game-config: кількість раундів (10 за замовчуванням)

ВИХОДИ:
  - game-logs: Історія всіх дій
  - round-results: Результати кожного раунду
  → memory-system (дані для оновлення MEMORY.json)

БІЛІ ДІРКИ:
  - Тільки 1 раунд повністю реалізований (треба 10)
  - DM система базова
  - Немає real-time мультиплеєра
```

#### Action Core System [Planned 🔵 → Partially Current 🟡]
```yaml
Нода: action-core
Тип: Complex
Фаза: Planned (MVP v0.1 → Current)
Статус: Документовано, частково впроваджено

ЩО РОБИТЬ:
  Уніфікована система дій — 4 категорії × TU (Time Units)

4 КАТЕГОРІЇ ДІЙ:
  1. LEARN — Дізнатися інформацію (Investigate, Scan, Observe)
  2. INFLUENCE — Змінити поведінку (Persuade, Intimidate, Seduce)
  3. ALTER — Змінити ресурси/стан (Steal, Sabotage, Gift)
  4. PACT — Створити зобов'язання (Alliance, Promise, Betray)

МЕХАНІКА TU:
  - Кожен агент має 6 TU на раунд
  - Швидкі дії: 1 TU (Погляд, Шепіт)
  - Стандартні: 2 TU (Дослідити, Натиснути)
  - Важкі: 3 TU (Зламати, Переконати, Угода)

OUTCOME TABLES (d20):
  - 1: Крит. провал (5%)
  - 2-5: Провал (20%)
  - 6-14: Частковий (45%)
  - 15-19: Успіх (25%)
  - 20+: Крит. успіх (5%)

ЗВ'ЯЗКИ:
  → game-emulation-engine (дії в фазах гри)
  → dodecahedron-system (модифікатори від параметрів)
  → mathematical-environment (розрахунок ймовірностей)

БІЛІ ДІРКИ:
  - Поки що базові таблиці, без модифікаторів від трейтів
  - Немає підтипів (Seduce, Blackmail, Frame)
```

---

### 3.3 ШАР 3: Advanced Systems (Розширення)

#### Dodecahedron System [Planned 🔵]
```yaml
Нода: dodecahedron-system
Тип: Complex
Фаза: Planned
Статус: Документовано, не впроваджено

ЩО РОБИТЬ:
  12 параметрів × 12 під-параметрів = 144 характеристики

12 ОСНОВНИХ ОСЕЙ (0-100, 50 = баланс):
  1. Fire vs Water — Енергія vs Плинність
  2. Earth vs Air — Матеріальність vs Ідеальність
  3. Light vs Shadow — Відкритість vs Прихованість
  4. Life vs Death — Створення vs Руйнування
  5. Mind vs Heart — Логіка vs Емоції
  6. Order vs Chaos — Контроль vs Свобода
  7. Individual vs Collective — Я vs Ми
  8. Body vs Spirit — Матерія vs Трансценденція
  9. Past vs Future — Традиція vs Прогрес
  10. Strength vs Weakness — Міць vs Вразливість
  11. Submission vs Rebellion — Підпорядкування vs Бунт
  12. Trust vs Suspicion — Довіра vs Підозра

12 ДІЙ ГЕРОЯ:
  Attack, Defend, Heal, Scout, Manipulate, Inspire,
  Create, Destroy, Intimidate, Persuade, Escape, Seduce

ЗВ'ЯЗКИ:
  → action-core (модифікатори для кидків d20)
  → soul-generation (генерація CORE.json)
  → archetype-detection (визначення архетипу)
```

#### Corruption & Obsession System [Planned 🔵]
```yaml
Нода: corruption-obsession
Тип: Container
Фаза: Planned
Статус: Документовано в ARCHITECTURE_V2

ВНУТРІШНІ ПІД-НОДИ:
  - corruption-tracker: 0-100, thresholds (30/60/90)
  - obsession-manager: Типи (Vengeance, Protection, Greed, Validation, Chaos)
  - auto-betray: При corruption > 90 — автоматична зрада
  - mood-detector: Frenzy (3 зради), Despair (3 раунди останній)

СТАДІЇ КОРУПЦІЇ:
  0-30: Чистий (pure)
  31-60: Сірий (grey)
  61-90: Корумпований (corrupt)
  91-100: Демон (demon) → auto-betray

ЗВ'ЯЗКИ:
  → game-emulation-engine (впливає на рішення)
  → agent-storage (зберігається в CORE.json)
```

#### Secrets & Blackmail System [Planned 🔵]
```yaml
Нода: secrets-blackmail
Тип: Complex
Фаза: Planned

ЩО РОБИТЬ:
  Таємниці агентів, шантаж, розкриття

СТРУКТУРА:
  SECRETS.json:
    - own_secret: Текст таємниці, exposed (bool)
    - known_secrets: Що знає про інших
    - blackmail_history: Історія шантажу

МЕХАНІКА EXPOSE:
  - Investigate → crit success → дізнатися секрет
  - Blackmail → ціль виконує вимогу або секрет стає публічним
  - Reputation drop при expose

ЗВ'ЯЗКИ:
  → action-core (Learn → може дати секрет)
  → information-control (що бачать агенти)
```

---

### 3.4 ШАР 4: External Systems (Supabase, Timer, etc.)

#### Supabase Integration [Current 🟢]
```yaml
Нода: supabase-integration
Тип: Interface
Фаза: Current

ТАБЛИЦІ:
  - game_sessions: Активні ігри
  - game_agents: Агенти в грі зі станом
  - time_war_players: Для TimeWars режиму
  - action_codes: Одноразові коди дій
  - game_events: Real-time події

REALTIME:
  - broadcast_state: Оновлення стану гри
  - agent_updates: Зміни позиції/стану агентів
```

#### TimeWars Mode [Future 🟠]
```yaml
Нода: timewars-mode
Тип: Complex
Фаза: Future (поки що окремий документ)

КОНЦЕПЦІЯ:
  - Кожен агент має власний таймер (10-20 хвилин)
  - Час = життя. 0:00 = вибуття
  - Можна додати собі або вкрасти в іншого
  - Кооперація vs Крадіжка (d20 + модифікатори)

ЗВ'ЯЗКИ:
  → game-emulation-engine (альтернативний режим гри)
  → action-core (Steal дія)
```

#### Convergence Merge [Future 🟠]
```yaml
Нода: convergence-merge
Тип: Complex
Фаза: Future

КОНЦЕПЦІЯ (TIMER × 4_agents):
  - Локації (гекси): Ліс, Річка, Печера, Центр
  - Переміщення: Move (1 TU за гекс)
  - Fog of War: Бачиш сусідні гекси, але не хто там
  - The Convergence: Таймер веде до фінальної зустрічі в Центрі
  - Фази зведення: Розосередження → Перші контакти → Final Approach

ЗВ'ЯЗКИ:
  → timewars-mode (таймери)
  → game-emulation-engine (ігровий цикл)
  → action-core (дії в локаціях)
```

---

## 4. Візуалізація Зв'язків

### 4.1 Головний Pipeline (MVP)

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  USER INPUT     │────▶│  SOUL GEN       │────▶│  AGENT STORAGE  │
│  (короткий      │     │  (12 питань)    │     │  (SOUL.md       │
│   бриф)         │     │                 │     │   CORE.json)    │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                                                         ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  MEMORY SYSTEM  │◀────│  GAME EMULATION │◀────│  LOBBY MANAGER  │
│  (оновлення     │     │  ENGINE         │     │  (вибір 4       │
│   після гри)    │     │  (10 раундів)   │     │   агентів)      │
└─────────────────┘     └────────┬────────┘     └─────────────────┘
                                 │
                    ┌────────────┼────────────┐
                    ▼            ▼            ▼
            ┌──────────┐  ┌──────────┐  ┌──────────┐
            │  DIALOG  │  │ DECISION │  │ REVEAL   │
            │  PHASE   │  │  PHASE   │  │  PHASE   │
            └──────────┘  └──────────┘  └──────────┘
```

### 4.2 Розширений Pipeline (з D&D системами)

```
┌─────────────────────────────────────────────────────────────────┐
│                      ADVANCED SYSTEMS                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ Dodecahedron │  │  Corruption  │  │ Secrets & Blackmail  │  │
│  │  (144 stats) │  │  & Obsession │  │                      │  │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘  │
└─────────┼─────────────────┼─────────────────────┼──────────────┘
          │                 │                     │
          └─────────────────┼─────────────────────┘
                            ▼
                  ┌─────────────────┐
                  │  ACTION CORE    │
                  │  (4 категорії   │
                  │   × d20)        │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  GAME EMULATION │
                  │  ENGINE         │
                  └─────────────────┘
```

---

## 5. JSON Формат для Візуалізації

```json
{
  "metadata": {
    "project": "4_agents",
    "version": "2.0",
    "last_updated": "2026-04-10"
  },
  
  "nodes": [
    {
      "id": "soul-generation",
      "type": "complex",
      "name": "SOUL Generation",
      "phase": "current",
      "status": "mvp",
      "description": "Ритуал ініціалізації — 12 питань → генерація агента",
      "internals": [
        {"id": "seed-gen", "name": "Seed Generator"},
        {"id": "question-engine", "name": "Question Engine"},
        {"id": "soul-compiler", "name": "SOUL Compiler"},
        {"id": "core-calc", "name": "CORE Calculator"}
      ],
      "gaps": [
        "BIO.md іноді пустий",
        "Потрібен backfill для старих агентів"
      ],
      "position": {"x": 100, "y": 100}
    },
    {
      "id": "game-emulation",
      "type": "complex",
      "name": "Game Emulation Engine",
      "phase": "current",
      "status": "partial",
      "description": "Управління ігровими сесіями — 10 раундів",
      "internals": [
        {"id": "lobby", "name": "Lobby Manager"},
        {"id": "round-ctrl", "name": "Round Controller"},
        {"id": "phase-switch", "name": "Phase Switcher"},
        {"id": "payoff-calc", "name": "Payoff Calculator"}
      ],
      "gaps": [
        "Тільки 1 раунд повністю реалізований",
        "Немає real-time мультиплеєра"
      ],
      "position": {"x": 400, "y": 300}
    },
    {
      "id": "action-core",
      "type": "complex",
      "name": "Action Core",
      "phase": "planned",
      "status": "documented",
      "description": "4 категорії дій × TU × d20 outcome tables",
      "internals": [
        {"id": "learn", "name": "LEARN (Investigate)"},
        {"id": "influence", "name": "INFLUENCE (Persuade)"},
        {"id": "alter", "name": "ALTER (Steal, Sabotage)"},
        {"id": "pact", "name": "PACT (Alliance)"}
      ],
      "gaps": ["Ще не впроваджено в повному обсязі"],
      "position": {"x": 400, "y": 500}
    },
    {
      "id": "dodecahedron",
      "type": "complex",
      "name": "Dodecahedron System",
      "phase": "planned",
      "status": "documented",
      "description": "12 параметрів × 12 під-параметрів = 144 stats",
      "internals": [
        {"id": "fire-water", "name": "Fire vs Water"},
        {"id": "earth-air", "name": "Earth vs Air"},
        {"id": "light-shadow", "name": "Light vs Shadow"}
      ],
      "gaps": ["Повністю не впроваджено"],
      "position": {"x": 700, "y": 500}
    }
  ],
  
  "edges": [
    {
      "id": "e1",
      "source": "soul-generation",
      "target": "agent-storage",
      "type": "data-flow",
      "label": "agent-files",
      "description": "SOUL.md, CORE.json, BIO.md"
    },
    {
      "id": "e2",
      "source": "agent-storage",
      "target": "lobby-manager",
      "type": "data-flow",
      "label": "4 agents",
      "description": "Вибір агентів для гри"
    },
    {
      "id": "e3",
      "source": "action-core",
      "target": "game-emulation",
      "type": "dependency",
      "label": "uses",
      "description": "Дії в фазах гри"
    },
    {
      "id": "e4",
      "source": "dodecahedron",
      "target": "action-core",
      "type": "dependency",
      "label": "modifiers",
      "description": "Модифікатори для d20"
    }
  ]
}
```

---

## 6. Питання для Уточнення

Перед імплементацією візуалізації потрібно узгодити:

1. **Що є LEGACY?** Які архітектури/підходи вже застаріли?
2. **Що з Planned вже частково працює?** (наприклад, action-core — базові таблиці є, але не всі модифікатори)
3. **Чи актуальний Convergence Merge?** Це ще планується чи відкладено?
4. **TimeWars — окремий режим чи частина Island Simulation?**
5. **Які саме "білі дірки" пріоритетні для фіксу?**

---

## 7. Технічні Рекомендації для Візуалізації

### Бібліотеки
- **React Flow** — найкраще для node-based UI з React
- **D3.js** — для складних layout алгоритмів
- **Cytoscape.js** — для великих графів з фільтрами

### Функціональність
- [ ] Zoom & pan
- [ ] Collapsible containers (розгортати/згортати складні ноди)
- [ ] Фільтри по фазах (показувати/ховати Legacy, Future)
- [ ] Клік на ноду — детальна інформація в сайдбарі
- [ ] Клік на зв'язок — опис що передається
- [ ] Export to PNG/SVG

---

*ТЗ перероблено з урахуванням реальних файлів в workspace*  
*Попередня версія була абстрактною — ця відображає реальну архітектуру*
