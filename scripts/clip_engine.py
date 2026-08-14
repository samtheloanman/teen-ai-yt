import os
import json
import subprocess
import argparse
from pathlib import Path

def get_last_session():
    config_path = Path("../config/last_session.json")
    if config_path.exists():
        with open(config_path, "r") as f:
            data = json.load(f)
            return data.get("recording_path")
    return None

def run_ffmpeg(input_path, output_path, args):
    cmd = ["ffmpeg", "-y", "-i", input_path] + args + [output_path]
    print(f"Running FFmpeg: {' '.join(cmd)}")
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error running FFmpeg:\n{result.stderr.decode()}")
    else:
        print(f"Successfully created: {output_path}")

def generate_short(input_path, output_dir):
    """Generates a 9:16 60-second Short from the input video."""
    output_path = os.path.join(output_dir, "short_clip.mp4")
    
    # 9:16 crop: typical 1080p is 1920x1080.
    # A 9:16 crop from the center of 1920x1080 would be 608x1080.
    # The crop filter syntax is crop=w:h:x:y. 
    # crop=ih*9/16:ih forces a 9:16 aspect ratio based on input height (ih), centered by default.
    args = [
        "-vf", "crop=ih*9/16:ih",
        "-t", "60",         # First 60 seconds
        "-c:a", "copy"      # Copy audio stream without re-encoding
    ]
    run_ffmpeg(input_path, output_path, args)

def generate_highlight(input_path, output_dir):
    """Generates a horizontal 3-minute highlight reel."""
    output_path = os.path.join(output_dir, "highlight_clip.mp4")
    args = [
        "-t", "180",        # First 180 seconds
        "-c:v", "copy",     # Copy video stream without re-encoding
        "-c:a", "copy"      # Copy audio stream without re-encoding
    ]
    run_ffmpeg(input_path, output_path, args)

def main():
    parser = argparse.ArgumentParser(description="Auto-Clip Engine for OBS Recordings")
    parser.add_argument("--input", help="Path to the raw OBS recording MP4")
    parser.add_argument("--output-dir", default="../clips", help="Directory to save clips")
    args = parser.parse_args()

    input_path = args.input or get_last_session()

    if not input_path or not os.path.exists(input_path):
        print(f"Error: Input video not found at {input_path}")
        return

    print(f"Starting Clip Engine for: {input_path}")
    
    os.makedirs(args.output_dir, exist_ok=True)

    generate_short(input_path, args.output_dir)
    generate_highlight(input_path, args.output_dir)

    print("Clip Engine finished.")

if __name__ == "__main__":
    main()
