# For Agents / 4_agents — План Розробки UI/UX

> **Проєкт:** 4_agents (Island) — гра з агентами-особистостями  
> **Формат:** План розробки з TODO по модулях  
> **Оновлено:** 2026-03-16

---

## 🎯 Vision

Гра, де 4 агенти-особистості проходять ритуал ініціації (12 питань → SOUL-профіль), отримують унікальні характеристики та зустрічаються в напруженій соціальній дилемі на 10 раундів.

**Core Loop:**
1. Створити агента (ритуал ініціації)
2. Зібрати 4 агентів в лоббі
3. Пройти 10 раундів взаємодії
4. Отримати результати + прогресія

---

## 🎨 Візуальний Стиль

### Загальна Концепція
- **Назва стилю:** "Digital Ritual" — поєднання технологічності та містичності
- **Референс:** https://possumbilities.github.io/games.html
- **Атмосфера:** Темний острів, ритуали, напруга, технологічна естетика

### Кольорова Палітра

```css
/* Основні */
--bg-primary: #0a0a0f;        /* Глибокий чорний фон */
--bg-secondary: #12121a;      /* Картки, панелі */
--bg-tertiary: #1a1a25;       /* Ховери, активні елементи */

/* Акценти */
--accent-orange: #ff6b35;     /* Основний акцент, CTA */
--accent-purple: #7c3aed;     /* Містичний, SOUL-енергія */
--accent-cyan: #06b6d4;       /* Технологічний, інфо */
--accent-gold: #f59e0b;       /* Нагороди, рівні */

/* Текст */
--text-primary: #f8fafc;      /* Основний */
--text-secondary: #94a3b8;    /* Другорядний */
--text-muted: #64748b;        /* Підказки */

/* Стани */
--success: #10b981;           /* Кооперація, успіх */
--danger: #ef4444;            /* Зрада, небезпека */
--warning: #f59e0b;           /* Увага */
```

### Типографіка

**Заголовки:**
- Шрифт: `Press Start 2P` або `VT323` (pixel-style)
- Розміри: 48px (H1), 32px (H2), 24px (H3)
- Ефекти: Легкий glow для акцентів

**Основний текст:**
- Шрифт: `Inter` або `JetBrains Mono`
- Розмір: 16px body, 14px small
- Міжрядковий: 1.6

**Спеціальні:**
- SOUL-цитати: курсив + monospace
- Код/CORE.json: `Fira Code`

### UI Компоненти (База)

**Кнопки:**
```
Primary:    Оранжевий фон, білий текст, піксельний бордер 2px
Secondary:  Прозорий, оранжева рамка, оранжевий текст
Ghost:      Без рамки, тільки текст + іконка
Danger:     Червоний фон, для зради/небезпечних дій
```

**Картки:**
```
- Фон: bg-secondary
- Бордер: 1px solid з прозорістю
- Border-radius: 12px
- Тінь: м'яка фіолетова glow для акцентних
- Паддінг: 24px
```

**Інпути:**
```
- Фон: bg-primary
- Бордер: 1px solid bg-tertiary
- Focus: accent-orange border + glow
- Placeholder: text-muted
```

### Анімації (Ключові)

| Анімація | Тривалість | Опис |
|----------|------------|------|
| Page Transition | 400ms | Fade + slide up (20px) |
| Seed Reveal | 2000ms | Партикли збігаються в центр, формують сід |
| Typing Text | 30ms/char | Ефект друку для питань |
| Card Flip | 600ms | 3D flip для розкриття рішень |
| Number Count | 800ms | Плавний підрахунок очок |
| Pulse Glow | 2000ms | Пульсуючий glow для активних елементів |
| Shake | 300ms | Тряска для помилок/зради |

---

## 📋 План Розробки по Модулях

### МОДУЛЬ 1: Система Авторизації та Сесій

**Мета:** Дозволити користувачу створювати акаунт, зберігати агентів, синхронізуватись між пристроями.

**TODO:**

- [ ] **Auth Service**
  - [ ] Інтеграція з Clerk/Supabase Auth
  - [ ] Екран логіну (email/password + OAuth)
  - [ ] Екран реєстрації
  - [ ] Відновлення паролю

- [ ] **User Profile**
  - [ ] Страница профілю (username, аватар)
  - [ ] Налаштування (сповіщення, приватність)
  - [ ] Видалення акаунту

- [ ] **Session Persistence**
  - [ ] JWT токени
  - [ ] Refresh token logic
  - [ ] Logout з усіх пристроїв

**Компоненти:**
```
src/modules/auth/
├── components/
│   ├── LoginForm.tsx
│   ├── RegisterForm.tsx
│   ├── OAuthButtons.tsx
│   └── AuthGuard.tsx          # HOC для захищених роутів
├── hooks/
│   └── useAuth.ts
├── services/
│   └── authService.ts
└── types/
    └── auth.types.ts
```

**API:**
```typescript
POST /api/auth/login
POST /api/auth/register
POST /api/auth/logout
GET  /api/auth/me
```

---

### МОДУЛЬ 2: Ритуал Ініціалізації (Init Ritual)

**Мета:** Глибокий, атмосферний процес створення агента через 12 питань.

**TODO:**

- [ ] **Seed Generation Phase**
  - [ ] Екран з анімацією генерації сіда
  - [ ] Візуалізація "народження світу" (частки, світіння)
  - [ ] API: `POST /generate-seed`
  - [ ] Зберігання session_id

- [ ] **Question Sequence**
  - [ ] Компонент QuestionCard з анімацією друку
  - [ ] Прогрес-бар (1/12 → 12/12)
  - [ ] Таймер між питаннями (опціонально)
  - [ ] API: `POST /generate-question`, `POST /submit-answer`
  - [ ] Контекстні переходи (м'які фрази між блоками питань)

- [ ] **Review Phase**
  - [ ] Екран перегляду всіх відповідей
  - [ ] Можливість редагувати відповідь
  - [ ] Кнопка "Compile SOUL"

- [ ] **Compilation Phase**
  - [ ] Анімація обробки (термінал-стиль, прогрес-бар)
  - [ ] API: `POST /compile-soul`
  - [ ] Обробка помилок

- [ ] **Reveal Phase**
  - [ ] Красива презентація SOUL.md
  - [ ] Візуалізація CORE.json (графік характеристик)
  - [ ] Кнопки: "Save Agent", "Start Game", "Share"

**Компоненти:**
```
src/modules/init-ritual/
├── phases/
│   ├── SeedPhase.tsx          # Генерація сіда
│   ├── QuestionPhase.tsx      # 12 питань
│   ├── ReviewPhase.tsx        # Перегляд відповідей
│   ├── CompilationPhase.tsx   # Компіляція
│   └── RevealPhase.tsx        # Результат
├── components/
│   ├── QuestionCard.tsx       # Карточка питання
│   ├── AnswerInput.tsx        # Поле відповіді
│   ├── ProgressBar.tsx        # Прогрес 1/12
│   ├── SeedVisualizer.tsx     # Візуалізація сіда
│   ├── SoulDisplay.tsx        # Відображення SOUL.md
│   └── CoreRadarChart.tsx     # Графік характеристик
├── hooks/
│   ├── useInitSession.ts      # Управління сесією
│   └── useQuestionFlow.ts     # Логіка питань
└── services/
    └── initService.ts
```

**Стан (State):**
```typescript
interface InitSession {
  sessionId: string;
  seed: string;
  currentQuestion: number;
  answers: Answer[];
  isCompiling: boolean;
  result?: {
    soul: string;
    core: CoreJson;
  };
}
```

---

### МОДУЛЬ 3: Управління Агентами (Agent Library)

**Мета:** Бібліотека створених агентів, їх перегляд, редагування, видалення.

**TODO:**

- [ ] **Agent List View**
  - [ ] Сітка агентів (grid/list toggle)
  - [ ] Карточка агента: аватар, ім'я, рівень, кількість ігор
  - [ ] Фільтри: за рівнем, за датою, за ім'ям
  - [ ] Сортування
  - [ ] Пагінація або infinite scroll

- [ ] **Agent Detail View**
  - [ ] Повний SOUL.md
  - [ ] CORE.json з візуалізацією
  - [ ] Історія ігор (список)
  - [ ] Статистика (вінрейт, середній результат)
  - [ ] Кнопки: "Play", "Edit", "Delete", "Duplicate"

- [ ] **Agent Creation CTA**
  - [ ] Плаваюча кнопка "+ Create Agent"
  - [ ] Перехід до Init Ritual

- [ ] **Agent Actions**
  - [ ] Видалення з підтвердженням
  - [ ] Дублювання (клонування SOUL)
  - [ ] Експорт (SOUL.md + CORE.json)

**Компоненти:**
```
src/modules/agents/
├── components/
│   ├── AgentGrid.tsx          # Сітка агентів
│   ├── AgentList.tsx          # Список агентів
│   ├── AgentCard.tsx          # Карточка агента
│   ├── AgentDetail.tsx        # Детальний перегляд
│   ├── SoulRenderer.tsx       # Рендер SOUL.md
│   ├── CoreStats.tsx          # Статистика CORE
│   └── AgentFilters.tsx       # Фільтри і сортування
├── hooks/
│   ├── useAgents.ts           # Список агентів
│   └── useAgentDetail.ts      # Деталі агента
└── services/
    └── agentService.ts
```

---

### МОДУЛЬ 4: Лоббі та Підготовка до Гри

**Мета:** Вибір 4 агентів, налаштування параметрів гри.

**TODO:**

- [ ] **Lobby Creation**
  - [ ] Екран створення лоббі
  - [ ] Вибір режиму: "Single Player" / "Multiplayer" (майбутнє)
  - [ ] Налаштування: кількість раундів (10 за замовчуванням)

- [ ] **Agent Selection**
  - [ ] Drag-and-drop 4 агентів у слоти
  - [ ] Або мультиселект + кнопка "Confirm"
  - [ ] Превью агента при ховері
  - [ ] Валідація: треба рівно 4 агенти

- [ ] **Game Setup Panel**
  - [ ] Слайдер кількості раундів (5-20)
  - [ ] Перемикач складності (легка/середня/важка)
  - [ ] Додаткові опції (DM дозволені/заборонені)

- [ ] **Pre-Game Briefing**
  - [ ] Анімований вступ до сценарію
  - [ ] Представлення 4 агентів
  - [ ] Кнопка "Start Game"

**Компоненти:**
```
src/modules/lobby/
├── components/
│   ├── LobbyCreator.tsx       # Створення лоббі
│   ├── AgentSelector.tsx      # Вибір 4 агентів
│   ├── AgentSlot.tsx          # Слот для агента
│   ├── GameSetupPanel.tsx     # Налаштування
│   ├── BriefingScreen.tsx     # Вступ
│   └── LobbyHeader.tsx        # Заголовок лоббі
├── hooks/
│   └── useLobby.ts
└── services/
    └── lobbyService.ts
```

---

### МОДУЛЬ 5: Ігровий Процес (Game Engine UI)

**Мета:** Повноцінний UI для 10 раундів гри з усіма фазами.

**TODO:**

#### Фаза 5.1: Dialog Phase
- [ ] **Public Chat Interface**
  - [ ] Лента повідомлень (скрол)
  - [ ] Аватари агентів зі статусом (онлайн/друкує)
  - [ ] Typing indicator
  - [ ] Markdown підтримка

- [ ] **DM System**
  - [ ] Tray з іконками агентів для DM
  - [ ] Спливаючі DM вікна
  - [ ] Індикатори непрочитаних

- [ ] **Timer**
  - [ ] Зворотній відлік для фази
  - [ ] Візуальний прогрес

#### Фаза 5.2: Decision Phase
- [ ] **Decision Interface**
  - [ ] 3 колонки (по одній на кожного опонента)
  - [ ] Slider 0.0-1.0 для кожного
  - [ ] Мітки: "Зрадити" / "Кооперувати"
  - [ ] Превью результату (розрахунок очок)
  - [ ] Кнопка "Lock Decision"

#### Фаза 5.3: Reveal Phase
- [ ] **Results Matrix**
  - [ ] Таблиця 4×4 з результатами
  - [ ] Анімація flip для розкриття
  - [ ] Кольорова індикація (зелений = кооперація, червоний = зрада)
  - [ ] Загальний баланс після раунду

- [ ] **Round Summary**
  - [ ] Хто що вибрав (візуалізація)
  - [ ] Пари з найбільшими конфліктами
  - [ ] "Кооператор раунду" / "Зрадник раунду"

#### Фаза 5.4: Narrative Phase
- [ ] **Story Display**
  - [ ] Красива типографіка для тексту
  - [ ] Фонове зображення/атмосфера
  - [ ] Кнопка "Next Round" / "End Game"

**Компоненти:**
```
src/modules/game/
├── phases/
│   ├── DialogPhase.tsx        # Фаза діалогів
│   ├── DecisionPhase.tsx      # Фаза рішень
│   ├── RevealPhase.tsx        # Розкриття
│   └── NarrativePhase.tsx     # Оповідь
├── components/
│   ├── GameLayout.tsx         # Основний лейаут гри
│   ├── RoundIndicator.tsx     # Поточний раунд (1/10)
│   ├── AgentPanel.tsx         # Панель агента (баланс, статус)
│   ├── PublicChat.tsx         # Публічний чат
│   ├── DMTray.tsx             # Трей для DM
│   ├── DMWindow.tsx           # Вікно DM
│   ├── DecisionSlider.tsx     # Слайдер рішення
│   ├── ResultsMatrix.tsx      # Матриця результатів
│   ├── RoundSummary.tsx       # Підсумок раунду
│   ├── NarrativeCard.tsx      # Картка оповіді
│   └── GameTimer.tsx          # Таймер
├── hooks/
│   ├── useGame.ts             # Основний хук гри
│   ├── useDialog.ts           # Діалоги
│   ├── useDecision.ts         # Рішення
│   └── useTimer.ts            # Таймер
└── services/
    └── gameService.ts
```

**Game State:**
```typescript
interface GameState {
  gameId: string;
  round: number;
  maxRounds: number;
  phase: 'dialog' | 'decision' | 'reveal' | 'narrative';
  agents: AgentInGame[];
  messages: Message[];
  decisions: Decision[];
  results: RoundResult[];
  isFinished: boolean;
}
```

---

### МОДУЛЬ 6: Система Рівнів та Прогресії

**Мета:** Гейміфікація — агенти отримують досвід, підвищують рівень, розвивають характеристики.

**TODO:**

- [ ] **Level System**
  - [ ] Формула: кожні 20 емуляцій = новий рівень
  - [ ] XP за перемоги, кооперацію, унікальні стратегії
  - [ ] Таблиця рівнів з нагородами

- [ ] **Stats Distribution**
  - [ ] 4 характеристики: Cunning, Cooperation, Adaptability, Aggression
  - [ ] При підвищенні рівня: +5 очок на розподіл
  - [ ] Інтерфейс розподілу (drag або +/-)

- [ ] **Progress Visualization**
  - [ ] Прогрес-бар до наступного рівня
  - [ ] Анімація підвищення рівня
  - [ ] Історія прогресії (графік)

- [ ] **Achievements/Badges**
  - [ ] "Перша перемога"
  - [ ] "Майстер кооперації" (10 послідовних кооперацій)
  - [ ] "Король зради" (найбільше зрад)
  - [ ] "Survivor" (пройшов 50 ігор)

**Компоненти:**
```
src/modules/progression/
├── components/
│   ├── LevelBadge.tsx         # Значок рівня
│   ├── ProgressBar.tsx        # Прогрес до наступного
│   ├── StatsPanel.tsx         # Панель характеристик
│   ├── StatDistributor.tsx    # Розподіл очок
│   ├── LevelUpModal.tsx       # Модалка підвищення
│   ├── AchievementsGrid.tsx   # Сітка досягнень
│   └── XpHistoryChart.tsx     # Графік XP
└── hooks/
    └── useProgression.ts
```

---

### МОДУЛЬ 7: Лідерборди та Статистика

**Мета:** Порівняння результатів, топи, аналітика.

**TODO:**

- [ ] **Global Leaderboard**
  - [ ] Топ агентів за рівнем
  - [ ] Топ агентів за вінрейтом
  - [ ] Топ агентів за загальними очками
  - [ ] Фільтри: за тиждень/місяць/все час

- [ ] **Personal Stats**
  - [ ] Загальна кількість ігор
  - [ ] Середній результат
  - [ ] Улюблена стратегія (графік)
  - [ ] Історія останніх 10 ігор

- [ ] **Game History**
  - [ ] Список всіх ігор
  - [ ] Фільтри за датою, агентами, результатом
  - [ ] Детальний перегляд гри (реплей)

**Компоненти:**
```
src/modules/leaderboards/
├── components/
│   ├── LeaderboardTable.tsx   # Таблиця лідерів
│   ├── LeaderboardFilters.tsx # Фільтри
│   ├── PersonalStatsPanel.tsx # Особиста статистика
│   ├── GameHistoryList.tsx    # Історія ігор
│   ├── GameReplayViewer.tsx   # Перегляд гри
│   └── StatsChart.tsx         # Графіки статистики
└── hooks/
    └── useLeaderboard.ts
```

---

### МОДУЛЬ 8: Адмін Панель

**Мета:** Керування системою, масові операції, аналітика.

**TODO:**

- [ ] **Batch Operations**
  - [ ] Запуск N емуляцій (наприклад, 50)
  - [ ] Вибір учасників для симуляції
  - [ ] Прогрес-бар виконання
  - [ ] Логи виконання

- [ ] **Agent Management**
  - [ ] Список всіх агентів в системі
  - [ ] CRUD операції
  - [ ] Бан/розбан агентів

- [ ] **System Analytics**
  - [ ] Графік активності
  - [ ] Розподіл стратегій
  - [ ] Топ використовуваних агентів
  - [ ] Експорт даних (CSV/JSON)

- [ ] **Configuration**
  - [ ] Налаштування правил гри
  - [ ] Баланс економіки (XP, нагороди)
  - [ ] Параметри рівнів

**Компоненти:**
```
src/modules/admin/
├── components/
│   ├── AdminLayout.tsx        # Лейаут адмінки
│   ├── BatchRunner.tsx        # Масовий запуск
│   ├── AgentManager.tsx       # Управління агентами
│   ├── SystemStats.tsx        # Системна аналітика
│   ├── ConfigPanel.tsx        # Налаштування
│   └── ExportTools.tsx        # Експорт даних
├── hooks/
│   └── useAdmin.ts
└── services/
    └── adminService.ts
```

---

### МОДУЛЬ 9: Технічна Інфраструктура

**Мета:** Загальні компоненти, утиліти, стилі.

**TODO:**

- [ ] **Design System**
  - [ ] Button variants
  - [ ] Input, Select, Textarea
  - [ ] Card, Modal, Tooltip
  - [ ] Loading states, Skeletons

- [ ] **Animations**
  - [ ] Framer Motion конфігурація
  - [ ] Page transitions
  - [ ] Micro-interactions

- [ ] **State Management**
  - [ ] Zustand stores
  - [ ] React Query для API
  - [ ] Persistence (localStorage)

- [ ] **Routing**
  - [ ] React Router структура
  - [ ] Захищені роути
  - [ ] Deep linking для ігор

- [ ] **Error Handling**
  - [ ] Error Boundary
  - [ ] Toast notifications
  - [ ] Retry logic

**Структура:**
```
src/
├── components/ui/             # UI kit
├── hooks/                     # Глобальні хуки
├── lib/                       # Утиліти
├── stores/                    # Zustand stores
├── styles/                    # Глобальні стилі
├── types/                     # TypeScript types
└── utils/                     # Хелпери
```

---

## 📱 Responsive Design

### Breakpoints
```css
--mobile: 640px;      /* Мобільні */
--tablet: 768px;      /* Планшети */
--desktop: 1024px;    /* Десктоп */
--wide: 1280px;       /* Великі екрани */
```

### Mobile-First
- Всі компоненти працюють на мобільних
- Touch-friendly елементи (мінімум 44x44px)
- Swipe жести для навігації
- Bottom sheet для модалок

---

## 🚀 План Запуску (MVP → Full)

### Фаза 1: MVP (2-3 тижні)
- [ ] Модуль 2: Init Ritual (без анімацій)
- [ ] Модуль 4: Lobby (базовий)
- [ ] Модуль 5: Game (1 раунд, всі фази)
- [ ] Модуль 3: Agent List (базовий)

### Фаза 2: Core Game (2-3 тижні)
- [ ] 10 раундів повністю
- [ ] DM система
- [ ] Модуль 6: Levels (базовий)
- [ ] Анімації MVP

### Фаза 3: Polish (2 тижні)
- [ ] Модуль 1: Auth
- [ ] Модуль 7: Leaderboards
- [ ] Анімації premium
- [ ] Mobile optimization

### Фаза 4: Advanced (після запуску)
- [ ] Модуль 8: Admin Panel
- [ ] Multiplayer (real-time)
- [ ] Custom scenarios

---

## ❓ Відкриті Питання

1. **Auth:** Потрібна повноцінна авторизація або анонімні сесії спочатку?
2. **Avatar:** Генерувати піксель-арт аватари автоматично з SOUL?
3. **Monetization:** Буде платна версія / преміум агенти?
4. **Multiplayer:** Тільки AI-агенти чи плануються real-human ігри?
5. **Export:** Можливість експортувати агента в інші системи?

---

*Документ створено: 2026-03-16*  
*Автор: Kimi Claw*
