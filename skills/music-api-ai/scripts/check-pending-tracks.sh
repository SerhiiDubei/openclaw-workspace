#!/bin/bash
# Check pending music tracks and process BOTH variants when ready

SUPABASE_URL="${SUPABASE_URL}"
SUPABASE_SERVICE_KEY="${SUPABASE_SERVICE_KEY}"
MUSICAPI_KEY="${MUSICAPI_KEY}"

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
    # Get user info from first track record
    TRACK_RECORD=$(curl -s "${SUPABASE_URL}/rest/v1/music_tracks?metadata->>task_id=eq.${TASK_ID}&limit=1" \
      -H "apikey: ${SUPABASE_SERVICE_KEY}" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}")
    
    USER_ID=$(echo "$TRACK_RECORD" | jq -r '.[0].user_id')
    USERNAME=$(echo "$TRACK_RECORD" | jq -r '.[0].username')
    TRACK_NAME=$(echo "$TRACK_RECORD" | jq -r '.[0].track_name')
    
    # Process v1
    V1_DATA=$(echo "$STATUS_RESPONSE" | jq -r '.data[0]')
    V1_CLIP=$(echo "$V1_DATA" | jq -r '.clip_id')
    V1_URL=$(echo "$V1_DATA" | jq -r '.audio_url')
    V1_DUR=$(echo "$V1_DATA" | jq -r '.duration')
    
    # Process v2
    V2_DATA=$(echo "$STATUS_RESPONSE" | jq -r '.data[1]')
    V2_CLIP=$(echo "$V2_DATA" | jq -r '.clip_id')
    V2_URL=$(echo "$V2_DATA" | jq -r '.audio_url')
    V2_DUR=$(echo "$V2_DATA" | jq -r '.duration')
    
    # Download both
    DATE=$(date +%Y-%m-%d)
    SAFE_NAME=$(echo "$TRACK_NAME" | sed 's/ /_/g')
    
    V1_FILE="/tmp/${USERNAME// /_}_${SAFE_NAME}_v1.mp3"
    V2_FILE="/tmp/${USERNAME// /_}_${SAFE_NAME}_v2.mp3"
    
    curl -s -L "$V1_URL" -o "$V1_FILE"
    curl -s -L "$V2_URL" -o "$V2_FILE"
    
    # Upload to Storage with correct naming
    V1_PATH="music/tracks/${USERNAME}/${DATE}/${USERNAME} - ${TRACK_NAME} - v1.mp3"
    V2_PATH="music/tracks/${USERNAME}/${DATE}/${USERNAME} - ${TRACK_NAME} - v2.mp3"
    
    curl -s -X POST "${SUPABASE_URL}/storage/v1/object/$(echo "$V1_PATH" | sed 's/ /%20/g')" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: audio/mpeg" --data-binary @"$V1_FILE"
    
    curl -s -X POST "${SUPABASE_URL}/storage/v1/object/$(echo "$V2_PATH" | sed 's/ /%20/g')" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: audio/mpeg" --data-binary @"$V2_FILE"
    
    # Update BOTH records in database
    curl -s -X PATCH "${SUPABASE_URL}/rest/v1/music_tracks?metadata->>task_id=eq.${TASK_ID}&variant=eq.1" \
      -H "apikey: ${SUPABASE_SERVICE_KEY}" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: application/json" \
      -d "{\"audio_url\": \"${V1_URL}\", \"clip_id\": \"${V1_CLIP}\", \"duration\": \"${V1_DUR}\", \"storage_path\": \"${V1_PATH}\", \"metadata\": {\"status\": \"completed\"}}"
    
    curl -s -X PATCH "${SUPABASE_URL}/rest/v1/music_tracks?metadata->>task_id=eq.${TASK_ID}&variant=eq.2" \
      -H "apikey: ${SUPABASE_SERVICE_KEY}" \
      -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
      -H "Content-Type: application/json" \
      -d "{\"audio_url\": \"${V2_URL}\", \"clip_id\": \"${V2_CLIP}\", \"duration\": \"${V2_DUR}\", \"storage_path\": \"${V2_PATH}\", \"metadata\": {\"status\": \"completed\"}}"
    
    # Send ONE message with BOTH tracks
    echo "🎵 ${USERNAME} - ${TRACK_NAME} READY!"
    echo "v1: ${V1_URL}"
    echo "v2: ${V2_URL}"
    
    rm "$V1_FILE" "$V2_FILE"
  fi
done
