# Home Improvement Research Project

## Опис
Дослідження хуків і візуалів для home improvement вертикалі (walk-in showers, bathroom remodeling, тощо).

## Структура

```
projects/home-improvement-research/
├── README.md                 # Цей файл
├── hooks/                    # Дослідження хуків
│   ├── research-plan.md      # План дослідження
│   ├── affiliate-sources.md  # Джерела афіліат-пропозицій
│   ├── hooks-database.md     # База зібраних хуків
│   └── analysis/             # Аналізи
│       ├── trigger-analysis.md
│       └── top-performers.md
├── images/                   # Зібрані зображення
│   ├── categories/           # Категоризовані
│   │   ├── family-with-people/
│   │   ├── luxury-quality/
│   │   ├── same-day-install/
│   │   ├── before-after/
│   │   └── minimalist/
│   └── raw/                  # Сирі завантаження
└── cron/                     # Cron job скрипти
    ├── hooks-research.sh
    └── image-collection.sh
```

## Supabase Integration

Таблиця для хуків:
```sql
CREATE TABLE home_improvement_hooks (
  id serial PRIMARY KEY,
  source text,
  hook_text text,
  hook_type text, -- discount, urgency, social_proof, guarantee, etc.
  offer_format text, -- percentage, fixed_amount, free_installation, same_day, etc.
  trigger_type text, -- fear, greed, convenience, trust, etc.
  target_emotion text,
  why_it_works text,
  context text, -- де знайдено
  screenshot_path text,
  created_at timestamp DEFAULT now()
);
```

Таблиця для зображень:
```sql
CREATE TABLE home_improvement_images (
  id serial PRIMARY KEY,
  category text, -- family, luxury, same-day, before-after, minimalist
  subcategory text, -- walk-in-shower, full-bathroom, etc.
  style text, -- modern, classic, spa, etc.
  has_people boolean,
  people_count int,
  emotion text, -- happy, relaxed, proud, etc.
  quality_focus text, -- materials, craftsmanship, accessibility, etc.
  storage_path text, -- шлях в Supabase Storage
  source_url text,
  tags jsonb,
  created_at timestamp DEFAULT now()
);
```

## Cron Jobs

### 1. Hooks Research (щоденно, 10:17)
- Пошук нових афіліат-оферів
- Аналіз конкурентів
- Оновлення бази хуків

### 2. Image Collection (щоденно, 14:23)
- Збір референсів з різних джерел
- Категоризація
- Завантаження в Supabase Storage

## Джерела для моніторингу

### Афіліат-мережі:
- MaxBounty
- ClickBank
- CJ Affiliate
- ShareASale
- Impact
- Awin

### Прямі конкуренти:
- Bath Fitter
- Re-Bath
- West Shore Home
- Jacuzzi Bath Remodel
- HomeAdvisor / Angi

### Способи моніторингу:
- Facebook Ad Library (пошук за keywords)
- Google Ads Transparency
- Native ad networks (Taboola, Outbrain)
- Landing page scrapers
- Affiliate newsletters
