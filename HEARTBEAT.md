# HEARTBEAT.md - Periodic Tasks

## GitHub Auto-Pull
Run this command:
```bash
/root/.openclaw/workspace/.git/auto-pull.sh
```

If changes pulled, report: "📥 Workspace updated from GitHub"
If no changes, reply: HEARTBEAT_OK

## Files Check — Перевірка зайвих файлів

### Що перевіряти
```bash
# Знайти файли в memory/ поза структурою
find /root/.openclaw/workspace/memory -maxdepth 1 -type f -name "*.md"
find /root/.openclaw/workspace/memory -maxdepth 1 -type f -name "*.json"
```

### Якщо знайдено файли поза структурою:

**НЕ видаляти автоматично!**

**Дії:**
1. Прочитати файл — чи є там важлива інформація
2. Перенести інформацію в правильне місце:
   - Про користувача → `memory/users/{username}/insights.md`
   - Проект → `projects/{name}/`
   - Системне → `_system/` або корінь
3. Повідомити: "Знайдено файл X — перенесено в Y"
4. Після підтвердження видалення → видалити

### Правильні місця для файлів

| Тип файлу | Куди |
|-----------|------|
| Профіль користувача | `memory/users/{username}/profile.md` |
| Інсайти користувача | `memory/users/{username}/insights.md` |
| Щоденні логи | `memory/YYYY-MM-DD.md` (тут ок) |
| Проектні файли | `projects/{project-name}/` |
| Системні інструкції | `_system/` або корінь |

## Last Check
- 2026-02-27 04:57 PM - Files check added
- 2026-02-24 03:54 AM - GitHub auto-pull executed
