# Multi-User Configuration

## Активні користувачі

| Username | Telegram ID | Директорія | Статус |
|----------|-------------|------------|--------|
| Сергій Дубей | @bomberman047 (488426634) | `memory/users/serhii-dubei/` | Активний |
| Ліза (Eliza Dubey) | @mental_ninja (542906702) | `memory/users/mental-ninja/` | Активний |

## Мапа користувачів (для скриптів)

```bash
# log-current-session.sh
USER_MAP["bomberman047"]="serhii-dubei"
USER_MAP["mental-ninja"]="mental-ninja"
```

## Розділення сесій

### Принцип роботи
1. Кожен користувач має власну директорію в `memory/users/{username}/`
2. Сесії записуються окремо: `memory/users/{username}/sessions/YYYY-MM-DD.md`
3. Контекст не перемішується — кожна розмова прив'язана до `conversation_label`

### Структура директорій
```
memory/users/
├── serhii-dubei/
│   ├── profile.md
│   ├── insights.md
│   └── sessions/
│       └── 2026-03-13.md
└── mental-ninja/
    ├── profile.md
    ├── insights.md
    └── sessions/
        └── 2026-03-13.md
```

## Job Hunting (окремо для кожного)

```
projects/job-hunting/
├── Сергій/
│   ├── README.md
│   ├── profile.md
│   ├── vacancies/
│   ├── research/
│   └── cover-letters/
└── Ліза/
    ├── README.md
    ├── profile.md
    ├── vacancies/
    ├── research/
    └── cover-letters/
```

## Правила розділення

1. **Не змішувати контекст** — кожен користувач бачить тільки свої файли
2. **Окремі сесії** — логи в різних директоріях
3. **Окремі job search** — вакансії та кавери не перетинаються
4. **Прив'язка до Telegram ID** — система розпізнає по `conversation_label`

## Перевірка розділення

- [x] Сергій: `conversation_label: telegram:488426634` → `serhii-dubei`
- [x] Ліза: `conversation_label: mental ninja (@mental_ninja) id:542906702` → `mental-ninja`
- [x] Окремі папки сесій
- [x] Окремі job-hunting папки
- [x] Скрипт логування підтримує мапу

## Налаштування завершено ✅

**Дата:** 2026-03-13
**Статус:** Розділення активно
