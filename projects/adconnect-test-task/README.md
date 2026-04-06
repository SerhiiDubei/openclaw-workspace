# 🎯 AdConnect Test Task

## Огляд проєкту

Цей проєкт — комплексне тестове завдання на позицію **Product Marketing Manager** у AdConnect. Включає технічне завдання на інтеграцію Google Ads, продуктовий аналіз dating review ніші та аналіз датасету для оптимізації оферів.

---

## 📁 Структура проєкту

```
projects/adconnect-test-task/
├── README.md                           # Огляд проєкту (ви тут)
├── 01-google-ads-integration/          # Завдання 1: Технічне завдання
│   ├── technical-spec.md              # Технічне завдання на інтеграцію
│   └── diagrams/                      # Схеми інтеграції
├── 02-product-analysis/                # Завдання 2: Продуктовий аналіз
│   ├── competitor-analysis.md         # Аналіз конкурентів
│   ├── funnel-economics.md            # Фанел та unit economy
│   ├── product-mechanics.md           # 3 механіки для CR/LTV
│   └── prototype/                     # Клікабельний прототип
├── 03-dataset-analysis/                # Завдання 3: Аналіз датасету
│   ├── metrics-calculation.md         # Розрахунки метрик
│   └── prioritization.md              # Перепріоритизація оферів
└── google-ads-guide.md                # Гайд для користувача
```

---

## 🎯 Завдання 1: Google Ads Інтеграція

**Мета:** Розробити технічне завдання на інтеграцію Google Ads для dating review сайту thedatingcritic.com

**Ключові аспекти:**
- Передача конверсій з продукту в Google Ads
- Збір статистики в In-house Data Storage
- Ідентифікатори: GCLID, User ID, Session ID, Conversion ID, Timestamp
- Схема: User → Product → Partner Offer → Postback → Google Ads Conversion

📄 [Детальне ТЗ](./01-google-ads-integration/technical-spec.md)

---

## 📊 Завдання 2: Продуктовий Аналіз

**Мета:** Проаналізувати thedatingcritic.com та запропонувати покращення

**Що включено:**
- Аналіз конкурентів (SimilarWeb, Serpstat)
- Фанел аналіз: Landing → Review Page → Partner Click → Registration → Payment
- Unit Economy: CAC, LTV, Revenue per click/lead/user
- 3 механіки для збільшення CR і LTV
- Клікабельний прототип

📄 [Аналіз конкурентів](./02-product-analysis/competitor-analysis.md)  
📄 [Фанел та економіка](./02-product-analysis/funnel-economics.md)  
📄 [Продуктові механіки](./02-product-analysis/product-mechanics.md)

---

## 📈 Завдання 3: Аналіз Датасету

**Мета:** Розрахувати ключові метрики та перепріоритизувати офери

**Метрики:**
- Revenue per Click (RPC)
- Revenue per Lead (RPL)
- Revenue per User Engagement (RPUE)
- Revenue per Sale (RPS)
- ROI за оферами

📄 [Розрахунки метрик](./03-dataset-analysis/metrics-calculation.md)  
📄 [Перепріоритизація](./03-dataset-analysis/prioritization.md)

---

## 📚 Google Ads Гайд

Окремий гайд для користувачів, який пояснює:
- Як працює Google Ads інтеграція (порівняння з Meta Pixel)
- GCLID vs fbclid
- Enhanced Conversions
- Google Tag vs gtag.js
- Прокидування конверсій через postback

📄 [Читати гайд](./google-ads-guide.md)

---

## 🔑 Ключові Результати

1. **Технічна інтеграція:** Розроблена схема Server-to-Server інтеграції з Google Ads API з підтримкою offline conversions

2. **Продуктові інсайти:** Виявлено 3 ключові механіки для зростання CR на 25-40%: персоналізація, соціальний доказ та гейміфікація

3. **Оптимізація оферів:** Розроблена методологія перепріоритизації на основі ROI з урахуванням LTV

---

## 🛠️ Використані інструменти

- Google Ads API Documentation
- SimilarWeb для аналізу трафіку
- Serpstat для SEO-аналізу
- Mermaid для діаграм
- Markdown для документації

---

*Проєкт виконано з ❤️ для AdConnect*  
*Дата: Квітень 2026*
