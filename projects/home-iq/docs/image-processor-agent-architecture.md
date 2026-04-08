# Image Processing Agent — Architecture Document

**Project:** Home Improvement Lead Gen  
**Agent Name:** `image-processor-agent`  
**Purpose:** Automated image processing pipeline for landing page assets  
**Primary Tool:** Nano Banana API  
**Author:** Claude Code (for Dmytro)  
**Date:** April 8, 2026

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Directory Structure](#directory-structure)
3. [Core Modules](#core-modules)
4. [Acceptance Criteria](#acceptance-criteria)
5. [Naming Conventions](#naming-conventions)
6. [Tools & Libraries](#tools--libraries)
7. [Nano Banana Integration](#nano-banana-integration)
8. [Workflow Diagrams](#workflow-diagrams)
9. [Error Handling](#error-handling)
10. [Future Enhancements](#future-enhancements)

---

## System Overview

The Image Processing Agent is an automated pipeline that transforms raw home improvement photos into production-ready assets for landing pages. It handles text removal, upscaling, color correction, text overlay, and AI-powered generation.

### Key Capabilities

| Feature | Input | Output | Tool |
|---------|-------|--------|------|
| Text Removal | Photo with text/logo | Clean photo | Nano Banana |
| Upscale | Low-res image (≥800px) | High-res (2x-4x) | Nano Banana |
| Color Correction | Mismatched photos | Consistent style | Nano Banana + PIL |
| Text Overlay | Clean photo | Photo with branded text | Pillow/PIL |
| AI Generation | Reference photo + prompt | New variation | Nano Banana |

### Categories Supported

```
hvac/
├── hero-page/
├── projects/
├── before-after/
└── products/

home-security/
├── hero-page/
├── projects/
├── before-after/
└── products/

flooring/
├── hero-page/
├── projects/
├── before-after/
└── products/

windows/
├── hero-page/
├── projects/
├── before-after/
└── products/

walk-in-shower/
├── hero-page/
├── projects/
├── before-after/
└── products/
```

---

## Directory Structure

```
/home-iq/
├── assets/
│   └── images/                    # Raw source images
│       ├── hvac/
│       ├── home-security/
│       ├── flooring/
│       ├── windows/
│       └── walk-in-shower/
├── processed/                     # Processed outputs
│   ├── hvac/
│   │   ├── hero-page/
│   │   │   ├── raw/              # Original uploads
│   │   │   ├── clean/            # Text removed
│   │   │   ├── upscaled/         # High resolution
│   │   │   ├── corrected/        # Color corrected
│   │   │   └── final/            # With text overlay
│   │   ├── projects/
│   │   ├── before-after/
│   │   └── products/
│   └── [other-categories]/
├── generated/                     # AI-generated images
│   └── [category]/[subfolder]/
├── fonts/                         # Brand fonts for overlays
│   ├── primary/
│   └── secondary/
├── templates/                     # Text overlay templates
│   ├── before-after.json
│   ├── promo-banner.json
│   └── special-offer.json
├── logs/                          # Processing logs
└── config/
    ├── nano-banana.yaml
    ├── naming-rules.yaml
    └── style-guide.yaml
```

---

## Core Modules

### Module 1: Text Remover (`text_remove.py`)

**Purpose:** Remove existing text, watermarks, and logos from images.

**Workflow:**
1. Detect text regions using OCR (EasyOCR)
2. Send to Nano Banana inpainting endpoint
3. Verify removal quality
4. Save to `clean/` folder

**Input:** `assets/images/{category}/{subfolder}/IMG_2024_001.jpg`  
**Output:** `processed/{category}/{subfolder}/clean/IMG_2024_001_clean.jpg`

---

### Module 2: Upscaler (`upscale.py`)

**Purpose:** Increase image resolution while maintaining quality.

**Workflow:**
1. Check current resolution
2. If < 1920px on shortest side → upscale 2x or 4x
3. Use Nano Banana upscaling
4. Verify output quality (no artifacts)
5. Save to `upscaled/` folder

**Input:** `processed/{category}/{subfolder}/clean/*.jpg`  
**Output:** `processed/{category}/{subfolder}/upscaled/*.jpg`

---

### Module 3: Color Corrector (`color_correct.py`)

**Purpose:** Normalize lighting and colors across all images.

**Workflow:**
1. Analyze image histogram
2. Compare against style guide reference
3. Adjust brightness, contrast, saturation, white balance
4. Apply consistent LUT (Look-Up Table) if configured
5. Save to `corrected/` folder

**Style Targets:**
- Brightness: 110-130% (slightly brighter)
- Contrast: 105-115% (subtle enhancement)
- Saturation: 95-105% (natural, not oversaturated)
- Temperature: Slightly warm (5500K-6000K)

**Input:** `processed/{category}/{subfolder}/upscaled/*.jpg`  
**Output:** `processed/{category}/{subfolder}/corrected/*.jpg`

---

### Module 4: Text Overlay (`text_overlay.py`)

**Purpose:** Add branded text overlays (Before/After labels, promo banners, etc.).

**Workflow:**
1. Load template configuration
2. Calculate safe zones (avoid faces, main subject)
3. Render text with brand fonts
4. Add background blur/shadow for readability
5. Save to `final/` folder

**Template Types:**
- `before-after`: Split screen with labels
- `promo-banner`: Special offer text overlay
- `trust-badge": "Licensed & Insured" badge
- `cta-overlay`: "Get Free Quote" button overlay

**Input:** `processed/{category}/{subfolder}/corrected/*.jpg`  
**Output:** `processed/{category}/{subfolder}/final/*.jpg`

---

### Module 5: AI Generator (`ai_generate.py`)

**Purpose:** Generate new images based on reference photos and prompts.

**Workflow:**
1. Analyze reference image (subject, style, composition)
2. Build prompt using category-specific templates
3. Send to Nano Banana image generation
4. Post-process (upscale, color correct)
5. Save to `generated/` folder

**Use Cases:**
- Generate variations of hero images
- Create seasonal versions (winter/summer HVAC)
- Produce different room angles from one reference
- Generate "lifestyle" scenes from product shots

**Input:** `processed/{category}/{subfolder}/corrected/reference.jpg` + prompt  
**Output:** `generated/{category}/{subfolder}/{naming_convention}.jpg`

---

## Acceptance Criteria

### AC-1: Text Removal

```gherkin
Feature: Text Removal from Images

Scenario: Remove watermark from product photo
  Given an image with visible text/watermark
  When the text_remover module processes it
  Then the output image should have no visible text
  And the inpainted area should match surrounding texture
  And the image dimensions should remain unchanged
  And processing time should be < 30 seconds

Scenario: Handle image with no text
  Given a clean image without text
  When the text_remover module processes it
  Then the image should be copied to output unchanged
  And the system should log "No text detected"

Scenario: Complex background text removal
  Given an image with text over complex pattern (tile, wood)
  When processed through Nano Banana
  Then the text should be removed
  And the pattern should continue seamlessly
  And no blur artifacts should be visible
```

**Quality Metrics:**
- SSIM (Structural Similarity) between clean and original background: ≥ 0.85
- No visible blur in inpainted region
- No text fragments remain (verified by OCR check)

---

### AC-2: Upscale

```gherkin
Feature: Image Upscaling

Scenario: Upscale low-resolution image
  Given an image with width < 1920px
  When the upscaler module processes it
  Then output should be 2x or 4x larger
  And image should maintain sharpness
  And no pixelation or artifacts should appear
  And file size should increase proportionally

Scenario: Skip already high-res image
  Given an image with width ≥ 1920px
  When the upscaler checks it
  Then it should skip processing
  And log "Resolution sufficient"

Scenario: Batch upscale folder
  Given a folder with 50 mixed-resolution images
  When batch processing runs
  Then all images < 1920px should be upscaled
  And all images ≥ 1920px should be skipped
  And processing report should be generated
```

**Quality Metrics:**
- Output resolution: minimum 1920px on shortest side
- No visible upscaling artifacts
- Sharp edges preserved
- PSNR ≥ 30 dB compared to theoretical perfect upscale

---

### AC-3: Color Correction

```gherkin
Feature: Color Consistency Correction

Scenario: Correct underexposed photo
  Given a dark photo from phone camera
  When color_corrector processes it
  Then brightness should increase to target range
  And shadows should retain detail
  And highlights should not clip

Scenario: Match photo to style guide
  Given a photo with color cast (too warm/cool)
  When compared to style guide reference
  Then white balance should be adjusted
  And overall tone should match reference
  And the correction should look natural

Scenario: Batch color consistency
  Given 20 photos from different sources
  When color_corrector runs on batch
  Then all outputs should have similar histograms
  And visual comparison should show consistent style
```

**Quality Metrics:**
- Brightness: 110-130% of original
- Contrast: within ±10% of style guide
- Color temperature: 5500K-6000K
- No banding artifacts

---

### AC-4: Text Overlay

```gherkin
Feature: Add Branded Text Overlays

Scenario: Add Before/After labels
  Given a side-by-side comparison image
  When text_overlay applies "before-after" template
  Then "BEFORE" label appears on left side
  And "AFTER" label appears on right side
  And text is readable against image background
  And font matches brand guidelines

Scenario: Add promo banner
  Given a clean hero image
  When "promo-banner" template applied with text "Save up to $500"
  Then banner appears in safe zone (top or bottom)
  And text is legible with sufficient contrast
  And banner has semi-transparent background
  And text doesn't cover important image elements

Scenario: Auto-position text
  Given an image with detected faces/objects
  When text overlay is applied
  Then text avoids face regions
  And text avoids main subject (room center)
  And position prioritizes corners/edges
```

**Quality Metrics:**
- Text contrast ratio ≥ 4.5:1 (WCAG AA)
- Text doesn't overlap with detected faces (using face detection)
- Font rendering is crisp at full resolution
- Safe zone detection accuracy ≥ 90%

---

### AC-5: AI Generation

```gherkin
Feature: AI Image Generation

Scenario: Generate variation from reference
  Given a reference image of modern bathroom
  And prompt "similar bathroom, different angle, natural lighting"
  When ai_generator processes
  Then new image should be generated
  And style should match reference
  And content should be relevant to prompt
  And quality should match processed photos

Scenario: Generate seasonal variation
  Given a summer HVAC installation photo
  And prompt "same scene, winter season, snow outside"
  When ai_generator processes
  Then generated image should show winter context
  And HVAC unit should remain consistent
  And overall style should match brand

Scenario: Generate from text prompt only
  Given a category "flooring" and prompt "luxury hardwood floor, warm lighting, spacious living room"
  When ai_generator runs without reference
  Then image should be generated
  And content should match flooring category
  And quality should be production-ready
```

**Quality Metrics:**
- Generated image resolution ≥ 1920px
- CLIP similarity to prompt: ≥ 0.25
- Visual consistency with reference (if provided): ≥ 0.7
- No anatomical errors (if people present)

---

## Naming Conventions

### File Naming Pattern

```
{category}--{subfolder}--{descriptor}--{version}--{process-flag}.{ext}
```

### Components

| Component | Options | Description |
|-----------|---------|-------------|
| `category` | `hvac`, `home-security`, `flooring`, `windows`, `walk-in-shower` | Main category |
| `subfolder` | `hero-page`, `projects`, `before-after`, `products` | Content type |
| `descriptor` | Slug of content description | `modern-kitchen-install`, `senior-couple-comfort` |
| `version` | `v1`, `v2`, `v3`... | Iteration/version |
| `process-flag` | `raw`, `clean`, `upscaled`, `corrected`, `final` | Processing stage |
| `ext` | `jpg`, `png`, `webp` | File format |

### Examples

```
# Raw upload
hvac--hero-page--winter-comfort-scene--v1--raw.jpg

# After text removal
hvac--hero-page--winter-comfort-scene--v1--clean.jpg

# After upscaling
hvac--hero-page--winter-comfort-scene--v1--upscaled.jpg

# After color correction
hvac--hero-page--winter-comfort-scene--v1--corrected.jpg

# Final with text overlay
hvac--hero-page--winter-comfort-scene--v1--final.jpg

# Generated image
hvac--hero-page--cozy-winter-installation--v1--generated.jpg

# Before/After composite
flooring--before-after--oak-living-room-transformation--v1--final.jpg
```

### Generated Image Naming

```
{category}--{subfolder}--{descriptor}--{gen-method}--v{version}.{ext}
```

Where `gen-method`:
- `gen-variation` — Variation from reference
- `gen-seasonal` — Seasonal adaptation
- `gen-prompt` — Generated from text only
- `gen-extend` — Outpainting/extension

### Metadata Tags (for database/S3)

```json
{
  "file_name": "hvac--hero-page--winter-comfort--v1--final.jpg",
  "category": "hvac",
  "subfolder": "hero-page",
  "descriptor": "winter-comfort",
  "version": 1,
  "stage": "final",
  "has_text": false,
  "has_people": true,
  "emotion": "comfortable",
  "quality_focus": "lifestyle",
  "tags": ["senior", "winter", "cozy", "installation"],
  "dimensions": { "width": 1920, "height": 1080 },
  "file_size_kb": 245,
  "source": "generated",
  "parent_image": "hvac--hero-page--winter-comfort--v1--corrected.jpg",
  "created_at": "2026-04-08T15:30:00Z",
  "processing_time_sec": 45.2
}
```

---

## Tools & Libraries

### Required Python Packages

```txt
# requirements.txt

# Image Processing
Pillow>=10.0.0
opencv-python>=4.8.0
numpy>=1.24.0
scikit-image>=0.21.0

# OCR for text detection
easyocr>=1.7.0

# Color correction
colour-science>=0.4.2

# ML/AI
requests>=2.31.0
httpx>=0.25.0

# Face detection (for safe zones)
mediapipe>=0.10.0
# OR
face-recognition>=1.3.0

# Utilities
PyYAML>=6.0.1
tqdm>=4.66.0
python-dotenv>=1.0.0
pydantic>=2.0.0

# Testing
pytest>=7.4.0
pytest-asyncio>=0.21.0
```

### Alternative OCR Options

| Library | Pros | Cons |
|---------|------|------|
| **EasyOCR** (recommended) | Multi-language, easy setup | Slower on CPU |
| **PaddleOCR** | Fast, accurate | Complex dependencies |
| **Tesseract** | Established, fast | Lower accuracy on complex backgrounds |
| **Google Vision API** | Very accurate | Requires API key, cost |

### Alternative Upscale Options

| Tool | Method | Best For |
|------|--------|----------|
| **Nano Banana** | AI-based | Primary choice, best quality |
| **Real-ESRGAN** | GAN-based | Open source alternative |
| **Upscayl** | Multiple models | GUI/CLI tool |
| **waifu2x** | CNN | Anime/illustrations |

---

## Nano Banana Integration

### API Endpoints

Based on available Nano Banana capabilities:

```python
# config/nano-banana.yaml
nano_banana:
  base_url: "https://api.nano-banana.com/v1"
  api_key: "${NANO_BANANA_API_KEY}"
  
  endpoints:
    text_removal:
      path: "/image/inpaint"
      method: "POST"
      params:
        - mask_type: "auto"  # or "manual"
        - inpaint_model: "lama"  # or "sd"
        
    upscale:
      path: "/image/upscale"
      method: "POST"
      params:
        - scale: 2  # or 4
        - model: "real-esrgan"  # or "swinir"
        
    color_correction:
      path: "/image/adjust"
      method: "POST"
      params:
        - brightness: 1.2
        - contrast: 1.1
        - saturation: 1.0
        - temperature: 5800
        
    generate:
      path: "/image/generate"
      method: "POST"
      params:
        - prompt: "string"
        - negative_prompt: "text, watermark, blurry"
        - width: 1024
        - height: 768
        - reference_image: "optional_base64"
        - style_preset: "photorealistic"
        - steps: 30
        - cfg_scale: 7.0
```

### Python Client Example

```python
# clients/nano_banana_client.py
import httpx
import base64
from typing import Optional, Dict, Any
from pathlib import Path

class NanoBananaClient:
    def __init__(self, api_key: str, base_url: str = "https://api.nano-banana.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.client = httpx.Client(
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=120.0
        )
    
    def remove_text(self, image_path: Path, mask_type: str = "auto") -> bytes:
        """Remove text from image using inpainting."""
        with open(image_path, "rb") as f:
            image_b64 = base64.b64encode(f.read()).decode()
        
        response = self.client.post(
            f"{self.base_url}/image/inpaint",
            json={
                "image": image_b64,
                "mask_type": mask_type,
                "inpaint_model": "lama"
            }
        )
        response.raise_for_status()
        result = response.json()
        return base64.b64decode(result["image"])
    
    def upscale(self, image_path: Path, scale: int = 2) -> bytes:
        """Upscale image resolution."""
        with open(image_path, "rb") as f:
            image_b64 = base64.b64encode(f.read()).decode()
        
        response = self.client.post(
            f"{self.base_url}/image/upscale",
            json={
                "image": image_b64,
                "scale": scale,
                "model": "real-esrgan"
            }
        )
        response.raise_for_status()
        result = response.json()
        return base64.b64decode(result["image"])
    
    def color_correct(
        self, 
        image_path: Path, 
        brightness: float = 1.0,
        contrast: float = 1.0,
        saturation: float = 1.0,
        temperature: int = 6500
    ) -> bytes:
        """Adjust color and lighting."""
        with open(image_path, "rb") as f:
            image_b64 = base64.b64encode(f.read()).decode()
        
        response = self.client.post(
            f"{self.base_url}/image/adjust",
            json={
                "image": image_b64,
                "brightness": brightness,
                "contrast": contrast,
                "saturation": saturation,
                "temperature": temperature
            }
        )
        response.raise_for_status()
        result = response.json()
        return base64.b64decode(result["image"])
    
    def generate(
        self,
        prompt: str,
        reference_image: Optional[Path] = None,
        width: int = 1024,
        height: int = 768,
        steps: int = 30
    ) -> bytes:
        """Generate image from prompt with optional reference."""
        payload: Dict[str, Any] = {
            "prompt": prompt,
            "negative_prompt": "text, watermark, blurry, low quality",
            "width": width,
            "height": height,
            "steps": steps,
            "cfg_scale": 7.0,
            "style_preset": "photorealistic"
        }
        
        if reference_image:
            with open(reference_image, "rb") as f:
                payload["reference_image"] = base64.b64encode(f.read()).decode()
        
        response = self.client.post(
            f"{self.base_url}/image/generate",
            json=payload
        )
        response.raise_for_status()
        result = response.json()
        return base64.b64decode(result["image"])
```

---

## Workflow Diagrams

### Complete Pipeline

```
┌─────────────────┐
│   RAW IMAGE     │
│   (uploaded)    │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│ 1. TEXT REMOVAL         │
│    - Detect text (OCR)  │
│    - Inpaint with Nano  │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ 2. UPSCALE              │
│    - Check resolution   │
│    - Upscale if < 1920px│
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ 3. COLOR CORRECTION     │
│    - Match style guide  │
│    - Adjust WB/tone     │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐     ┌─────────────────┐
│ 4. TEXT OVERLAY         │◄────┤  TEMPLATES      │
│    - Load template      │     │  - before-after │
│    - Detect safe zones  │     │  - promo        │
│    - Render text        │     │  - cta          │
└────────┬────────────────┘     └─────────────────┘
         │
         ▼
┌─────────────────────────┐
│    FINAL IMAGE          │
│    (production ready)   │
└─────────────────────────┘
```

### AI Generation Workflow

```
┌─────────────────┐
│  REFERENCE IMG  │
│  or PROMPT      │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│  ANALYZE REFERENCE      │
│  - Subject detection    │
│  - Style extraction     │
│  - Build prompt         │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  NANO BANANA GENERATE   │
│  - Send prompt + ref    │
│  - Wait for generation  │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  POST-PROCESS           │
│  - Upscale if needed    │
│  - Color correct        │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  GENERATED IMAGE        │
│  (saved to folder)      │
└─────────────────────────┘
```

---

## Error Handling

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `TextNotDetected` | OCR confidence too low | Lower threshold or skip step |
| `InpaintFailed` | Complex background | Try different inpaint model |
| `UpscaleTimeout` | Image too large | Process in tiles |
| `NanoBananaRateLimit` | Too many requests | Implement exponential backoff |
| `FaceDetectionFailed` | No faces in image | Use center-based safe zones |
| `TemplateNotFound` | Missing config | Use default template |

### Retry Logic

```python
# utils/retry.py
from functools import wraps
import time
from typing import Callable, Any

def retry_with_backoff(
    max_retries: int = 3,
    base_delay: float = 1.0,
    exceptions: tuple = (Exception,)
):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_retries - 1:
                        raise
                    delay = base_delay * (2 ** attempt)
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

# Usage
@retry_with_backoff(max_retries=3, exceptions=(httpx.TimeoutException,))
def process_image_with_nano(image_path: Path) -> bytes:
    ...
```

---

## Future Enhancements

### Phase 2 (Next Sprint)
- [ ] Automatic categorization using image classification
- [ ] Duplicate detection (avoid processing same image twice)
- [ ] A/B testing framework for different text overlays
- [ ] Integration with landing page builder (auto-upload)

### Phase 3 (Future)
- [ ] Video processing (remove text from video frames)
- [ ] 3D room generation from 2D photos
- [ ] Virtual staging (add furniture to empty rooms)
- [ ] Multi-language text overlay support

---

## Getting Started

### 1. Clone & Setup

```bash
git clone <repo>
cd home-iq/image-processor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with:
# - NANO_BANANA_API_KEY
# - SOURCE_DIR
# - OUTPUT_DIR
```

### 3. Run Single Image

```bash
python -m processor single \
  --input assets/images/hvac/hero-page/photo.jpg \
  --output processed/hvac/hero-page/ \
  --steps text_remove,upscale,color_correct
```

### 4. Run Batch

```bash
python -m processor batch \
  --input assets/images/hvac/ \
  --output processed/hvac/ \
  --parallel 4
```

### 5. Generate New Images

```bash
python -m processor generate \
  --reference processed/hvac/hero-page/clean/photo.jpg \
  --prompt "similar scene, different angle, morning light" \
  --output generated/hvac/hero-page/
```

---

## Appendix

### A. Color Style Guide Reference

```yaml
# config/style-guide.yaml
style_guide:
  name: "Home IQ Brand"
  
  color_temperature: 5800  # Kelvin, slightly warm
  
  brightness:
    min: 1.10
    target: 1.20
    max: 1.30
  
  contrast:
    min: 1.05
    target: 1.10
    max: 1.15
  
  saturation:
    min: 0.95
    target: 1.00
    max: 1.05
  
  highlights:
    clip_threshold: 250  # Prevent blown highlights
  
  shadows:
    lift: 0.05  # Slight shadow lift for detail
```

### B. Font Requirements

```yaml
# config/fonts.yaml
fonts:
  primary:
    name: "Inter"
    file: "fonts/primary/Inter-Bold.ttf"
    use_for: ["headlines", "promo_banners"]
  
  secondary:
    name: "Roboto"
    file: "fonts/secondary/Roboto-Regular.ttf"
    use_for: ["body_text", "labels"]
  
  fallback:
    name: "Arial"
    system: true
```

### C. Template Definitions

```json
{
  "templates": {
    "before-after": {
      "type": "split",
      "labels": {
        "before": {
          "text": "BEFORE",
          "position": "top-left",
          "bg_color": "#333333",
          "text_color": "#FFFFFF"
        },
        "after": {
          "text": "AFTER",
          "position": "top-right",
          "bg_color": "#28A745",
          "text_color": "#FFFFFF"
        }
      }
    },
    "promo-banner": {
      "type": "overlay",
      "position": "bottom-center",
      "bg_opacity": 0.8,
      "padding": 20,
      "font_size": 48
    }
  }
}
```

---

**Document Version:** 1.0  
**Last Updated:** 2026-04-08  
**Author:** Kimi Claw for Dmytro
