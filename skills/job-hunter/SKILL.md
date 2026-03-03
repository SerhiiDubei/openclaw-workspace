---
name: job-hunter
description: Job search assistant for analyzing vacancies, selecting relevant positions, and creating tailored cover letters. Use when user needs help with job hunting, resume analysis, vacancy evaluation, or writing cover letters for specific job applications.
---

# Job Hunter

Job search assistant that helps analyze vacancies, select relevant positions, and create tailored cover letters.

## Workflow

### Phase 1: Setup (One-time)
1. Load user's resume from `references/my-resume.md`
2. Load additional info from `references/my-profile.md`
3. Understand target roles, industries, and preferences

### Phase 2: Vacancy Analysis
When user shares a vacancy:
1. **Analyze the vacancy** — extract key requirements, skills, culture fit
2. **Match with profile** — compare against resume and preferences
3. **Score relevance** — rate 1-10 with reasoning
4. **Identify gaps** — what skills/experience are missing

### Phase 3: Cover Letter Creation
For selected vacancies:
1. **Research company** — understand their mission, values, products
2. **Highlight matches** — connect user's experience to job requirements
3. **Address gaps** — explain how user can compensate for missing skills
4. **Write tailored letter** — specific, not generic; 3-4 paragraphs
5. **Iterate based on feedback** — user reviews and suggests improvements

## Output Format

### Vacancy Analysis
```markdown
## Vacancy: [Company] — [Role]

**Relevance Score:** X/10

**Key Requirements:**
- [requirement 1]
- [requirement 2]

**Match Analysis:**
✅ Strong match: [what fits]
⚠️ Partial match: [what partially fits]
❌ Gap: [what's missing]

**Recommendation:** [Apply / Skip / Consider with caveats]
```

### Cover Letter Structure
1. **Hook** — specific connection to company/role
2. **Value proposition** — 2-3 key achievements relevant to job
3. **Motivation** — why this company specifically
4. **Call to action** — request for interview

## Rules

- Never use generic phrases like "I am a perfect fit" without evidence
- Always research company before writing cover letter
- Address gaps honestly but positively
- Keep cover letters under 400 words
- Use active voice and specific metrics
- Iterate until user is satisfied with quality

## Files

- `references/my-resume.md` — user's resume (load first)
- `references/my-profile.md` — additional preferences and info
- `references/cover-letter-template.md` — template structure
