#!/bin/bash
# validate-session-log.sh - Перевірка чи записана сесія перед відповіддю

USERNAME="${1:-bomberman047}"
DATE=$(date +%Y-%m-%d)
SESSION_FILE="/root/.openclaw/workspace/memory/users/${USERNAME}/sessions/${DATE}.md"

if [ ! -f "$SESSION_FILE" ]; then
    echo "❌ ERROR: Session file $SESSION_FILE does not exist!"
    echo "Creating file..."
    
    mkdir -p "$(dirname "$SESSION_FILE")"
    cat > "$SESSION_FILE" << EOF
# Сесія: $DATE

## Учасники
- Сергій Дубей (@$USERNAME)

## Лог повідомлень

EOF
    echo "✅ Created: $SESSION_FILE"
    exit 1
else
    echo "✅ Session file exists: $SESSION_FILE"
    exit 0
fi
