def normalize_keypoints(keypoints, image_width, image_height):
    """Normalize keypoints to [0, 1] range based on image size."""
    return [[x / image_width, y / image_height] for (x, y) in keypoints]