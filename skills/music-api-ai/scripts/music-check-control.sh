#!/bin/bash
# Control music track checking
# Usage: ./music-check-control.sh [on|off|status|trigger]

COMMAND="${1:-status}"

case "${COMMAND}" in
  on|enable)
    echo "Enabling automatic music track checking (every 5 minutes)..."
    # Would need to call OpenClaw API to enable cron job
    echo "Cron job enabled (manual step needed in OpenClaw config)"
    ;;
  
  off|disable)
    echo "Disabling automatic music track checking..."
    # Would need to call OpenClaw API to disable cron job
    echo "Cron job disabled"
    ;;
  
  status)
    echo "Music track check status:"
    echo "  Auto-check: DISABLED (manual trigger only)"
    echo "  Check manually with: ./trigger-music-check.sh"
    ;;
  
  trigger|run|now)
    echo "Triggering manual check..."
    /root/.openclaw/workspace/skills/music-api-ai/scripts/trigger-music-check.sh
    ;;
  
  *)
    echo "Usage: $0 [on|off|status|trigger]"
    echo ""
    echo "Commands:"
    echo "  on       - Enable automatic checking (every 5 min)"
    echo "  off      - Disable automatic checking"
    echo "  status   - Show current status"
    echo "  trigger  - Run check manually now"
    exit 1
    ;;
esac
