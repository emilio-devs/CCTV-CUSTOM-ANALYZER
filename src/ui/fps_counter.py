from .drawable_object import DrawableObject, Position
import cv2

class FPSCounter(DrawableObject):
    def __init__(self, position: Position = Position.TOP_LEFT, color: tuple = (0, 255, 0)):
        """
        Constructor de FPSCounter.
        :param position: Posición donde se mostrará el contador de FPS.
        :param color: Color del texto del FPS en formato BGR.
        """
        super().__init__(position, color)
        self.prev_time = 0

    def draw(self, frame):
        """
        Sobrescribe el método draw para mostrar los FPS.
        :param frame: Frame donde se dibujará.
        """
        current_time = cv2.getTickCount() / cv2.getTickFrequency()
        fps = 1.0 / (current_time - self.prev_time) if self.prev_time != 0 else 0
        self.prev_time = current_time

        # Redondear FPS y convertir a texto
        text = f"FPS: {int(fps)}"

        # Calcular tamaño del texto
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_DUPLEX, 0.6, 2)[0]

        # Obtener las coordenadas ajustadas
        x, y = self._get_position_coordinates(frame, box_width=text_size[0], box_height=text_size[1])

        # Dibujar el texto de FPS
        cv2.putText(frame, text, (x, y + text_size[1]), cv2.FONT_HERSHEY_DUPLEX, 0.5, self.color, 2)