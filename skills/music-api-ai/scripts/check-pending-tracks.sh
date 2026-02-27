#!/bin/bash
# Check pending music tracks and send files via Telegram
# Runs every 2 minutes via cron

SUPABASE_URL="${SUPABASE_URL}"
SUPABASE_SERVICE_KEY="${SUPABASE_SERVICE_KEY}"
MUSICAPI_KEY="${MUSICAPI_KEY}"

# Get tracks that need processing:
# 1. status = 'running' (new tracks)
# 2. status = 'completed' BUT sent is NULL or not 'true' (finished but not sent)
PENDING_TRACKS=$(curl -s "${SUPABASE_URL}/rest/v1/music_tracks?or=(metadata->>status.eq.running,and(metadata->>status.eq.completed,or(metadata->>sent.is.null,metadata->>sent.neq.true)))&select=*" \
  -H "apikey: ${SUPABASE_SERVICE_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}")

# Process each track
echo "$PENDING_TRACKS" | jq -c '.[]' | while read TRACK; do
  ID=$(echo "$TRACK" | jq -r '.id')
  USER_ID=$(echo "$TRACK" | jq -r '.user_id')
  USERNAME=$(echo "$TRACK" | jq -r '.username')
  TRACK_NAME=$(echo "$TRACK" | jq -r '.track_name')
  VARIANT=$(echo "$TRACK" | jq -r '.variant')
  TASK_ID=$(echo "$TRACK" | jq -r '.metadata.task_id // empty')
  SENT=$(echo "$TRACK" | jq -r '.metadata.sent // "false"')
  
  # Skip if already sent
  if [ "$SENT" = "true" ]; then
    echo "Skipping $TRACK_NAME v$VARIANT - already sent"
    continue
  fi
  
  # Skip if no task_id (can't check status)
  if [ -z "$TASK_ID" ]; then
    echo "Skipping $TRACK_NAME v$VARIANT - no task_id"
    continue
  fi
  
  # Check MusicAPI status
  STATUS_RESPONSE=$(curl -s "https://api.musicapi.ai/api/v1/sonic/task/${TASK_ID}" \
    -H "Authorization: Bearer ${MUSICAPI_KEY}")
  
  # Get variant status (0-indexed in API)
  API_INDEX=$((VARIANT - 1))
  STATE=$(echo "$STATUS_RESPONSE" | jq -r ".data[${API_INDEX}].state // \"unknown\"")
  
  if [ "$STATE" = "succeeded" ]; then
    # Get file info
    AUDIO_URL=$(echo "$STATUS_RESPONSE" | jq -r ".data[${API_INDEX}].audio_url")
    CLIP_ID=$(echo "$STATUS_RESPONSE" | jq -r ".data[${API_INDEX}].clip_id")
    DURATION=$(echo "$STATUS_RESPONSE" | jq -r ".data[${API_INDEX}].duration // \"0\"")
    
    # Normalize username - replace spaces with underscores, remove special chars
    USERNAME_CLEAN=$(echo "$USERNAME" | tr ' ' '_' | tr -cd '[:alnum:]_-')
    
    # Download file
    DATE=$(date +%Y-%m-%d)
    OUTPUT_DIR="/tmp/cron_tracks/${USERNAME_CLEAN}"
    mkdir -p "$OUTPUT_DIR"
    
    SAFE_NAME="${USERNAME_CLEAN} - ${TRACK_NAME} - v${VARIANT}.mp3"
    LOCAL_FILE="${OUTPUT_DIR}/${SAFE_NAME}"
    
    curl -s -L "$AUDIO_URL" -o "$LOCAL_FILE"
    
    # Upload to Storage with clean path
    STORAGE_PATH="music/tracks/${USERNAME_CLEAN}/${DATE}/${SAFE_NAME}"
    curl -s -X POST "${SUPABASE_URL}/storage/v1/object/$(echo "$STORAGE_PATH" | sed 's/ /%20/g')" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: audio/mpeg" \
      --data-binary @"$LOCAL_FILE" > /dev/null
    
    # Update database - mark as completed and sent
    curl -s -X PATCH "${SUPABASE_URL}/rest/v1/music_tracks?id=eq.${ID}" \
      -H "apikey: ${SUPABASE_SERVICE_KEY}" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: application/json" \
      -d "{
        \"audio_url\": \"${AUDIO_URL}\",
        \"clip_id\": \"${CLIP_ID}\",
        \"duration\": \"${DURATION}\",
        \"storage_path\": \"${STORAGE_PATH}\",
        \"metadata\": {
          \"status\": \"completed\",
          \"sent\": \"true\",
          \"sent_at\": \"$(date -Iseconds)\",
          \"task_id\": \"${TASK_ID}\"
        }
      }" > /dev/null
    
    # Output for sending via Telegram
    echo "SEND:${USER_ID}:${USERNAME}:${TRACK_NAME}:${VARIANT}:${LOCAL_FILE}"
    
    # Clean up - will be done by the caller after sending
    
  elif [ "$STATE" = "running" ] || [ "$STATE" = "pending" ]; then
    echo "Waiting for $TRACK_NAME v$VARIANT - status: $STATE"
  else
    echo "Failed $TRACK_NAME v$VARIANT - status: $STATE"
  fi
done

# Clean up empty directories
rmdir /tmp/cron_tracks/* 2>/dev/null || true

# Clean up old files (older than 1 hour)
find /tmp/cron_tracks -name "*.mp3" -type f -mmin +60 -delete 2>/dev/null || true
