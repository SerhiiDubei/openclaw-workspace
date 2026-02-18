---
name: image-analysis-toolkit
description: |
  Comprehensive image analysis toolkit using OpenAI Vision API.
  Features: detailed description, AI prompt generation, OCR text extraction.
  Supports multiple analysis modes for different use cases.
allowed-tools:
  - Exec
  - Read
---

# Image Analysis Toolkit

## Capabilities

| Mode | Description |
|------|-------------|
| **describe** | Detailed image description (subjects, colors, composition, mood) |
| **prompt** | Generate AI image generation prompt from photo |
| **ocr** | Extract all visible text from image |
| **full** | Complete analysis (all modes combined) |

## Usage

```bash
# Full analysis
./analyze.sh /path/to/image.jpg

# Specific modes
./analyze.sh /path/to/image.jpg describe
./analyze.sh /path/to/image.jpg prompt
./analyze.sh /path/to/image.jpg ocr
```

## Output Examples

### Describe Mode
- Main subjects and objects
- Color palette and lighting
- Composition and perspective
- Mood and atmosphere
- Style identification

### Prompt Mode
- Detailed prompt for Stable Diffusion/Midjourney
- Style references
- Technical parameters
- Composition guidelines

### OCR Mode
- All visible text extracted
- Preserved formatting
- Multi-language support

## Requirements

- OPENAI_API_KEY environment variable
- jq for JSON parsing
- curl for API requests

## Integration

Results can be used for:
- AI image generation workflows
- Content cataloging
- Accessibility (alt text generation)
- Design reference documentation
