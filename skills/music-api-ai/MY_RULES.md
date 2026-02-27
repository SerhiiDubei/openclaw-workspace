# MusicAPI.ai - Мої інструкції

## ОБОВ'ЯЗКОВИЙ ФЛОУ (читати перед кожною генерацією!)

### 1. НЕЙМІНГ (запитати спочатку!)
- Формат: `[Хто замовив] - [Стиль/Жанр]`
- Приклади: "Ромко і Сергій - Detroit Acid", "Shishov's Walk - Part I"
- Запитати: "Хто замовляє і як назвати трек?"

### 2. PROMPT FORMAT (з BEST_PRACTICES.md)
```
[Intro][Instrument][Style] Текст
[Verse][Instrument][Style] Текст
[Chorus][Instrument][Style] Текст
[Outro][Instrument][Style] Текст
```
- Теги інструментів: [TB-303], [Roland TR-909], [Analog Synth]
- Теги стилю: [Acid], [Detroit Techno], [Dark Bass]

### 3. ASYNC WORKFLOW
- НЕ блокувати чат
- Відповісти: "🎵 Трек у черзі! Чекаємо ~3 хвилини..."
- Запустити фоновий трекер
- Надіслати результат окремим повідомленням

### 4. ЗАВЖДИ 2 ВАРІАНТИ
- Надіслати обидва окремими повідомленнями
- З поясненням який який

### 5. АВТОМАТИЧНЕ ЗБЕРЕЖЕННЯ В SUPABASE
- Відразу після отримання треків — завантажити в Supabase Storage
- Створити запис в таблиці `sessions`
- Створити записи в таблиці `messages` (2 варіанти)
- НЕ питати підтвердження — робити автоматично

**Структура даних для запису:**

#### Таблиця `sessions`:
```json
{
  "id": "uuid",
  "user_id": "telegram:123456789",
  "created_at": "2026-02-27T14:30:00Z",
  "updated_at": "2026-02-27T14:35:00Z",
  "title": "Назва сесії (запит користувача)",
  "metadata": {
    "requester": "Ім'я замовника",
    "requester_id": "telegram:123456789",
    "track_count": 2,
    "status": "completed"
  }
}
```

#### Таблиця `messages` (2 записи — по одному на кожен варіант):
```json
{
  "id": "uuid",
  "session_id": "uuid (посилання на sessions)",
  "created_at": "2026-02-27T14:35:00Z",
  "role": "assistant",
  "content": "Назва треку: [Хто] - [Стиль] (Варіант 1/2)",
  "metadata": {
    "track_name": "Повна назва треку",
    "track_url": "URL в Supabase Storage",
    "variant": 1,
    "prompt": "Повний текст промпта який був відправлений в API",
    "api_params": {
      "custom_mode": true,
      "style_weight": 0.8,
      "weirdness_constraint": 0.5,
      "mv": "sonic-v5",
      "tags": "жанр,стиль,настрій",
      "negative_tags": "що уникати",
      "make_instrumental": false,
      "gpt_description_prompt": "опис для генерації"
    },
    "generated_at": "2026-02-27T14:35:00Z",
    "storage_path": "tracks/user_id/timestamp/track_name.mp3"
  }
}
```

#### Обов'язкові поля для збереження:
| Поле | Опис | Приклад |
|------|------|---------|
| `user_id` | ID користувача в Telegram | `telegram:337958464` |
| `created_at` | Час створення (ISO 8601) | `2026-02-27T14:30:00Z` |
| `prompt` | Повний промпт для API | `[Intro][TB-303][Acid]...` |
| `api_params` | Всі параметри API запиту | `{style_weight: 0.8, ...}` |
| `track_url` | URL в Supabase Storage | `https://.../tracks/...mp3` |
| `variant` | Номер варіанту (1 або 2) | `1` |

### 6. ЛОГУВАННЯ
- Записати в `memory/music-log.jsonl`
- Хто замовив, назва, URL

**Формат запису:**
```json
{
  "timestamp": "2026-02-27T14:35:00Z",
  "user_id": "telegram:337958464",
  "user_name": "Євген Шишов",
  "track_name": "Shishov's Walk - Part I",
  "variant": 1,
  "prompt": "[Intro][TB-303][Acid]...",
  "api_params": {...},
  "storage_url": "https://...",
  "session_id": "uuid"
}
```

### 7. ПАРАМЕТРИ
- `style_weight`: 0.8-0.9
- `weirdness_constraint`: 0.5-0.7
- `mv`: sonic-v5
- `negative_tags`: що уникати

---

## Чекліст перед генерацією:
- [ ] Неймінг узгоджено (хто замовляє + назва)
- [ ] Prompt з правильними тегами
- [ ] Async workflow
- [ ] Логування налаштовано
- [ ] Supabase credentials доступні

## Чекліст після генерації:
- [ ] Завантажено в Supabase Storage
- [ ] Створено запис в `sessions`
- [ ] Створено 2 записи в `messages` з повними metadata
- [ ] Записано в `memory/music-log.jsonl`
- [ ] Надіслано користувачу обидва варіанти
