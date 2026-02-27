# USER_ONBOARDING.md — Інструкція для нових користувачів

## Коли додавати нового користувача

Додавати ТІЛЬКИ після підтвердження від Сергія (@bomberman047).

## Кроки onboarding

### 1. Отримати інформацію
- Telegram ID (формат: `telegram:123456789`)
- Username (опціонально)
- Ім'я для відображення

### 2. Створити структуру папок

```bash
mkdir -p memory/users/{username}/sessions
mkdir -p memory/users/{username}/pinned
```

### 3. Створити profile.md

Шаблон:
```markdown
# Профіль: [Ім'я]

## Основна інформація
- **ID:** [telegram ID]
- **Username:** @[username]
- **Роль:** Користувач
- **Додано:** [YYYY-MM-DD]

## Інтереси
- [список інтересів]

## Типи контенту
- `session` — звичайні сесії (кеш медіа 7 днів)
- `pinned` — закріплені файли (постійно)
- `insight` — важливі ідеї (постійно)
```

### 4. Оновити cache-config.json

Додати в масив `users`:
```json
{
  "id": "telegram:123456789",
  "username": "new-username",
  "folder": "memory/users/new-username"
}
```

### 5. Створити insights.md (порожній)

```bash
touch memory/users/{username}/insights.md
```

### 6. Закомітити зміни

```bash
git add -A
git commit -m "Add new user: [username]"
git push origin main
```

### 7. Прив'язка треків до користувача

**ВАЖЛИВО:** При створенні треку через music-api-ai:
- Перевірити хто замовник (запитати ім'я/ID)
- Записати сесію в Supabase з правильним `user_id`
- Завантажити треки в Storage одразу після генерації
- НЕ чекати підтвердження — робити автоматично

**Структура даних для збереження треків:**

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

**Приклад SQL для створення запису:**
```sql
-- Створити сесію
INSERT INTO sessions (user_id, title, metadata)
VALUES ('telegram:337958464', 'Detroit Acid Track', 
        '{"requester": "Євген Шишов", "track_count": 2}'::jsonb)
RETURNING id;

-- Створити повідомлення з треком
INSERT INTO messages (session_id, role, content, metadata)
VALUES (
  'session-uuid',
  'assistant',
  'Shishov - Detroit Acid (Варіант 1)',
  '{
    "track_name": "Shishov - Detroit Acid",
    "track_url": "https://.../tracks/...mp3",
    "variant": 1,
    "prompt": "[Intro][TB-303][Acid]...",
    "api_params": {"style_weight": 0.8, ...},
    "generated_at": "2026-02-27T14:35:00Z"
  }'::jsonb
);
```

---

## Важливі правила

- **НЕ створювати** користувачів без підтвердження
- **НЕ видаляти** існуючих користувачів без дозволу
- **Завжди питати** перед зміною структури

## Поточні користувачі

| ID | Username | Папка |
|----|----------|-------|
| telegram:488426634 | serhii-dubei | `memory/users/serhii-dubei/` |
| telegram:542906702 | mental-ninja | `memory/users/mental-ninja/` |
| telegram:337958464 | evgen-shishov | `memory/users/evgen-shishov/` |
