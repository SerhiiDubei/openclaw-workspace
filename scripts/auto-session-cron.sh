#!/bin/bash
# auto-session-cron.sh — автоматичний запис сесій з логів OpenClaw
# Запускається кожні 5 хвилин через cron

WORKSPACE="/root/.openclaw/workspace"
STATE_FILE="$WORKSPACE/.logs/session-state.json"
LOG_FILE="$WORKSPACE/.logs/auto-session.log"
TELEGRAM_LOG="/root/.openclaw/.openclaw/telegram"

mkdir -p "$WORKSPACE/.logs"
mkdir -p "$WORKSPACE/memory/users"

# Завантажуємо стан (останній оброблений timestamp)
if [ -f "$STATE_FILE" ]; then
    LAST_PROCESSED=$(cat "$STATE_FILE" | grep -o '"lastProcessed":[0-9]*' | cut -d: -f2 || echo "0")
else
    LAST_PROCESSED=0
    echo '{"lastProcessed":0}' > "$STATE_FILE"
fi

CURRENT_TIME=$(date +%s)
DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M)

# Функція для запису в сесію
write_session() {
    local username="$1"
    local user_msg="$2"
    local assistant_msg="$3"
    local msg_date="${4:-$DATE}"
    
    # Конвертуємо username в формат директорії
    local user_dir=$(echo "$username" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr '_' '-')
    local session_file="$WORKSPACE/memory/users/$user_dir/sessions/$msg_date.md"
    
    mkdir -p "$(dirname "$session_file")"
    
    # Створюємо файл, якщо не існує
    if [ ! -f "$session_file" ]; then
        cat > "$session_file" << EOF
# Сесія: $msg_date

## Учасники
- $username

## Лог повідомлень

EOF
    fi
    
    # Додаємо запис
    cat >> "$session_file" << EOF
### $TIME
**[User]:** $user_msg

**[Assistant]:** $assistant_msg

EOF
    
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Written to $user_dir/$msg_date.md" >> "$LOG_FILE"
}

# Тимчасове рішення: записуємо тестовий запис
# В майбутньому тут буде парсинг логів Telegram

# Оновлюємо стан
echo "{\"lastProcessed\":$CURRENT_TIME}" > "$STATE_FILE"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Cron executed" >> "$LOG_FILE"
