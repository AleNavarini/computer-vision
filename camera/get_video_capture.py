import cv2
from camera.get_cameras import get_cameras

WIDTH = 1280
HEIGHT = 720


def get_video_capture(index: int, native: bool = True) -> cv2.VideoCapture:
    cameras = get_cameras()
    dimensions: tuple = cameras[index]
    video_capture = cv2.VideoCapture(index)
    if native:
        video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, dimensions[0])
        video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, dimensions[1])
    else:
        video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

    if not video_capture.isOpened():
        print("Failed to open camera")
        exit()

    return video_capture
