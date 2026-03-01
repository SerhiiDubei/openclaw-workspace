# Music Storage Naming Rules

## User Folders
- Використовувати латиницю (транслітерація з кирилиці)
- Пробіли замість підкреслень
- Кожне слово з великої літери

### Приклади:
- `Serhii Dubei` (не `Serhii_Dubei`)
- `Roman Romanyuk` (не `Роман Романюк`)
- `Dmitrii Churilov`
- `Evgen Shishov`

## Структура папок
```
music/tracks/
├── {Username}/
│   ├── {YYYY-MM-DD}/
│   │   └── {Username} - {Track Name} - v{1|2}.mp3
```

## Формат файлів
`{Username} - {Track Name} - v{variant}.mp3`

### Приклади:
- `Serhii Dubei - Detroit Techno - v1.mp3`
- `Roman Romanyuk - Cosmic Journey - v2.mp3`

## Заборонено
- Кирилиця в шляхах (Supabase Storage не підтримує)
- Підкреслення замість пробілів
- Малі літери на початку слів
