# MusicAPI.ai Skill

## Структура папок

```
skills/music-api-ai/
├── README.md              ← вказівник що читати
├── SKILL.md               ← публічна API документація
├── WORKFLOW.md            ← детальний флоу
├── MY_RULES.md            ← мій чекліст
├── BEST_PRACTICES.md      ← поради
├── api/                   ← робота з API
│   └── endpoints.md
├── storage/               ← зберігання, Supabase
│   └── workflow.md
├── prompts/               ← prompt engineering
│   ├── lyrics-generation.md
│   └── style-generation.md
├── flows/                 ← готові сценарії
│   └── music-creation-flow.md
├── scripts/               ← скрипти
│   ├── client.js
│   ├── music-api-ai.js
│   ├── prompt-generator.js
│   └── track-generation.sh
└── examples/              ← приклади
    └── requests/          ← request-*.json
```

## Швидкий старт

1. **Перший раз?** → читай `WORKFLOW.md`
2. **API деталі?** → `api/endpoints.md`
3. **Prompt engineering?** → `prompts/`
4. **Готовий сценарій?** → `flows/music-creation-flow.md`
