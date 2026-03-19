# Claude Code Skills: Quick Reference for RPG/AI Agent Developers

## 🎯 Your Recommended Skill Stack

### Base Foundation (Install Immediately)
| # | Skill | Command/Install | Why You Need It |
|---|-------|-----------------|-----------------|
| 1 | **skill-creator** | `/plugin install skill-creator@anthropic-agent-skills` | Build custom skills for your four-agents project |
| 2 | **brainstorming** | `git clone https://github.com/obra/superpowers ~/.claude/skills/superpowers` | Plan agent architectures |
| 3 | **mcp-builder** | `/plugin install mcp-builder@anthropic-agent-skills` | Create tools for your agents |
| 4 | **claude-memory-skill** | `git clone https://github.com/hanfang/claude-memory-skill` | Persistent agent memory |
| 5 | **test-driven-development** | From obra/superpowers | Quality code for game mechanics |

### Game Development Stack
| # | Skill | Source | Use Case |
|---|-------|--------|----------|
| 6 | **rpg-progression-design** | mcpmarket | Character stats, XP, talent trees |
| 7 | **claude-code-game-master** | Sstobo/Claude-Code-Game-Master | Full RPG system with RAG |
| 8 | **skills-weaver** | nicmarti/skills-weaver | D&D 5e AI DM |

### AI Agent Systems Stack
| # | Skill | Install | Purpose |
|---|-------|---------|---------|
| 9 | **agent-designer** | `/plugin install agent-designer@claude-code-skills` | Multi-agent orchestration |
| 10 | **rag-architect** | From alirezarezvani | Knowledge retrieval for agents |
| 11 | **self-improving-agent** | `/plugin install self-improving-agent@claude-code-skills` | Auto-curation & learning |
| 12 | **insight-extractor** | From glebis/claude-skills | Capture session learnings |

### Advanced Memory & Learning
| # | Skill | Source | Superpower |
|---|-------|--------|------------|
| 13 | **vault-daydream** | glebis/claude-skills | Find hidden connections in your notes |
| 14 | **thinking-patterns** | glebis/claude-skills | Analyze your cognitive patterns |
| 15 | **retrospective** | glebis/claude-skills | Continual learning from sessions |

---

## 🚀 Installation Cheat Sheet

### Quick Setup (One-Liner)
```bash
# Add marketplaces
/plugin marketplace add anthropics/skills
/plugin marketplace add alirezarezvani/claude-skills

# Install core skills
/plugin install skill-creator@anthropic-agent-skills
/plugin install mcp-builder@anthropic-agent-skills
/plugin install frontend-design@anthropic-agent-skills
/plugin install security-auditor@claude-code-skills
/plugin install agent-designer@claude-code-skills
```

### Clone Key Repositories
```bash
# Create skills directory
mkdir -p ~/.claude/skills

# obra/superpowers - Core workflow skills
git clone https://github.com/obra/superpowers ~/.claude/skills/superpowers

# glebis/claude-skills - Memory & analysis
git clone https://github.com/glebis/claude-skills ~/.claude/skills/glebis

# hanfang/claude-memory-skill - Memory system
git clone https://github.com/hanfang/claude-memory-skill ~/.claude/skills/memory

# sickn33/antigravity-awesome-skills - Massive collection (1,273 skills)
git clone https://github.com/sickn33/antigravity-awesome-skills ~/.claude/skills/antigravity
```

---

## 🎮 For Your Four-Agents RPG Project

### Recommended Custom Skills to Build

1. **four-agents-orchestrator** 
   - Define agent roles (RPG classes/archetypes)
   - Set up communication patterns
   - Handle turn-based interactions

2. **rpg-mechanics-engine**
   - Stat calculations
   - Combat resolution
   - XP/leveling formulas

3. **agent-memory-sync**
   - Shared world state
   - Persistent character data
   - Cross-session continuity

4. **narrative-generator**
   - Story progression
   - Quest generation
   - Dynamic dialogue

### Use These Existing Skills as Templates

| Skill | What to Learn From It |
|-------|----------------------|
| `claude-code-game-master` | RAG integration, persistent world state |
| `skills-weaver` | Agent loop, dice rolling, character gen |
| `agent-designer` | Multi-agent orchestration patterns |
| `synapse-skill` | Multi-model coordination |

---

## 📊 Skill Complexity Ratings

### Beginner (Just Works)
- brainstorming
- test-driven-development
- doc-coauthoring
- insight-extractor

### Intermediate (Some Config)
- mcp-builder (needs API keys)
- claude-memory-skill (needs vault path)
- rpg-progression-design
- security-auditor

### Advanced (Complex Setup)
- vault-daydream (costs $0.40-0.50/run)
- thinking-patterns (multi-agent, 6-8 min runtime)
- self-improving-agent
- claude-code-game-master

---

## 🔗 Key URLs

| Resource | URL |
|----------|-----|
| Official Skills | https://github.com/anthropics/skills |
| Antigravity (1,273 skills) | https://github.com/sickn33/antigravity-awesome-skills |
| Alireza's Collection (205 skills) | https://github.com/alirezarezvani/claude-skills |
| VoltAgent Awesome (500+) | https://github.com/VoltAgent/awesome-agent-skills |
| Glebis Skills (Memory focus) | https://github.com/glebis/claude-skills |
| Skills Marketplace | https://mcpmarket.com |
| Agent Skills Standard | https://agentskills.io |

---

## 💡 Pro Tips

1. **Always run security-auditor before installing community skills**
   ```bash
   python3 skill_security_auditor.py /path/to/skill/
   ```

2. **Use progressive disclosure** - Skills load metadata first (~100 tokens), then body only when needed

3. **Create CLAUDE.md in your project root** for persistent context about your four-agents RPG

4. **Combine MCP + Skills**: Use MCP for tools, Skills for workflows

5. **Start with /init** in Claude Code to auto-generate project context

6. **Cost-aware**: vault-daydream costs ~$0.50/run; thinking-patterns ~$3.50/run

7. **Cross-platform**: One skill works in Claude Code, Cursor, Codex, Gemini CLI, etc.

---

## 🔄 Recommended Workflow

```
1. Planning Phase:
   "Use @brainstorming to design my four-agents RPG architecture"

2. Setup Phase:
   "Use @mcp-builder to create an MCP for my game state API"

3. Development Phase:
   "Use @test-driven-development to build the combat system"

4. Memory Phase:
   Run /insights, then "Use @insight-extractor to save learnings"

5. Review Phase:
   "Use @security-auditor to review my agent skills"

6. Improvement Phase:
   "Use @retrospective to capture today's learnings"
```
