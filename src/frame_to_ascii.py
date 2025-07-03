import cv2
from colorama import Fore, Style, init
init()

CHARS = "@%#*+=-:. "
COLOR_MAP = [
    Fore.WHITE,
    Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.YELLOW,
    Fore.LIGHTRED_EX,
    Fore.RED,
    Fore.MAGENTA,
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
]

def convert_frame_to_ascii(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ascii_image = ""
    for row in gray:
        line = ""
        for pixel in row:
            val = int(pixel)
            idx = min(len(CHARS) - 1, val * len(CHARS) // 256)
            color = COLOR_MAP[val * len(COLOR_MAP) // 256]
            line += f"{color}{CHARS[idx]}{Style.RESET_ALL}"
        ascii_image += line + "\n"
    return ascii_image
