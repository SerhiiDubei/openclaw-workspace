# FILE_CREATION_RULES.md — Правила створення файлів

## Золоте правило
**НЕ створювати файли в кореневій папці без крайньої необхідності!**

---

## Структура папок

```
/root/.openclaw/workspace/
│
├── [КОРІНЬ] — тільки системні файли
│   ├── AGENTS.md
│   ├── BOOTSTRAP.md
│   ├── HEARTBEAT.md
│   ├── IDENTITY.md
│   ├── INSTRUCTION.md
│   ├── MEMORY.md
│   ├── SOUL.md
│   ├── TOOLS.md
│   └── USER.md
│
├── memory/ — користувачі та сесії
│   └── users/
│       └── {username}/
│           ├── profile.md
│           ├── insights.md
│           ├── pinned/
│           └── sessions/
│
├── projects/ — проектні файли
│   └── {project-name}/
│       ├── README.md
│       └── ...
│
├── skills/ — навички (skills)
│   └── {skill-name}/
│       ├── SKILL.md
│       ├── scripts/
│       └── ...
│
└── _system/ — системні налаштування
    ├── cache-config.json
    └── USER_ONBOARDING.md
```

---

## Алгоритм визначення місця для файлу

### Крок 1: Що це за файл?

| Тип файлу | Куди помістити |
|-----------|----------------|
| **Системний** (AGENTS, SOUL, MEMORY...) | Корінь `/` |
| **Сесія користувача** | `memory/users/{username}/sessions/` |
| **Профіль користувача** | `memory/users/{username}/` |
| **Проектний** (тестування, розробка) | `projects/{project-name}/` |
| **Skill** (скрипт, конфіг) | `skills/{skill-name}/` або `skills/{skill-name}/scripts/` |
| **Тимчасовий** | `tmp/` (створити якщо потрібно) |

### Крок 2: Чи існує папка?

- **Так** → помістити туди
- **Ні** → створити папку, потім помістити

### Крок 3: Підтвердження

**Завжди питати підтвердження** перед створенням файлу в новій локації!

---

## Приклади

### ❌ Неправильно:
```
TESTING_TODO.md → /
script.sh → /
user-profile.md → /
```

### ✅ Правильно:
```
TESTING_TODO.md → projects/nano-banana/
script.sh → skills/music-api-ai/scripts/
user-profile.md → memory/users/serhii-dubei/
```

---

## Чекліст перед створенням файлу

- [ ] Визначив тип файлу
- [ ] Знайшов правильну папку
- [ ] Папка існує (або створена)
- [ ] Отримав підтвердження від користувача
- [ ] Не в корені (крім системних файлів)

---

## Винятки

Можна створювати в корені ТІЛЬКИ:
- `AGENTS.md`
- `BOOTSTRAP.md`
- `HEARTBEAT.md`
- `IDENTITY.md`
- `INSTRUCTION.md`
- `MEMORY.md`
- `SOUL.md`
- `TOOLS.md`
- `USER.md`

**Все інше — в підпапки!**
