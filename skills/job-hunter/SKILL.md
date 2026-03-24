---
name: job-hunter
description: Job search assistant for analyzing vacancies, selecting relevant positions, and creating tailored cover letters. Use when user needs help with job hunting, resume analysis, vacancy evaluation, or writing cover letters for specific job applications.
---

# Job Hunter

**⚠️ ОБОВ'ЯЗКОВО прочитати `ARCHITECTURE.md` перед роботою!**

Job search assistant that helps analyze vacancies, select relevant positions, and create tailored cover letters.

---

## 🎯 Швидкий старт (для тих, хто пам'ятає)

1. Вакансії → `00-inbox/`
2. Скринінг → `01-screening/`
3. Дослідження → `02-research/{company}/`
4. Cover letter → `03-cover-letters/{company}/`
5. Надіслано → `04-applied/{company}/`

**Деталі — в `ARCHITECTURE.md`**

---

## 🔄 Повний Пайплайн (крок за кроком)

### Крок 0: Отримання вакансій
**Коли:** Користувач кидає batch вакансій
**Дія:** Зберегти "як є" без обробки
**Куди:** `projects/job-hunting/{username}/00-inbox/{YYYY-MM-DD}-raw-batch.md`
**Шаблон:**
```markdown
# Вакансії — {date}

## {Company} — {Role}
- **Джерело:** @djinni_jobs_bot / посилання
- **Локація:** {місто}
- **Формат:** {remote/hybrid/office}
- **Зарплата:** {range}
- **Статус:** 🆕 Нова
```

### Крок 1: Скринінг (Screening)
**Коли:** Після отримання batch'я
**Дія:** Відфільтрувати і розподілити по tiers
**Куди:** `01-screening/{date}-tier-distribution.md`
**Чекліст:**
- [ ] Відкрити `references/my-profile.md` — перевірити фільтри
- [ ] Відфільтрувати по формату (remote/hybrid/office)
- [ ] Відфільтрувати по індустрії (no iGaming?)
- [ ] Відфільтрувати по досвіду (no junior)
- [ ] Розподілити: Tier 1 (AI/Growth), Tier 2 (можливо), Tier 3 (слабо)

**Формат виходу:**
```markdown
## Tier 1 — Пріоритет
- [ ] {Company} — {Role} (причина: ...)

## Tier 2 — Можливо
...

## Tier 3 — Слабо
...

## Відфільтровано
- ❌ {Company} — причина: hybrid в Києві, релокейт не планую
```

### Крок 2: Дослідження (Research)
**Коли:** Для кожної Tier 1 компанії
**Дія:** Дослідити компанію і записати
**Куди:** `02-research/{company-name}/research.md`
**Чекліст (див. `references/research-protocol.md`):**
- [ ] Сайт компанії (що роблять)
- [ ] Продукт (для кого, як вирішує проблему)
- [ ] Формат роботи (remote/гібрид/офіс)
- [ ] Recent news / funding
- [ ] 2-3 цікавих факти

### Крок 3: Match Analysis
**Коли:** Після дослідження
**Дія:** Порівняти requirements з резюме
**Куди:** Додати в той же `02-research/{company}/research.md`
**Чекліст:**
- [ ] Відкрити `references/my-resume.md`
- [ ] Відкрити `references/my-skills-detailed.md`
- [ ] Списати ВСІ strong matches з метриками
- [ ] Вказати gaps (якщо є)
- [ ] Оцінка: Apply / Skip / Consider

**Формат:**
```markdown
## Match Analysis
✅ Strong: {requirement} — {твій досвід з метрикою}
⚠️ Partial: {requirement} — {частково, бо...}
❌ Gap: {requirement} — {немає, але transferable...}

**Рекомендація:** Apply / Skip / Consider
```

### Крок 4: Cover Letter
**Коли:** Після Match Analysis
**Дія:** Написати кавер українською
**Куди:** `03-cover-letters/{company-name}/draft.md`
**Обов'язково:** Див. `references/cover-letter-template.md`

**Структура:**
1. **Match Summary** — 2-3 булети з конкретними матриками
2. **Hook** — рефлексія на основі досвіду
3. **Deep Dive** — [що робив] → [результат з цифрами] → [релевантність]
4. **Gap Address** — чесно, з transferable skills
5. **Questions (1-3)** — прості, для діалогу
6. **CTA** — 1 речення

**CRITICAL:**
- Українською мовою (не англійською)
- Змінна кількість питань (не обов'язково 3)
- Мінімум назв компаній — "на попередній роботі", не "At Point2Web"

### Крок 5: Рев'ю
**Коли:** Cover letter готовий
**Дія:** Перевірити перед відправкою
**Чекліст:**
- [ ] Прочитати вголос — звучить як людина?
- [ ] Перевірити на "AI-slop" — немає "When I saw... it resonated"?
- [ ] Всі метрики є в `my-resume.md`?
- [ ] Довжина < 400 слів?
- [ ] Питання прості — не "який retention healthy"?

### Крок 6: Відправка
**Коли:** Користувач схвалив
**Дія:** Перенести в applied
**Куди:** `04-applied/{company-name}/`

---

## 📋 Правила (швидкий参考)

### Мова
- **УКРАЇНСЬКОЮ** — дефолт
- Англійською — тільки якщо вакансія вимагає

### Метрики
- ТІЛЬКИ з `my-resume.md` і `my-skills-detailed.md`
- НЕ вигадувати цифри
- НЕ перебільшувати

### Питання
- Прості, для діалогу
- Не "екзаменаційні"
- Змінна кількість (1-3)

Приклади хороших:
- "Скільки людей у команді?"
- "У вас є план на півроку?"
- "Процеси вже налагоджені?"

Приклади поганих:
- "Який retention ви бачите як healthy?"
- "Як виглядає інфраструктура A/B-тестів?"

### Назви компаній
- Мінімізувати в cover letter
- "На попередній роботі..."
- "На минулому проєкті..."
- Не "At Point2Web, I..."

---

## 📁 Файли (де що лежить)

**Проектні файли:**
- `projects/job-hunting/{username}/00-inbox/` — вхідні вакансії
- `projects/job-hunting/{username}/01-screening/` — після відбору
- `projects/job-hunting/{username}/02-research/{company}/` — дослідження
- `projects/job-hunting/{username}/03-cover-letters/{company}/` — кавери
- `projects/job-hunting/{username}/04-applied/{company}/` — надіслані
- `projects/job-hunting/{username}/99-archive/` — архів

**Референси (завжди читати):**
- `references/my-resume.md` — резюме
- `references/my-skills-detailed.md` — детальні скіли
- `references/my-profile.md` — преференції
- `references/research-protocol.md` — як досліджувати
- `references/dos-and-donts.md` — що можна/не можна
- `references/cover-letter-template.md` — шаблон кавера

**Приклади:**
- `examples/` — зразки cover letters

---

## 🚫 Anti-patterns

❌ **Все в одну папку** — робиш `ls` і не розумієш що де
❌ **Назви без дат** — не зрозуміло що нове
❌ **Англійська без причини** — тільки якщо вакансія вимагає
❌ **Загальні фрази** — "AI Product Development" без контексту
❌ **Фіксовані 3 питання** — має бути змінна кількість
❌ **Назви компаній в кавері** — "At Point2Web, I..."

---

## ✅ Чекліст перед комітом

- [ ] Файл в правильній папці (див. ARCHITECTURE.md)
- [ ] Назва з датою
- [ ] Мова: українська
- [ ] Конкретика з резюме, не загальні фрази
- [ ] Прості питання
- [ ] Немає "AI-slop"

---

## Changelog

### 2026-03-24 — Оновлено пайплайн ✅
- Додано `ARCHITECTURE.md` з чіткою структурою
- Пайплайн: 00-inbox → 01-screening → 02-research → 03-cover-letters → 04-applied
- Чіткі чеклісти на кожному кроці
- Приклади файлів

### 2026-03-13 — User Approval ✅
User approved new cover letter structure after testing on 3 real vacancies.

### 2026-03-24 — Українська мова ✅
- Всі cover letters українською
- Прості питання для діалогу
- Змінна кількість питань
