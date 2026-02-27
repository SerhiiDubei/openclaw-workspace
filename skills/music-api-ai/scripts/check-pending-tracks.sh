#!/bin/bash
# Check pending music tracks and send files via Telegram
# Only cron sends files - agent only registers

SUPABASE_URL="${SUPABASE_URL}"
SUPABASE_SERVICE_KEY="${SUPABASE_SERVICE_KEY}"
MUSICAPI_KEY="${MUSICAPI_KEY}"

# Clean up old ready tracks
rm -rf /tmp/ready_tracks/*

# Get tracks with status 'running' OR completed but not sent
TASK_IDS=$(curl -s "${SUPABASE_URL}/rest/v1/music_tracks?or=(metadata->>status.eq.running,and(metadata->>status.eq.completed,metadata->>sent.neq.true))&select=metadata->>task_id" \
  -H "apikey: ${SUPABASE_SERVICE_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" | jq -r '.[].task_id' | sort -u)

for TASK_ID in $TASK_IDS; do
  # Check MusicAPI status
  STATUS_RESPONSE=$(curl -s "https://api.musicapi.ai/api/v1/sonic/task/${TASK_ID}" \
    -H "Authorization: Bearer ${MUSICAPI_KEY}")
  
  V1_STATE=$(echo "$STATUS_RESPONSE" | jq -r '.data[0].state')
  V2_STATE=$(echo "$STATUS_RESPONSE" | jq -r '.data[1].state')
  
  # Only process if BOTH are ready
  if [ "$V1_STATE" = "succeeded" ] && [ "$V2_STATE" = "succeeded" ]; then
    # Get track info
    TRACK_RECORD=$(curl -s "${SUPABASE_URL}/rest/v1/music_tracks?metadata->>task_id=eq.${TASK_ID}&limit=1" \
      -H "apikey: ${SUPABASE_SERVICE_KEY}" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}")
    
    USER_ID=$(echo "$TRACK_RECORD" | jq -r '.[0].user_id')
    USERNAME=$(echo "$TRACK_RECORD" | jq -r '.[0].username')
    TRACK_NAME=$(echo "$TRACK_RECORD" | jq -r '.[0].track_name')
    
    # Check if already sent - SKIP if sent=true
    ALREADY_SENT=$(echo "$TRACK_RECORD" | jq -r '.[0].metadata.sent // "false"')
    if [ "$ALREADY_SENT" = "true" ]; then
      echo "Skipping ${TRACK_NAME} - already sent"
      continue
    fi
    
    # Get URLs
    V1_URL=$(echo "$STATUS_RESPONSE" | jq -r '.data[0].audio_url')
    V2_URL=$(echo "$STATUS_RESPONSE" | jq -r '.data[1].audio_url')
    V1_CLIP=$(echo "$STATUS_RESPONSE" | jq -r '.data[0].clip_id')
    V2_CLIP=$(echo "$STATUS_RESPONSE" | jq -r '.data[1].clip_id')
    V1_DUR=$(echo "$STATUS_RESPONSE" | jq -r '.data[0].duration')
    V2_DUR=$(echo "$STATUS_RESPONSE" | jq -r '.data[1].duration')
    
    # Download files
    DATE=$(date +%Y-%m-%d)
    OUTPUT_DIR="/tmp/ready_tracks/${USERNAME}"
    mkdir -p "$OUTPUT_DIR"
    
    V1_FILE="${OUTPUT_DIR}/${USERNAME} - ${TRACK_NAME} - v1.mp3"
    V2_FILE="${OUTPUT_DIR}/${USERNAME} - ${TRACK_NAME} - v2.mp3"
    
    curl -s -L "$V1_URL" -o "$V1_FILE"
    curl -s -L "$V2_URL" -o "$V2_FILE"
    
    # Upload to Storage
    V1_PATH="music/tracks/${USERNAME}/${DATE}/${USERNAME} - ${TRACK_NAME} - v1.mp3"
    V2_PATH="music/tracks/${USERNAME}/${DATE}/${USERNAME} - ${TRACK_NAME} - v2.mp3"
    
    curl -s -X POST "${SUPABASE_URL}/storage/v1/object/$(echo "$V1_PATH" | sed 's/ /%20/g')" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: audio/mpeg" --data-binary @"$V1_FILE" > /dev/null
    
    curl -s -X POST "${SUPABASE_URL}/storage/v1/object/$(echo "$V2_PATH" | sed 's/ /%20/g')" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: audio/mpeg" --data-binary @"$V2_FILE" > /dev/null
    
    # Update database - mark as sent (only v1 record)
    curl -s -X PATCH "${SUPABASE_URL}/rest/v1/music_tracks?id=eq.$(echo "$TRACK_RECORD" | jq -r '.[0].id')" \
      -H "apikey: ${SUPABASE_SERVICE_KEY}" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: application/json" \
      -d "{
        \"audio_url\": \"${V1_URL}\",
        \"clip_id\": \"${V1_CLIP}\",
        \"duration\": \"${V1_DUR}\",
        \"storage_path\": \"${V1_PATH}\",
        \"metadata\": {\"status\": \"completed\", \"sent\": \"true\", \"task_id\": \"${TASK_ID}\", \"sent_at\": \"$(date -Iseconds)\"}
      }" > /dev/null
    
    echo "SENT:${USER_ID}:${USERNAME}:${TRACK_NAME}"
  fi
done
