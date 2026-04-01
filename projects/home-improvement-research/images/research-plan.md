# План збору зображень

## Методологія

### Фаза 1: Визначення категорій
Структура папок вже створена — 5 основних категорій.

### Фаза 2: Збір референсів
Пошук за ключовими словами, завантаження, первинна категоризація.

### Фаза 3: Детальний аналіз
Тегування, опис емоцій, контекст використання.

---

## Категорії зображень

### 1. Family / With People
**Опис:** Зображення з людьми — сімейні сцени, користування продуктом.

**Підкатегорії:**
- Senior couple (основний сегмент для accessible showers)
- Middle-aged couple
- Family with kids
- Single person (relaxation focus)

**Емоції для відстеження:**
- Happy, satisfied
- Relaxed, spa-like
- Proud (showing off)
- Safe, secure (for accessibility)

**Ключові слова для пошуку:**
- "happy couple bathroom"
- "senior walk in shower"
- "family enjoying new bathroom"
- "accessible shower elderly"

### 2. Luxury / Quality Focus
**Опис:** Акцент на матеріали, ремесло, дизайнерські деталі.

**Підкатегорії:**
- Marble/granite textures
- Glass enclosures
- Premium fixtures
- Lighting design

**Ключові слова:**
- "luxury walk in shower"
- "marble bathroom design"
- "spa shower design"
- "high end bathroom remodel"

### 3. Same-Day / Speed
**Опис:** Візуалізація швидкості, процесу, "before-during-after".

**Підкатегорії:**
- Installation process
- Timeline graphics
- Worker in action
- Completed in one day

**Ключові слова:**
- "one day bathroom remodel"
- "fast shower installation"
- "same day bathroom"
- "quick bathroom renovation"

### 4. Before / After
**Опис:** Контрастні пари — трансформація.

**Підкатегорії:**
- Tub to shower conversion
- Outdated → Modern
- Cramped → Spacious
- Unsafe → Accessible

**Ключові слова:**
- "bathroom before after"
- "tub to shower conversion before after"
- "shower remodel transformation"

### 5. Minimalist / Clean
**Опис:** Простір, світло, чисті лінії — без людей, фокус на продукт.

**Підкатегорії:**
- White/clean aesthetic
- Open walk-in design
- Glass & light
- Modern fixtures

**Ключові слова:**
- "minimalist walk in shower"
- "modern bathroom design"
- "clean bathroom aesthetic"
- "white shower design"

---

## Джерела для збору

### 1. Конкуренти (скріншоти)
- Bath Fitter gallery
- Re-Bath portfolio
- Houzz профілі contractors
- HomeAdvisor project photos

### 2. Stock фото (безкоштовні)
- Unsplash — unsplash.com/s/photos/walk-in-shower
- Pexels — pexels.com/search/walk%20in%20shower/
- Pixabay

### 3. Stock фото (платні — для референсів)
- Shutterstock
- Adobe Stock
- iStock

### 4. Pinterest
- Пошук за "walk in shower ideas"
- Дошки bathroom remodeling

### 5. Instagram
- Хештеги: #walkinshower #bathroomremodel #showerdesign
- Акаунти: @bathrooms_of_insta, @bathroomdecor

---

## Формат метаданих

Для кожного зображення створюємо JSON:

```json
{
  "id": "IMG-001",
  "filename": "luxury-marble-shower-001.jpg",
  "category": "luxury-quality",
  "subcategory": "marble-textures",
  "style": "modern",
  "has_people": false,
  "people_count": 0,
  "demographic": null,
  "emotion": "aspirational",
  "quality_focus": "materials",
  "color_palette": ["white", "gray", "gold"],
  "lighting": "natural",
  "composition": "centered",
  "source": "unsplash.com/photos/xxx",
  "photographer": "Name",
  "license": "unsplash-free",
  "tags": ["marble", "luxury", "spa", "gold-fixtures"],
  "hero_suitable": true,
  "notes": "Strong aspirational quality, good for premium positioning"
}
```

---

## Supabase Storage структура

```
bucket: home-improvement-images
├── family-with-people/
│   ├── seniors/
│   ├── couples/
│   └── families/
├── luxury-quality/
│   ├── marble/
│   ├── glass/
│   └── fixtures/
├── same-day-install/
├── before-after/
└── minimalist/
```

---

## Щоденні ліміти

- Максимум 50 зображень на день
- Пріоритет: конкуренти → Unsplash → Pinterest
- Тільки висока якість (min 1200px width)
- Перевірка на дублікати перед завантаженням
