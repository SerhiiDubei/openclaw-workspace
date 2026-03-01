#!/bin/bash
# Async music generation - register BOTH variants
# Actual checking done via HEARTBEAT / cron

TASK_ID="$1"
USER_ID="$2"
USERNAME="$3"
TRACK_NAME="${4:-Pending}"
PROMPT="$5"
API_PARAMS="$6"

# Register v1
curl -s -X POST "${SUPABASE_URL}/rest/v1/music_tracks" \
  -H "apikey: ${SUPABASE_SERVICE_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"user_id\": \"${USER_ID}\",
    \"username\": \"${USERNAME}\",
    \"track_name\": \"${TRACK_NAME}\",
    \"variant\": 1,
    \"prompt\": \"${PROMPT}\",
    \"api_params\": ${API_PARAMS},
    \"metadata\": {
      \"task_id\": \"${TASK_ID}\",
      \"status\": \"running\",
      \"created_at\": \"$(date -Iseconds)\"
    }
  }" > /dev/null 2>&1

# Register v2
curl -s -X POST "${SUPABASE_URL}/rest/v1/music_tracks" \
  -H "apikey: ${SUPABASE_SERVICE_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"user_id\": \"${USER_ID}\",
    \"username\": \"${USERNAME}\",
    \"track_name\": \"${TRACK_NAME}\",
    \"variant\": 2,
    \"prompt\": \"${PROMPT}\",
    \"api_params\": ${API_PARAMS},
    \"metadata\": {
      \"task_id\": \"${TASK_ID}\",
      \"status\": \"running\",
      \"created_at\": \"$(date -Iseconds)\"
    }
  }" > /dev/null 2>&1

echo "Task ${TASK_ID} registered for ${USERNAME} - ${TRACK_NAME} (v1 + v2)"

# Trigger immediate check (non-blocking)
(/root/.openclaw/workspace/skills/music-api-ai/scripts/check-pending-tracks.sh &)
