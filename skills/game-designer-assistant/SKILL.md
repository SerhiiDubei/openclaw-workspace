---
name: game-designer-assistant
description: Assistant for creating and managing evening/bar games. Helps generate questions, design game mechanics, and prepare game packs for 10-40 people. Use when user needs help with quiz games, team competitions, bar games, or any social gaming formats.
---

# Game Designer Assistant

Assistant for designing evening and bar games. **Beta version — learning by doing.**

## Core Principle

**10 ручних сесій перед будь-якою автоматизацією.**

Кожна реальна гра = дані для покращення. Спочатку ручне логування, потім автоматизація.

## What This Skill Does

1. **Підбирає механіки** під параметри гри (кількість людей, час, місце)
2. **Допомагає з питаннями** — генерація або вибір з існуючих
3. **Готує game-pack** — готовий до використання набір
4. **Логує сесії** — що спрацювало, що ні (для навчання)

## Game Parameters

Кожна гра має:
- **Player count**: 10-40 людей
- **Duration**: 30-60 хвилин
- **Format**: Бар / дім / корпоратив
- **Phase**: Start (енергія) → Mid (основа) → Late (фінал)

### Question Attributes
- **Difficulty**: 1-5
- **Topic**: Історія, спорт, наука, поп-культура...
- **Format**: Бар-квіз, бліц, коло, так/ні, донетки
- **Target audience**: Вік, локація, інтереси
- **Phase**: Start / mid / late

## Workflow (Beta)

### 1. Creating a Game (Manual)
1. Користувач каже параметри (люди, час, місце)
2. Шукаємо в `references/game-mechanics/` підходящі механіки
3. Пропонуємо питання (генерація або з бази)
4. Експортуємо `game-pack` (markdown)

### 2. After Game Session (CRITICAL)
1. Користувач розповідає, що було
2. Логуємо в `references/sessions/YYYY-MM-DD-description.md`
3. Оновлюємо `BETA.md` — гіпотези, висновки
4. Оновлюємо рейтинг питань

### 3. Learning (After 5-10 sessions)
- Аналізуємо логи
- Виділяємо патерни
- Оновлюємо механіки (draft → tested → approved)

## File Structure

```
game-designer-assistant/
├── SKILL.md                 # Цей файл
├── BETA.md                  # Лог навчання (гіпотези, сесії, рішення)
├── scripts/
│   ├── init-db.py          # Ініціалізація SQLite (3 таблиці)
│   ├── log-session.py      # Запис сесії після гри
│   └── export-gamepack.py  # Експорт готового набору
├── references/
│   ├── game-mechanics/     # Каталог механік
│   ├── theory/             # Теорія ігор
│   ├── templates/          # Шаблони
│   └── sessions/           # Логи реальних ігор (додаються після кожної гри)
├── _learning/              # Мета-аналіз
│   ├── hypotheses.md       # Що тестуємо
│   ├── decisions.md        # Чому прийняли так
│   └── metrics.md          # Що працює
└── assets/
    └── game-pack-template/ # Шаблон для експорту
```

## Database (SQLite)

**Тільки 3 таблиці:**

```sql
mechanics (
    id TEXT PRIMARY KEY,
    name TEXT,
    description TEXT,
    status TEXT  -- draft | tested | approved
)

questions (
    id TEXT PRIMARY KEY,
    text TEXT,
    topic TEXT,
    difficulty INT,  -- 1-5
    format TEXT,     -- bar | blitz | circle | yesno | donetki
    times_used INT,
    rating INT       -- 1-5 після гри
)

sessions (
    id TEXT PRIMARY KEY,
    date TEXT,
    game_type TEXT,     -- bar | home | corporate
    player_count INT,
    duration_min INT,
    mechanics_used TEXT, -- JSON ["quiz", "blitz"]
    what_worked TEXT,
    what_didnt TEXT
)
```

## Rules

1. **Після КОЖНОЇ гри** — логувати сесію
2. **10 сесій** — мінімум для будь-якої автоматизації
3. **Зберігати в BETA.md** — гіпотези та рішення
4. **Питання** — завжди під цільову аудиторію
5. **Start phase** — найвища енергія, прості правила

## Beta Status

Цей skill в активній розробці через реальні ігри.
Користувач грає → ми логуємо → аналізуємо → покращуємо.
