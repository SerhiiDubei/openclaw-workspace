# WORKFLOW.md — Головний флоу генерації музики

> **Читати цей файл перед КОЖНОЮ генерацією!**

## 🚀 Швидкий старт

```
1. Неймінг → Хто замовляє і як назвати
2. Prompt → Деталі в prompts/lyrics-generation.md та prompts/style-generation.md
3. API → Деталі в api/endpoints.md
4. Async → Не блокувати чат
5. 2 варіанти → Завантажити обидва
6. Supabase → Деталі в storage/storage_workflow.md
7. Логування → Записати в music-log.jsonl
```

---

## 📋 Детальний флоу (7 кроків)

### Крок 1: НЕЙМІНГ

**Запитати:**
```
Хто замовляє трек і як назвати?
Формат: [Ім'я] - [Стиль/Жанр]
```

**Приклади:**
- "Ромко і Сергій - Detroit Acid"
- "Shishov's Walk - Part I"

---

### Крок 2: PROMPT

**Формат:**
```
[Intro][Instrument][Style] Текст
[Verse][Instrument][Style] Текст
[Chorus][Instrument][Style] Текст
[Outro][Instrument][Style] Текст
```

**Детальніше:**
- Тексти → `prompts/lyrics-generation.md`
- Стиль/теги → `prompts/style-generation.md`

---

### Крок 3: API ЗАПИТ

**POST /create** з параметрами:
```json
{
  "custom_mode": true,
  "prompt": "...",
  "title": "Назва",
  "tags": "...",
  "style_weight": 0.8,
  "weirdness_constraint": 0.5,
  "mv": "sonic-v5"
}
```

**Детальніше:** `api/endpoints.md`

---

### Крок 4: ASYNC WORKFLOW

**Не блокувати чат!**

1. Відповісти: "🎵 Трек у черзі! Чекаємо ~3 хвилини..."
2. Запустити фоновий трекер: `./scripts/track-generation.sh TASK_ID USER_ID &`
3. Надіслати результат окремим повідомленням

---

### Крок 5: 2 ВАРІАНТИ

**Завжди генерувати 2 варіанти!**

Надіслати окремо з поясненням:
```
Варіант 1: [опис]
Варіант 2: [опис]
```

---

### Крок 6: SUPABASE

**Автоматично, без питань!**

1. Завантажити в Storage
2. Створити запис в `sessions`
3. Створити 2 записи в `messages`

**Детальніше:** `storage/storage_workflow.md`

---

### Крок 7: ЛОГУВАННЯ

Записати в `memory/music-log.jsonl`:
```json
{
  "timestamp": "...",
  "user_id": "...",
  "track_name": "...",
  "prompt": "..."
}
```

---

## ✅ Чекліст

### Перед:
- [ ] Неймінг узгоджено
- [ ] Prompt з тегами (див. prompts/)
- [ ] Async workflow налаштовано

### Після:
- [ ] Завантажено в Supabase (див. storage/)
- [ ] Створено записи в БД
- [ ] Записано в music-log.jsonl
- [ ] Надіслано 2 варіанти

---

## 📁 Структура файлів

| Файл | Призначення |
|------|-------------|
| `WORKFLOW.md` | Цей файл — головний флоу |
| `SKILL.md` | Мінімальна публічна документація |
| `MY_RULES.md` | Мій чекліст |
| `api/endpoints.md` | API endpoints |
| `storage/storage_workflow.md` | Supabase зберігання |
| `prompts/lyrics-generation.md` | Генерація текстів |
| `prompts/style-generation.md` | Генерація стилю |
| `flows/music-creation-flow.md` | Тригерний флоу |
