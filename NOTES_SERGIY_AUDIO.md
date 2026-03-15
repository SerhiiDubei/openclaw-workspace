# Правила роботи з аудіо Сергія (bomberman047)

## Де зберігаються файли

### Оригінальні голосові повідомлення
```
/root/.openclaw/media/inbound/
├── file_xxx---uuid.ogg  ← свіжі файли
```

### Референси для SunoAPI
```
Supabase: music/references/Sergiy/YYYY-MM-DD/
├── Sergiy-Source.mp3
```

### Завантажені треки
```
/tmp/music_output/
├── Sergiy - {Track Name} - v1.mp3
└── Sergiy - {Track Name} - v2.mp3
```

## Флоу обробки аудіо

```
1. Користувач надсилає аудіо (OGG)
   ↓
2. OpenClaw зберігає в /root/.openclaw/media/inbound/
   ↓
3. Я знаходжу файл: ls -lt /root/.openclaw/media/inbound/*.ogg
   ↓
4. Конвертую OGG → MP3: ffmpeg -i input.ogg output.mp3
   ↓
5. Завантажую в Supabase Storage (публічний URL)
   ↓
6. Відправляю URL в SunoAPI /generate/upload-cover
   ↓
7. Чекаю SUCCESS, завантажую 2 варіанти
   ↓
8. Надсилаю користувачеві
```

## Команди для швидкого доступу

```bash
# Знайти свіжі аудіо
ls -lt /root/.openclaw/media/inbound/*.ogg | head -5

# Конвертувати останній файл
ffmpeg -i /root/.openclaw/media/inbound/file_300-xxx.ogg /tmp/sergiy_latest.mp3 -y

# Перевірити Supabase референси
ls /root/.openclaw/workspace/music/references/Sergiy/
```

## Важливо

- ЗАВЖДИ використовувати свіжий файл з /root/.openclaw/media/inbound/
- НІКОЛИ не брати старі референси без підтвердження
- Після генерації логувати в memory/music-log.jsonl

## Контакти
- Telegram: @bomberman047
- ID: 488426634
