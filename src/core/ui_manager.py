from ui import FPSCounter, StatisticsBox, SpeedMultiplierDisplay, Position

class UiManager:
    def __init__(self):
        self.fps_counter = FPSCounter(position=Position.TOP_RIGHT, color=(0, 255, 0))
        self.stats_box = StatisticsBox(position=Position.BOTTOM_RIGHT, color=(0, 255, 0))
        self.speed_display = SpeedMultiplierDisplay(
            position=Position.BOTTOM_RIGHT, color=(0, 255, 0), yoffset=-100
        )

    def update_ui(self, frame, results, video_speed_multiplier, paused):
        self.fps_counter.draw(frame)
        self.stats_box.update_stats(results)
        self.stats_box.draw(frame)
        self.speed_display.update_multiplier(video_speed_multiplier, paused)
        self.speed_display.draw(frame)