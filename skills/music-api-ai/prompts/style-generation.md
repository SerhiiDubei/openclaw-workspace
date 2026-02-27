# Style Generation — Генерація стилю

## Параметри

### style_weight (0.0 - 1.0)
Сила стилю. Више = чіткіше слідує тегам.
- **0.8-0.9** — оптимально

### weirdness_constraint (0.0 - 1.0)
Креативність. Више = експериментальніше.
- **0.5-0.7** — оптимально

## Теги інструментів

| Тег | Звук |
|-----|------|
| `[TB-303]` | Acid bass |
| `[Roland TR-909]` | Drums |
| `[Analog Synth]` | Synth leads |
| `[Distorted Bass]` | Heavy bass |
| `[Laser Synth]` | Laser sounds |

## Теги жанрів

| Жанр | Теги |
|------|------|
| Techno | `[Detroit Techno]`, `[Acid]`, `[Minimal]` |
| Post-Punk | `[Post Punk]`, `[Cold Wave]`, `[Dark Bass]` |
| Big Beat | `[Big Beat]`, `[Breakbeat]`, `[Aggressive]` |
| House | `[House]`, `[Four on the floor]` |

## negative_tags
Що уникати:
```json
"negative_tags": "pop, soft, melodic, low vocals"
```
