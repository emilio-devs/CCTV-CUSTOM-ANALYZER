from enum import Enum
import cv2

# Enum para las posiciones en la pantalla
class Position(Enum):
    TOP_LEFT = 1
    TOP_RIGHT = 2
    BOTTOM_LEFT = 3
    BOTTOM_RIGHT = 4

# Clase base para pintar objetos en pantalla
class DrawableObject:
    def __init__(self, position: Position, color: tuple=(0, 255, 0), xoffset: int = 0, yoffset: int = 0):
        """
        Constructor de DrawableObject.
        :param position: Posición (esquina) donde se dibujará el objeto.
        :param color: Color del objeto en formato BGR.
        """
        self.position = position
        self.color = color
        self.xoffset = xoffset
        self.yoffset = yoffset

    def draw(self, frame, text: str):
        """
        Dibuja el objeto en el frame dado.
        :param frame: Frame donde se dibujará.
        :param text: Texto a mostrar.
        """
        x, y = self._get_position_coordinates(frame)
        cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.6, self.color, 2)

    def _get_position_coordinates(self, frame, box_width=0, box_height=0):
        """
        Calcula las coordenadas en función de la posición seleccionada,
        ajustando para que el cuadro no se salga del frame.
        :param frame: Frame donde se calcula la posición.
        :param box_width: Ancho del cuadro.
        :param box_height: Alto del cuadro.
        :return: Coordenadas (x, y) ajustadas.
        """
        height, width, _ = frame.shape
        margin = 10  # Margen desde las esquinas

        # Coordenadas base según la posición
        if self.position == Position.TOP_LEFT:
            x, y = margin, margin
        elif self.position == Position.TOP_RIGHT:
            x, y = width - box_width - margin, margin
        elif self.position == Position.BOTTOM_LEFT:
            x, y = margin, height - box_height - margin
        elif self.position == Position.BOTTOM_RIGHT:
            x, y = width - box_width - margin, height - box_height - margin
        else:
            x, y = margin, margin  # Por defecto, top-left

        # # Aplicar desplazamientos (offsets)
        x += self.xoffset
        y += self.yoffset

        # Asegurarse de que las coordenadas estén dentro del frame
        x = max(0, min(x, width - box_width))
        y = max(0, min(y, height - box_height))

        return x, y