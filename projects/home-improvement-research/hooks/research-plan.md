# План дослідження хуків

## Методологія

### Фаза 1: Збір (1-2 тижні)
Пасивний моніторинг — щоденне сканування джерел, запис у базу.

### Фаза 2: Аналіз (3-4 тиждень)
Кластеризація, визначення патернів, ранжування.

### Фаза 3: Верифікація (5-6 тиждень)
Перехресна перевірка, A/B тест гіпотез.

---

## Джерела для моніторингу

### 1. Facebook Ads Library
**URL:** https://www.facebook.com/ads/library

**Запити для пошуку:**
- "walk in shower"
- "bathroom remodel"
- "tub to shower conversion"
- "accessible shower"
- "senior shower"
- "shower installation"
- "free installation shower"

**Що фіксувати:**
- Текст хука
- CTA button
- Зображення/відео стиль
- Дата активності
- Регіон

### 2. Google Ads Transparency
**URL:** https://adstransparency.google.com/

**Запити:** ті ж самі + brand names

### 3. Афіліат-мережі (публічні лендінги)

**MaxBounty** — пошук offers у категорії Home Services
**ClickBank** — Home & Garden категорія
**CJ Affiliate** — Home Improvement

**Метод:** Реєстрація як affiliate → перегляд доступних offers → аналіз їхніх лендінгів

### 4. Прямі конкуренти (monitoring)

| Компанія | Що моніторити | Як часто |
|----------|--------------|----------|
| Bath Fitter | Головна сторінка, seasonal offers | Щодня |
| Re-Bath | Promotions page | Щодня |
| West Shore Home | Special offers, financing | Щодня |
| Jacuzzi Bath Remodel | Current deals | Щодня |
| HomeAdvisor | Lead gen форми, messaging | Щотижня |
| Angi | Pricing transparency, promos | Щотижня |

### 5. Native Ad Networks

**Taboola / Outbrain** — пошук за home improvement keywords
- Які headlines використовують?
- Які thumbnails?

---

## Категорії хуків для відстеження

### A. Фінансові стимули

| Тип | Приклади | Примітки |
|-----|----------|----------|
| Percentage discount | "Save up to 50%" | Звичайний, але ефективний |
| Fixed amount | "Save $500" | Конкретніше, менше friction |
| Bundle discount | "Shower + Installation package deal" | Підвищує AOV |
| Seasonal | "Spring Sale - Extra 15% off" | Ургентність |
| Rebate/Credit | "Up to $1000 tax credit" | Government programs |

### B. Сервісні стимули

| Тип | Приклади | Примітки |
|-----|----------|----------|
| Free installation | "Free Installation ($1500 value)" | Висока сприйнятлива цінність |
| Same-day install | "Installed in as little as 1 day" | Convenience factor |
| Next-day install | "Next day installation available" | Середня ургентність |
| Flexible financing | "0% APR for 12 months" | Знижує бар'єр входу |
| No payments | "No payments for 6 months" | Cash flow relief |

### C. Якісні гарантії

| Тип | Приклади | Примітки |
|-----|----------|----------|
| Lifetime warranty | "Lifetime warranty on acrylic" | Довгострокова впевненість |
| Satisfaction guarantee | "100% satisfaction guarantee" | Risk reversal |
| Price match | "We'll beat any competitor's price" | Конкурентне позиціонування |
| Certified installers | "Licensed & insured pros only" | Trust building |

### D. Соціальні докази

| Тип | Приклади | Примітки |
|-----|----------|----------|
| Review count | "Rated 4.9/5 by 10,000+ homeowners" | Об'єм = довіра |
| Specific testimonial | "The Johnsons, Denver CO" | Локальність |
| Celebrity/local figure | "As seen on HGTV" | Авторитет |
| Before/after | "See real transformations" | Візуальний proof |

---

## Аналіз тригерів

Для кожного хука фіксувати:

1. **На що націлений?**
   - Price sensitivity
   - Time urgency
   - Quality concern
   - Trust deficit
   - Convenience desire

2. **Який emotion hook?**
   - Fear (missing out, making wrong choice)
   - Greed (getting deal, saving money)
   - Pride (home improvement, status)
   - Relief (problem solved, hassle-free)
   - Belonging (join thousands of homeowners)

3. **Чому це CTA?**
   - Конкретність пропозиції
   - Обмеження в часі/кількості
   - Низький ризик
   - Висока сприйнятлива цінність

---

## Формат запису

```markdown
### Hook ID: HOOK-001
**Source:** Bath Fitter homepage, 2026-04-01
**Hook:** "Save up to $500 on your new shower + FREE installation"
**Type:** Financial + Service bundle
**Offer Format:** Fixed amount discount + free service
**Trigger:** Greed + Convenience
**Target Emotion:** "I'm getting a deal AND avoiding hassle"
**Why it works:** 
- Конкретна сума ($500) створює якорь цінності
- FREE installation — magic word
- "Up to" — compliance + FOMO
**Context:** Hero banner, seasonal spring promotion
**Screenshot:** hooks/screenshots/hook-001-bath-fitter.png
```

---

## Пріоритетність збору

**Тиждень 1-2:**
1. Bath Fitter, Re-Bath, West Shore Home — їхні головні
2. Facebook Ads Library — активні оголошення
3. Google search ads — top 10 results

**Тиждень 3-4:**
4. Афіліат-лендінги
5. Native ads
6. Email розсилки (підписка на конкурентів)

**Тиждень 5-6:**
7. Cross-analysis, визначення топ-5 патернів
8. Документація рекомендацій
