# Supabase Database Structure

## Таблиці

### 1. users
Користувачі системи.

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  telegram_id TEXT UNIQUE,
  username TEXT,
  full_name TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  metadata JSONB DEFAULT '{}'
);
```

### 2. music_tracks ⭐ ГОЛОВНА ДЛЯ МУЗИКИ
Всі згенеровані треки.

```sql
CREATE TABLE music_tracks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id TEXT,                    -- telegram:123456789
  username TEXT,                   -- Serhii Dubei
  track_name TEXT,                 -- Detroit Techno
  variant INTEGER,                 -- 1 або 2
  prompt TEXT,                     -- Повний промпт
  api_params JSONB,                -- {style_weight, weirdness_constraint...}
  storage_path TEXT,               -- music/tracks/Serhii Dubei/...
  audio_url TEXT,                  -- https://cdn1.suno.ai/...
  clip_id TEXT,                    -- ID від Suno
  duration TEXT,                   -- 87.64
  created_at TIMESTAMPTZ DEFAULT NOW(),
  metadata JSONB DEFAULT '{}'      -- Додаткові дані
);
```

**Приклад запису:**
```json
{
  "user_id": "telegram:488426634",
  "username": "Serhii Dubei",
  "track_name": "Detroit Techno",
  "variant": 1,
  "prompt": "[Intro][Detroit Techno]...",
  "api_params": {
    "style_weight": 0.85,
    "weirdness_constraint": 0.6,
    "mv": "sonic-v5"
  },
  "storage_path": "music/tracks/Serhii Dubei/2026-02-27/Serhii Dubei - Detroit Techno - v1.mp3",
  "audio_url": "https://cdn1.suno.ai/...",
  "clip_id": "a7eea56f-...",
  "duration": "87.64"
}
```

### 3. sessions
Тільки для чат-сесій (не для музики).

```sql
CREATE TABLE sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id TEXT,
  started_at TIMESTAMPTZ,
  ended_at TIMESTAMPTZ,
  status TEXT,                     -- active, closed
  metadata JSONB DEFAULT '{}'
);
```

### 4. messages
Тільки текстові повідомлення (не для треків).

```sql
CREATE TABLE messages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id UUID REFERENCES sessions(id),
  type TEXT,                       -- text
  content TEXT,
  timestamp TIMESTAMPTZ DEFAULT NOW(),
  metadata JSONB DEFAULT '{}'
);
```

## НЕ ВИКОРИСТОВУЄМО

- `chat_messages` — не використовуємо
- `chat_sessions` — не використовуємо
- `media_files` — не використовуємо (все в music_tracks)

## Storage

**Bucket:** `music`

**Структура:**
```
music/
├── tracks/
│   └── {Username}/
│       └── {YYYY-MM-DD}/
│           ├── {Username} - {Track} - v1.mp3
│           └── {Username} - {Track} - v2.mp3
└── references/
    └── {Username}/
        └── filename.mp3
```
