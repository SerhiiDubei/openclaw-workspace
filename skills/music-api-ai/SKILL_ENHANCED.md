---
name: music-api-ai-enhanced
description: |
  Enhanced AI music generation with Base of Knowledge validation.
  Uses supertracks database for style consistency and quality control.
  Two-stage pipeline: generation → validation against supertracks → refinement.
allowed-tools:
  - Read
  - Write
  - Edit
  - Exec
  - WebFetch
  - Message
---

# MusicAPI.ai Enhanced Skill

Generate AI music through MusicAPI.ai with Base of Knowledge validation.

## Base of Knowledge Location
`/root/.openclaw/memory/supertracks-db-global.json` (shared across all users)

## Two-Stage Pipeline

### Stage 1: Generation
Use ELITE AI MUSIC PRODUCTION SPECIALIST v2.1 to generate initial track.

### Stage 2: Validation
Compare generated track against supertracks database:
- Genre alignment
- Vocal style consistency
- Instrument palette match
- Structure quality
- Unique features presence

## Supertrack Patterns (Common Elements)

### Vocal Styles
- spoken-word cadence
- gospel choir call-and-response
- mantra-like repetition
- baritone-lyrical intimate
- half-spoken half-rapped detached

### Instrument Palette
- Analog/Moog bass (warm, round)
- Rhodes piano (dusty, warm)
- Lo-fi drum machines (808/909)
- Vinyl crackle and tape hiss
- Church organ and gospel pads

### FX Signature
- Vinyl crackle, tape saturation
- Room reverb tails, micro-delays
- Chorus haze, AM radio filters

### User Signature Elements
- Ukrainian philosophical poetry
- Vintage analog warmth
- Gospel/soul vocal textures
- Lo-fi dusty aesthetic
- Church/religious ambience

## Validation Checklist

Before submitting to API, verify:
- [ ] Character count: 1650-2100
- [ ] Metatags format: [Section][Instrument][Style]
- [ ] Genre matches request or supertrack reference
- [ ] Vocal style aligns with user preference
- [ ] Instrument palette includes signature elements
- [ ] Structure follows proven patterns
- [ ] Lyrics end with [Outro], no meta after

## Quality Gates

### Gate 1: Format Validation
- Proper JSON structure
- Required fields present
- Character count in range

### Gate 2: Style Validation
- Compare against closest supertrack
- Check genre alignment
- Verify vocal character

### Gate 3: Signature Validation
- At least 2 signature elements present
- Ukrainian language if requested
- Analog warmth indicators

## Request Format

```json
{
  "custom_mode": true,
  "title": "Track Title",
  "prompt": "[Intro][Instrument][Style]\\nLyrics...",
  "tags": "genre,style,mood",
  "style_weight": 0.8,
  "weirdness_constraint": 0.5,
  "negative_tags": "elements to avoid",
  "gpt_description_prompt": "Production description (max 350 chars)",
  "make_instrumental": false,
  "mv": "sonic-v5"
}
```

## Supertrack Matching

When user requests a track:
1. Identify closest supertrack by genre/mood
2. Use as reference for structure and style
3. Adapt to user's specific request
4. Validate output against reference

## Output Format

After validation, provide:
1. Final JSON for API
2. Validation report (which supertracks matched)
3. Confidence score
4. Suggested improvements if any
