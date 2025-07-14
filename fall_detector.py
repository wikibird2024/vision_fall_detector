import numpy as np
import time

FALL_THRESHOLD_ANGLE = 60  # degrees
FALL_DURATION_THRESHOLD = 1.0  # seconds

def calculate_angle(a, b, c):
    """Calculate angle at point b given three points a, b, c (x, y)."""
    a, b, c = np.array(a), np.array(b), np.array(c)
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6)
    angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
    return np.degrees(angle)

def get_midpoint(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

def is_fall_detected(keypoints, image_height, image_width, state):
    try:
        nose = keypoints[0][:2]
        left_shoulder = keypoints[5][:2]
        right_shoulder = keypoints[6][:2]
        left_hip = keypoints[11][:2]
        right_hip = keypoints[12][:2]
        mid_shoulder = get_midpoint(left_shoulder, right_shoulder)
        mid_hip = get_midpoint(left_hip, right_hip)
        torso_vec_x = mid_shoulder[0] - mid_hip[0]
        torso_vec_y = mid_shoulder[1] - mid_hip[1]
        torso_angle = np.abs(np.degrees(np.arctan2(torso_vec_x, -torso_vec_y)))
        if torso_angle > 90:
            torso_angle = 180 - torso_angle
        nose_y_pixel = int(nose[1])
        is_horizontal = torso_angle > FALL_THRESHOLD_ANGLE
        is_low = nose[1] > image_height * 0.75
        is_current_fall = is_horizontal and is_low
        now = time.time()
        if is_current_fall:
            if state['fall_start'] is None:
                state['fall_start'] = now
            elif (now - state['fall_start']) > FALL_DURATION_THRESHOLD:
                return True
        else:
            state['fall_start'] = None
        return False
    except Exception:
        state['fall_start'] = None
        return False

def draw_alert(frame, image_width, image_height):
    import cv2
    cv2.putText(frame, "!!! FALL DETECTED !!!", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3, cv2.LINE_AA)
    cv2.rectangle(frame, (0, 0), (image_width, image_height), (0, 0, 255), 5)