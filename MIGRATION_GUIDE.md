# OpenClaw Migration Guide
## Перенесення з Kimi на DigitalOcean

---

## Що включено в бекап

- ✅ Всі проєкти (workspace/projects/)
- ✅ Пам'ять (workspace/memory/)
- ✅ Скилли (workspace/skills/)
- ✅ Агенти (workspace/agents/)
- ✅ Скрипти (workspace/scripts/)
- ✅ Конфігурація (openclaw.json) - без секретів
- ❌ API ключі (Kimi, OpenAI, Telegram) - треба ввести вручну
- ❌ Сесії (sessions) - можна відновити з GitHub

---

## Крок 1: Створення сервера (DigitalOcean)

### 1.1 Реєстрація
- Перейти на digitalocean.com
- Sign Up (через GitHub або email)
- Верифікація: прив'язати картку (спишуть $1, повернуть)
- Поповнити рахунок на $5

### 1.2 Створити Droplet
- **OS:** Ubuntu 24.04 (LTS)
- **Plan:** Basic $6/міс
- **Specs:** 1 GB RAM / 1 CPU / 25 GB SSD
- **Region:** Frankfurt (ближче до України)
- **Auth:** SSH key (рекомендовано) або пароль
- **Hostname:** claw-server

**Зберегти IP адресу!**

---

## Крок 2: Підключення та підготовка

```bash
# Підключення
ssh root@YOUR_DROPLET_IP

# Оновлення
apt update && apt upgrade -y

# Встановлення необхідних пакетів
apt install -y curl git nodejs npm python3 python3-pip nginx certbot

# Перевірка Node.js
node --version  # має бути v18+
npm --version
```

---

## Крок 3: Встановлення OpenClaw

```bash
# Встановлення
curl -fsSL https://openclaw.dev/install.sh | bash

# Перевірка
openclaw --version  # 2026.2.13 або новіше
```

---

## Крок 4: Відновлення даних

### 4.1 Клонуємо GitHub репо
```bash
cd /root/.openclaw/workspace
git clone https://github.com/SerhiiDubei/openclaw-workspace.git .
```

### 4.2 Відновлюємо сесії
```bash
# Сесії зберігаються в GitHub, але перевіримо
ls -la /root/.openclaw/workspace/memory/users/
```

---

## Крок 5: Налаштування API ключів

### 5.1 Створюємо .env файл
```bash
cat > /root/.openclaw/.env << 'EOF'
# OpenAI API Key
OPENAI_API_KEY=sk-proj-...  # Вставити свій ключ

# Telegram Bot Token
TELEGRAM_BOT_TOKEN=8572675120:AAF86HqKSQ6no2pMFgjXwtuspd2sSsJOrxI

# Optional: Brave Search
BRAVE_API_KEY=...
EOF
```

### 5.2 Налаштовуємо openclaw.json
```bash
openclaw config edit
```

Змінити:
- `gateway.bind` → "0.0.0.0"
- `gateway.publicUrl` → "https://www.bomberman047.com"
- `channels.telegram.botToken` → вставити токен
- `models.providers.openai` → додати OpenAI провайдера
- ВИДАЛИТИ `kimi-coding` провайдера

---

## Крок 6: Встановлення плагінів

### 6.1 Видаляємо китайські плагіни (якщо є)
```bash
openclaw plugins remove kimi-claw
openclaw plugins remove feishu
openclaw plugins remove dingtalk-connector
```

### 6.2 Встановлюємо потрібні
```bash
# Telegram (вже має бути вбудований)
# OpenAI bridge (якщо є в репо)
# Brave Search (якщо потрібен)
```

---

## Крок 7: Налаштування Cron

```bash
# Створюємо cron job для автозапису сесій
openclaw cron add --name "auto-session-logger" \
  --schedule "every 1m" \
  --command "Check recent conversation history and write any new messages to session files"
```

---

## Крок 8: Запуск та тестування

### 8.1 Запускаємо Gateway
```bash
openclaw gateway start
```

### 8.2 Перевіряємо
```bash
# Локально
curl http://localhost:18789/health

# Через тунель (після налаштування)
curl https://www.bomberman047.com/health
```

### 8.3 Тест Telegram
Написати боту в Telegram — має відповісти.

---

## Крок 9: Cloudflare Tunnel (опціонально)

### 9.1 Встановлення
```bash
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
dpkg -i cloudflared-linux-amd64.deb
```

### 9.2 Авторизація
```bash
cloudflared tunnel login
# Відкрити посилання в браузері, авторизуватися
```

### 9.3 Створення тунелю
```bash
cloudflared tunnel create openclaw-web
cloudflared tunnel route dns openclaw-web www.bomberman047.com

# Конфіг
cat > /root/.cloudflared/config.yml << 'EOF'
tunnel: TUNNEL_ID
credentials-file: /root/.cloudflared/TUNNEL_ID.json

ingress:
  - hostname: www.bomberman047.com
    service: http://localhost:18789
  - service: http_status:404
EOF

# Запуск
cloudflared tunnel run openclaw-web
```

---

## Крок 10: Автозапуск (Systemd)

### 10.1 OpenClaw Service
```bash
cat > /etc/systemd/system/openclaw.service << 'EOF'
[Unit]
Description=OpenClaw Gateway
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/openclaw gateway start
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable openclaw
systemctl start openclaw
```

### 10.2 Cloudflared Service
```bash
cloudflared service install
systemctl enable cloudflared
systemctl start cloudflared
```

---

## Крок 11: Pairing

1. Відкрити https://www.bomberman047.com
2. Ввести Gateway Token (згенерується автоматично)
3. Запитати pairing в Telegram: /pair
4. Підтвердити pairing
5. Готово!

---

## Тривалість

- Створення сервера: 5 хв
- Встановлення: 15 хв
- Налаштування: 20 хв
- Тестування: 10 хв
- **Всього: ~50 хвилин**

---

## Чекліст

- [ ] Сервер створено
- [ ] OpenClaw встановлено
- [ ] GitHub репо клоновано
- [ ] API ключі налаштовані
- [ ] Cron job створено
- [ ] Gateway запущено
- [ ] Telegram працює
- [ ] Cloudflare Tunnel працює
- [ ] Автозапуск налаштовано
- [ ] Pairing пройдено

---

## Після переїзду

1. На старому сервері: зупинити Kimi-Claw плагін
2. Перевірити що всі сесії перенесено
3. Видалити старий сервер (якщо не потрібен)
4. Насолоджуватися роботою без Kimi обмежень!
