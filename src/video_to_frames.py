import cv2

def extract_frames(video_path, scale=0.2):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (0, 0), fx=scale, fy=scale*0.5) # adjust for character width/height ratio
        frames.append(frame)
    cap.release()
    return frames
