from .drawable_object import DrawableObject, Position
import cv2

class SpeedMultiplierDisplay(DrawableObject):
    def __init__(self, position: Position = Position.BOTTOM_RIGHT, color: tuple = (255, 255, 255), xoffset: int = 0, yoffset: int = 0):
        """
        Constructor de SpeedMultiplierDisplay.
        :param position: Posición donde se mostrará el multiplicador.
        :param color: Color del texto en formato BGR.
        """
        super().__init__(position, color, xoffset, yoffset)
        self.speed_multiplier = 1.0

    def update_multiplier(self, multiplier, paused):
        """
        Actualiza el valor del multiplicador de velocidad.
        :param multiplier: Nuevo valor del multiplicador.
        """
        self.speed_multiplier = multiplier
        self.paused = paused

    def draw(self, frame):
        """
        Dibuja el multiplicador de velocidad en el frame.
        :param frame: Frame donde se dibujará.
        """
    
        # Mostrar el multiplicador dentro del cuadro
        symbol = ">>" if self.speed_multiplier > 1 else ("<<" if self.speed_multiplier < 1 else "")
        text = f" x{self.speed_multiplier:.2f}"

        # Calcular tamaño del texto
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_DUPLEX, 0.6, 2)[0]

        x, y = self._get_position_coordinates(frame, box_width=text_size[0], box_height=text_size[1])

        cv2.putText(frame, text, (x, y + text_size[1]), cv2.FONT_HERSHEY_DUPLEX, 0.5, self.color, 1)
        cv2.putText(frame, symbol, (x - 35, y + text_size[1]), cv2.FONT_HERSHEY_DUPLEX, 0.5, self.color, 1)