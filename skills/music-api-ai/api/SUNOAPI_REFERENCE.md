# SunoAPI Documentation — Повний довідник

**URL документації:** https://docs.sunoapi.org/  
**Base URL API:** https://api.sunoapi.org  
**Дата збору:** 2026-03-13

---

## 📋 Зміст

1. [Аутентифікація](#аутентифікація)
2. [AI Моделі](#ai-моделі)
3. [Генерація музики](#генерація-музики)
4. [Робота з референсами](#робота-з-референсами)
5. [Розширення треків](#розширення-треків)
6. [Додавання вокалу/інструменталу](#додавання-вокалуінструменталу)
7. [Обробка аудіо](#обробка-аудіо)
8. [Утиліти](#утиліти)
9. [Status Codes](#status-codes)
10. [Callback System](#callback-system)

---

## Аутентифікація

Всі запити вимагають Bearer Token:

```
Authorization: Bearer YOUR_API_KEY
```

---

## AI Моделі

| Модель | Опис | Макс. тривалість |
|--------|------|------------------|
| V4 | Покращений вокал | 4 хвилини |
| V4_5 | Розумні промпти, швидша генерація | 8 хвилин |
| V4_5PLUS | Найкраща якість, багаті тони | 8 хвилин |
| V4_5ALL | Краща структура пісні | 8 хвилин |
| V5 | Найновіша модель | 8 хвилин |

---

## Генерація музики

### POST /api/v1/generate

Створити музику з текстового опису.

**Request:**
```json
{
  "customMode": true,
  "instrumental": true,
  "model": "V4_5ALL",
  "callBackUrl": "https://api.example.com/callback",
  "prompt": "A calm and relaxing piano track with soft melodies",
  "style": "Classical",
  "title": "Peaceful Piano Meditation",
  "personaId": "persona_123",
  "personaModel": "style_persona",
  "negativeTags": "Heavy Metal, Upbeat Drums",
  "vocalGender": "m",
  "styleWeight": 0.65,
  "weirdnessConstraint": 0.65,
  "audioWeight": 0.65
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

### GET /api/v1/generate/record-info?taskId={taskId}

Перевірити статус генерації.

**Response (SUCCESS):**
```json
{
  "code": 200,
  "data": {
    "taskId": "...",
    "status": "SUCCESS",
    "response": {
      "sunoData": [
        {
          "id": "...",
          "audioUrl": "https://...",
          "streamAudioUrl": "https://...",
          "imageUrl": "https://...",
          "title": "...",
          "duration": 198.44
        }
      ]
    }
  }
}
```

---

## Робота з референсами

### POST /api/v1/generate/upload-cover ⭐ КАВЕР

Трансформувати існуюче аудіо в новий стиль, зберігаючи мелодію.

**Request:**
```json
{
  "uploadUrl": "https://storage.example.com/your-audio.mp3",
  "customMode": true,
  "instrumental": false,
  "model": "V4_5ALL",
  "callBackUrl": "https://api.example.com/callback",
  "prompt": "Techno remix, energetic beat, powerful bass",
  "style": "Techno",
  "title": "My Cover - Techno Version",
  "negativeTags": "Heavy Metal",
  "vocalGender": "m",
  "styleWeight": 0.65,
  "weirdnessConstraint": 0.65,
  "audioWeight": 0.65
}
```

**Параметри:**
- `uploadUrl` — URL аудіо-файлу (публічний)
- `audioWeight` — сила впливу оригіналу (0.0 - 1.0)
- `styleWeight` — сила стилю (0.0 - 1.0)

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

### POST /api/v1/generate/upload-extend

Завантажити аудіо і розширити його AI-генерацією.

**Request:**
```json
{
  "uploadUrl": "https://storage.example.com/your-audio.mp3",
  "defaultParamFlag": true,
  "model": "V4_5ALL",
  "callBackUrl": "https://api.example.com/callback",
  "instrumental": true,
  "prompt": "Extend the music with more relaxing notes",
  "style": "Classical",
  "title": "Peaceful Piano Extended",
  "continueAt": 60,
  "personaId": "persona_123",
  "personaModel": "style_persona",
  "negativeTags": "Relaxing Piano",
  "vocalGender": "m",
  "styleWeight": 0.65,
  "weirdnessConstraint": 0.65,
  "audioWeight": 0.65
}
```

---

## Розширення треків

### POST /api/v1/generate/extend

Розширити існуючий трек Suno.

**Request:**
```json
{
  "defaultParamFlag": true,
  "audioId": "e231****-****-****-****-****8cadc7dc",
  "model": "V4_5ALL",
  "callBackUrl": "https://api.example.com/callback",
  "prompt": "Extend the music with more relaxing notes",
  "style": "Classical",
  "title": "Peaceful Piano Extended",
  "continueAt": 60,
  "personaId": "persona_123",
  "personaModel": "style_persona",
  "negativeTags": "Relaxing Piano",
  "vocalGender": "m",
  "styleWeight": 0.65,
  "weirdnessConstraint": 0.65,
  "audioWeight": 0.65
}
```

---

## Додавання вокалу/інструменталу

### POST /api/v1/generate/add-instrumental

Додати інструментальний супровід до вокального треку.

**Request:**
```json
{
  "uploadUrl": "https://example.com/vocals.mp3",
  "title": "Relaxing Piano",
  "negativeTags": "Heavy Metal, Aggressive Drums",
  "tags": "Relaxing Piano, Ambient, Peaceful",
  "callBackUrl": "https://api.example.com/callback",
  "vocalGender": "m",
  "styleWeight": 0.61,
  "weirdnessConstraint": 0.72,
  "audioWeight": 0.65,
  "model": "V4_5PLUS"
}
```

### POST /api/v1/generate/add-vocals

Додати вокал до інструментального треку.

**Request:**
```json
{
  "prompt": "A calm and relaxing piano track with soothing vocals",
  "title": "Relaxing Piano with Vocals",
  "negativeTags": "Heavy Metal, Aggressive Vocals",
  "style": "Jazz",
  "uploadUrl": "https://example.com/instrumental.mp3",
  "callBackUrl": "https://api.example.com/callback",
  "vocalGender": "m",
  "styleWeight": 0.61,
  "weirdnessConstraint": 0.72,
  "audioWeight": 0.65,
  "model": "V4_5PLUS"
}
```

---

## Обробка аудіо

### POST /api/v1/generate/boost-style

Покращити стиль музики.

### POST /api/v1/generate/cover

Переробити музику в іншому стилі.

### POST /api/v1/generate/replace-section

Замінити частину треку.

### POST /api/v1/tools/separate

Розділити вокал і інструментал.

### POST /api/v1/tools/convert-wav

Конвертувати в WAV формат.

### POST /api/v1/tools/generate-midi

Створити MIDI з аудіо.

---

## Утиліти

### GET /api/v1/user/credits

Перевірити залишок кредитів.

**Response:**
```json
{
  "code": 200,
  "data": 100
}
```

---

## Status Codes

| Код | Значення |
|-----|----------|
| 200 | ✅ Успіх |
| 400 | ⚠️ Невірні параметри |
| 401 | ⚠️ Не авторизовано |
| 404 | ⚠️ Невірний endpoint |
| 405 | ⚠️ Rate limit |
| 413 | ⚠️ Промпт занадто довгий |
| 429 | ⚠️ Недостатньо кредитів |
| 430 | ⚠️ Занадто часті запити |
| 455 | ⚠️ Технічне обслуговування |
| 500 | ❌ Помилка сервера |

---

## Callback System

Всі endpoint'и підтримують webhook callbacks.

**Статуси генерації:**
- `PENDING` — в черзі
- `FIRST_SUCCESS` — перший етап готовий
- `TEXT_SUCCESS` — текст готовий (для генерації з вокалом)
- `SUCCESS` — повністю готово
- `FAILED` — помилка

**Callback payload:**
```json
{
  "taskId": "...",
  "status": "SUCCESS",
  "data": {
    "sunoData": [...]
  }
}
```

---

## Особливості роботи

### Генерація з референсом (upload-cover)

1. Файл має бути доступний за публічним URL
2. Підтримувані формати: MP3, WAV, OGG
3. Макс. розмір: залежить від плану
4. Час генерації: 2-5 хвилин

### Параметри ваги

- `audioWeight` — як сильно зберігати оригінал (0.0 = повністю новий, 1.0 = мінімальні зміни)
- `styleWeight` — сила стилістичних змін
- `weirdnessConstraint` — креативність (0.0 = консервативно, 1.0 = експериментально)

### Збереження файлів

**SunoAPI повертає:**
- `audioUrl` — пряме посилання на MP3
- `streamAudioUrl` — посилання для стрімінгу
- `imageUrl` — обкладинка

Файли зберігаються тимчасово (~24 години).

---

## Приклад workflow (кавер)

```bash
# 1. Завантажити референс в публічне сховище (Supabase/S3)
# 2. Викликати upload-cover
curl -X POST https://api.sunoapi.org/api/v1/generate/upload-cover \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "uploadUrl": "https://your-storage.com/reference.mp3",
    "prompt": "Techno remix",
    "style": "Techno",
    "title": "My Cover",
    "model": "V4_5",
    "audioWeight": 0.7,
    "styleWeight": 0.8
  }'

# 3. Отримати taskId
# 4. Чекати через /generate/record-info
# 5. Завантажити результат
```

---

**Джерело:** https://docs.sunoapi.org/  
**Дата оновлення:** 2026-03-13
