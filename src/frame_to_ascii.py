import cv2
from colorama import Fore, Style, init

init()  # initialize colorama on Windows

CHARS = "@%#*+=-:. "

def pixel_to_ansi(r, g, b):
    # Map RGB to basic ANSI 16 colors (feel free to improve this for 256-color later)
    if r > 200 and g > 200 and b > 200:
        return Fore.WHITE
    elif r > 200:
        return Fore.RED
    elif g > 200:
        return Fore.GREEN
    elif b > 200:
        return Fore.BLUE
    elif r > 100 and g > 100:
        return Fore.YELLOW
    elif g > 100 and b > 100:
        return Fore.CYAN
    elif r > 100 and b > 100:
        return Fore.MAGENTA
    else:
        return Fore.BLACK

def convert_frame_to_ascii(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ascii_image = ""
    for i, row in enumerate(gray):
        line = ""
        for j, pixel in enumerate(row):
            char = CHARS[int(pixel * len(CHARS) / 256)]
            b, g, r = frame[i][j]
            color = pixel_to_ansi(r, g, b)
            line += f"{color}{char}{Style.RESET_ALL}"
        ascii_image += line + "\n"
    return ascii_image
