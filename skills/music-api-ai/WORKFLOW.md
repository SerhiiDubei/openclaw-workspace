# WORKFLOW.md — Флоу генерації музики

> **Читати цей файл перед КОЖНОЮ генерацією!**

## 🚀 Швидкий старт (досвідчений користувач)

```bash
# 1. Запитати неймінг
"Хто замовляє і як назвати трек?"

# 2. Сформувати промпт
[Intro][Instrument][Style] Текст

# 3. Відправити в API
POST /create з параметрами

# 4. Зачекати ~3 хв
Poll статус → отримати URL

# 5. Зберегти в Supabase
Storage + sessions + messages

# 6. Надіслати 2 варіанти
З поясненням який який
```

---

## 📋 Детальний флоу

### Крок 1: НЕЙМІНГ (обов'язково!)

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

**Теги інструментів:**
- `[TB-303]` — acid bass
- `[Roland TR-909]` — drums
- `[Analog Synth]` — synth leads

**Теги стилю:**
- `[Acid]`, `[Detroit Techno]`, `[Dark Bass]`

---

### Крок 3: API ПАРАМЕТРИ

```json
{
  "custom_mode": true,
  "prompt": "...",
  "title": "Назва треку",
  "tags": "genre,style,mood",
  "style_weight": 0.8,
  "weirdness_constraint": 0.5,
  "negative_tags": "elements to avoid",
  "gpt_description_prompt": "опис (max 350 chars)",
  "make_instrumental": false,
  "mv": "sonic-v5"
}
```

---

### Крок 4: ASYNC WORKFLOW

**Не блокувати чат!**

1. Відповісти: "🎵 Трек у черзі! Чекаємо ~3 хвилини..."
2. Запустити фоновий трекер
3. Надіслати результат окремим повідомленням

---

### Крок 5: 2 ВАРІАНТИ

**Завжди генерувати 2 варіанти!**

Надіслати окремими повідомленнями з поясненням:
```
Варіант 1: [опис чим відрізняється]
Варіант 2: [опис чим відрізняється]
```

---

### Крок 6: ЗБЕРЕЖЕННЯ В SUPABASE

**Автоматично, без питань!**

#### Таблиця `sessions`:
```json
{
  "id": "uuid",
  "user_id": "telegram:123456789",
  "created_at": "2026-02-27T14:30:00Z",
  "updated_at": "2026-02-27T14:35:00Z",
  "title": "Назва сесії",
  "metadata": {
    "requester": "Ім'я",
    "requester_id": "telegram:123456789",
    "track_count": 2,
    "status": "completed"
  }
}
```

#### Таблиця `messages` (2 записи):
```json
{
  "id": "uuid",
  "session_id": "uuid",
  "created_at": "2026-02-27T14:35:00Z",
  "role": "assistant",
  "content": "Назва треку (Варіант 1/2)",
  "metadata": {
    "track_name": "...",
    "track_url": "https://...",
    "variant": 1,
    "prompt": "повний промпт",
    "api_params": {...},
    "generated_at": "2026-02-27T14:35:00Z",
    "storage_path": "tracks/..."
  }
}
```

---

### Крок 7: ЛОГУВАННЯ

Записати в `memory/music-log.jsonl`:
```json
{
  "timestamp": "2026-02-27T14:35:00Z",
  "user_id": "telegram:337958464",
  "user_name": "Євген Шишов",
  "track_name": "Shishov's Walk - Part I",
  "variant": 1,
  "prompt": "[Intro][TB-303]...",
  "api_params": {...},
  "storage_url": "https://...",
  "session_id": "uuid"
}
```

---

## ✅ Чекліст

### Перед генерацією:
- [ ] Неймінг узгоджено
- [ ] Prompt з правильними тегами
- [ ] Async workflow налаштовано

### Після генерації:
- [ ] Завантажено в Supabase Storage
- [ ] Створено запис в `sessions`
- [ ] Створено 2 записи в `messages`
- [ ] Записано в `music-log.jsonl`
- [ ] Надіслано користувачу обидва варіанти

---

## 📁 Інші файли в цьому skill

| Файл | Призначення |
|------|-------------|
| `SKILL.md` | Загальна документація API |
| `WORKFLOW.md` | Цей файл — конкретний флоу |
| `MY_RULES.md` | Мій особистий чекліст |
| `BEST_PRACTICES.md` | Поради щодо промптів |
