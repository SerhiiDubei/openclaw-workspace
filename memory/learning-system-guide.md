# Learning Music Generation System

## Workflow

### Крок 1: Генерація Draft
На основі запиту + supertracks створюю:
1. **Lyrics with metatags** — текст пісні з розміткою
2. **Style description** — опис продакшну
3. **Parameters** — технічні параметри

### Крок 2: Твій Review
Відправляю тобі:
```
🎵 DRAFT: [Назва пісні]

📜 LYRICS:
[Intro][Instrument][Style]
...

🎨 STYLE DESCRIPTION:
...

⚙️ PARAMETERS:
BPM: ...
Key: ...
Tags: ...

❓ Твої дії:
✅ Approve — генерувати
❌ Reject — скасувати  
💬 Comment — вказати зміни
```

### Крок 3: Обробка Коментарів
Якщо коментарі:
- **Розпізнаю тип** — lyrics/style/vocal/structure
- **Зберігаю патерн** — що ти змінив
- **Оновлю draft** — перегенерую з правками
- **Повторю review** — поки не approve

### Крок 4: Навчання
Кожен коментар:
- Додається в `learning-patterns.json`
- Аналізується для кореляцій
- Використовується в наступних генераціях
- Оновлює main prompt еволюцію

## Приклад Learning

**Твоє коментування:**
> "Зроби більше vinyl crackle і додай gospel choir"

**Що зберігається:**
```json
{
  "requestType": "deep house",
  "feedback": {
    "fx": ["more vinyl crackle"],
    "vocals": ["add gospel choir"]
  },
  "applied": true,
  "timestamp": "..."
}
```

**Наступний раз:**
- Автоматично додаю vinyl + gospel для deep house
- Підвищую confidence score
- Можу запропонувати auto-approve

## Auto-Approve

Після 3 успішних approve для схожих запитів:
- Пропоную auto-approve mode
- Ти все ще можеш коментувати
- Але генерація йде швидше

## Команди

| Команда | Дія |
|---------|-----|
| `approve` / `так` / `кайф` | Генерувати пісню |
| `reject` / `ні` / `не так` | Скасувати |
| `більше [X]` | Додати/посилити елемент |
| `менше [X]` | Прибрать/зменшити елемент |
| `зміни [Y]` | Замінити елемент |
| `додай [Z]` | Додати новий елемент |

## Готовий тестувати?

Скажи що згенерувати — покажу новий workflow!