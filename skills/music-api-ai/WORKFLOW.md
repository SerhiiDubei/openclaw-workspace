# WORKFLOW.md — Головний флоу генерації музики (SunoAPI)

> **⚠️ ТІЛЬКИ SunoAPI — НІ MusicAPI.ai!**
> 
> **Читати цей файл перед КОЖНОЮ генерацією!**

## 🚀 Швидкий старт (8 кроків)

```
1. Неймінг     → Хто замовляє і як назвати
2. Prompt      → Деталі в prompts/
3. API         → POST /generate (SunoAPI)
4. Poll        → Чекати TEXT_SUCCESS
5. Download    → Завантажити 2 файли
6. Rename      → [Name] - [Title] - v[1/2].mp3
7. Send        → Надіслати файли користувачеві
8. Log         → Записати в music-log.jsonl
```

---

## 📋 Детальний флоу

### Крок 1: НЕЙМІНГ (ОБОВ'ЯЗКОВО)

**Запитати:**
```
Хто замовляє трек і як назвати?
Формат: [Ім'я] - [Назва треку]
Приклад: "Sergiy - Detroit Acid"
```

**Важливо:** Це ім'я буде в назві файлу!

---

### Крок 2: PROMPT

**SunoAPI Format:**
```json
{
  "prompt": "Опис треку для Suno",
  "customMode": true,
  "instrumental": true/false,
  "style": "Genre/Style",
  "title": "Track Title",
  "model": "V4_5",
  "callBackUrl": "https://httpbin.org/post"
}
```

**Детальніше:**
- Тексти → `prompts/lyrics-generation.md`
- Стиль → `prompts/style-generation.md`

---

### Крок 3: API ЗАПИТ (SunoAPI)

```bash
curl -X POST "https://api.sunoapi.org/api/v1/generate" \
  -H "Authorization: Bearer $SUNOAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "...",
    "customMode": true,
    "instrumental": true,
    "style": "...",
    "title": "...",
    "model": "V4_5",
    "callBackUrl": "https://httpbin.org/post"
  }'
```

**Response:**
```json
{
  "code": 200,
  "data": {
    "taskId": "..."
  }
}
```

---

### Крок 4: POLL STATUS

**Чекати поки статус не буде `TEXT_SUCCESS`:**

```bash
curl "https://api.sunoapi.org/api/v1/generate/record-info?taskId=XXX" \
  -H "Authorization: Bearer $SUNOAPI_KEY"
```

**Status flow:** PENDING → FIRST_SUCCESS → TEXT_SUCCESS

**Час очікування:** 2-5 хвилин

---

### Крок 5: ЗАВАНТАЖИТИ 2 ВАРІАНТИ

**З response.data.sunoData:**
- `streamAudioUrl` — для прослуховування
- `sourceStreamAudioUrl` — оригінал з Suno

**Завантажити обидва файли:**
```bash
curl -o "temp-v1.mp3" "[streamAudioUrl-1]"
curl -o "temp-v2.mp3" "[streamAudioUrl-2]"
```

---

### Крок 6: ПЕРЕЙМЕНУВАТИ (КРИТИЧНО ВАЖЛИВО!)

**Формат назви файлу:**
```
[Ім'я користувача] - [Назва треку] - v1.mp3
[Ім'я користувача] - [Назва треку] - v2.mp3
```

**Приклад:**
```
Sergiy - Detroit Acid - v1.mp3
Sergiy - Detroit Acid - v2.mp3
```

**НІЯКИХ інших форматів!**

---

### Крок 7: НАДІСЛАТИ ФАЙЛИ (КРИТИЧНО ВАЖЛИВО!)

**Як відправляти:**
1. Одне повідомлення
2. Два файли (v1 і v2)
3. Короткий опис

**Приклад повідомлення:**
```
🎵 Готово! Sergiy - Detroit Acid

Варіант 1: Більш агресивний, фокус на бас
Варіант 2: Більш мелодійний, фокус на синтезатори

Обидва варіанти прикріплені 👇
```

**ВАЖЛИВО:** Надіслати як **файли**, не як посилання!

---

### Крок 8: ЛОГУВАННЯ

Записати в `memory/music-log.jsonl`:
```json
{
  "timestamp": "2026-03-13T16:20:00Z",
  "user_id": "telegram:488426634",
  "user_name": "Sergiy",
  "track_name": "Detroit Acid",
  "task_id": "...",
  "prompt": "...",
  "urls": ["...", "..."]
}
```

---

## ✅ Чекліст (ЧИТАТИ КОЖЕН РАЗ!)

### Перед генерацією:
- [ ] Неймінг узгоджено з користувачем
- [ ] Prompt містить правильний стиль
- [ ] Використовую SunoAPI (api.sunoapi.org)

### Після генерації:
- [ ] Статус TEXT_SUCCESS
- [ ] Завантажено обидва варіанти
- [ ] Файли перейменовано: [Name] - [Title] - v[1/2].mp3
- [ ] Надіслано як **файли** (не посилання)
- [ ] Записано в music-log.jsonl

---

## ❌ ЗАБОРОНЕНО

- **НІ** MusicAPI.ai — видалено
- **НІ** вигаданим метрикам у відповідях
- **НІ** відправляти посилання замість файлів
- **НІ** іншим форматам неймінгу
- **НІ** ігнорувати узгоджений неймінг

---

## 📁 Структура файлів

| Файл | Призначення |
|------|-------------|
| `SKILL.md` | Основна інформація + правила |
| `WORKFLOW.md` | Цей файл — покроковий флоу |
| `api/endpoints.md` | SunoAPI endpoints |
| `prompts/lyrics-generation.md` | Генерація текстів |
| `prompts/style-generation.md` | Генерація стилю |
| `scripts/sunoapi-client.js` | Клієнт для SunoAPI |

---

## 🔧 API Configuration

```yaml
Base URL: https://api.sunoapi.org/api/v1
Endpoints:
  - POST /generate        # Створити трек
  - GET /generate/record-info  # Перевірити статус
Model: V4_5
Auth: Bearer (в ENV)
```

**⚠️ Якщо спрацює щось інше — це БАГ, повідомити користувача!**
