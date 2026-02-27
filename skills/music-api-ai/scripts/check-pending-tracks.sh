#!/bin/bash
# Check pending music tracks and prepare files for sending
# Returns list of ready tracks for agent to send

SUPABASE_URL="${SUPABASE_URL}"
SUPABASE_SERVICE_KEY="${SUPABASE_SERVICE_KEY}"
MUSICAPI_KEY="${MUSICAPI_KEY}"

READY_TRACKS=""

# Get unique task_ids with pending tracks
TASK_IDS=$(curl -s "${SUPABASE_URL}/rest/v1/music_tracks?select=metadata->>task_id&metadata->>status=eq.running&order=created_at.desc&limit=100" \
  -H "apikey: ${SUPABASE_SERVICE_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" | jq -r '.[].task_id' | sort -u)

for TASK_ID in $TASK_IDS; do
  # Check MusicAPI status
  STATUS_RESPONSE=$(curl -s "https://api.musicapi.ai/api/v1/sonic/task/${TASK_ID}" \
    -H "Authorization: Bearer ${MUSICAPI_KEY}")
  
  # Check BOTH variants
  V1_STATE=$(echo "$STATUS_RESPONSE" | jq -r '.data[0].state')
  V2_STATE=$(echo "$STATUS_RESPONSE" | jq -r '.data[1].state')
  
  # Only process if BOTH are ready
  if [ "$V1_STATE" = "succeeded" ] && [ "$V2_STATE" = "succeeded" ]; then
    # Get user info
    TRACK_RECORD=$(curl -s "${SUPABASE_URL}/rest/v1/music_tracks?metadata->>task_id=eq.${TASK_ID}&limit=1" \
      -H "apikey: ${SUPABASE_SERVICE_KEY}" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}")
    
    USER_ID=$(echo "$TRACK_RECORD" | jq -r '.[0].user_id')
    USERNAME=$(echo "$TRACK_RECORD" | jq -r '.[0].username')
    TRACK_NAME=$(echo "$TRACK_RECORD" | jq -r '.[0].track_name')
    
    # Get URLs
    V1_URL=$(echo "$STATUS_RESPONSE" | jq -r '.data[0].audio_url')
    V2_URL=$(echo "$STATUS_RESPONSE" | jq -r '.data[1].audio_url')
    V1_CLIP=$(echo "$STATUS_RESPONSE" | jq -r '.data[0].clip_id')
    V2_CLIP=$(echo "$STATUS_RESPONSE" | jq -r '.data[1].clip_id')
    V1_DUR=$(echo "$STATUS_RESPONSE" | jq -r '.data[0].duration')
    V2_DUR=$(echo "$STATUS_RESPONSE" | jq -r '.data[1].duration')
    
    # Create user folder if not exists
    DATE=$(date +%Y-%m-%d)
    USER_FOLDER="music/tracks/${USERNAME}/${DATE}"
    
    # Download files with correct names
    OUTPUT_DIR="/tmp/ready_tracks/${USERNAME}"
    mkdir -p "$OUTPUT_DIR"
    
    V1_FILENAME="${USERNAME} - ${TRACK_NAME} - v1.mp3"
    V2_FILENAME="${USERNAME} - ${TRACK_NAME} - v2.mp3"
    
    V1_FILE="${OUTPUT_DIR}/${V1_FILENAME}"
    V2_FILE="${OUTPUT_DIR}/${V2_FILENAME}"
    
    curl -s -L "$V1_URL" -o "$V1_FILE"
    curl -s -L "$V2_URL" -o "$V2_FILE"
    
    # Upload to Storage
    V1_PATH="${USER_FOLDER}/${V1_FILENAME}"
    V2_PATH="${USER_FOLDER}/${V2_FILENAME}"
    
    curl -s -X POST "${SUPABASE_URL}/storage/v1/object/$(echo "$V1_PATH" | sed 's/ /%20/g')" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: audio/mpeg" --data-binary @"$V1_FILE" > /dev/null
    
    curl -s -X POST "${SUPABASE_URL}/storage/v1/object/$(echo "$V2_PATH" | sed 's/ /%20/g')" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: audio/mpeg" --data-binary @"$V2_FILE" > /dev/null
    
    # Update database
    curl -s -X PATCH "${SUPABASE_URL}/rest/v1/music_tracks?metadata->>task_id=eq.${TASK_ID}&variant=eq.1" \
      -H "apikey: ${SUPABASE_SERVICE_KEY}" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: application/json" \
      -d "{\"audio_url\": \"${V1_URL}\", \"clip_id\": \"${V1_CLIP}\", \"duration\": \"${V1_DUR}\", \"storage_path\": \"${V1_PATH}\", \"metadata\": {\"status\": \"completed\"}}" > /dev/null
    
    curl -s -X PATCH "${SUPABASE_URL}/rest/v1/music_tracks?metadata->>task_id=eq.${TASK_ID}&variant=eq.2" \
      -H "apikey: ${SUPABASE_SERVICE_KEY}" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: application/json" \
      -d "{\"audio_url\": \"${V2_URL}\", \"clip_id\": \"${V2_CLIP}\", \"duration\": \"${V2_DUR}\", \"storage_path\": \"${V2_PATH}\", \"metadata\": {\"status\": \"completed\"}}" > /dev/null
    
    # Add to ready list
    READY_TRACKS="${READY_TRACKS}${USERNAME}|${TRACK_NAME}|${V1_FILE}|${V2_FILE}|${USER_ID}\n"
  fi
done

# Output ready tracks for agent to send
echo -e "$READY_TRACKS"
