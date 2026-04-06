# 📈 Розрахунок Ключових Метрик

> Детальний розбір метрик ефективності для dating affiliate мережі

---

## 📊 Структура Датасету

### Опис даних

Припустимо, ми маємо датасет з наступними колонками:

| Поле | Опис | Тип |
|------|------|-----|
| `offer_id` | Унікальний ID офера | Integer |
| `partner_name` | Назва партнера (dating сайту) | String |
| `clicks` | Кількість кліків | Integer |
| `leads` | Кількість реєстрацій | Integer |
| `sales` | Кількість продажів (FTD) | Integer |
| `engagements` | Кількість активних дій | Integer |
| `revenue` | Загальний дохід ($) | Decimal |
| `payout` | Виплата партнеру ($) | Decimal |
| `date` | Дата | Date |
| `geo` | Географія | String |
| `device` | Пристрій | String |

### Sample Data (за 30 днів)

```
┌──────────┬────────────────┬────────┬───────┬───────┬─────────────┬─────────┬─────────┐
│ offer_id │ partner_name   │ clicks │ leads │ sales │ engagements│ revenue │ payout  │
├──────────┼────────────────┼────────┼───────┼───────┼─────────────┼─────────┼─────────┤
│ 101      │ Match.com      │ 12,500 │ 3,125 │  312  │    8,750    │ 18,720  │ 11,232  │
│ 102      │ eHarmony       │ 8,000  │ 2,000 │  240  │    5,600    │ 16,800  │ 10,080  │
│ 103      │ EliteSingles   │ 6,000  │ 1,500 │  165  │    4,200    │ 10,725  │  6,435  │
│ 104      │ Tinder         │ 25,000 │ 5,000 │  375  │   15,000    │ 13,500  │  8,100  │
│ 105      │ Bumble         │ 15,000 │ 3,750 │  300  │   10,500    │ 12,600  │  7,560  │
│ 106      │ Hinge          │ 10,000 │ 2,800 │  224  │    7,000    │ 10,080  │  6,048  │
│ 107      │ OkCupid        │ 18,000 │ 3,600 │  216  │   11,700    │  7,560  │  4,536  │
│ 108      │ PlentyOfFish   │ 22,000 │ 4,400 │  220  │   13,200    │  6,600  │  3,960  │
│ 109      │ Zoosk          │ 9,000  │ 1,800 │  126  │    5,850    │  5,670  │  3,402  │
│ 110      │ ChristianMingle│ 5,000  │ 1,250 │  150  │    3,500    │  7,500  │  4,500  │
└──────────┴────────────────┴────────┴───────┴───────┴─────────────┴─────────┴─────────┘
```

---

## 💰 Розрахунок Revenue per Click (RPC)

### Формула

```
RPC = Revenue / Clicks
```

### Розрахунок для кожного офера

| Offer | Revenue | Clicks | RPC | Rating |
|-------|---------|--------|-----|--------|
| Match.com | $18,720 | 12,500 | **$1.50** | ⭐⭐⭐⭐⭐ Excellent |
| eHarmony | $16,800 | 8,000 | **$2.10** | ⭐⭐⭐⭐⭐ Excellent |
| EliteSingles | $10,725 | 6,000 | **$1.79** | ⭐⭐⭐⭐⭐ Excellent |
| Tinder | $13,500 | 25,000 | **$0.54** | ⭐⭐⭐ Average |
| Bumble | $12,600 | 15,000 | **$0.84** | ⭐⭐⭐⭐ Good |
| Hinge | $10,080 | 10,000 | **$1.01** | ⭐⭐⭐⭐ Good |
| OkCupid | $7,560 | 18,000 | **$0.42** | ⭐⭐ Below Average |
| PlentyOfFish | $6,600 | 22,000 | **$0.30** | ⭐⭐ Below Average |
| Zoosk | $5,670 | 9,000 | **$0.63** | ⭐⭐⭐ Average |
| ChristianMingle | $7,500 | 5,000 | **$1.50** | ⭐⭐⭐⭐⭐ Excellent |

### Інтерпретація

```
RPC Benchmarks for Dating Vertical:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$2.00+  ⭐⭐⭐⭐⭐ EXCELLENT (Top 5%)
$1.50+  ⭐⭐⭐⭐⭐ VERY GOOD (Top 15%)
$1.00+  ⭐⭐⭐⭐ GOOD (Top 35%)
$0.75+  ⭐⭐⭐ AVERAGE (Median)
$0.50+  ⭐⭐ BELOW AVERAGE
<$0.50  ⭐ POOR (Review needed)
```

### Висновки по RPC

**Топ-3 за RPC:**
1. 🥇 **eHarmony** — $2.10 (преміум аудиторія, високі payouts)
2. 🥈 **EliteSingles** — $1.79 (цільова ніша)
3. 🥉 **Match.com** — $1.50 (бренд, довіра)

**Аутсайдери:**
- PlentyOfFish — $0.30 (low-quality traffic, низькі payouts)
- OkCupid — $0.42 (freemium модель, низька конверсія в sale)

---

## 👥 Розрахунок Revenue per Lead (RPL)

### Формула

```
RPL = Revenue / Leads
```

### Розрахунок

| Offer | Revenue | Leads | RPL | Lead→Sale CR |
|-------|---------|-------|-----|--------------|
| Match.com | $18,720 | 3,125 | **$5.99** | 10.0% |
| eHarmony | $16,800 | 2,000 | **$8.40** | 12.0% |
| EliteSingles | $10,725 | 1,500 | **$7.15** | 11.0% |
| Tinder | $13,500 | 5,000 | **$2.70** | 7.5% |
| Bumble | $12,600 | 3,750 | **$3.36** | 8.0% |
| Hinge | $10,080 | 2,800 | **$3.60** | 8.0% |
| OkCupid | $7,560 | 3,600 | **$2.10** | 6.0% |
| PlentyOfFish | $6,600 | 4,400 | **$1.50** | 5.0% |
| Zoosk | $5,670 | 1,800 | **$3.15** | 7.0% |
| ChristianMingle | $7,500 | 1,250 | **$6.00** | 12.0% |

### Інтерпретація

```
RPL Benchmarks:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$7.00+  ⭐⭐⭐⭐⭐ EXCELLENT
$5.00+  ⭐⭐⭐⭐⭐ VERY GOOD
$3.50+  ⭐⭐⭐⭐ GOOD
$2.50+  ⭐⭐⭐ AVERAGE
$2.00+  ⭐⭐ BELOW AVERAGE
<$2.00  ⭐ POOR
```

### Висновки по RPL

**Топ-3 за RPL:**
1. 🥇 **eHarmony** — $8.40 (висока якість лідів)
2. 🥈 **EliteSingles** — $7.15 (професійна аудиторія)
3. 🥉 **ChristianMingle** — $6.00 (нішева лояльність)

**Проблемні офери:**
- PlentyOfFish — $1.50 (низька якість трафіку)
- OkCupid — $2.10 (мала конверсія лідів в продажі)

---

## 🎯 Розрахунок Revenue per User Engagement (RPUE)

### Формула

```
RPUE = Revenue / Engagements

Де Engagements = активні дії користувачів:
- Time on site > 60 сек
- Scroll depth > 50%
- CTA clicks
- Form interactions
```

### Розрахунок

| Offer | Revenue | Engagements | RPUE | Engagement Rate |
|-------|---------|-------------|------|-----------------|
| Match.com | $18,720 | 8,750 | **$2.14** | 70% |
| eHarmony | $16,800 | 5,600 | **$3.00** | 70% |
| EliteSingles | $10,725 | 4,200 | **$2.55** | 70% |
| Tinder | $13,500 | 15,000 | **$0.90** | 60% |
| Bumble | $12,600 | 10,500 | **$1.20** | 70% |
| Hinge | $10,080 | 7,000 | **$1.44** | 70% |
| OkCupid | $7,560 | 11,700 | **$0.65** | 65% |
| PlentyOfFish | $6,600 | 13,200 | **$0.50** | 60% |
| Zoosk | $5,670 | 5,850 | **$0.97** | 65% |
| ChristianMingle | $7,500 | 3,500 | **$2.14** | 70% |

### Інтерпретація

```
RPUE Benchmarks:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$2.50+  ⭐⭐⭐⭐⭐ EXCELLENT (High intent)
$2.00+  ⭐⭐⭐⭐⭐ VERY GOOD
$1.50+  ⭐⭐⭐⭐ GOOD
$1.00+  ⭐⭐⭐ AVERAGE
$0.75+  ⭐⭐ BELOW AVERAGE
<$0.75  ⭐ POOR (Low engagement quality)
```

### Висновки по RPUE

**Топ-3 за RPUE:**
1. 🥇 **eHarmony** — $3.00 (високоцільова аудиторія)
2. 🥈 **EliteSingles** — $2.55 (залучені користувачі)
3. 🥉 **Match.com / ChristianMingle** — $2.14 (сильний бренд)

---

## 💵 Розрахунок Revenue per Sale (RPS)

### Формула

```
RPS = Revenue / Sales

Це середній чек комісії за продаж
```

### Розрахунок

| Offer | Revenue | Sales | RPS | Avg Order Value |
|-------|---------|-------|-----|-----------------|
| Match.com | $18,720 | 312 | **$60.00** | $150 |
| eHarmony | $16,800 | 240 | **$70.00** | $175 |
| EliteSingles | $10,725 | 165 | **$65.00** | $162 |
| Tinder | $13,500 | 375 | **$36.00** | $90 |
| Bumble | $12,600 | 300 | **$42.00** | $105 |
| Hinge | $10,080 | 224 | **$45.00** | $112 |
| OkCupid | $7,560 | 216 | **$35.00** | $87 |
| PlentyOfFish | $6,600 | 220 | **$30.00** | $75 |
| Zoosk | $5,670 | 126 | **$45.00** | $112 |
| ChristianMingle | $7,500 | 150 | **$50.00** | $125 |

### Інтерпретація

```
RPS Benchmarks:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$65+    ⭐⭐⭐⭐⭐ EXCELLENT (Premium offers)
$55+    ⭐⭐⭐⭐⭐ VERY GOOD
$45+    ⭐⭐⭐⭐ GOOD
$40+    ⭐⭐⭐ AVERAGE
$35+    ⭐⭐ BELOW AVERAGE
<$35    ⭐ POOR (Review commission structure)
```

### Висновки по RPS

**Топ-3 за RPS:**
1. 🥇 **eHarmony** — $70.00 (найвищі commission rates)
2. 🥈 **EliteSingles** — $65.00 (преміум pricing)
3. 🥉 **Match.com** — $60.00 (стабільні payouts)

**Низький RPS = низька прибутковість:**
- PlentyOfFish — $30.00 (рекомендовано переглянути)
- OkCupid — $35.00 (рекомендовано переглянути)

---

## 📊 Summary Matrix

### Всі метрики разом

| Offer | RPC | RPL | RPUE | RPS | **Composite Score** |
|-------|-----|-----|------|-----|---------------------|
| eHarmony | $2.10 | $8.40 | $3.00 | $70.00 | **⭐ 9.5/10** |
| EliteSingles | $1.79 | $7.15 | $2.55 | $65.00 | **⭐ 9.0/10** |
| Match.com | $1.50 | $5.99 | $2.14 | $60.00 | **⭐ 8.5/10** |
| ChristianMingle | $1.50 | $6.00 | $2.14 | $50.00 | **⭐ 8.0/10** |
| Hinge | $1.01 | $3.60 | $1.44 | $45.00 | **⭐ 6.5/10** |
| Bumble | $0.84 | $3.36 | $1.20 | $42.00 | **⭐ 6.0/10** |
| Zoosk | $0.63 | $3.15 | $0.97 | $45.00 | **⭐ 5.5/10** |
| Tinder | $0.54 | $2.70 | $0.90 | $36.00 | **⭐ 4.5/10** |
| OkCupid | $0.42 | $2.10 | $0.65 | $35.00 | **⭐ 3.5/10** |
| PlentyOfFish | $0.30 | $1.50 | $0.50 | $30.00 | **⭐ 2.5/10** |

### Composite Score розрахунок

```python
def calculate_composite_score(offer):
    """
    Weighted average of normalized metrics
    """
    # Normalize each metric (0-1 scale)
    rpc_score = min(offer['rpc'] / 2.5, 1.0)      # Max expected: $2.50
    rpl_score = min(offer['rpl'] / 10.0, 1.0)     # Max expected: $10
    rpue_score = min(offer['rpue'] / 3.5, 1.0)    # Max expected: $3.50
    rps_score = min(offer['rps'] / 75.0, 1.0)     # Max expected: $75
    
    # Weighted average
    composite = (
        rpc_score * 0.25 +    # 25% вага
        rpl_score * 0.25 +    # 25% вага
        rpue_score * 0.20 +   # 20% вага
        rps_score * 0.30      # 30% вага (найважливіше)
    )
    
    return round(composite * 10, 1)
```

---

## 📈 Додаткові метрики

### 1. **Conversion Rates**

| Offer | Click→Lead | Lead→Sale | Click→Sale | Engagement→Sale |
|-------|------------|-----------|------------|-----------------|
| eHarmony | 25.0% | 12.0% | 3.0% | 4.3% |
| EliteSingles | 25.0% | 11.0% | 2.75% | 3.9% |
| Match.com | 25.0% | 10.0% | 2.5% | 3.6% |
| ChristianMingle | 25.0% | 12.0% | 3.0% | 4.3% |
| Bumble | 25.0% | 8.0% | 2.0% | 2.9% |
| Hinge | 28.0% | 8.0% | 2.24% | 3.2% |
| Tinder | 20.0% | 7.5% | 1.5% | 2.5% |
| Zoosk | 20.0% | 7.0% | 1.4% | 2.2% |
| OkCupid | 20.0% | 6.0% | 1.2% | 1.8% |
| PlentyOfFish | 20.0% | 5.0% | 1.0% | 1.7% |

### 2. **Profitability Metrics**

| Offer | Revenue | Payout | **Gross Profit** | **Margin** | ROI |
|-------|---------|--------|------------------|------------|-----|
| eHarmony | $16,800 | $10,080 | **$6,720** | **40%** | 1.67x |
| EliteSingles | $10,725 | $6,435 | **$4,290** | **40%** | 1.67x |
| Match.com | $18,720 | $11,232 | **$7,488** | **40%** | 1.67x |
| ChristianMingle | $7,500 | $4,500 | **$3,000** | **40%** | 1.67x |
| Bumble | $12,600 | $7,560 | **$5,040** | **40%** | 1.67x |
| Hinge | $10,080 | $6,048 | **$4,032** | **40%** | 1.67x |
| Tinder | $13,500 | $8,100 | **$5,400** | **40%** | 1.67x |
| Zoosk | $5,670 | $3,402 | **$2,268** | **40%** | 1.67x |
| OkCupid | $7,560 | $4,536 | **$3,024** | **40%** | 1.67x |
| PlentyOfFish | $6,600 | $3,960 | **$2,640** | **40%** | 1.67x |

**Примітка:** Всі офери мають однакову commission structure (40% margin). Різниця в абсолютних цифрах!

### 3. **Efficiency Metrics**

| Offer | Revenue per 1K Clicks | Profit per 1K Clicks | Payback Period |
|-------|----------------------|---------------------|----------------|
| eHarmony | $2,100 | $840 | 1.2 days |
| EliteSingles | $1,790 | $716 | 1.4 days |
| Match.com | $1,500 | $600 | 1.7 days |
| ChristianMingle | $1,500 | $600 | 1.7 days |
| Hinge | $1,010 | $404 | 2.5 days |
| Bumble | $840 | $336 | 3.0 days |
| Zoosk | $630 | $252 | 4.0 days |
| Tinder | $540 | $216 | 4.6 days |
| OkCupid | $420 | $168 | 6.0 days |
| PlentyOfFish | $300 | $120 | 8.3 days |

---

## 🎯 Ключові Інсайти

### Топ-інсайти з аналізу:

1. **🏆 eHarmony — абсолютний лідер**
   - Найвищий RPC ($2.10)
   - Найвищий RPL ($8.40)
   - Найвищий RPUE ($3.00)
   - Найвищий RPS ($70.00)

2. **💰 Premium > Volume**
   - Менший трафік (8K vs 25K) = вища прибутковість
   - EliteSingles приносить більше прибутку за клік ніж Tinder

3. **⚠️ PlentyOfFish — red flag**
   - Найнижчі метрики по всіх показниках
   - Рекомендовано: переглянути або видалити

4. **📊 RPS найважливіша метрика**
   - Корелює з загальною прибутковістю
   - Преміум офери мають вищий LTV

---

## 📋 Рекомендації

### Для оптимізації:

1. **Scale up:** eHarmony, EliteSingles, Match.com
2. **Optimize:** Hinge, Bumble (потенціал зростання)
3. **Review:** Tinder, Zoosk (низька ефективність)
4. **Consider removal:** PlentyOfFish, OkCupid (нижче breakeven)

---

*Розрахунки виконано: Квітень 2026*  
*Методологія: Standard affiliate metrics × Dating vertical benchmarks*
