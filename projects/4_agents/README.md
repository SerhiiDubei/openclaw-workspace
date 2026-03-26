# 4_agents / MCS (Multi-Consciousness System)

## 🎯 Проєкт

Система емуляції мультисвідомості для NPC в narrative RPG. Замість простих станів ("злий", "наляканий") — конкуруючі personas, які формують глибоку, непередбачувану поведінку персонажів.

## 📁 Структура

```
projects/4_agents/
├── MCS_TECH_SPEC_v1.md      # ← ПОЧИНАЙ ТУТ (повне ТЗ)
├── mcs_emulation.py          # ← Емуляція (запускай для демо)
├── README.md                 # ← Цей файл
└── implementation/           # ← Сюди будемо писати код
    ├── engine/
    │   ├── __init__.py
    │   ├── tick_processor.py
    │   ├── delta.py
    │   └── meta_mind.py
    └── personas/
        ├── __init__.py
        ├── base.py
        ├── protector.py
        ├── instinct.py
        ├── thinker.py
        └── mask.py
```

## 🚀 Швидкий старт

### 1. Прочитай спеку
```bash
# Відкрий в редакторі
code projects/4_agents/MCS_TECH_SPEC_v1.md
```

### 2. Запусти емуляцію
```bash
cd projects/4_agents
python mcs_emulation.py
```

Очікуваний вивід:
```
============================================================
MCS EMULATION: Катерина — захист сестри
============================================================

============================================================
1. Гравець погрожує сестрі
============================================================
NPC: katerina | Tick #1
============================================================

📢 ПОДІЯ: loved_one_threatened (інтенсивність: 0.9)

🎭 PERSONAS:
  protector    █████████░░░  45.2% [—0.0% —]
    💭 Вона під моїм захистом.
  ...
```

### 3. Подивись приклади
- Секція 5 у TECH_SPEC — візуалізація 3 ticks
- Розділ "Емуляція" — пояснення всіх компонентів

## 🧠 Основні концепції

| Концепція | Опис |
|-----------|------|
| **4 Personas** | Protector, Instinct, Thinker, Mask — базові архетипи |
| **Tick System** | Подія → оцінка → softmax → delta → вихід |
| **Delta** | Різкість зміни стану (EXPLOSIVE/RAPID/GRADUAL/STABLE) |
| **Whispers** | Внутрішній монолог для debug та narrative |
| **Core Connection** | Personas читають CORE.json кожного NPC |

## 🔧 Як працювати з Claude

### Prompt шаблони в TECH_SPEC:
1. **Prompt #1** — Генерація persona з CORE
2. **Prompt #2** — Обробка tick
3. **Prompt #3** — Meta-mind (фінальний output)

### Приклад використання:
```
Контекст: Працюємо над implementation personas/protector.py

Промпт:
"З Tech Spec секції 2.3.1 візьми специфікацію Protector.
Створи клас ProtectorPersona що наслідує BasePersona.
Реалізуй evaluate() з усіма тригерами.
Додай whisper generation з delta-модифікаторами."
```

## 📋 Roadmap

- [ ] **Phase 1**: Core Engine (TickProcessor, Delta, Softmax)
- [ ] **Phase 2**: 4 Personas (hardcoded configs)
- [ ] **Phase 3**: Core Integration (читання CORE.json)
- [ ] **Phase 4**: Meta-Mind (whispers → дії)
- [ ] **Phase 5**: Polish (баланс, тюнінг)

## 🔗 Інтеграція

Цей модуль підключається до існуючої структури 4_agents:

```
npc_name/
├── CORE.json              # ← Читаємо звідси
├── SOUL.md                # ← Контекст для whispers  
├── BIO.md                 # ← Історія
├── MEMORY.json            # ← Зберігаємо persona memory
├── consciousness/         # ← НОВИЙ МОДУЛЬ (цей проєкт)
│   └── ...
└── states/                # ← Існуюча система
```

## 👥 Команда

- **Product/Architecture**: Сергій Дубей
- **AI Advisor**: Kimi Claw (upper-level guidance)
- **Implementation**: Claude / GPT + Сергій

## 📝 Правила роботи

1. **Всі зміни через Kimi** — перед комітом показуй що зробив
2. **Тести обов'язкові** — кожна фаза має тест
3. **Документація** — оновлюй TECH_SPEC при змінах архітектури
4. **Називай референси** — чий стиль використовуєш (Dieter Rams, Carver, etc.)

---

**Статус**: Phase 0 — Ready to implement
**Останнє оновлення**: 2026-03-26