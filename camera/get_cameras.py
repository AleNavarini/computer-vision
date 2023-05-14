import cv2


def get_cameras() -> dict:
    index = 0
    cameras = {}
    while True:
        try:
            video_capture = cv2.VideoCapture(index)
            if not video_capture.isOpened():
                break
            _, frame = video_capture.read()

            cameras[index] = (frame.shape[1], frame.shape[0])
            video_capture.release()
            index += 1
        except:
            break
    print(f"Cameras : {cameras}")
    return cameras
