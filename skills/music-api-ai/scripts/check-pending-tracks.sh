#!/bin/bash
# Check pending music tracks and process completed ones

SUPABASE_URL="${SUPABASE_URL}"
SUPABASE_SERVICE_KEY="${SUPABASE_SERVICE_KEY}"
MUSICAPI_KEY="${MUSICAPI_KEY}"

# Get pending tracks from Supabase
PENDING_TRACKS=$(curl -s "${SUPABASE_URL}/rest/v1/music_tracks?select=*&metadata->>status=eq.running" \
  -H "apikey: ${SUPABASE_SERVICE_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}")

# Check each track
for row in $(echo "$PENDING_TRACKS" | jq -r '.[] | @base64'); do
  _jq() {
    echo ${row} | base64 --decode | jq -r ${1}
  }
  
  ID=$(_jq '.id')
  TASK_ID=$(_jq '.metadata.task_id')
  USER_ID=$(_jq '.user_id')
  USERNAME=$(_jq '.username')
  VARIANT=$(_jq '.variant')
  
  if [ -n "$TASK_ID" ]; then
    # Check status via MusicAPI
    STATUS_RESPONSE=$(curl -s "https://api.musicapi.ai/api/v1/sonic/task/${TASK_ID}" \
      -H "Authorization: Bearer ${MUSICAPI_KEY}")
    
    # Get variant data
    TRACK_DATA=$(echo "$STATUS_RESPONSE" | jq -r ".data[$((VARIANT-1))]")
    STATE=$(echo "$TRACK_DATA" | jq -r '.state')
    
    if [ "$STATE" = "succeeded" ]; then
      CLIP_ID=$(echo "$TRACK_DATA" | jq -r '.clip_id')
      AUDIO_URL=$(echo "$TRACK_DATA" | jq -r '.audio_url')
      DURATION=$(echo "$TRACK_DATA" | jq -r '.duration')
      
      # Download to temp
      TEMP_FILE="/tmp/${USERNAME// /_}_v${VARIANT}.mp3"
      curl -s -L "$AUDIO_URL" -o "$TEMP_FILE"
      
      # Upload to Storage
      STORAGE_PATH="music/tracks/${USERNAME}/$(date +%Y-%m-%d)/${USERNAME// /%20}%20-%20v${VARIANT}.mp3"
      curl -s -X POST "${SUPABASE_URL}/storage/v1/object/${STORAGE_PATH}" \
        -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
        -H "Content-Type: audio/mpeg" \
        --data-binary @"$TEMP_FILE"
      
      # Update database
      curl -s -X PATCH "${SUPABASE_URL}/rest/v1/music_tracks?id=eq.${ID}" \
        -H "apikey: ${SUPABASE_SERVICE_KEY}" \
        -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
        -H "Content-Type: application/json" \
        -d "{
          \"audio_url\": \"${AUDIO_URL}\",
          \"clip_id\": \"${CLIP_ID}\",
          \"duration\": \"${DURATION}\",
          \"storage_path\": \"${STORAGE_PATH}\",
          \"metadata\": {\"status\": \"completed\", \"task_id\": \"${TASK_ID}\"}
        }"
      
      # Notify user via Telegram (through OpenClaw)
      echo "Track v${VARIANT} ready for ${USERNAME}"
      
      rm "$TEMP_FILE"
    fi
  fi
done
