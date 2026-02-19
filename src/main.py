# Importar las librerías necesarias
import argparse
from config import DEFAULTS


from core import VideoProcessor, UiManager

def main(video_name, target_width, target_height, classes_of_interest):
    processor = VideoProcessor(video_name, target_width, target_height, classes_of_interest)
    processor.process()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CocoWatch")

    parser.add_argument(
        "--video_name", 
        type=str, 
        default=DEFAULTS["video_name"], 
        help="Ruta del video o fuente de cámara. (por defecto: camera.mp4 en carpeta data)"
    )
    parser.add_argument(
        "--target_width", 
        type=int, 
        default=DEFAULTS["target_width"], 
        help="Ancho objetivo del frame."
    )
    parser.add_argument(
        "--target_height", 
        type=int, 
        default=DEFAULTS["target_height"], 
        help="Alto objetivo del frame."
    )
    parser.add_argument(
        "--classes_of_interest", 
        type=int, 
        nargs="+", 
        default=DEFAULTS["classes_of_interest"], 
        help="Clases de interés (IDs del dataset COCO)."
    )

    args = parser.parse_args()

    main(
        args.video_name, 
        args.target_width, 
        args.target_height, 
        args.classes_of_interest
    )
