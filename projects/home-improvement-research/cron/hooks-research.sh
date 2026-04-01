#!/bin/bash
# Hooks Research Cron Job
# Runs daily to collect and analyze competitor hooks

WORKSPACE="/root/.openclaw/workspace"
PROJECT="$WORKSPACE/projects/home-improvement-research"
LOG_FILE="$PROJECT/cron/hooks-research.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting hooks research..." >> "$LOG_FILE"

# Check if we have required tools
if ! command -v curl &> /dev/null; then
    echo "[$DATE] ERROR: curl not found" >> "$LOG_FILE"
    exit 1
fi

# 1. Check competitor websites for changes
echo "[$DATE] Checking competitor sites..." >> "$LOG_FILE"

COMPETITORS=(
    "https://www.bathfitter.com/|bath-fitter"
    "https://www.rebath.com/|re-bath"
    "https://www.westshorehome.com/|west-shore"
)

for site in "${COMPETITORS[@]}"; do
    IFS='|' read -r url name <<< "$site"
    
    # Fetch and check for promotional content
    response=$(curl -s -L "$url" 2>/dev/null | grep -iE "(save|discount|free|offer|deal|sale|promo|%|\$[0-9]+)" | head -20)
    
    if [ -n "$response" ]; then
        echo "[$DATE] Found offers on $name" >> "$LOG_FILE"
        echo "$response" > "$PROJECT/hooks/scraped/${name}-$(date +%Y%m%d).txt"
    fi
done

# 2. Log completion
echo "[$DATE] Hooks research completed" >> "$LOG_FILE"

# 3. Notify if new hooks found
NEW_HOOKS=$(find "$PROJECT/hooks/scraped" -name "*.txt" -mtime -1 | wc -l)
if [ "$NEW_HOOKS" -gt 0 ]; then
    echo "[$DATE] Found $NEW_HOOKS new potential hooks" >> "$LOG_FILE"
fi
