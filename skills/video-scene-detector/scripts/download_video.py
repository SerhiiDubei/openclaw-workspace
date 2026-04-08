#!/usr/bin/env python3
"""
Download video from YouTube or copy local file.
Usage: python3 download_video.py <youtube_url_or_path> <output_path>
"""
import sys
import os
import shutil
import subprocess

def download_youtube(url: str, output_path: str) -> str:
    """Download video from YouTube using yt-dlp."""
    try:
        # Check if yt-dlp is installed
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Installing yt-dlp...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "yt-dlp"], check=True)
    
    print(f"Downloading from YouTube: {url}")
    cmd = [
        "yt-dlp",
        "-f", "best[height<=1080]",  # Best quality up to 1080p
        "-o", output_path,
        "--no-playlist",
        url
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error downloading: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Downloaded to: {output_path}")
    return output_path

def copy_local(source: str, output_path: str) -> str:
    """Copy local video file."""
    if not os.path.exists(source):
        print(f"Error: File not found: {source}", file=sys.stderr)
        sys.exit(1)
    
    shutil.copy2(source, output_path)
    print(f"Copied to: {output_path}")
    return output_path

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 download_video.py <youtube_url_or_path> <output_path>")
        sys.exit(1)
    
    source = sys.argv[1]
    output_path = sys.argv[2]
    
    # Check if source is URL or local file
    if source.startswith(("http://", "https://", "youtube.com", "www.youtube.com", "youtu.be")):
        download_youtube(source, output_path)
    else:
        copy_local(source, output_path)

if __name__ == "__main__":
    main()
