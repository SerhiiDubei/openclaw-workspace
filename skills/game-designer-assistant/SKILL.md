---
name: game-designer-assistant
description: Assistant for creating and managing evening/bar games. Helps generate questions, design game mechanics, and prepare game packs for 10-40 people. Use when user needs help with quiz games, team competitions, bar games, or any social gaming formats.
---

# Game Designer Assistant

Assistant for designing evening and bar games.

## What This Skill Does

Helps create games for groups of 10-40 people:
- Generates questions adapted to context (difficulty, format, audience)
- Suggests game mechanics based on constraints
- Prepares game packs ready to use
- Logs sessions to improve future games

## Core Concepts

### Game Parameters
Every game has:
- **Player count**: 10-40 people
- **Duration**: 30-60 minutes typical
- **Format**: Bar, home, corporate
- **Phase**: Start (high energy) → Mid (established) → Late (final)

### Question Attributes
- Difficulty (1-5)
- Topic (history, sport, pop culture, etc.)
- Format (bar quiz, blitz, circle, yes/no)
- Cooldown (can reuse or not)
- Target audience (age, location, interests)

### Game Formats
- **Bar quiz**: teams at tables, questions on screen/paper
- **Blitz**: 10-20 questions rapid-fire to one person
- **Circle**: questions move around the group
- **Team battle**: two teams compete
- **Donetki**: hints gradually revealed

## Workflow

### Creating a New Game
1. Ask: player count, duration, location, occasion
2. Suggest 2-3 mechanics suitable for context
3. Generate/select questions matching parameters
4. Export game pack (questions + rules + materials)

### After Game Session
1. Log what worked and what didn't
2. Update question ratings
3. Note mechanic effectiveness
4. Save insights for future games

## File Structure

```
sessions/           # Game session logs
questions/          # Question bank
mechanics/          # Game mechanics catalog
templates/          # Export templates
```

## Rules

- Always ask about audience (age, location, interests)
- Start phase needs highest energy questions
- Log every session for learning
- Questions must be answerable by target audience
- Keep game packs simple (no complex rules)

## Beta Status

This skill is in active development. Each real game session improves it.
