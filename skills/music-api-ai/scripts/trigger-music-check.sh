#!/bin/bash
# Trigger music track check manually
# Usage: ./trigger-music-check.sh

echo "Triggering music track check..."

# Call OpenClaw cron run API
# This will run the check-music-tracks job immediately

openclaw cron run check-music-tracks 2>/dev/null || echo "Job triggered (if openclaw CLI available)"

# Alternative: direct API call via curl
SUPABASE_URL="${SUPABASE_URL}"
SUPABASE_SERVICE_KEY="${SUPABASE_SERVICE_KEY}"

# Check if there are pending tracks
PENDING_COUNT=$(curl -s "${SUPABASE_URL}/rest/v1/music_tracks?or=(metadata->>status.eq.running,and(metadata->>status.eq.completed,or(metadata->>sent.is.null,metadata->>sent.neq.true)))&select=count" \
  -H "apikey: ${SUPABASE_SERVICE_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
  -H "Accept: application/vnd.pgrst.object+json" | jq -r '.count // 0')

echo "Pending tracks found: ${PENDING_COUNT}"

if [ "${PENDING_COUNT}" -gt 0 ]; then
  echo "Running check-pending-tracks.sh..."
  /root/.openclaw/workspace/skills/music-api-ai/scripts/check-pending-tracks.sh
else
  echo "No pending tracks. Nothing to do."
fi
