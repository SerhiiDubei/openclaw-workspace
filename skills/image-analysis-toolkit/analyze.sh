#!/usr/bin/env bash
# Image Analysis Toolkit
# Comprehensive image analysis: description, prompt generation, OCR

set -euo pipefail

API_KEY="${OPENAI_API_KEY:-}"
if [[ -z "$API_KEY" ]]; then
  echo "Error: OPENAI_API_KEY not set" >&2
  exit 1
fi

analyze_image() {
  local image_path="$1"
  local mode="${2:-full}"
  
  if [[ ! -f "$image_path" ]]; then
    echo "Error: File not found: $image_path" >&2
    exit 1
  fi
  
  # Convert image to base64
  local base64_image
  base64_image=$(base64 -w 0 "$image_path")
  
  local prompt_text
  case "$mode" in
    describe)
      prompt_text="Describe this image in detail. Include: main subjects, colors, composition, lighting, mood, style, and any notable elements."
      ;;
    prompt)
      prompt_text="Create a detailed prompt for AI image generation that would recreate this image. Include style, subject, composition, lighting, colors, and technical details."
      ;;
    ocr)
      prompt_text="Extract all text visible in this image. Preserve formatting and layout as much as possible."
      ;;
    full|*)
      prompt_text="Provide comprehensive analysis: 1) Detailed description of content, 2) Suggested AI generation prompt, 3) Any text visible (OCR), 4) Style and artistic elements, 5) Technical composition details."
      ;;
  esac
  
  curl -s https://api.openai.com/v1/chat/completions \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -d "{
      \"model\": \"gpt-4o\",
      \"messages\": [
        {
          \"role\": \"user\",
          \"content\": [
            {\"type\": \"text\", \"text\": \"$prompt_text\"},
            {
              \"type\": \"image_url\",
              \"image_url\": {
                \"url\": \"data:image/jpeg;base64,$base64_image\"
              }
            }
          ]
        }
      ],
      \"max_tokens\": 2000
    }" | jq -r '.choices[0].message.content'
}

# Main
if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <image_path> [mode]"
  echo "Modes: describe | prompt | ocr | full (default)"
  exit 1
fi

analyze_image "$1" "${2:-full}"
