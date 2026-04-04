# Milestones: GB AI Automation

## Формат
Кожен milestone має:
- **Дату** — коли має бути досягнуто
- **Deliverable** — що саме буде готове
- **Success Criteria** — як вимірюємо успіх (конкретні цифри)
- **Owner** — хто відповідає

---

## Milestone 1: Foundation Complete
**Дата:** 18 квітня 2026 (кінець Sprint 2)

### Deliverables
- [ ] Всі API endpoints задокументовані (Swagger)
- [ ] AI stress testing пройдено (20-50 parallel tests без помилок)
- [ ] Всі критичні баги пофікшено
- [ ] QA sign-off (Юля підтверджує готовність)
- [ ] 10-15 тест-кейсів написано та пройдено
- [ ] ML команда дала рекомендації (впроваджені або заплановані)

### Success Criteria
- [ ] Система стабільно тримає 50 parallel тестів
- [ ] Нуль critical багів у production
- [ ] 100% тест-кейсів проходить успішно
- [ ] Code coverage ≥ 70%

### Owner
Віталій (Lead Dev) + Михайло (Delivery)

---

## Milestone 2: Phase 1 Market Test Launch
**Дата:** 25 квітня 2026 (кінець Sprint 3)

### Deliverables
- [ ] 1-3 лендінги підключено до системи
- [ ] 1-2 команди байерів дають трафік
- [ ] Перші 10 A/B тестів запущено AI агентом
- [ ] Dashboard v0.1 (базова аналітика)
- [ ] Manual verification process налаштовано

### Success Criteria
- [ ] Система працює 99%+ uptime перші 7 днів
- [ ] AI успішно створює тест з текстового запиту (≥90% випадків)
- [ ] ≥ 1000 views per test (достатньо для статистики)
- [ ] Жоден тест не "зламав" лендінг
- [ ] Команда байерів дає positive feedback

### Owner
Сергій (Product) + Михайло (Delivery)

---

## Milestone 3: Phase 1 Validation
**Дата:** 23 травня 2026 (4 тижні після launch)

### Deliverables
- [ ] Результати мінімум 20 A/B тестів
- [ ] Звіт: "Що працює, що не працює"
- [ ] Валідовані гіпотези (3-5 winners)
- [ ] ROI розрахунок (вигода від тестів vs витрати на систему)

### Success Criteria
- [ ] ≥ 20 тестів запущено
- [ ] ≥ 3 тести показали статистично значущий uplift (p < 0.05)
- [ ] Середній uplift по winners: ≥ 10%
- [ ] Час на запуск тесту: ≤ 2 години (від ідеї до запуску)
- [ ] NPS команти байерів ≥ 7/10

### Owner
Сергій (Product)

---

## Milestone 4: Product-Market Fit
**Дата:** 30 червня 2026

### Deliverables
- [ ] 10 paying customers (або letter of intent)
- [ ] Self-service onboarding (клієнт може підключитись сам)
- [ ] Автоматична валідація (не потребує manual verification)
- [ ] Pricing model валідовано
- [ ] Case studies (3-5 успішних історій)

### Success Criteria
- [ ] 10+ клієнтів платять або підписали LOI
- [ ] MRR (Monthly Recurring Revenue) ≥ $1000
- [ ] Churn rate ≤ 10% (або відсутній)
- [ ] Customer Acquisition Cost (CAC) визначено
- [ ] Product-led growth: ≥ 30% нових клієнтів від referrals

### Owner
Сергій (Product) + Михайло (Delivery)

---

## Milestone 5: Scale Ready
**Дата:** 30 вересня 2026

### Deliverables
- [ ] 100+ активних команд
- [ ] Enterprise features (API, advanced targeting, SSO)
- [ ] Автоматичний аналіз (AI сам пропонує гіпотези)
- [ ] Team розширено (мінімум +2 dev, +1 sales)
- [ ] Фінансова стабільність (MRR покриває витрати)

### Success Criteria
- [ ] 100+ активних команд
- [ ] MRR ≥ $10,000
- [ ] Unit economics positive (LTV > 3× CAC)
- [ ] Uptime 99.9%
- [ ] NPS ≥ 50

### Owner
Сергій (CEO/Founder)

---

## Залежності між Milestones

```
M1: Foundation
    ↓ (без M1 не запускаємо M2)
M2: Phase 1 Launch
    ↓ (потрібні результати для M3)
M3: Phase 1 Validation
    ↓ (валідація перед масштабуванням)
M4: Product-Market Fit
    ↓ (готові до росту)
M5: Scale
```

---

## Risk Mitigation

| Milestone | Ризик | Plan B |
|-----------|-------|--------|
| M1 (18.04) | Stress testing показує баги | Додати ще 1 спринт на фікси |
| M2 (25.04) | Лендінги не готові | Знайти резервні варіанти |
| M3 (23.05) | Результати тестів слабкі | Проаналізувати, скоригувати продукт |
| M4 (30.06) | Немає paying customers | Pivot або залишитися internal tool |
| M5 (30.09) | Не набираємо 100 команд | Залишитися нішовим продуктом |

---

## Tracking

**Щотижневий review:**
- Які milestones в зеленій зоні?
- Які жовті (ризик затримки)?
- Які червоні (вже затримані)?

**Tools:**
- GitHub Projects milestones
- Або ClickUp goals (при переході)

---

## Питання для команди

1. **M2 дата (25.04)** — реалістично? Чи краще 2 травня (після вихідних)?
2. **M3 тривалість** — 4 тижні достатньо для збору даних? Чи краще 6?
3. **M4 MRR $1000** — реалістична ціль для 10 клієнтів?
4. **M5 $10,000 MRR** — амбітно чи занадто консервативно?

---

*Document created: 2026-04-04*  
*Ready for team discussion and date adjustments*
