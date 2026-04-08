#!/usr/bin/env python3
"""
Complete video processing pipeline: download → detect scenes → extract frames.
Usage: python3 process_video.py <youtube_url_or_video_path> --output ./frames/
"""
import sys
import os
import tempfile
import shutil
import argparse

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from download_video import download_youtube, copy_local
from detect_scenes import detect_scenes, save_timestamps
from extract_frames import extract_frames

def main():
    parser = argparse.ArgumentParser(
        description='Download video and extract frames at scene changes'
    )
    parser.add_argument('source', help='YouTube URL or path to video file')
    parser.add_argument('--output', '-o', default='./frames',
                        help='Output directory for frames (default: ./frames)')
    parser.add_argument('--threshold', '-t', type=float, default=0.3,
                        help='Scene detection threshold (0.1-0.5, default: 0.3)')
    parser.add_argument('--keep-video', action='store_true',
                        help='Keep downloaded video file (default: delete)')
    parser.add_argument('--temp-dir', default=None,
                        help='Temporary directory for processing')
    
    args = parser.parse_args()
    
    # Create temp directory
    temp_dir = tempfile.mkdtemp(prefix="video_scene_")
    video_path = os.path.join(temp_dir, "video.mp4")
    timestamps_file = os.path.join(temp_dir, "scenes.txt")
    
    try:
        # Step 1: Download/Copy video
        print("=" * 60)
        print("STEP 1: Getting video")
        print("=" * 60)
        
        if args.source.startswith(("http://", "https://", "youtube.com", "www.youtube.com", "youtu.be")):
            download_youtube(args.source, video_path)
        else:
            copy_local(args.source, video_path)
        
        # Step 2: Detect scenes
        print("\n" + "=" * 60)
        print("STEP 2: Detecting scene changes")
        print("=" * 60)
        
        timestamps = detect_scenes(video_path, args.threshold)
        save_timestamps(timestamps, timestamps_file)
        
        # Step 3: Extract frames
        print("\n" + "=" * 60)
        print("STEP 3: Extracting frames")
        print("=" * 60)
        
        extracted = extract_frames(video_path, timestamps_file, args.output)
        
        # Summary
        print("\n" + "=" * 60)
        print("COMPLETE!")
        print("=" * 60)
        print(f"Detected scenes: {len(timestamps)}")
        print(f"Extracted frames: {len(extracted)}")
        print(f"Output directory: {os.path.abspath(args.output)}")
        
        if extracted:
            print("\nExtracted frames:")
            for frame in extracted:
                print(f"  - {frame}")
        
    finally:
        # Cleanup
        if not args.keep_video and os.path.exists(temp_dir):
            print(f"\nCleaning up temporary files...")
            shutil.rmtree(temp_dir, ignore_errors=True)
        elif args.keep_video:
            print(f"\nVideo kept at: {video_path}")

if __name__ == "__main__":
    main()
