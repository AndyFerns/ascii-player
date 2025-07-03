import os
import time
from datetime import timedelta
import logging

def render_ascii_frames(frames, fps=24):
    delay = 1 / fps
    total = len(frames)
    for idx, frame in enumerate(frames):
        os.system("cls" if os.name == "nt" else "clear")
        timestamp = str(timedelta(seconds=idx / fps))
        print(f"[Time: {timestamp}] Frame {idx+1}/{total}\n")
        print(frame)
        time.sleep(delay)
        
        # if KeyboardInterrupt:
        #     logging.error("User Interrupt! Stopping Video Playback")
        #     break