#!/bin/bash
# Check pending music tracks and send files via Telegram
# Runs every 2 minutes via cron
# Updated for sunoapi.org provider

SUPABASE_URL="${SUPABASE_URL}"
SUPABASE_SERVICE_KEY="${SUPABASE_SERVICE_KEY}"
SUNOAPI_KEY="${SUNOAPI_KEY:-9d1c695345ed3583c3c56b26c45d0b50}"

# API Configuration
SUNOAPI_BASE="https://api.sunoapi.org/api/v1"

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
  
  # Check SunoAPI status
  STATUS_RESPONSE=$(curl -s "${SUNOAPI_BASE}/generate/record-info?taskId=${TASK_ID}" \
    -H "Authorization: Bearer ${SUNOAPI_KEY}")
  
  # Check if request was successful
  API_CODE=$(echo "$STATUS_RESPONSE" | jq -r '.code // 500')
  
  if [ "$API_CODE" != "200" ]; then
    echo "API error for $TRACK_NAME v$VARIANT - code: $API_CODE"
    continue
  fi
  
  # Get task status
  TASK_STATUS=$(echo "$STATUS_RESPONSE" | jq -r '.data.status // "UNKNOWN"')
  
  if [ "$TASK_STATUS" = "SUCCESS" ]; then
    # Get variant data (0-indexed in API)
    API_INDEX=$((VARIANT - 1))
    
    # Check if sunoData exists and has the variant
    SUNO_DATA_LENGTH=$(echo "$STATUS_RESPONSE" | jq -r '.data.response.sunoData | length // 0')
    
    if [ "$API_INDEX" -ge "$SUNO_DATA_LENGTH" ]; then
      echo "Variant $VARIANT not found for $TRACK_NAME - only $SUNO_DATA_LENGTH variants available"
      continue
    fi
    
    # Get file info
    AUDIO_URL=$(echo "$STATUS_RESPONSE" | jq -r ".data.response.sunoData[${API_INDEX}].audioUrl // empty")
    CLIP_ID=$(echo "$STATUS_RESPONSE" | jq -r ".data.response.sunoData[${API_INDEX}].id // empty")
    DURATION=$(echo "$STATUS_RESPONSE" | jq -r ".data.response.sunoData[${API_INDEX}].duration // \"0\"")
    
    if [ -z "$AUDIO_URL" ] || [ "$AUDIO_URL" = "null" ]; then
      echo "No audio URL for $TRACK_NAME v$VARIANT"
      continue
    fi
    
    # Normalize username: transliterate Cyrillic, keep spaces as-is for consistency
    USERNAME_CLEAN=$(python3 -c "
import sys
name = sys.argv[1]
# Cyrillic to Latin mapping
mapping = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'д': 'd', 'е': 'e', 'ё': 'yo',
    'ж': 'zh', 'з': 'z', 'и': 'y', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
    'і': 'i', 'ї': 'yi', 'є': 'ye', 'ґ': 'g'
}
result = ''
for c in name.lower():
    result += mapping.get(c, c)
# Keep original spacing (don't replace spaces with underscores)
result = ''.join(c for c in result if c.isalnum() or c in ' _-')
# Capitalize first letter of each word for consistency
result = ' '.join(word.capitalize() for word in result.split())
print(result)
" "$USERNAME")
    
    # Download file
    DATE=$(date +%Y-%m-%d)
    OUTPUT_DIR="/tmp/cron_tracks/${USERNAME_CLEAN}"
    mkdir -p "$OUTPUT_DIR"
    
    SAFE_NAME="${USERNAME_CLEAN} - ${TRACK_NAME} - v${VARIANT}.mp3"
    LOCAL_FILE="${OUTPUT_DIR}/${SAFE_NAME}"
    
    curl -s -L "$AUDIO_URL" -o "$LOCAL_FILE"
    
    # Verify file was downloaded
    if [ ! -f "$LOCAL_FILE" ] || [ ! -s "$LOCAL_FILE" ]; then
      echo "Failed to download $TRACK_NAME v$VARIANT"
      continue
    fi
    
    # Upload to Storage with clean path using multipart/form-data
    STORAGE_PATH="music/tracks/${USERNAME_CLEAN}/${DATE}/${SAFE_NAME}"
    
    # Create multipart upload using curl
    BOUNDARY="----FormBoundary$(date +%s%N)"
    
    # Build multipart body
    {
      echo "--${BOUNDARY}"
      echo 'Content-Disposition: form-data; name="file"; filename="'"${SAFE_NAME}"'"'
      echo "Content-Type: audio/mpeg"
      echo ""
      cat "$LOCAL_FILE"
      echo ""
      echo "--${BOUNDARY}--"
    } > /tmp/upload_body_$$.tmp
    
    curl -s -X POST "${SUPABASE_URL}/storage/v1/object/${STORAGE_PATH}" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: multipart/form-data; boundary=${BOUNDARY}" \
      --data-binary @/tmp/upload_body_$$.tmp > /dev/null
    
    rm -f /tmp/upload_body_$$.tmp
    
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
    
  elif [ "$TASK_STATUS" = "PENDING" ] || [ "$TASK_STATUS" = "RUNNING" ] || [ "$TASK_STATUS" = "PROCESSING" ]; then
    echo "Waiting for $TRACK_NAME v$VARIANT - status: $TASK_STATUS"
  else
    echo "Failed $TRACK_NAME v$VARIANT - status: $TASK_STATUS"
    # Update database with failed status
    curl -s -X PATCH "${SUPABASE_URL}/rest/v1/music_tracks?id=eq.${ID}" \
      -H "apikey: ${SUPABASE_SERVICE_KEY}" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: application/json" \
      -d "{
        \"metadata\": {
          \"status\": \"failed\",
          \"task_id\": \"${TASK_ID}\"
        }
      }" > /dev/null
  fi
done

# Clean up empty directories
rmdir /tmp/cron_tracks/* 2>/dev/null || true

# Clean up old files (older than 1 hour)
find /tmp/cron_tracks -name "*.mp3" -type f -mmin +60 -delete 2>/dev/null || true