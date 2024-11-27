from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QPixmap, QPainter, QMovie
from PyQt6.QtCore import Qt

class VistaDialogGanador(QtWidgets.QDialog):
    def __init__(self, jugador, parent=None):
        """
        Crea un diálogo para mostrar al ganador.
        :param jugador: Objeto que contiene información del jugador (nombre, avatar).
        :param parent: Ventana principal o contenedor del diálogo.
        """
        super().__init__(parent)
        self.jugador = jugador
        self.setWindowTitle("¡Ganador!")
        self.setWindowIcon(QtGui.QIcon('vista/img/icono_ganador.png'))
        self.setFixedSize(330, 300)
        with open("vista/estilos.qss") as f:
            self.setStyleSheet(f.read())
        self.setup_ui()

    def setup_ui(self):
        """
        Configura la interfaz del diálogo.
        """
        # Establecer fondo
        palette = self.palette()
        pixmap = QtGui.QPixmap("vista/img/fondo_ganador.png").scaled(self.size(), QtCore.Qt.AspectRatioMode.IgnoreAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(pixmap))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # Layout principal
        layout = QtWidgets.QVBoxLayout(self)

        #Layout gif - avatar - gif
        layout_gifs = QtWidgets.QHBoxLayout()

        gif1_label = QtWidgets.QLabel(self)
        gif1_label.setFixedSize(100, 120)
        gif1 = QMovie("vista/img/sparkle.gif")
        gif1.setScaledSize(gif1_label.size())
        gif1_label.setMovie(gif1)
        gif1.start()

        gif2_label = QtWidgets.QLabel(self)
        gif2_label.setFixedSize(100, 120)
        gif2 = QMovie("vista/img/sparkle.gif")
        gif2.setScaledSize(gif2_label.size())
        gif2_label.setMovie(gif2)
        gif2.start()

        #Titulo ganador
        titulo_ganador = QtWidgets.QLabel(self)
        titulo_ganador.setPixmap(QtGui.QPixmap("vista/img/titulo_ganador.png"))
        titulo_ganador.setScaledContents(True)
        titulo_ganador.setMaximumSize(QtCore.QSize(320, 70))
        layout.addWidget(titulo_ganador)

        # Avatar del jugador
        avatar_label= QtWidgets.QLabel(self)
        avatar_label.setPixmap(self.__decorar_avatar_jugador(self.jugador))
        avatar_label.setScaledContents(True)
        avatar_label.setFixedSize(100, 100)
        
        layout_gifs.addWidget(gif1_label)
        layout_gifs.addWidget(avatar_label)
        layout_gifs.addWidget(gif2_label)
        layout.addLayout(layout_gifs)

        # Texto del ganador
        nombre = self.jugador.get_nombre_visual()
        ganador_label = QtWidgets.QLabel(f"{nombre}", self)
        ganador_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        #ganador_label.setFixedSize(100, 25)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        ganador_label.setFont(font)
        ganador_label.setProperty("tipo","nombre_ganador")
        layout.addWidget(ganador_label)

        # Botón para cerrar el diálogo
        close_button = QtWidgets.QPushButton("Cerrar", self)
        close_button.clicked.connect(self.accept)  # Cierra el diálogo al hacer clic
        close_button.setProperty("tipo", "boton_vista_ganador")
        #close_button.setFixedSize(100, 30)
        layout.addStretch()
        layout.addWidget(close_button)
        layout.addStretch()
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
    
    def __decorar_avatar_jugador(self, jugador)-> QPixmap:
        decoracion = QtGui.QPixmap("vista/img/medalla_ganador.png")
        avatar_jugador = QtGui.QPixmap(jugador.get_avatar_visual())

        decoracion = decoracion.scaledToHeight(int(avatar_jugador.height() * 0.45))

        lienzo = QPixmap(avatar_jugador.size()) #lienzo para pintar dos imagenes
        lienzo.fill(Qt.GlobalColor.transparent)

        painter = QPainter(lienzo)
        painter.drawPixmap(0, 0, avatar_jugador) #pinta el jugador

        decoracion_x = 0
        decoracion_y = avatar_jugador.height() - decoracion.height()
        painter.drawPixmap(decoracion_x, decoracion_y, decoracion) #pinta la decoración
        painter.end()
        return lienzo
