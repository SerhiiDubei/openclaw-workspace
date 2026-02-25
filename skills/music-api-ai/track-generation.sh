#!/bin/bash
# Async music generation tracker

TASK_ID="$1"
USER_ID="$2"
LOG_FILE="/tmp/music-gen-${TASK_ID}.log"

echo "[$(date)] Starting tracking for task: $TASK_ID, user: $USER_ID" > "$LOG_FILE"

for i in {1..20}; do
    sleep 30
    
    STATUS=$(curl -s -H "Authorization: Bearer 0f8dc17272d612483647231c6aef1705" \
        "https://api.musicapi.ai/api/v1/sonic/task/${TASK_ID}" | jq -r '.data[0].state')
    
    echo "[$(date)] Check $i: status=$STATUS" >> "$LOG_FILE"
    
    if [ "$STATUS" = "succeeded" ]; then
        echo "[$(date)] Task complete!" >> "$LOG_FILE"
        # Download and notify via OpenClaw gateway
        curl -s -X POST "http://127.0.0.1:18789/api/v1/message" \
            -H "Authorization: Bearer cd2bf242160b2cf3c47d4143d9228a9652033b70d06cd105" \
            -H "Content-Type: application/json" \
            -d "{\"target\":\"${USER_ID}\",\"message\":\"🎵 Трек готовий! (Task: ${TASK_ID})\"}" >> "$LOG_FILE" 2>&1
        exit 0
    fi
    
    if [ "$STATUS" = "failed" ] || [ "$STATUS" = "error" ]; then
        echo "[$(date)] Task failed!" >> "$LOG_FILE"
        exit 1
    fi
done

echo "[$(date)] Timeout reached" >> "$LOG_FILE"
exit 1
