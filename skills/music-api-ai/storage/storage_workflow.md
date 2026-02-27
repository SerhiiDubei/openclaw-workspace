# Storage Workflow — Зберігання треків

## Правило
Треки зберігаються тільки в **Supabase Storage**.
Локальна папка `output/` — тимчасова, видаляється після завантаження.

## Флоу

### 1. Завантаження в Supabase
```bash
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
    "track_name": "...",
    "track_url": "https://...",
    "storage_path": "tracks/user_id/...",
    "variant": 1,
    "prompt": "...",
    "api_params": {...}
  }
}
```

### 3. Очищення
```bash
rm output/track_name.mp3
```

## Референс-аудіо

**Коли користувач надсилає аудіо:**

1. **Конвертувати** OGG → MP3:
   ```bash
   ffmpeg -i input.ogg -codec:a libmp3lame -q:a 2 output.mp3
   ```

2. **Закинути в Storage:**
   - Bucket: `music`
   - Path: `references/USER_ID/filename.mp3`

3. **Записати в БД** (`media_files`):
   - `file_type`: `reference_audio`
   - `user_id`: хто надіслав
   - `metadata`: опис мелодії

4. **Використати в prompt:**
   - Додати в `gpt_description_prompt`: "Inspired by user's reference audio..."

## Структура в Storage

```
tracks/
├── {user_id}/
│   └── {timestamp}/
│       ├── track_v1.mp3
│       └── track_v2.mp3
references/
├── {user_id}/
│   └── filename.mp3
```
