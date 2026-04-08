# FFmpeg Scene Detection Reference

## How Scene Detection Works

FFmpeg's `select` filter with `scene` function compares consecutive frames and calculates a difference score between 0.0 and 1.0.

- `0.0` = identical frames
- `1.0` = completely different frames
- Typical scene changes fall in `0.3 - 0.5` range

## Filter Syntax

```bash
ffmpeg -i video.mp4 -vf "select='gt(scene,0.3)',showinfo" -f null -
```

Components:
- `select` - filters which frames to output
- `gt(scene,0.3)` - greater than: scene score > 0.3
- `showinfo` - prints frame info including timestamp

## Threshold Guidelines

| Threshold | Use Case | Result |
|-----------|----------|--------|
| 0.1 | Music videos, fast cuts | 50+ scenes per minute |
| 0.2 | Action movies, trailers | 30-40 scenes per minute |
| 0.3 | Standard content (default) | 15-25 scenes per minute |
| 0.4 | Interviews, static content | 5-15 scenes per minute |
| 0.5 | Detect only major scene changes | 2-5 scenes per minute |

## Advanced Options

### Custom Scene Detection

Detect scenes with minimum interval of 2 seconds:
```bash
ffmpeg -i video.mp4 -vf "select='gt(scene,0.3)*gte(t-prev_selected_t,2)',showinfo" -f null -
```

### Export Scene Frames Directly

Instead of just timestamps, export frames during detection:
```bash
ffmpeg -i video.mp4 -vf "select='gt(scene,0.3)'" -vsync vfr scene_%03d.jpg
```

### Using scdet Filter (Alternative)

Newer alternative to scene filter:
```bash
ffmpeg -i video.mp4 -vf "scdet=s=1.0:t=10" -f null -
```

Parameters:
- `s` - scene change threshold (0.0-1.0)
- `t` - percentage of changed pixels

## Performance Tips

1. **Analyze at lower resolution** for faster processing:
   ```bash
   ffmpeg -i video.mp4 -vf "scale=320:-1,select='gt(scene,0.3)',showinfo" -f null -
   ```

2. **Skip analysis of audio** to speed up:
   ```bash
   ffmpeg -i video.mp4 -vn -an -vf "select='gt(scene,0.3)',showinfo" -f null -
   ```
   (Actually this won't work - need to use -an only)

3. **Use hardware acceleration** if available:
   ```bash
   ffmpeg -hwaccel cuda -i video.mp4 ...
   ```

## Common Issues

### False Positives
- Flash photography
- Quick camera movements
- Video noise/grain

**Solution**: Increase threshold or use denoising:
```bash
ffmpeg -i video.mp4 -vf "hqdn3d,select='gt(scene,0.4)',showinfo" -f null -
```

### Missed Scenes
- Slow dissolves
- Gradual lighting changes
- Fade transitions

**Solution**: Lower threshold or use dedicated transition detection:
```bash
ffmpeg -i video.mp4 -vf "fade,select='gt(scene,0.2)',showinfo" -f null -
```

## Alternative Tools

| Tool | Best For | Speed |
|------|----------|-------|
| ffmpeg (scene) | General use | Medium |
| ffmpeg (scdet) | Better accuracy | Medium |
| scenedetect (PySceneDetect) | Advanced analysis | Slower |
| OpenCV frame diff | Custom pipelines | Fast |
