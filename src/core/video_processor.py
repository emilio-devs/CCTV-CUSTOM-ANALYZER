import os
import time
import cv2
import logging

from ultralytics import YOLO
from core import UiManager, SpeedManager
from config import DATA_DIR

logging.getLogger('ultralytics').setLevel(logging.ERROR)

class VideoProcessor:
    def __init__(self, video_name, target_width, target_height, classes_of_interest):
        self.video_name = video_name
        self.target_width = target_width
        self.target_height = target_height
        self.classes_of_interest = classes_of_interest
        self.model = YOLO('yolov8m.pt', verbose=False)
        self.capture = cv2.VideoCapture(os.path.join(DATA_DIR, video_name))
        self.ui_manager = UiManager()

        if not self.capture.isOpened():
            raise ValueError("Error: No se pudo abrir el video/cámara.")

        self.video_fps = self.capture.get(cv2.CAP_PROP_FPS) or 30
        self.frame_interval = 1.0 / self.video_fps
        self.speed_manager = SpeedManager(self.frame_interval)
        self.last_processed_time = time.time()
        self.paused = False

        self.results = None
        self.frame = None

    def process(self):
        while self.capture.isOpened():
            if not self.speed_manager.paused:
                current_time = time.time()
                delta_time = max(0, current_time - self.last_processed_time)
                adjusted_frame_interval = self.speed_manager.frame_interval / self.speed_manager.video_speed_multiplier

                if delta_time > adjusted_frame_interval:
                    skip_frames = int(delta_time / adjusted_frame_interval)
                    for _ in range(skip_frames - 1):
                        self.capture.grab()
                    self.last_processed_time += (skip_frames - 1) * adjusted_frame_interval

                ret, self.frame = self.capture.read()
                if not ret:
                    print("Fin del video o error al leer el frame.")
                    break

                self.last_processed_time += adjusted_frame_interval
                self.results = self.model.predict(self.frame, classes=self.classes_of_interest)
            
            self.ui_manager.update_ui(self.frame, self.results, self.speed_manager.video_speed_multiplier, self.speed_manager.paused)
            
            if self.results[0]:
                self.frame = self.results[0].plot()

            cv2.imshow("Analisis de camara", self.frame)

            wait_time = max(1, int(1000 * adjusted_frame_interval))
            key = cv2.waitKey(wait_time) & 0xFF
            if key == ord('q'):
                print("Saliendo del programa...")
                break
            elif key == ord(' '): 
                self.paused = self.speed_manager.toggle_pause()
                self.last_processed_time = time.time()
            if key in (ord('d'), ord('a')):
                adjusted_frame_interval = self.speed_manager.adjust_speed(key)

        self.capture.release()
        cv2.destroyAllWindows()