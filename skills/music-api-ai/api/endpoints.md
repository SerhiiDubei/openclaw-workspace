# SunoAPI Endpoints

**⚠️ ТІЛЬКИ SunoAPI — НІ MusicAPI.ai!**

## Base URL
```
https://api.sunoapi.org/api/v1
```

## Endpoints

### POST /generate
Створити новий трек.

**Request:**
```json
{
  "prompt": "Electronic synthwave with driving beat",
  "customMode": true,
  "instrumental": true,
  "style": "Electronic Synthwave",
  "title": "Track Title",
  "model": "V4_5",
  "callBackUrl": "https://httpbin.org/post"
}
```

**Response:**
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "taskId": "uuid"
  }
}
```

### GET /generate/record-info
Перевірити статус генерації.

**URL:**
```
/generate/record-info?taskId={task_id}
```

**Response (PENDING):**
```json
{
  "code": 200,
  "data": {
    "status": "PENDING",
    "response": null
  }
}
```

**Response (TEXT_SUCCESS):**
```json
{
  "code": 200,
  "data": {
    "status": "TEXT_SUCCESS",
    "response": {
      "sunoData": [
        {
          "id": "...",
          "streamAudioUrl": "https://...",
          "title": "...",
          "tags": "..."
        },
        {
          "id": "...",
          "streamAudioUrl": "https://...",
          "title": "...",
          "tags": "..."
        }
      ]
    }
  }
}
```

## Status Flow

```
PENDING → FIRST_SUCCESS → TEXT_SUCCESS
```

**Час очікування:** 2-5 хвилин

## Auth

Bearer token в заголовку:
```
Authorization: Bearer {SUNOAPI_KEY}
```

## Важливо

- Завжди використовувати `callBackUrl` (навіть фейковий)
- Завжди чекати `TEXT_SUCCESS`
- Завжди отримуємо 2 варіанти
- **НІ** інших endpoints!
