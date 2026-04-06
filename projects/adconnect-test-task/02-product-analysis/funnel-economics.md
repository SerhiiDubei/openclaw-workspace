# 📊 Фанел та Unit Economy Analysis

> Розбираємо математику прибутковості dating review сайту

---

## 🔄 Повний Фанел

### Візуалізація фанелу

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. LANDING PAGE (Traffic Acquisition)                                   │
│    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│    100,000 visitors (100%)                                              │
│    • Organic search: 45,000                                             │
│    • Paid ads (Google/Meta): 35,000                                     │
│    • Social media: 12,000                                               │
│    • Direct: 5,000                                                      │
│    • Referrals: 3,000                                                   │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼ CR: 35%
┌─────────────────────────────────────────────────────────────────────────┐
│ 2. REVIEW PAGE ENGAGEMENT                                               │
│    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│    35,000 visitors (35%)                                                │
│    • Avg. time on page: 2:30                                            │
│    • Scroll depth: 65%                                                  │
│    • Pages per session: 1.8                                             │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼ CR: 25%
┌─────────────────────────────────────────────────────────────────────────┐
│ 3. PARTNER CLICK (CTA Click)                                            │
│    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│    8,750 clicks (8.75%)                                                 │
│    • Primary CTA: 6,125 (70%)                                           │
│    • Secondary CTA: 2,625 (30%)                                         │
│    • Avg. CTR: 12.5%                                                    │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼ CR: 40%
┌─────────────────────────────────────────────────────────────────────────┐
│ 4. REGISTRATION (Lead Generation)                                       │
│    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│    3,500 registrations (3.5%)                                           │
│    • Form completion: 2,800 (80%)                                       │
│    • Social login: 700 (20%)                                            │
│    • Verified emails: 2,975 (85%)                                       │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼ CR: 8%
┌─────────────────────────────────────────────────────────────────────────┐
│ 5. FIRST TIME DEPOSIT / SALE                                            │
│    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│    280 sales (0.28%)                                                    │
│    • Avg. order value: $45                                              │
│    • Total revenue: $12,600                                             │
│    • Commission (40%): $5,040                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

### Покроковий breakdown

| Етап | Кількість | CR від попереднього | CR від початку |
|------|-----------|---------------------|----------------|
| **Traffic** | 100,000 | — | 100% |
| **Review Page** | 35,000 | 35% | 35% |
| **Partner Click** | 8,750 | 25% | 8.75% |
| **Registration** | 3,500 | 40% | 3.5% |
| **Sale (FTD)** | 280 | 8% | 0.28% |

---

## 💰 Unit Economics

### Ключові метрики

#### 1. **Revenue per Click (RPC)**

```
Formula: Total Revenue / Total Clicks

Calculation:
$5,040 (commission) / 8,750 (clicks) = $0.576 per click

Industry benchmark: $0.30 - $1.50
Статус: ✅ GOOD
```

#### 2. **Revenue per Lead (RPL)**

```
Formula: Total Revenue / Total Registrations

Calculation:
$5,040 / 3,500 = $1.44 per lead

Industry benchmark: $1.00 - $3.00
Статус: ✅ GOOD
```

#### 3. **Revenue per User Engagement (RPUE)**

```
Formula: Total Revenue / Engaged Users
Engaged Users = ті, хто провів >60 сек на review

Assumption: 60% review page visitors = engaged
21,000 engaged / $5,040 = $0.24 per engagement

(Для порівняння: відвідувачі <30 сек = $0.08 per view)
```

#### 4. **Revenue per Sale (RPS)**

```
Formula: Total Commission / Number of Sales

Calculation:
$5,040 / 280 = $18 per sale

Industry benchmark: $15 - $50
Статус: ✅ GOOD
```

#### 5. **Customer Acquisition Cost (CAC)**

```
Formula: Total Marketing Spend / New Customers

Breakdown:
- Paid ads: $4,200 (Google: $2,800, Meta: $1,400)
- Content creation: $1,500
- SEO tools & optimization: $800
- Total: $6,500

CAC = $6,500 / 280 = $23.21 per customer

⚠️ УВАГА: CAC > RPS = проблема!
```

#### 6. **Lifetime Value (LTV)**

```
Formula: (RPS × Repeat Purchase Rate × Avg. Lifetime)

Assumptions:
- Repeat purchase rate: 25% (роблять 2+ покупки)
- Avg. lifetime: 6 місяців
- Retention payout: $12 per repeat

LTV Calculation:
= $18 (initial) + ($12 × 0.25 × 6)
= $18 + $18
= $36

LTV:CAC Ratio = $36 : $23.21 = 1.55:1

Target: 3:1+
Статус: ❌ NEEDS IMPROVEMENT
```

---

## 📈 Детальний Unit Economics Breakdown

### По каналах трафіку

| Канал | Трафік | Витрати | Реєстрації | Продажі | Дохід | ROAS |
|-------|--------|---------|------------|---------|-------|------|
| **Organic** | 45,000 | $1,500* | 1,575 | 126 | $2,268 | 1.51x |
| **Google Ads** | 25,000 | $2,800 | 875 | 70 | $1,260 | 0.45x |
| **Meta Ads** | 15,000 | $1,400 | 525 | 42 | $756 | 0.54x |
| **Social** | 12,000 | $600 | 420 | 33 | $594 | 0.99x |
| **Direct** | 5,000 | $200 | 175 | 14 | $252 | 1.26x |
| **Referrals** | 3,000 | $0 | 105 | 8 | $144 | ∞ |

\* SEO-витрати амортизовані

### Ключові інсайти з таблиці:

1. **Google Ads — найбільша проблема**
   - ROAS 0.45x = витрачаємо $2.8K, отримуємо $1.26K
   - CAC для цього каналу: $40 (дуже високий!)
   
2. **Organic — найприбутковіший**
   - ROAS 1.51x (без врахування часу на SEO)
   - Потрібно інвестувати більше в контент

3. **Referrals — hidden gem**
   - Безкоштовний трафік з найвищою конверсією
   - Потрібно активувати реферальну програму

---

## 🎯 Моделі оптимізації

### Сценарій 1: Покращення CR на +25%

| Метрика | Поточно | +25% | Різниця |
|---------|---------|------|---------|
| Review → Click CR | 25% | 31.25% | +2,187 кліків |
| Click → Reg CR | 40% | 50% | +1,093 реєстрацій |
| Reg → Sale CR | 8% | 10% | +109 продажів |
| **Total Revenue** | $5,040 | $7,560 | **+$2,520** |
| **ROAS** | 0.78x | 1.16x | **+0.38x** |

### Сценарій 2: Зниження CAC на 30%

| Метрика | Поточно | -30% | Різниця |
|---------|---------|------|---------|
| Paid Ads Budget | $4,200 | $2,940 | -$1,260 |
| Оптимізація: | | | |
• Better targeting | | -15% | |
• Improved creatives | | -10% | |
• Retention focus | | -5% | |
| **Net Profit** | -$1,460 | +$280 | **+$1,740** |

### Сценарій 3: Збільшення LTV на 50%

| Стратегія | Вплив на LTV | Investment |
|-----------|--------------|------------|
| Email nurture campaign | +$6 | $200/mo |
| Retargeting ads | +$4 | $300/mo |
| Loyalty program | +$5 | $150/mo |
| Better partner matching | +$7 | $0 (продуктова зміна) |
| **Total LTV increase** | **+$22** ($36 → $58) | **$650/mo** |

**LTV:CAC після змін:** 58:23 = **2.5:1** ✅

---

## 📊 Порівняння з індустрією

### Dating Affiliate Benchmarks

| Метрика | Top 10% | Average | TheDatingCritic | Потенціал |
|---------|---------|---------|-----------------|-----------|
| **CR (Click→Reg)** | 55% | 35% | 40% | +37.5% |
| **CR (Reg→Sale)** | 12% | 6% | 8% | +50% |
| **RPC** | $1.20 | $0.60 | $0.58 | +106% |
| **LTV:CAC** | 4:1 | 2:1 | 1.55:1 | +158% |
| **Payback Period** | 2 місяці | 6 місяців | 8 місяців | -75% |

### Що працює в топів:

1. **Високоцільовий трафік**
   - Long-tail keywords
   - Lookalike audiences на Meta
   - Retargeting warm traffic

2. **Optimized landing pages**
   - Personalization
   - Social proof
   - Urgency/scarcity

3. **Quality score optimization**
   - Високий Quality Score = нижчий CPC
   - Relevant ad copy
   - Fast page load

4. **Partner selection**
   - Тільки висококонвертуючі offers
   - Exclusive deals
   - Higher payouts

---

## 🚨 Red Flags та проблеми

### 🔴 Критичні

1. **LTV:CAC = 1.55:1** (потрібно 3:1+)
   - Рішення: збільшити LTV через retention

2. **Google Ads ROAS = 0.45x**
   - Рішення: призупинити і переналаштувати

3. **Conversion Rate Reg→Sale = 8%**
   - Рішення: покращити quality leads

### 🟡 Потребують уваги

1. **Bounce rate на landing = 65%**
   - Рішення: A/B testing headlines

2. **Avg. session duration = 1:45**
   - Рішення: кращий контент, internal linking

3. **Mobile CR нижчий на 30% vs desktop**
   - Рішення: mobile-first optimization

---

## 💡 Рекомендації для покращення

### Швидкі виграші (0-30 днів)

1. **Audit Google Ads campaigns**
   - Pause keywords з CPA > $50
   - Додати negative keywords
   - Test new ad copy

2. **Optimize landing pages**
   - Додати social proof (відгуки)
   - Покращити CTA buttons
   - Зменшити form fields

3. **Fix mobile experience**
   - Accelerated Mobile Pages (AMP)
   - Responsive design fixes
   - Touch-friendly elements

### Середньострокові (1-3 місяці)

1. **Implement lead scoring**
   - Віддавати пріоритет high-intent leads
   - Персоналізувати offers

2. **Email automation**
   - Welcome series
   - Abandoned cart recovery
   - Re-engagement campaign

3. **A/B testing program**
   - Test 2 зміни на тиждень
   - Focus на highest-impact areas

### Довгострокові (3-6 місяців)

1. **AI-powered matching**
   - Алгоритм підбору dating сайтів
   - Персоналізовані рекомендації

2. **Content expansion**
   - 100+ нових оглядів
   - Video content
   - User-generated content

3. **New traffic channels**
   - TikTok organic
   - Pinterest
   - YouTube SEO

---

## 📋 Financial Model (12 місяців)

### Поточна траєкторія

| Місяць | Traffic | Витрати | Revenue | Profit | Cumulative |
|--------|---------|---------|---------|--------|------------|
| 1 | 100K | $6,500 | $5,040 | -$1,460 | -$1,460 |
| 2 | 100K | $6,500 | $5,040 | -$1,460 | -$2,920 |
| 3 | 100K | $6,500 | $5,040 | -$1,460 | -$4,380 |
| ... | ... | ... | ... | ... | ... |
| 12 | 100K | $6,500 | $5,040 | -$1,460 | **-$17,520** |

### З оптимізаціями

| Місяць | Traffic | Витрати | Revenue | Profit | Cumulative |
|--------|---------|---------|---------|--------|------------|
| 1 | 100K | $5,500 | $6,300 | +$800 | +$800 |
| 2 | 110K | $5,500 | $6,930 | +$1,430 | +$2,230 |
| 3 | 120K | $5,500 | $7,560 | +$2,060 | +$4,290 |
| ... | ... | ... | ... | ... | ... |
| 12 | 200K | $6,000 | $14,000 | +$8,000 | **+$52,000** |

**Різниця:** $69,520 за рік! 🚀

---

*Аналіз виконано: Квітень 2026*  
*Методологія: Funnel analysis × Unit economics × Benchmarking*
