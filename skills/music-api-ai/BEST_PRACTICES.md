# MusicAPI.ai Best Practices

Наші напрацювання для генерації музики через MusicAPI.ai (Suno/Udio).

## Async Workflow (Не блокувати чат)

**Проблема:** Генерація займає 2-3 хвилини, користувач чекає без відповіді.

**Рішення:**
1. Одразу відповісти: "🎵 Трек у черзі! Чекаємо ~3 хвилини..."
2. Запустити фоновий трекер
3. Продовжувати спілкування
4. Надіслати трек окремим повідомленням коли готовий

**Реалізація:**
```bash
# Запуск трекера в фоні
./track-generation.sh TASK_ID USER_ID > /dev/null 2>&1 &
```

## Завжди 2 варіанти

MusicAPI.ai генерує 2 версії кожного треку. Завантажувати і надсилати **обидві**.

**Чому:** Користувач обирає який краще, або використовує обидва.

## Prompt Structure для MusicAPI.ai

**Формат:**
```
[Section][Tags][Tags]\nLyrics\n[Section][Tags]\nLyrics
```

**Приклад:**
```
[Intro][Post Punk][Cold Wave][Dark Bass]\nПід прозорим покровом ночі\n\n[Verse][Driving Bass][Ukrainian Lyrics]\nНе побачу у дзеркалі очі
```

## Теги секцій (важливі!)

Теги в квадратних дужках керують звучанням:

| Тег | Ефект |
|-----|-------|
| `[Intro]` | Початок треку |
| `[Verse]` | Куплет |
| `[Chorus]` | Приспів |
| `[Drop]` | Дроп (для електроніки) |
| `[Build Up]` | Наростання |
| `[Breakdown]` | Спад напруги |
| `[Outro]` | Завершення |

**Інструментальні теги:**
- `[TB-303]` — кислотний бас
- `[Roland TR-909]` — драм-машина
- `[Analog Synth]` — аналогові синти
- `[Distorted Bass]` — дисторшн бас
- `[Laser Synth]` — лазерні звуки

## Параметри запиту

**Важливі:**
- `style_weight: 0.8-0.9` — сила стилю (вище = чіткіше слідує тегам)
- `weirdness_constraint: 0.5-0.7` — креативність (вище = експериментальніше)
- `negative_tags` — що уникати ("pop, soft, melodic")

**gpt_description_prompt:**
- Max 350 символів
- Описує загальне звучання
- Приклад: "Ukrainian post-punk with cold wave atmosphere..."

## Мова пісень

**Працює краще:**
- Англійська — найкраща вимова
- Українська — прийнятна, але може бути акцент
- Змішана — 50/50 українська/англійська працює добре

**Теги для голосу:**
- `[High Vocals]` — високий голос
- `[Male Vocals]` — чоловічий
- `[Female Vocals]` — жіночий
- `[Falsetto]` — фальцет

## Жанрові специфіки

### Techno / House
- `[TB-303]`, `[Acid]`, `[Roland TR-909]`
- `[Four on the floor]` — класичний техно біт
- `[Warehouse Rave]` — енергія рейву

### Post-Punk / Cold Wave
- `[Cold Wave]`, `[Dark Bass]`, `[Reverb]`
- `[Melancholic]`, `[Atmospheric]`
- Ukrainian lyrics працюють добре

### Big Beat / Breakbeat
- `[Breakbeat Chaos]`, `[Distorted Bass]`
- `[Aggressive Energy]`, `[Punk Attitude]`
- The Prodigy style references

## Помилки та їх вирішення

| Проблема | Рішення |
|----------|---------|
| Трек занадто м'який | Додати `negative_tags: "soft, melodic"` |
| Голос низький | Додати `[High Vocals]`, `negative_tags: "low vocals"` |
| Не той жанр | Підвищити `style_weight` до 0.9 |
| Текст невиразний | Додати більше тегів до секцій |

## Приклади успішних prompts

**Detroit Techno:**
```
[Intro][Detroit Techno][Minimal][TB-303][Dark]
Бля бля сука бля

[Drop][Full Power][Acid Peak]
Бля бля сука бля!
```

**Post-Punk:**
```
[Verse][Post Punk][Cold Wave][Ukrainian Lyrics]
Під прозорим покровом ночі
```

**Big Beat:**
```
[Drop][Big Beat][Breakbeat][Aggressive]
Bass drops chaos reigns
```

## Робота з референс-аудіо (голосові мелодії)

**Коли користувач просить "взяти аудіо і написати трек":**

1. **Конвертувати** OGG → MP3 (FFmpeg)
2. **Закинути в Supabase Storage**
   - Bucket: `music`
   - Path: `references/USER_ID/filename.mp3`
3. **Записати в БД** (`media_files`)
   - `file_type`: `reference_audio`
   - `user_id`: хто надіслав
   - `metadata`: опис що це за мелодія
4. **Використати як референс**
   - Додати в `gpt_description_prompt`: "Inspired by user's reference audio..."
   - Описати стиль/настрій з аудіо
5. **Згенерувати трек** звичайним процесом
6. **Зберегти результат** в Supabase

**Приклад FFmpeg:**
```bash
ffmpeg -i input.ogg -codec:a libmp3lame -q:a 2 output.mp3
```

## Логування

Зберігати всі генерації в `memory/music-log.jsonl`:
- Дата/час
- Запит (prompt)
- Результат (URL треку)
- Хто замовив

## Інтеграція з Supabase

Зберігати метадані треків:
- `media_files` таблиця
- Bucket: `music`
- Теги: жанр, мова, хто замовив

---

*Останнє оновлення: 2026-02-19*
