import cv2

def open_camera(camera_id=0):
    cap = cv2.VideoCapture(camera_id)
    if not cap.isOpened():
        raise RuntimeError("Cannot open webcam")
    return cap

def read_frame(cap):
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Failed to read frame from camera")
    return frame

def release_camera(cap):
    cap.release()
    cv2.destroyAllWindows()