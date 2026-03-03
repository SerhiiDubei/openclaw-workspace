#!/bin/bash
# log-current-session.sh — записує поточну сесію
# Викликається автоматично після кожної відповіді

WORKSPACE="/root/.openclaw/workspace"
DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M)

# Отримуємо дані з аргументів
USERNAME="$1"
USER_MESSAGE="$2"
ASSISTANT_MESSAGE="$3"
USER_ID="$4"

if [ -z "$USERNAME" ] || [ -z "$USER_MESSAGE" ]; then
    echo "Usage: $0 <username> <user_message> <assistant_message> [user_id]"
    exit 1
fi

# Конвертуємо username в формат директорії
USER_DIR=$(echo "$USERNAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr '_' '-')
SESSION_FILE="$WORKSPACE/memory/users/$USER_DIR/sessions/$DATE.md"

# Створюємо директорію
mkdir -p "$(dirname "$SESSION_FILE")"

# Створюємо файл, якщо не існує
if [ ! -f "$SESSION_FILE" ]; then
    cat > "$SESSION_FILE" << EOF
# Сесія: $DATE

## Учасники
- $USERNAME

## Лог повідомлень

EOF
fi

# Додаємо запис
cat >> "$SESSION_FILE" << EOF
### $TIME
**[User]:** $USER_MESSAGE

**[Assistant]:** $ASSISTANT_MESSAGE

EOF

echo "Session logged: $USER_DIR/$DATE.md"
