# INSTRUCTION.md — Контрольний файл тригерів

## 🎯 Основні тригери (завжди перевіряй першим)

| Тригер | Дія | Куди йти |
|--------|-----|----------|
| **Новий користувач** | Перше повідомлення | `projects/onboarding/` → `README.md` |
| **Генерація музики** | Запит "згенеруй музику" | `skills/music-api-ai/` → `WORKFLOW.md` |
| **Heartbeat** | Системне повідомлення | `HEARTBEAT.md` |
| **Статус** | Команда /status | Показати session_status |

## 🔧 Додаткові тригери

| Тригер | Дія | Куди йти |
|--------|-----|----------|
| Додати користувача | Запит від @bomberman047 | `_system/USER_ONBOARDING.md` |
| Куди класти файл | Питання про локацію | `_system/FILE_CREATION_RULES.md` |
| Плани та задачі | Що доробляти | `PLANS.md` |

## 📋 Правила навігації

1. **Спочатку цей файл** — визначити тригер
2. **Йти за посиланням** — не вигадувати
3. **В skill завжди є WORKFLOW.md** — читати перед роботою
4. **Після виконання** — логувати якщо потрібно

## 🗂️ Структура залежностей

```
INSTRUCTION.md (ти тут)
    ├── projects/onboarding/README.md
    ├── skills/music-api-ai/WORKFLOW.md
    ├── _system/USER_ONBOARDING.md
    ├── _system/FILE_CREATION_RULES.md
    └── PLANS.md
```
