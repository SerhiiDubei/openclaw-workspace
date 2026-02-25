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
