# Storage Workflow — Зберігання треків

## Правило
Треки зберігаються тільки в **Supabase Storage**.
Локальна папка `output/` — тимчасова, видаляється після завантаження.

## Флоу

### 1. Завантаження в Supabase
```bash
# Завантажити файл
supabase storage upload tracks/user_id/timestamp/track_name.mp3
```

### 2. Запис в БД
**Таблиця `sessions`:**
```json
{
  "id": "uuid",
  "user_id": "telegram:123456789",
  "created_at": "2026-02-27T14:30:00Z",
  "title": "Назва сесії"
}
```

**Таблиця `messages` (2 записи):**
```json
{
  "session_id": "uuid",
  "metadata": {
    "track_url": "https://...",
    "storage_path": "tracks/user_id/..."
  }
}
```

### 3. Очищення
```bash
# Видалити локальний файл після завантаження
rm output/track_name.mp3
```

## Структура в Storage
```
tracks/
├── {user_id}/
│   └── {timestamp}/
│       ├── track_v1.mp3
│       └── track_v2.mp3
```
