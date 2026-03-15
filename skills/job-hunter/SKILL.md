---
name: job-hunter
description: Job search assistant for analyzing vacancies, selecting relevant positions, and creating tailored cover letters. Use when user needs help with job hunting, resume analysis, vacancy evaluation, or writing cover letters for specific job applications.
---

# Job Hunter

Job search assistant that helps analyze vacancies, select relevant positions, and create tailored cover letters.

## Workflow

### Phase 1: Setup (One-time)
1. Load user's resume from `references/my-resume.md`
2. Load detailed skills from `references/my-skills-detailed.md`
3. Load additional info from `references/my-profile.md`
4. Understand target roles, industries, and preferences

### Phase 2: Vacancy Analysis (CRITICAL)
**Step 0: Research (MANDATORY)** — Follow `references/research-protocol.md`
1. **Research company** — visit website, understand product
2. **Research product** — what it does, for whom, differentiation
3. **Check format** — remote / hybrid / office, relocation requirements
4. **Analyze requirements** — compare with detailed skills
5. **Score relevance** — rate 1-10 with reasoning

**Step 1: Match Analysis**
- Load `references/my-skills-detailed.md`
- Compare key requirements with actual skills
- Identify: ✅ Strong match / ⚠️ Partial / ❌ Gap
- **DO NOT limit to fixed number of matches** — list ALL strong matches

### Phase 3: Cover Letter Creation (NEW STRUCTURE)

**Обов'язкова структура (див. `references/cover-letter-template.md`):**

1. **Match Summary (ОБОВ'ЯЗКОВО)** — 2-3 булети з конкретними матчами requirements ↔ досвід з метриками
2. **Hook** — рефлексія на основі власного досвіду, не пустий комплімент
3. **Deep Dive** — [що робив] → [результат з цифрами] → [релевантність вакансії]
4. **Gap Address** — чесно, з transferable skills (якщо є gap)
5. **Questions** — 2-3 конкретних про їхній продукт
6. **CTA** — 1 речення

**CRITICAL RULES (див. `references/dos-and-donts.md`):**
- **НІ** фіксованій кількості матчів — писати ВСІ сильні матчі
- **НІ** "працював з X" — тільки "зробив Y → результат Z → релевантно тому що"
- **НІ** пустим компліментам — тільки рефлексія на основі досвіду
- **НІ** ігноруванню gaps — адресувати чесно з transferable skills
- **НІ** офісу/гібриду без remote option — фільтрувати відразу

## Output Format

### Vacancy Analysis
```markdown
## Vacancy: [Company] — [Role]

**Relevance Score:** X/10
**Format:** [remote / hybrid / office] | **Relocation:** [required / optional / no]

**Key Requirements:**
- [requirement 1]
- [requirement 2]

**Match Analysis:**
✅ Strong match: [what fits with metrics]
✅ Strong match: [what fits with metrics]
⚠️ Partial match: [what partially fits]
❌ Gap: [what's missing — and how to address]

**Recommendation:** [Apply / Skip / Consider with caveats]
```

### Cover Letter Format
```markdown
Match: [requirement] — [experience with metrics]
Match: [requirement] — [experience with metrics]

[Hook — reflection based on experience]

[Deep dive — what → result → relevance]

[Gap address if needed]

Questions:
- [specific question 1]
- [specific question 2]
- [specific question 3]

[CTA]
```

## Rules

- Never use generic phrases like "I am a perfect fit" without evidence
- **Always research company before writing cover letter** — MANDATORY
- **Always start with Match Summary** — recruiters need quick guide
- Address gaps honestly but positively with transferable skills
- **Keep cover letters 100-150 words max** — recruiters don't read long texts
- Use active voice and specific metrics
- **Sound human, not AI** — avoid "When I saw... it resonated" type of water
- **Include 2-3 smart questions** — shows real interest
- **Filter by format early** — don't waste time on hybrid/office if not interested
- Iterate until user is satisfied with quality

## Understanding Job Descriptions

### JD ≠ Reality
- Job descriptions are often "wish lists" — 60-70% is "nice to have", not "must have"
- Recruiters copy from other postings and add "would be good to have"
- In reality, only 30-40% of listed requirements are actually needed

### Core vs Nice-to-have
- **Core (must have)** — required to get the job
- **Nice-to-have** — "bonus points", but not critical
- Good PMs can distinguish between these

### Domain Transferability
- PM skills (roadmap, prioritization, stakeholder management) are universal
- Product context changes (forest → tomatoes), but approach stays the same
- Business logic, metrics, team collaboration — repeat across domains

### Apply anyway rule
- If you cover 60%+ of core requirements — apply
- Interview clarifies what is actually needed
- Don't self-filter because of "no domain experience"

## Changelog & Approvals

### 2026-03-13 — User Approval ✅
User approved new cover letter structure after testing on 3 real vacancies (Gamzix, Universe, Everstar).
**Approved approach:**
- Match Summary з конкретними метриками з резюме
- Hook на основі реального досвіду (не вигаданий)
- Deep Dive: [що робив] → [результат] → [релевантність]
- Gap Address чесно з transferable skills
- Фільтрація по формату (офіс/гібрид/remote) відразу

**Key principle:** Use ONLY real data from `my-resume.md` and `my-skills-detailed.md`. NO invented metrics.

## Files

- `references/my-resume.md` — user's resume (load first)
- `references/my-skills-detailed.md` — detailed skills matrix (**load for every vacancy**)
- `references/my-profile.md` — additional preferences and info
- `references/research-protocol.md` — **mandatory research checklist**
- `references/dos-and-donts.md` — **CRITICAL: tone, structure, Match Summary, Gap Address rules**
- `references/cover-letter-template.md` — **updated template structure**
- `examples/` — **sample cover letters with new format**
