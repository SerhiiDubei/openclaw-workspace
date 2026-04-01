# Research Progress Report — 2026-04-01 (FINAL)

## ✅ Досягнення за сьогодні

### Хуки (Hooks)
| Метрика | Значення |
|---------|----------|
| **Зібрано хуків** | **17 штук** |
| Джерела | Bath Fitter, Re-Bath, West Shore Home, Payless Bath Makeover, First Choice Bathroom Remodeling, Safe Step, BCI Bath & Shower, Titan Bathworks, Lifetime & Kohler LuxStone |
| Категорії | Discount (12), Urgency (3), Guarantee (2), Social Proof (2) |

---

## Топ-10 Хуків (ранжовані)

| Rank | Hook | Джерело | Сила |
|------|------|---------|------|
| 1 | "50% off installation + $0 down / 0% interest" | Payless Bath Makeover | ⭐⭐⭐⭐⭐ |
| 2 | "Tax Season Special — Save Up to $500" | Bath Fitter | ⭐⭐⭐⭐⭐ |
| 3 | "1-Day Install — Installed Fast, Built to Last" | Bath Fitter | ⭐⭐⭐⭐⭐ |
| 4 | "FREE Installation ($1500 value)" | West Shore Home | ⭐⭐⭐⭐ |
| 5 | "$1,500 OFF Full Bathroom Remodel" | First Choice | ⭐⭐⭐⭐ |
| 6 | "FREE shower package + $1600 Off" | Safe Step | ⭐⭐⭐⭐ |
| 7 | "$1000 off OR No Payments/No Interest for 18 months" | BCI Bath | ⭐⭐⭐⭐ |
| 8 | "60-month zero-interest financing" | Lifetime & Kohler | ⭐⭐⭐⭐ |
| 9 | "Same Day Savings" | Payless Bath | ⭐⭐⭐⭐ |
| 10 | "10% Cash Rebate when you pay cash" | Titan Bathworks | ⭐⭐⭐⭐ |

---

## Ключові патерни

### Фінансові хуки (12/17 = 71%)
- **Combo offers** домінують: знижка + фінансування
- **$0 down** — magic words для entry barrier
- **Опції**: "АБО" дають ілюзію контролю ($1000 off OR 18 months)

### Ургентність (3/17)
- "Same Day Savings" — без конкретики, але з FOMO
- "Limited Time" — класика
- Seasonal hooks (Tax Season) — релевантність

### Унікальні знахідки
- **10% Cash Rebate** — не "discount", а "rebate" (психологічно інше)
- **60-month financing** — 5 років замість стандартних 1-2
- **FREE + $ off combo** — подвійна вигода

---

## Зображення
| Метрика | Значення |
|---------|----------|
| **Зібрано** | **~8 штук** (~0.8 MB) |
| Джерело | Pexels (free license) |
| Категорії | Luxury-quality, Minimalist |

---

## Наступні кроки

### Завтра (2026-04-02)
- **10:17** — наступний автоматичний збір хуків
- **14:23** — збір зображень (категорія: family-with-people)

### Ручні задачі
- [ ] Знайти зображення з людьми (seniors, families)
- [ ] Before/after фото
- [ ] Додати affiliate-мережі (MaxBounty, CJ)

---

## SQL для аналізу

```sql
-- Статистика за типами
SELECT hook_type, COUNT(*) as count 
FROM home_improvement_hooks 
GROUP BY hook_type 
ORDER BY count DESC;

-- Статистика за тригерами
SELECT trigger_type, COUNT(*) as count 
FROM home_improvement_hooks 
GROUP BY trigger_type 
ORDER BY count DESC;

-- Топ за емоціями
SELECT target_emotion, COUNT(*) as count 
FROM home_improvement_hooks 
WHERE target_emotion IS NOT NULL
GROUP BY target_emotion 
ORDER BY count DESC;
```

---

## Рекомендації для копірайтингу

### Hero Section — комбо:
```
"Save Up to $500 + 0% Financing"
"1-Day Install — No Mess, No Stress"
"2+ Million Happy Homeowners"
```

### Lead Form:
```
"See Your Price in 60 Seconds"
"Get $1500 Off — Limited Time"
"Free Design Consultation"
```

### Exit Intent:
```
"Wait! Same Day Savings Available"
"Don't Miss 50% Off Installation"
```
