from .drawable_object import DrawableObject, Position
import cv2

class StatisticsBox(DrawableObject):
    def __init__(self, position: Position = Position.BOTTOM_RIGHT, color: tuple = (255, 255, 255)):
        """
        Constructor de StatisticsBox.
        :param position: Posición donde se mostrará la caja de estadísticas.
        :param color: Color del texto y borde del cuadro en formato BGR.
        """
        super().__init__(position, color)
        self.stats = {"people": 0, "dogs": 0, "cats": 0}

    def update_stats(self, results):
        self.stats['people'] = 0
        self.stats['dogs'] = 0
        self.stats['cats'] = 0

        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0])
                if cls == 0:
                    self.stats['people'] += 1
                elif cls == 16:
                    self.stats['dogs'] += 1
                elif cls == 15:
                    self.stats['cats'] += 1

    def draw(self, frame):
        box_width = 110
        box_height = 90

        # Obtener las coordenadas ajustadas
        x, y = self._get_position_coordinates(frame, box_width, box_height)

        # Crear fondo
        overlay = frame.copy()
        alpha = 0.4
        cv2.rectangle(overlay, (x, y), (x + box_width, y + box_height), (255, 255, 255), -1)
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

        # Dibujar borde del cuadro
        cv2.rectangle(frame, (x, y), (x + box_width, y + box_height), self.color, 2)

        # Mostrar estadísticas dentro del cuadro
        stats_text = [
            f"People: {self.stats['people']}",
            f"Dogs: {self.stats['dogs']}",
            f"Cats: {self.stats['cats']}",
        ]

        for i, line in enumerate(stats_text):
            count = list(self.stats.values())[i]
            text_color = (0, 255, 0) if count > 0 else (80, 80, 80)

            cv2.putText(frame, line, (x + 10, y + 25 + i * 25), cv2.FONT_HERSHEY_DUPLEX, 0.6, text_color, 1)