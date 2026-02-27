# Storage Workflow — Зберігання треків

> Детальна схема БД: `_system/SUPABASE_SCHEMA.md`

## Правило
Треки зберігаються тільки в **Supabase Storage**.
Локальна папка `output/` — тимчасова, видаляється після завантаження.

## Структура файлів

### Неймінг
```
{Username} - {Track Name} - v{1|2}.mp3
```

**Приклади:**
- `Serhii Dubei - Detroit Techno - v1.mp3`
- `Yevhen Shishov - Walking - v2.mp3`

### Шлях в Storage
```
music/tracks/{Username}/{YYYY-MM-DD}/
```

**Приклад:**
```
music/tracks/Serhii Dubei/2026-02-27/
├── Serhii Dubei - Detroit Techno - v1.mp3
└── Serhii Dubei - Detroit Techno - v2.mp3
```

## Флоу

### 1. Завантаження в Supabase
```bash
# Формуємо шлях
USERNAME="Serhii Dubei"
TRACK_NAME="Detroit Techno"
DATE="2026-02-27"
FILENAME="${USERNAME} - ${TRACK_NAME} - v1.mp3"

# Завантажуємо
curl -X POST "${SUPABASE_URL}/storage/v1/object/music/tracks/${USERNAME}/${DATE}/${FILENAME}" \
  -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
  -H "Content-Type: audio/mpeg" \
  --data-binary @"track.mp3"
```

### 2. Запис в БД

**Таблиця `sessions`:**
```json
{
  "user_id": "telegram:488426634",
  "status": "closed",
  "metadata": {
    "title": "Serhii Dubei - Detroit Techno",
    "requester": "Serhii Dubei",
    "track_count": 2,
    "storage_paths": [
      "music/tracks/Serhii Dubei/2026-02-27/Serhii Dubei - Detroit Techno - v1.mp3",
      "music/tracks/Serhii Dubei/2026-02-27/Serhii Dubei - Detroit Techno - v2.mp3"
    ]
  }
}
```

**Таблиця `messages` (2 записи):**
```json
{
  "session_id": "uuid",
  "type": "audio",
  "content": "Serhii Dubei - Detroit Techno (Варіант 1)",
  "media_url": "https://cdn1.suno.ai/...",
  "metadata": {
    "track_name": "Serhii Dubei - Detroit Techno",
    "variant": 1,
    "storage_path": "music/tracks/Serhii Dubei/2026-02-27/Serhii Dubei - Detroit Techno - v1.mp3"
  }
}
```

### 3. Очищення
```bash
rm output/local_file.mp3
```

## Референс-аудіо

**Коли користувач надсилає аудіо:**

1. **Конвертувати** OGG → MP3:
   ```bash
   ffmpeg -i input.ogg -codec:a libmp3lame -q:a 2 output.mp3
   ```

2. **Закинути в Storage:**
   - Bucket: `music`
   - Path: `references/{Username}/filename.mp3`

3. **Записати в БД** (`media_files`):
   - `file_type`: `reference_audio`
   - `user_id`: хто надіслав
   - `metadata`: опис мелодії
