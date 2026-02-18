---
name: music-api-ai
description: |
  Generate AI music using MusicAPI.ai (Suno/Udio/ElevenLabs via unified API).
  Full pipeline: prompt generation → task creation → status polling → audio delivery.
  Supports sonic-v5 model with custom_mode for high-quality vocal and instrumental tracks.
allowed-tools:
  - Read
  - Write
  - Edit
  - Exec
  - WebFetch
  - Message
---

# MusicAPI.ai Skill

Generate AI music through MusicAPI.ai unified API.

## API Configuration

- **Base URL:** `https://api.musicapi.ai/api/v1/sonic/`
- **Auth:** Bearer token in header
- **Model:** `sonic-v5` (latest, best quality)
- **Mode:** `custom_mode: true`

## Workflow

1. **Generate Prompt** — expand user request into full production prompt
2. **Create Task** — POST /create with parameters
3. **Poll Status** — GET /task/{task_id} until complete
4. **Deliver Audio** — download and send to user

## Request Format

```json
{
  "custom_mode": true,
  "prompt": "[Intro][Guitar][Folk]\\nSong lyrics here...\\n[Outro][Fade]",
  "title": "Song Title",
  "tags": "genre,style,mood",
  "style_weight": 0.8,
  "weirdness_constraint": 0.5,
  "negative_tags": "elements to avoid",
  "gpt_description_prompt": "Production description (max 350 chars)",
  "make_instrumental": false,
  "mv": "sonic-v5"
}
```

## Response Handling

- **Pending:** Task queued, wait and poll
- **Processing:** Generation in progress
- **Complete:** Audio URL available for download
- **Failed:** Error message, retry or report

## Output

Send audio file to user's channel (Telegram supports up to 50MB).

## History

Log all generations locally in `memory/music-log.jsonl` with metadata.
