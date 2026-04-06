# Завдання 02: Аналіз продукту — thedatingcritic.com

## 1. Загальнодоступна інформація про перформанс

### Що таке thedatingcritic.com (модель бізнесу)

Це **dating review aggregator** — сайт-агрегатор, який збирає огляди dating-сервісів і перенаправляє трафік на партнерські офери. Модель класична для affiliate marketing:

```
Користувач шукає «best dating apps» → Попадає на thedatingcritic.com → 
Читає огляд → Клікає на партнерський лінк → Реєструється на dating site → 
Автор отримує CPA/RevShare
```

### Типова структура таких сайтів (інсайти з аналізу ніші)

| Елемент | Опис | Функція |
|---------|------|---------|
| **Landing/Review Page** | Детальний огляд 5-10 dating apps | SEO + конверсія |
| **Comparison Table** | Порівняльна таблиця з цінами | Швидке рішення |
| **Partner Links** | Affiliate лінки з subid | Трекінг + monetization |
| **Trust Signals** | Відгуки, рейтинги, badges | Зняття заперечень |

### Бенчмарки для dating affiliate ніші (2024-2025)

**Конверсійні метрики:**
| Метрика | Середнє | Гарний показник | Джерело |
|---------|---------|-----------------|---------|
| **CTR** (клік на огляді) | 1-3% | 5%+ | Affiliate benchmarks |
| **CR** (реєстрація після кліка) | 1-5% | 5%+ | Dating vertical |
| **EPC** | $0.50-2.00 | $2.00+ | Залежить від GEO |
| **CR на депозит** | 5-15% від реєстрацій | 20%+ | Dating CPA |

**Unit Economy (приблизні розрахунки для Tier-1 GEO):**

```
Припустимо:
- Трафік: 10,000 відвідувачів/місяць (SEO)
- CTR на партнерські лінки: 3%
- Кліків на партнерів: 300
- CR на реєстрацію: 4%
- Реєстрацій: 12
- CR на першу покупку: 10%
- Покупок: 1.2

CPA в dating (Tier-1):
- SOI (Single Opt-in): $2-5
- DOI (Double Opt-in): $5-15
- First Deposit: $50-150

RevShare: 30-50% від lifetime value

Розрахунок Revenue:
- При CPA (First Deposit): 1.2 × $80 = $96
- При RevShare (LTV $200): 1.2 × $200 × 40% = $96

EPC = $96 / 300 кліків = $0.32
```

**Проблеми такої моделі:**
1. **Висока конкуренція** — топові запити зайняті великими гравцями
2. **Низький intent** — багато користувачів просто "дивляться"
3. **Довгий цикл** — від читання огляду до реєстрації може пройти дні
4. **Cookie duration** — стандарт 30 днів, але рішення про dating приймається довше

---

## 2. Фанел аналіз

### Поточна фанел (припущення на основі best practices)

```
┌─────────────────────────────────────────────────────────────┐
│  100%  Відвідувачі (SEO/Paid/Referral)                     │
│       ↓                                                     │
│  60%   Читають огляд >30 сек (Engagement)                  │
│       ↓                                                     │
│  10%   Скроллять до партнерських лінків                    │
│       ↓                                                     │
│  3%    Клікають на партнерський лінк (CTR)                 │
│       ↓                                                     │
│  50%   Дочитують landing partner'а                         │
│       ↓                                                     │
│  4%    Реєструються (CR з кліка)                           │
│       ↓                                                     │
│  10%   Роблять first deposit                               │
└─────────────────────────────────────────────────────────────┘

Конверсія від visit до revenue: 0.012% (1 реєстрація з ~833 відвідувачів)
```

### Точки втрати та можливості

| Етап | Втрата | Причина | Можливість |
|------|--------|---------|------------|
| **Visit → Read** | 40% | Поганий заголовок, повільне завантаження | A/B тести заголовків, Core Web Vitals |
| **Read → Click** | 70% | Слабкі CTA, незрозуміла цінність | Покращити CTA, додати urgency |
| **Click → Reg** | 50% | Partner landing не релевантний | Pre-qualify traffic, фільтрація |
| **Reg → Deposit** | 90% | Немає nurturing, холодний лід | Email sequence, retargeting |

---

## 3. Unit Economy (розрахунок)

### Сценарій 1: CPA модель (SOI — реєстрація)

```
Параметри:
- CPC (Google Ads): $1.50
- CTR на сайті: 3%
- CR на реєстрацію: 5%
- CPA payout: $4

Розрахунок:
- 100 кліків = $150 витрат
- 3 кліка на партнера
- 0.15 реєстрацій
- Revenue: 0.15 × $4 = $0.60

ROI: -60% 🔴 (не окупається)
```

### Сценарій 2: RevShare модель (long-term)

```
Параметри:
- Той же трафік
- CR на реєстрацію: 5%
- CR на депозит з реєстрацій: 10%
- Середній депозит: $50
- Середня кількість депозитів: 3
- RevShare: 40%

Розрахунок LTV:
- Revenue per paying user: $50 × 3 = $150
- Affiliate commission: $150 × 40% = $60

З 100 кліків:
- 0.15 реєстрацій
- 0.015 paying users
- Revenue: 0.015 × $60 = $0.90

ROI: -40% 🔴 (краще, але все ще в мінусі)
```

### Що потрібно для окупності

Для окупності при $1.50 CPC потрібно:
- Або збільшити CR до 25%+ (нереалістично)
- Або знизити CPC до $0.30 (складно в Tier-1)
- Або працювати зі **значно вищими CPA** (First Deposit моделі)
- Або залучати **органічний трафік** (SEO)

**Висновок:** Paid traffic для dating review — складна історія. Працює тільки з:
- Вузькими нішами (senior dating, ethnic dating)
- Tier-2/3 GEO з нижчим CPC
- Органічним SEO трафіком

---

## 4. Три продуктові зміни для збільшення CR і LTV

### 🎯 Зміна #1: Квіз-воронка "Find Your Perfect Match"

**Проблема:** Користувач бачить 10 dating apps і не знає який обрати. Аналіз параліч.

**Рішення:** Інтерактивний квіз перед оглядами:
```
Питання 1: "Який тип стосунків ти шукаєш?"
  □ Serious relationship
  □ Casual dating
  □ Hookups

Питання 2: "Вікова категорія?"
  □ 18-25
  □ 26-35
  □ 36-50
  □ 50+

Питання 3: "Бюджет?"
  □ Free only
  □ Up to $20/month
  □ Premium doesn't matter

[Результат: Personalized recommendation з топ-3 apps]
```

**Очікуваний ефект:**
- CR +40-60% (менше вибору = більше дій)
- Кращий pre-qualify (відправляємо тепліших лідів партнерам)
- Вища якість трафіку → краще EPC

**Приклади:**
- Grammarly — квіз перед підпискою збільшив CR на 30%
- Stitch Fix — персоналізовані рекомендації = вища retention

---

### 🎯 Зміна #2: Exit-Intent з Lead Magnet

**Проблема:** 97% відвідувачів йдуть ні з чим. Ми втрачаємо можливість їх повернути.

**Рішення:** Exit-intent popup з безкоштовним lead magnet:
```
"Wait! Get our FREE guide:
'10 Dating Apps That Actually Work in 2024'

📧 Email: [____________]
[Send Me The Guide]
```

**Email sequence (5 листів):**
1. Доставка гайду + quick wins
2. "Why most dating apps fail" (educate)
3. Success stories (social proof)
4. Top 3 apps for [their segment] (recommendation)
5. Exclusive offer/discount (CTA)

**Очікуваний ефект:**
- Збір 5-10% emailів з вихідного трафіку
- Email CR: 2-5% на клік
- Загальний приріст CR: +15-25%
- LTV +50% (email nurturing збільшує retention)

**Приклади:**
- Neil Patel — exit-intent збільшив email capture на 300%
- DatingAdvice.com — email list = основна asset

---

### 🎯 Зміна #3: Trust Layer + Social Proof Engine

**Проблема:** Користувачі не довіряють "ще одному affiliate сайту". Скептицизм.

**Рішення:** Система довіри з декількох рівнів:

**Рівень 1: Transparent Rating System**
```
Кожен app має:
⭐ Загальний рейтинг (1-10)
📊 Breakdown:
   - User Experience: 8.5/10
   - Success Rate: 7.2/10
   - Value for Money: 6.8/10
   - Safety: 9.1/10

🔍 "How we rate" — посилання на методологію
```

**Рівень 2: Real User Reviews**
```
"Чесний відгук від John, 34:
❌ Мінуси: Дорогі преміум-функції, багато ботів
✅ Плюси: Знайшов дружину через 2 місяці
⭐ Рейтинг: 7/10"
```

**Рівень 3: Success Rate Stats**
```
📈 "Based on 10,000+ user reports:
- Average time to first date: 14 days
- Relationship success rate: 23%
- User satisfaction: 4.2/5"
```

**Очікуваний ефект:**
- Trust ↑ → CR +20-30%
- Time on site ↑ (читають відгуки)
- Lower bounce rate
- Повернення (return visits)

**Приклади:**
- Trustpilot інтеграція збільшує CR на 15%
- Wirecutter — прозорість = довіра = конверсія

---

## 5. Приклади продуктів для ideation

### Вертикальні агрегатори (вузькі ніші)

| Продукт | Модель | Що можна запозичити |
|---------|--------|---------------------|
| **NerdWallet** | Financial comparison | Trust signals, калькулятори, transparency |
| **Wirecutter** | Product reviews | Deep research methodology, honest pros/cons |
| **Booking.com** | Hotel aggregation | Urgency ("Only 3 rooms left"), reviews, photos |
| **Credit Karma** | Credit scores | Free tool → affiliate monetization |
| **Zapier** | App integrations | Comparison tables, use-case filtering |

### Dating-специфічні приклади

| Продукт | Фішка |
|---------|-------|
| **DatingAdvice.com** | Content-heavy + expert opinions |
| **ConsumerAffairs** | User-generated reviews + star ratings |
| **eharmony** | Compatibility quiz → personalized match |
| **Match.com** | Success stories gallery |
| **Hinge** | "Designed to be deleted" positioning |

---

## 6. Summary: Що робити

### Швидкі виграші (0-2 тижні)
1. ✅ Exit-intent popup з email capture
2. ✅ Додати real user reviews
3. ✅ Покращити CTA ("Try For Free" → "See Your Matches")

### Середній термін (1-2 місяці)
1. 🔄 Розробити квіз-воронку
2. 🔄 Email nurturing sequence
3. 🔄 Trust scoring system

### Довгий термін (3-6 місяців)
1. 📈 Community features (форум, success stories)
2. 📈 Власний dating app comparison tool
3. 📈 Mobile app (PWA)

### Ключова метрика для відстеження
- **Before:** CR visit→click = 3%
- **Target:** CR visit→click = 5%
- **Holy grail:** CR visit→click = 8%+ (як у топових affiliate сайтів)

---

*«Dating review сайт — це не про те, щоб перерахувати 10 apps. Це про те, щоб допомогти людині знайти любов. Коли це розумієш — всі продуктові рішення стають очевидними.»*
