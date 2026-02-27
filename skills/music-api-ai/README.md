# MusicAPI.ai Skill

## Структура

```
skills/music-api-ai/
├── WORKFLOW.md              ← ПОЧНИ ТУТ (головний флоу)
├── SKILL.md                 ← Мінімальна публічна документація
├── MY_RULES.md              ← Мій чекліст
├── api/
│   └── endpoints.md         ← API endpoints
├── storage/
│   └── storage_workflow.md  ← Supabase зберігання
├── prompts/
│   ├── lyrics-generation.md ← Генерація текстів
│   └── style-generation.md  ← Генерація стилю
├── flows/
│   └── music-creation-flow.md  ← Тригерний флоу
├── scripts/                 ← Скрипти
└── examples/requests/       ← Приклади запитів
```

## Швидкий старт

| Якщо ти... | Йди сюди |
|------------|----------|
| Вперше генеруєш | `WORKFLOW.md` |
| Потрібен API | `api/endpoints.md` |
| Потрібні тексти | `prompts/lyrics-generation.md` |
| Потрібен стиль | `prompts/style-generation.md` |
| Потрібно зберегти | `storage/storage_workflow.md` |
| Тригер "створити трек" | `flows/music-creation-flow.md` |
