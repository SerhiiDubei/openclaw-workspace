#!/bin/bash
# session-logger.sh — автоматичний запис сесій OpenClaw
# Запускається після кожної відповіді через cron

WORKSPACE="/root/.openclaw/workspace"
LOG_DIR="$WORKSPACE/.logs"
SESSION_DIR="$WORKSPACE/memory/users"

# Створюємо директорію для логів
mkdir -p "$LOG_DIR"

# Отримуємо поточну дату
DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M)

# Функція для запису сесії
log_session() {
    local username="$1"
    local user_message="$2"
    local assistant_message="$3"
    local message_type="${4:-text}"
    
    # Перетворюємо username в формат для директорії
    local user_dir=$(echo "$username" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr '_' '-')
    local session_file="$SESSION_DIR/$user_dir/sessions/$DATE.md"
    
    # Створюємо директорію, якщо не існує
    mkdir -p "$(dirname "$session_file")"
    
    # Якщо файл не існує — створюємо заголовок
    if [ ! -f "$session_file" ]; then
        cat > "$session_file" << EOF
# Сесія: $DATE

## Учасники
- [$username](tg://user?id=${username//[^0-9]/})

## Лог повідомлень

EOF
    fi
    
    # Додаємо запис
    cat >> "$session_file" << EOF
### $TIME
**[User]:** $user_message

**[Assistant]:** $assistant_message

EOF
    
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Logged to $session_file" >> "$LOG_DIR/session.log"
}

# Якщо скрипт викликаний з аргументами — записуємо одразу
if [ $# -ge 3 ]; then
    log_session "$1" "$2" "$3" "${4:-text}"
    exit 0
fi

echo "Usage: $0 <username> <user_message> <assistant_message> [message_type]"
exit 1
