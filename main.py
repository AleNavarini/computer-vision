import math
from ultralytics import YOLO
import cv2
import cvzone

from camera.get_video_capture import get_video_capture
from coco.coco import get_classnames

CAMERA_INDEX = 0


def main(model_size: str = "n") -> None:
    print("Getting video capture ... ")
    video_capture = get_video_capture(CAMERA_INDEX)
    print("Found video capture")
    classes = get_classnames()

    model = YOLO(f"weights/yolov8{model_size}.pt")

    while True:
        _, frame = video_capture.read()
        results = model(frame, stream=True)

        for result in results:
            for box in result.boxes:
                confidence = math.ceil(box.conf[0] * 100) / 100
                if confidence > 0.5:
                    draw_box(classes, frame, box)

        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()


def draw_box(classes: list[str], frame, box) -> None:
    x1, y1, x2, y2 = [int(x) for x in box.xyxy[0]]
    w, h = x2 - x1, y2 - y1
    cvzone.cornerRect(frame, (x1, y1, w, h))
    confidence = math.ceil(box.conf[0] * 100) / 100
    classname = classes[int(box.cls)]
    cvzone.putTextRect(frame, f"{classname} - {confidence}", (x1, y1))


if __name__ == "__main__":
    print("Starting ... ")
    model_size = "m"
    main(model_size)
