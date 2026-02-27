# MusicAPI.ai Skill

## Структура папок

```
skills/music-api-ai/
├── README.md              ← вказівник що читати
├── SKILL.md               ← публічна API документація
├── WORKFLOW.md            ← детальний флоу
├── MY_RULES.md            ← мій чекліст
├── api/                   ← робота з API
│   └── endpoints.md
├── storage/               ← зберігання, Supabase
│   └── storage_workflow.md
├── prompts/               ← prompt engineering
│   ├── lyrics-generation.md
│   └── style-generation.md
├── flows/                 ← готові сценарії
│   └── music-creation-flow.md
├── scripts/               ← скрипти
│   ├── client.js          ← HTTP клієнт для API
│   ├── music-api-ai.js    ← головний CLI
│   ├── prompt-generator.js ← генератор промптів
│   └── track-generation.sh ← фоновий трекер
├── examples/              ← приклади промптів
│   └── *.json
└── requests/              ← збережені запити
    └── *.json
```

## Швидкий старт

1. **Перший раз?** → читай `WORKFLOW.md`
2. **API деталі?** → `api/endpoints.md`
3. **Prompt engineering?** → `prompts/`
4. **Готовий сценарій?** → `flows/music-creation-flow.md`

## Скрипти

| Скрипт | Призначення |
|--------|-------------|
| `client.js` | HTTP клієнт: createTask, checkStatus, pollUntilComplete |
| `music-api-ai.js` | Головний CLI: generateMusic, submitToAPI, saveToSupabase |
| `prompt-generator.js` | Парсинг запитів + генерація промптів |
| `track-generation.sh` | Фоновий трекер, записує в Supabase |
