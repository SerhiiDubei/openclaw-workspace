# MusicAPI.ai Skill

Generate AI music through MusicAPI.ai unified API.

## Швидкий старт

1. Читай `WORKFLOW.md` — повний флоу
2. Дивись `prompts/` — lyrics та style
3. Дивись `api/endpoints.md` — API деталі
4. Дивись `storage/storage_workflow.md` — зберігання

## API Configuration

- **Base URL:** `https://api.musicapi.ai/api/v1/sonic/`
- **Auth:** Bearer token
- **Model:** `sonic-v5`

## Структура

```
skills/music-api-ai/
├── WORKFLOW.md              ← Почни тут
├── api/endpoints.md         ← API
├── prompts/                 ← Lyrics + Style
├── storage/storage_workflow.md  ← Supabase
└── flows/                   ← Тригери
```
