# Storage Workflow — Зберігання треків (SunoAPI)

**⚠️ ТІЛЬКИ SunoAPI — НІ MusicAPI.ai!**

> Детальна схема БД: `_system/SUPABASE_SCHEMA.md`

## Правило
Треки зберігаються тільки в **Supabase** (Storage + БД).
Локальна папка `output/` — тимчасова, видаляється після завантаження.

## Логування
Всі метадані треків зберігаються в таблиці `music_tracks`.
Локальні логи не використовуються.

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

## Референс-аудіо (ОНОВЛЕНО — система для референсів)

**Коли користувач надсилає аудіо як референс:**

### 1. Отримання файлу
- Користувач надсилає MP3/WAV/OGG файл
- Зберегти локально
- Конвертувати OGG → MP3 (якщо потрібно):
  ```bash
  ffmpeg -i input.ogg -codec:a libmp3lame -q:a 2 output.mp3
  ```

### 2. Неймінг референсу
**Формат:** `REF - {Username} - {Artist} - {Track Name}.mp3`

**Приклади:**
- `REF - Sergiy - Joy Orbison - flight fm.mp3`
- `REF - Roman - Daft Punk - One More Time.mp3`

### 3. Завантаження в Storage
```
music/references/{Username}/{YYYY-MM-DD}/
```

**Приклад:**
```
music/references/Sergiy/2026-03-13/
├── REF - Sergiy - Joy Orbison - flight fm.mp3
├── REF - Sergiy - The Prodigy - Breathe.mp3
└── REF - Sergiy - Aphex Twin - Windowlicker.mp3
```

### 4. Запис в БД (`reference_tracks`)
```json
{
  "user_id": "telegram:488426634",
  "username": "Sergiy",
  "original_artist": "Joy Orbison",
  "original_track": "flight fm",
  "storage_path": "music/references/Sergiy/2026-03-13/REF - Sergiy - Joy Orbison - flight fm.mp3",
  "style_dna": {
    "genre": "UK Garage",
    "bpm": 130,
    "mood": "dark, club energy",
    "key_elements": ["skippy drums", "wobbly bass", "filter modulation"]
  },
  "usage_status": "active",
  "created_at": "2026-03-13T17:00:00Z"
}
```

### 5. Відправка назад користувачу
- Перейменований файл
- Як файл (не посилання!)
- З описом Style DNA

### 6. Використання для генерації
При генерації нового треку:
1. Читати `style_dna` з референсу
2. Перетворити в SunoAPI промпт
3. Генерувати
4. Зберігати зв'язок: `generated_track` → `reference_track_id`
