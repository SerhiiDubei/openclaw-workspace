# 🛡️ Архітектурний Pipeline

## Компоненти

### 1. Pre-commit Hook (`scripts/pre-commit.sh`)
**Що робить:**
- ❌ Блокує створення папок в корені
- ❌ Блокує переміщення системних файлів
- ⚠️  Попереджає про фігурні кавички (curly quotes)

**Встановлено:** `.git/hooks/pre-commit`

### 2. Git Rules (`_system/GIT_RULES.md`)
- Перевіряти `git status` перед "готово"
- Шаблон відповіді про git

### 3. File Creation Rules (`_system/FILE_CREATION_RULES.md`)
- Алгоритм визначення місця для файлу
- Чекліст перед створенням

---

## Структура папок

```
/root/.openclaw/workspace/
│
├── [КОРІНЬ] — тільки системні файли
├── memory/users/{username}/ — сесії та профілі
├── projects/{project-name}/ — проектні файли ✅
├── skills/{skill-name}/ — навички
└── _system/ — системні налаштування
```

---

## Що змінено

**Перенесено:**
- `job-analysis/` → `projects/job-hunting/` ✅

**Створено:**
- `scripts/pre-commit.sh` — hook для захисту
- `_system/GIT_RULES.md` — правила роботи з git

---

## Тест pipeline

```bash
# Спроба створити папку в корені — БУДЕ ВІДХИЛЕНО
cd /root/.openclaw/workspace
mkdir bad-folder
git add bad-folder
git commit -m "test"
# 🚫 COMMIT ВІДХИЛЕНО: створення папок в корені
```
