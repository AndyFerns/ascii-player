import subprocess
import os
import uuid

def download_youtube_video(url, output=None):
    if output is None:
        output = f"yt_{uuid.uuid4().hex[:8]}.mp4"

    command = [
        "yt-dlp",
        "-f", "mp4",
        "-o", output,
        url
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"yt-dlp failed: {result.stderr.strip()}")

    # yt-dlp may not honor exact filename — find downloaded file
    if os.path.exists(output):
        return output
    else:
        for f in os.listdir("."):
            if f.endswith(".mp4") and os.path.getsize(f) > 1000000:  # ~1MB+
                return f
        raise FileNotFoundError("Video file not found after download.")
