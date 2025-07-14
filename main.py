import cv2
from ultralytics import YOLO
from camera import open_camera, read_frame, release_camera
from fall_detector import is_fall_detected, draw_alert

def main():
    model = YOLO('yolov8n-pose.pt')
    cap = open_camera()
    state = {'fall_start': None}

    cv2.namedWindow('Fall Detector', cv2.WINDOW_NORMAL)

    while True:
        frame = read_frame(cap)
        image_height, image_width = frame.shape[:2]
        results = model(frame)
        fall_detected = False

        for result in results:
            for kp in result.keypoints.xy:
                keypoints = kp.tolist()
                if len(keypoints) >= 13:
                    fall_detected = is_fall_detected(keypoints, image_height, image_width, state)
                    break
            frame = result.plot()

        if fall_detected:
            draw_alert(frame, image_width, image_height)
        cv2.imshow('Fall Detector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    release_camera(cap)

if __name__ == "__main__":
    main()