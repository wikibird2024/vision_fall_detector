# Vision Fall Detector

A real-time fall detection system using webcam and YOLOv8 pose estimation.

## Features

- Uses YOLOv8 for human pose estimation.
- Detects falls based on torso orientation and nose position.
- Real-time webcam feed, with alert overlay on fall detection.

## Usage

1. Install requirements:
    ```
    pip install -r requirements.txt
    ```
2. Run the system:
    ```
    python main.py
    ```

## File Structure

- `camera.py` - Handles webcam operations.
- `fall_detector.py` - Contains fall detection logic.
- `main.py` - Main run script.
- `utils.py` - Utilities (e.g., keypoint normalization).
- `requirements.txt` - Python dependencies.
- `readme.md` - Project description.