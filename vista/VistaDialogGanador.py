from PyQt6 import QtWidgets, QtGui, QtCore

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
        self.setFixedSize(300, 200)
        self.setup_ui()

    def setup_ui(self):
        """
        Configura la interfaz del diálogo.
        """
        # Layout principal
        layout = QtWidgets.QVBoxLayout(self)

        # Avatar del jugador
        avatar_label = QtWidgets.QLabel(self)
        avatar_label.setPixmap(QtGui.QPixmap(self.jugador.get_avatar_visual()))
        avatar_label.setScaledContents(True)
        avatar_label.setFixedSize(100, 100)
        avatar_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(avatar_label)

        # Texto del ganador
        nombre = self.jugador.get_nombre_visual()
        ganador_label = QtWidgets.QLabel(f"{nombre} ES EL GANADOR!!!", self)
        ganador_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        ganador_label.setFont(font)
        layout.addWidget(ganador_label)

        # Botón para cerrar el diálogo
        close_button = QtWidgets.QPushButton("Cerrar", self)
        close_button.clicked.connect(self.accept)  # Cierra el diálogo al hacer clic
        layout.addWidget(close_button)
