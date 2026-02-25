#!/bin/bash
# Auto-retry install until success

while true; do
  echo "Trying to install airtable... $(date)"
  if clawhub install airtable 2>&1 | grep -q "OK. Installed"; then
    echo "SUCCESS! Airtable installed."
    break
  fi
  echo "Failed, waiting 2 minutes..."
  sleep 120
done
