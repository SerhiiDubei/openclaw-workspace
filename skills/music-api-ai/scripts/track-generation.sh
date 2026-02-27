#!/bin/bash
# Async music generation tracker
# Records progress to Supabase, sends notification when complete

TASK_ID="$1"
USER_ID="$2"
USERNAME="$3"
LOG_FILE="/tmp/music-gen-${TASK_ID}.log"

# Supabase config from environment
SUPABASE_URL="${SUPABASE_URL}"
SUPABASE_SERVICE_KEY="${SUPABASE_SERVICE_KEY}"

echo "[$(date)] Starting tracking for task: $TASK_ID, user: $USER_ID" > "$LOG_FILE"

for i in {1..20}; do
    sleep 30
    
    # Check status
    RESPONSE=$(curl -s -H "Authorization: Bearer ${MUSICAPI_KEY}" \
        "https://api.musicapi.ai/api/v1/sonic/task/${TASK_ID}")
    
    STATUS=$(echo "$RESPONSE" | jq -r '.data[0].state')
    CLIP_ID=$(echo "$RESPONSE" | jq -r '.data[0].clip_id')
    AUDIO_URL=$(echo "$RESPONSE" | jq -r '.data[0].audio_url')
    DURATION=$(echo "$RESPONSE" | jq -r '.data[0].duration')
    
    echo "[$(date)] Check $i: status=$STATUS" >> "$LOG_FILE"
    
    if [ "$STATUS" = "succeeded" ]; then
        echo "[$(date)] Task complete! clip_id=$CLIP_ID" >> "$LOG_FILE"
        
        # Save result to Supabase (metadata only, audio stays in Suno CDN)
        curl -s -X POST "${SUPABASE_URL}/rest/v1/music_tracks" \
            -H "apikey: ${SUPABASE_SERVICE_KEY}" \
            -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
            -H "Content-Type: application/json" \
            -d "{
                \"user_id\": \"${USER_ID}\",
                \"username\": \"${USERNAME}\",
                \"clip_id\": \"${CLIP_ID}\",
                \"audio_url\": \"${AUDIO_URL}\",
                \"duration\": \"${DURATION}\",
                \"task_id\": \"${TASK_ID}\",
                \"status\": \"completed\"
            }" >> "$LOG_FILE" 2>&1
        
        exit 0
    fi
    
    if [ "$STATUS" = "failed" ] || [ "$STATUS" = "error" ]; then
        echo "[$(date)] Task failed!" >> "$LOG_FILE"
        exit 1
    fi
done

echo "[$(date)] Timeout reached" >> "$LOG_FILE"
exit 1
