#!/bin/bash
# Async music generation - just start and report
# Actual checking done via HEARTBEAT / cron

TASK_ID="$1"
USER_ID="$2"
USERNAME="$3"

# Save task info to Supabase for later checking
curl -s -X POST "${SUPABASE_URL}/rest/v1/music_tracks" \
  -H "apikey: ${SUPABASE_SERVICE_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"user_id\": \"${USER_ID}\",
    \"username\": \"${USERNAME}\",
    \"track_name\": \"Pending\",
    \"variant\": 1,
    \"metadata\": {
      \"task_id\": \"${TASK_ID}\",
      \"status\": \"running\",
      \"created_at\": \"$(date -Iseconds)\"
    }
  }" > /dev/null 2>&1

echo "Task ${TASK_ID} registered for ${USERNAME}"
# HEARTBEAT will check status every 30 seconds
