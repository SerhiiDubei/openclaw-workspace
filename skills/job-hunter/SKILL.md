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
3. **Analyze requirements** — compare with detailed skills
4. **Score relevance** — rate 1-10 with reasoning

**Step 1: Match Analysis**
- Load `references/my-skills-detailed.md`
- Compare key requirements with actual skills
- Identify: ✅ Strong match / ⚠️ Partial / ❌ Gap

### Phase 3: Cover Letter Creation
1. **Write hook** — based on research, not generic
2. **Highlight relevant experience** — 2-3 achievements with numbers
3. **Address gaps honestly** — if needed
4. **Ask smart questions** — 2-3 specific ones
5. **Iterate based on feedback**

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

## Rules

- Never use generic phrases like "I am a perfect fit" without evidence
- **Always research company before writing cover letter** — MANDATORY
- Address gaps honestly but positively
- **Keep cover letters 100-150 words max** — recruiters don't read long texts
- Use active voice and specific metrics
- **Sound human, not AI** — avoid "When I saw... it resonated" type of water
- **Include 2-3 smart questions** — shows real interest
- Iterate until user is satisfied with quality

## Cover Letter Structure

1. **Hook** — research-based, with reflection
2. **Relevant experience** — 2-3 achievements with numbers
3. **Questions** — 2-3 specific about team/goals/process
4. **Call proposal** — 1 sentence

See `references/dos-and-donts.md` for detailed guidelines.

## Files

- `references/my-resume.md` — user's resume (load first)
- `references/my-skills-detailed.md` — detailed skills matrix (**load for every vacancy**)
- `references/my-profile.md` — additional preferences and info
- `references/research-protocol.md` — **mandatory research checklist**
- `references/dos-and-donts.md` — tone and style guidelines
- `references/cover-letter-template.md` — template structure
- `examples/` — sample cover letters
