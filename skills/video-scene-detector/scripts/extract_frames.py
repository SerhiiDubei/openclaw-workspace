#!/usr/bin/env python3
"""
Extract frames from video at specified timestamps.
Usage: python3 extract_frames.py <video_path> <timestamps_file> --output ./frames/
"""
import sys
import os
import subprocess
import argparse
import re

def parse_timestamp(ts_str: str) -> float:
    """Parse timestamp string (HH:MM:SS or seconds) to seconds."""
    ts_str = ts_str.strip()
    
    # Try HH:MM:SS format
    if ':' in ts_str:
        parts = ts_str.split(':')
        if len(parts) == 3:
            hours, minutes, seconds = map(int, parts)
            return hours * 3600 + minutes * 60 + seconds
        elif len(parts) == 2:
            minutes, seconds = map(int, parts)
            return minutes * 60 + seconds
    
    # Try seconds format
    return float(ts_str)

def format_filename_time(seconds: float) -> str:
    """Format seconds for filename: 00-01-30 (HH-MM-SS)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}-{minutes:02d}-{secs:02d}"

def extract_frame(video_path: str, timestamp: float, output_path: str):
    """Extract single frame at timestamp."""
    cmd = [
        "ffmpeg",
        "-ss", str(timestamp),
        "-i", video_path,
        "-vframes", "1",
        "-q:v", "2",  # High quality JPEG
        "-y",  # Overwrite if exists
        output_path
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"  Warning: Failed to extract at {timestamp}s", file=sys.stderr)
        return False
    
    return True

def extract_frames(video_path: str, timestamps_file: str, output_dir: str):
    """Extract frames at all timestamps."""
    if not os.path.exists(video_path):
        print(f"Error: Video not found: {video_path}", file=sys.stderr)
        sys.exit(1)
    
    if not os.path.exists(timestamps_file):
        print(f"Error: Timestamps file not found: {timestamps_file}", file=sys.stderr)
        sys.exit(1)
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Read timestamps
    with open(timestamps_file, 'r') as f:
        timestamps = [parse_timestamp(line) for line in f if line.strip()]
    
    print(f"Extracting {len(timestamps)} frames to: {output_dir}")
    
    extracted = []
    for i, ts in enumerate(timestamps, 1):
        filename = f"scene_{i:03d}_{format_filename_time(ts)}.jpg"
        output_path = os.path.join(output_dir, filename)
        
        print(f"  [{i}/{len(timestamps)}] {filename} ...", end=' ')
        
        if extract_frame(video_path, ts, output_path):
            print("✓")
            extracted.append(output_path)
        else:
            print("✗")
    
    print(f"\nExtracted {len(extracted)}/{len(timestamps)} frames")
    return extracted

def main():
    parser = argparse.ArgumentParser(description='Extract frames at timestamps')
    parser.add_argument('video', help='Path to video file')
    parser.add_argument('timestamps', help='File with timestamps (one per line)')
    parser.add_argument('--output', '-o', default='./frames',
                        help='Output directory for frames (default: ./frames)')
    
    args = parser.parse_args()
    
    extract_frames(args.video, args.timestamps, args.output)

if __name__ == "__main__":
    main()
