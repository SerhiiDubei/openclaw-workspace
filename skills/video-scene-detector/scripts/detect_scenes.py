#!/usr/bin/env python3
"""
Detect scene changes in video using ffmpeg.
Usage: python3 detect_scenes.py <video_path> [--threshold 0.3] [--output scenes.txt]
"""
import sys
import os
import subprocess
import re
import argparse

def detect_scenes(video_path: str, threshold: float = 0.3) -> list:
    """
    Detect scene changes using ffmpeg scene filter.
    Returns list of timestamps in seconds.
    """
    if not os.path.exists(video_path):
        print(f"Error: Video file not found: {video_path}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Analyzing video for scene changes (threshold: {threshold})...")
    
    # ffmpeg command to detect scenes
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"select='gt(scene,{threshold})',showinfo",
        "-f", "null",
        "-"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Parse timestamps from stderr (ffmpeg outputs info to stderr)
    timestamps = [0.0]  # Always include start of video
    
    # Pattern to match: pts_time:12.345
    pts_pattern = re.compile(r'pts_time:([\d.]+)')
    
    for line in result.stderr.split('\n'):
        match = pts_pattern.search(line)
        if match:
            timestamp = float(match.group(1))
            timestamps.append(timestamp)
    
    # Remove duplicates and sort
    timestamps = sorted(set(timestamps))
    
    print(f"Detected {len(timestamps)} scenes")
    return timestamps

def format_timestamp(seconds: float) -> str:
    """Convert seconds to HH:MM:SS format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def save_timestamps(timestamps: list, output_path: str):
    """Save timestamps to file."""
    with open(output_path, 'w') as f:
        for i, ts in enumerate(timestamps, 1):
            f.write(f"{format_timestamp(ts)}\n")
    print(f"Timestamps saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Detect scene changes in video')
    parser.add_argument('video', help='Path to video file')
    parser.add_argument('--threshold', type=float, default=0.3,
                        help='Scene detection threshold (0.1-0.5, default: 0.3)')
    parser.add_argument('--output', '-o', default='scenes.txt',
                        help='Output file for timestamps')
    
    args = parser.parse_args()
    
    timestamps = detect_scenes(args.video, args.threshold)
    save_timestamps(timestamps, args.output)
    
    print("\nScene timestamps:")
    for i, ts in enumerate(timestamps, 1):
        print(f"  Scene {i:3d}: {format_timestamp(ts)}")

if __name__ == "__main__":
    main()
