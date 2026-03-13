#!/bin/bash
# Log a message to the user's session file

USERNAME="$1"
DATE="$2"
TIMESTAMP="$3"
CONTENT="$4"

if [ -z "$USERNAME" ] || [ -z "$DATE" ] || [ -z "$TIMESTAMP" ] || [ -z "$CONTENT" ]; then
  echo "Usage: $0 <username> <YYYY-MM-DD> <timestamp> <content>"
  exit 1
fi

SESSION_DIR="memory/users/${USERNAME}/sessions"
SESSION_FILE="${SESSION_DIR}/${DATE}.md"

mkdir -p "$SESSION_DIR"

# Add separator if file exists and is not empty
if [ -s "$SESSION_FILE" ]; then
  echo "" >> "$SESSION_FILE"
fi

echo "**${TIMESTAMP}**" >> "$SESSION_FILE"
echo "" >> "$SESSION_FILE"
echo "> ${CONTENT}" >> "$SESSION_FILE"

echo "Logged to $SESSION_FILE"
