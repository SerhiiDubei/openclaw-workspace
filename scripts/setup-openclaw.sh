#!/bin/bash
# setup-openclaw.sh — Автоматичне налаштування OpenClaw на новому сервері
# Запускати як root на свіжому Ubuntu 24.04

set -e

echo "🦞 OpenClaw Setup Script"
echo "========================"

# Перевірка root
if [ "$EUID" -ne 0 ]; then
   echo "❌ Запускати треба як root (sudo)"
   exit 1
fi

# 1. Оновлення системи
echo "📦 Оновлення системи..."
apt update && apt upgrade -y

# 2. Встановлення пакетів
echo "📦 Встановлення пакетів..."
apt install -y curl git nodejs npm python3 python3-pip nginx certbot ufw

# 3. Встановлення OpenClaw
echo "🦞 Встановлення OpenClaw..."
curl -fsSL https://openclaw.dev/install.sh | bash

# 4. Створення workspace
echo "📁 Налаштування workspace..."
mkdir -p /root/.openclaw/workspace
cd /root/.openclaw/workspace

# 5. Клонування GitHub репо
echo "📥 Завантаження проєктів..."
if [ ! -d ".git" ]; then
    git clone https://github.com/SerhiiDubei/openclaw-workspace.git .
fi

# 6. Налаштування прав
echo "🔧 Налаштування прав..."
chmod +x /root/.openclaw/workspace/scripts/*.sh 2>/dev/null || true

# 7. Створення .env шаблону
echo "📝 Створення шаблону .env..."
cat > /root/.openclaw/.env.template << 'EOF'
# Заповнити ці значення:
OPENAI_API_KEY=your_openai_key_here
TELEGRAM_BOT_TOKEN=8572675120:AAF86HqKSQ6no2pMFgjXwtuspd2sSsJOrxI
BRAVE_API_KEY=your_brave_key_here
EOF

# 8. Налаштування firewall
echo "🛡️ Налаштування firewall..."
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw allow 18789/tcp
ufw --force enable

# 9. Створення systemd service
echo "⚙️ Створення systemd service..."
cat > /etc/systemd/system/openclaw.service << 'EOF'
[Unit]
Description=OpenClaw Gateway
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/.openclaw
Environment="HOME=/root"
EnvironmentFile=/root/.openclaw/.env
ExecStart=/usr/bin/openclaw gateway start
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable openclaw

echo ""
echo "✅ Базове налаштування завершено!"
echo ""
echo "📋 Наступні кроки:"
echo "1. Заповни /root/.openclaw/.env (скопіюй з .env.template)"
echo "2. Налаштуй openclaw.json: openclaw config edit"
echo "3. Запусти: systemctl start openclaw"
echo "4. Перевір: curl http://localhost:18789/health"
echo ""
echo "📖 Детальна інструкція: /root/.openclaw/workspace/MIGRATION_GUIDE.md"
