
import argparse
import os
import logging
from video_to_frames import extract_frames
from frame_to_ascii import convert_frame_to_ascii
from terminal_renderer import render_ascii_frames
from youtube_downloader import download_youtube_video
import shutil

def main():
    parser = argparse.ArgumentParser(description="Play videos as ASCII in your terminal.")
    parser.add_argument("input", help="Path to video file or .yt file with YouTube URL")
    parser.add_argument("--scale", type=float, default=0.2, help="Scaling factor for video (default: 0.2)")
    parser.add_argument("--fps", type=int, default=24, help="Frames per second (default: 24)")
    args = parser.parse_args()

    video_path = args.input

    if video_path.endswith(".yt"):
        with open(video_path) as f:
            url = f.read().strip()
        logging.info("Downloading YouTube video...")
        video_path = download_youtube_video(url)
        logging.debug(f"Saved as {video_path}")
        
        
    term_width, term_height = shutil.get_terminal_size((80, 24))
    auto_scale = args.scale if args.scale else min(term_width / 160, term_height / 48)

    logging.info("Extracting frames...")
    frames = extract_frames(video_path, scale=auto_scale)

    logging.info("Converting to ASCII...")
    ascii_frames = [convert_frame_to_ascii(frame) for frame in frames]

    logging.info("Rendering in terminal...")
    render_ascii_frames(ascii_frames, fps=args.fps)

if __name__ == "__main__":
    main()