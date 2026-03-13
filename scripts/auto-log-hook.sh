#!/bin/bash
# auto-log-hook.sh — автоматичний запис сесії після відповіді
# Викликається через системний механізм

WORKSPACE="/root/.openclaw/workspace"
DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M)

# Отримуємо останнє повідомлення з логів Kimi
LAST_USER_MSG=$(tail -100 /var/log/openclay/kimi-bridge.log 2>/dev/null | grep "user.*message" | tail -1 | sed 's/.*message":"//;s/".*//')
LAST_ASSISTANT_MSG=$(tail -100 /var/log/openclay/kimi-bridge.log 2>/dev/null | grep "assistant.*message" | tail -1 | sed 's/.*message":"//;s/".*//')

# Якщо немає логів — використовуємо заглушку
if [ -z "$LAST_USER_MSG" ]; then
    exit 0
fi

# Визначаємо користувача з контексту
USERNAME="${SESSION_USER:-bomberman047}"
USER_ID="${SESSION_USER_ID:-488426634}"

# Викликаємо основний скрипт
$WORKSPACE/scripts/log-current-session.sh "$USERNAME" "$LAST_USER_MSG" "$LAST_ASSISTANT_MSG" "$USER_ID" 2>/dev/null
