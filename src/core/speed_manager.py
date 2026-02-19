class SpeedManager:
    def __init__(self, frame_interval):
        self.video_speed_multiplier = 1
        self.frame_interval = frame_interval
        self.paused = False

    def adjust_speed(self, key):
        if key == ord('d'):  # Aumentar velocidad
            augmentation = 1 if self.video_speed_multiplier >= 1 else 0.1
            self.video_speed_multiplier = min(self.video_speed_multiplier + augmentation, 16)
        elif key == ord('a'):  # Reducir velocidad
            augmentation = 1 if self.video_speed_multiplier > 1 else 0.1
            self.video_speed_multiplier = max(0.1, self.video_speed_multiplier - augmentation)
        self.video_speed_multiplier = round(self.video_speed_multiplier, 1)
        return self.frame_interval / self.video_speed_multiplier
    
    def toggle_pause(self):
        self.paused = not self.paused
        return self.paused