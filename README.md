
# ASCII Player

Convert and play videos (including YouTube links) as real-time ASCII art directly in your terminal.

## Features

- Supports `.mp4`, `.avi`, `.mkv`, `.mov`, and YouTube (`.yt`) formats
- Adjustable resolution via scaling
- CLI-friendly, modular, and extensible

## Usage

```bash
python src/ascii_player.py path/to/video.mp4
python src/ascii_player.py video.yt
```

`.yt` should contain a single line with a valid YouTube URL.

## Setup

```bash
pip install -r requirements.txt
```

## Dependencies

- opencv-python
- numpy
- pillow
- pytube
- ffmpeg-python
- colorama

---
