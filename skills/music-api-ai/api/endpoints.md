# MusicAPI.ai — API Endpoints

## Base URL
```
https://api.musicapi.ai/api/v1/sonic/
```

## Endpoints

### POST /create
Створити новий трек.

**Request:**
```json
{
  "custom_mode": true,
  "prompt": "[Intro][Guitar][Folk]\\nLyrics...",
  "title": "Song Title",
  "tags": "genre,style,mood",
  "style_weight": 0.8,
  "weirdness_constraint": 0.5,
  "negative_tags": "elements to avoid",
  "gpt_description_prompt": "Production description (max 350 chars)",
  "make_instrumental": false,
  "mv": "sonic-v5"
}
```

**Response:**
```json
{
  "task_id": "uuid",
  "status": "pending"
}
```

### GET /task/{task_id}
Перевірити статус генерації.

**Response:**
```json
{
  "id": "uuid",
  "status": "processing|complete|failed",
  "result": {
    "audio_url": "https://..."
  }
}
```

### GET /stems/{task_id}
Отримати STEMS (окремі доріжки).

## Auth
Bearer token в заголовку:
```
Authorization: Bearer {token}
```
