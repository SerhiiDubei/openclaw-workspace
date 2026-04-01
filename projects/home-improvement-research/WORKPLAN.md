# Home Improvement Research — План роботи

## Створена інфраструктура

### 📁 Файлова структура
```
projects/home-improvement-research/
├── README.md
├── hooks/
│   ├── research-plan.md      # Детальний план дослідження хуків
│   ├── affiliate-sources.md  # (додамо пізніше)
│   ├── hooks-database.md     # (додамо пізніше)
│   └── analysis/
│       ├── trigger-analysis.md
│       └── top-performers.md
├── images/
│   ├── research-plan.md      # План збору зображень
│   └── categories/
│       ├── family-with-people/
│       ├── luxury-quality/
│       ├── same-day-install/
│       ├── before-after/
│       └── minimalist/
└── cron/
    ├── hooks-research.sh     # Скрипт для хуків
    └── image-collection.sh   # Скрипт для зображень
```

### 🗄️ Supabase таблиці

**home_improvement_hooks:**
- `hook_text` — текст хука
- `hook_type` — тип (discount, urgency, social_proof, guarantee)
- `offer_format` — формат (percentage, fixed_amount, free_installation, same_day)
- `trigger_type` — тригер (fear, greed, convenience, trust)
- `target_emotion` — цільова емоція
- `why_it_works` — аналіз чому працює
- `source` — джерело

**home_improvement_images:**
- `category` — категорія
- `has_people` — чи є люди
- `emotion` — емоція
- `quality_focus` — фокус на якості
- `storage_path` — шлях в Storage

### ⏰ Cron Jobs (активні)

| Час | Завдання | Опис |
|-----|----------|------|
| **10:17** | Hooks Research | Перевірка конкурентів, Facebook Ad Library, запис хуків в БД |
| **14:23** | Image Collection | Збір зображень з Unsplash/Pexels, категоризація, upload в Storage |

---

## Як ділити роботу

### Поток 1: Hooks (щоденно, 10:17)
Кожен запуск:
1. **Сканування** — перевірка 3-5 конкурентів
2. **Facebook Ads** — пошук за 5-8 keywords
3. **Запис** — нові хуки → Supabase
4. **Категоризація** — автоматичне визначення типу
5. **Звіт** — summary в Telegram

### Поток 2: Images (щоденно, 14:23)
Кожен запуск:
1. **Пошук** — 1 категорія за раз (ротація)
2. **Відбір** — мін 1200px, висока якість
3. **Завантаження** → Supabase Storage
4. **Метадані** — теги, емоції, контекст
5. **Звіт** — кількість доданих

### Ручна робота (раз на тиждень)
- **Аналіз affiliate-мереж** — MaxBounty, ClickBank
- **Глибокий аналіз** — тригери, емоції, чому працює
- **Оновлення планів** — коригування стратегії

---

## Що робити зараз

### ✅ Вже зроблено:
- [x] Структура проєкту
- [x] Supabase таблиці
- [x] Cron jobs (10:17, 14:23)
- [x] Плани дослідження

### 🔄 Сьогодні запуститься:
- 10:17 — перший збір хуків
- 14:23 — перший збір зображень

### 📋 Твої наступні кроки (опціонально):
1. Перевірити перші результати cron jobs
2. Дати доступ до Unsplash API (для кращого пошуку)
3. Додати ще джерела (підписка на розсилки конкурентів)

---

## Очікуваний результат через 2 тижні

**Hooks:**
- 50-100 зібраних хуків
- Категоризація за типами
- Топ-10 патернів з аналізом

**Images:**
- 200+ зображень в категоріях
- Метадані для кожного
- Рекомендації для hero page

---

## Команда для ручного запуску

Якщо хочеш запустити дослідження прямо зараз:

```bash
# Хуки
/root/.openclaw/workspace/skills/supabase/scripts/supabase.sh \
  insert home_improvement_hooks \
  '{"source":"test","hook_text":"test"}'

# Перевірка
/root/.openclaw/workspace/skills/supabase/scripts/supabase.sh \
  select home_improvement_hooks --limit 5
```
