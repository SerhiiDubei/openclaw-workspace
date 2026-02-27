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

## Music Track Status Check — Перевірка статусу треків

### Що перевіряти
```bash
# Запустити скрипт перевірки
/root/.openclaw/workspace/skills/music-api-ai/scripts/check-pending-tracks.sh
```

### Дії:
1. Перевірити `music_tracks` на треки зі статусом "running"
2. Запитати статус через MusicAPI
3. Якщо ОБИДВА варіанти готові:
   - Завантажити файли з CDN
   - Завантажити в Supabase Storage
   - Оновити БД
   - **Надіслати повідомлення користувачу з файлами**
4. Якщо failed — оновити статус в БД

### Надсилання файлів:
- Завантажити v1 і v2 з CDN (Suno)
- Надіслати як **файли** в Telegram
- Неймінг: `Username - Track Name - v1.mp3`
- Одне повідомлення з двома файлами
