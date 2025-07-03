import cv2

CHARS = "@%#*+=-:. "

def convert_frame_to_ascii(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ascii_image = ""
    for row in gray:
        line = "".join([CHARS[int(pixel) * len(CHARS) // 256] for pixel in row])
        ascii_image += line + "\n"
    return ascii_image
