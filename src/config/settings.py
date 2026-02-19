import os

# Data dir
DATA_DIR = os.path.join(os.path.dirname(__file__), "../../data")

DEFAULTS = {
    "video_name": "camera.mp4", 
    "desired_fps": 10,  # Frames por segundo deseados
    "target_width": 640,  # Ancho objetivo del frame
    "target_height": 480,  # Alto objetivo del frame
    "classes_of_interest": [0, 16, 15],  # Clases de interés (IDs del dataset COCO)
}