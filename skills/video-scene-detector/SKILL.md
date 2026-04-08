---
name: video-scene-detector
description: |
  Download YouTube videos and automatically detect scene changes to extract keyframes.
  Use when user needs to:
  - Analyze video content by scenes
  - Extract representative frames from video at scene boundaries
  - Create video thumbnails or previews
  - Get first frame of each scene/cut in a video
  
  Supports YouTube URLs and local video files. Outputs frames with timestamps.
---

# Video Scene Detector

Automatically detect scene changes in videos and extract representative frames.

## Overview

This skill downloads videos (from YouTube or local files), analyzes them for scene changes using ffmpeg's scene detection filter, and extracts the first frame of each detected scene.

## Workflow

### 1. Download Video

For YouTube URLs, use `scripts/download_video.py`:

```bash
python3 scripts/download_video.py "https://youtube.com/watch?v=..." /tmp/video.mp4
```

### 2. Detect Scenes

Use `scripts/detect_scenes.py` to find all scene changes:

```bash
python3 scripts/detect_scenes.py /tmp/video.mp4 --threshold 0.3 --output /tmp/scenes.txt
```

Parameters:
- `--threshold`: Scene change sensitivity (0.1-0.5, default 0.3). Higher = fewer scenes detected
- `--output`: File to save timestamp list

### 3. Extract Frames

Use `scripts/extract_frames.py` to extract frames at scene timestamps:

```bash
python3 scripts/extract_frames.py /tmp/video.mp4 /tmp/scenes.txt --output /tmp/frames/
```

Output: JPG files named `scene_001_00-00-05.jpg`, `scene_002_00-01-23.jpg`, etc.

### 4. Full Pipeline

Or use one command for complete workflow:

```bash
# For YouTube URL
python3 scripts/process_video.py "https://youtube.com/watch?v=..." --output ./frames/

# For local file
python3 scripts/process_video.py /path/to/video.mp4 --output ./frames/
```

## Output

All extracted frames are saved to the specified output directory with naming format:
```
scene_{number}_{timestamp}.jpg
```

Example:
- `scene_001_00-00-00.jpg` - First scene (video start)
- `scene_002_00-00-15.jpg` - Scene starts at 15 seconds
- `scene_003_00-01-30.jpg` - Scene starts at 1 minute 30 seconds

## Requirements

- ffmpeg (must be installed)
- yt-dlp (for YouTube downloads, auto-installed if missing)
- Python 3.8+

## Scene Detection Threshold Guide

| Content Type | Recommended Threshold | Result |
|--------------|----------------------|--------|
| Fast cuts (music videos, trailers) | 0.1-0.2 | Many scenes detected |
| Standard video (interviews, vlogs) | 0.3 | Balanced detection |
| Slow content (documentaries, films) | 0.4-0.5 | Fewer scenes, major changes only |

## Troubleshooting

**Issue: No scenes detected**
- Lower the threshold (--threshold 0.2)
- Check video is not completely static

**Issue: Too many scenes**
- Increase threshold (--threshold 0.4)
- Videos with fast motion or grain may need higher threshold

**Issue: YouTube download fails**
- Ensure yt-dlp is installed: `pip install yt-dlp`
- Some videos may be age-restricted or blocked

## References

- For detailed ffmpeg scene detection parameters: see [references/ffmpeg_scene_detection.md](references/ffmpeg_scene_detection.md)
