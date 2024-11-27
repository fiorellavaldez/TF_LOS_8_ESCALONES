from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QFont, QKeyEvent
from PyQt6 import QtCore
from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QPixmap, QPainter, QMovie
from PyQt6.QtCore import Qt

class VistaPreguntaAproximacion(QDialog):
    def __init__(self, enunciado, jugador, parent=None):
        super().__init__(parent)
        self.__enunciado = enunciado
        self.__jugador = jugador
        self.__respuesta = None
        self.setup_ui()

    def setup_ui(self):

        palette = self.palette()
        pixmap = QtGui.QPixmap("vista/img/fondo_preguntas.png").scaled(self.size(), QtCore.Qt.AspectRatioMode.IgnoreAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(pixmap))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        self.setWindowTitle("Pregunta de Desempate")
        self.setFixedSize(400, 300)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint, False)

        # Configuración del layout
        self.layout = QVBoxLayout(self)

        # Etiqueta para el nombre del jugador
        self.label_jugador = QLabel(self)
        self.label_jugador.setFont(QFont("Segoe UI", 10))
        self.label_jugador.setText(f"Jugador: {self.__jugador}")
        self.layout.addWidget(self.label_jugador)

        # Etiqueta para el enunciado de la pregunta
        self.label_enunciado = QLabel(self)
        self.label_enunciado.setFont(QFont("Segoe UI", 10))
        self.label_enunciado.setWordWrap(True)
        self.label_enunciado.setText(f"Pregunta: {self.__enunciado}")
        self.layout.addWidget(self.label_enunciado)

        # Campo para ingresar la respuesta
        self.text_edit = QTextEdit(self)
        self.text_edit.setFont(QFont("Segoe UI", 12))
        self.layout.addWidget(self.text_edit)

        # Botón de enviar respuesta
        self.button_layout = QHBoxLayout()
        self.button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.button_enviar = QPushButton("Enviar Respuesta", self)
        self.button_enviar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.50965, y1:0.284, x2:0.491051, y2:1, stop:0 rgba(14, 72, 128, 255), stop:1 rgba(0, 0, 208, 255));height: 35px; width: 100px; font-size: 10px; color:#ffffff; font-weight:bold;border-radius: 3px;")

        self.button_enviar.setFont(QFont("Segoe UI", 12))
        self.button_enviar.clicked.connect(self.enviar_respuesta)
        self.button_layout.addWidget(self.button_enviar)
        self.button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.layout.addLayout(self.button_layout)

    def enviar_respuesta(self):
        # Validar la respuesta ingresada
        try:
            respuesta = int(self.text_edit.toPlainText().strip())
            self.__respuesta = respuesta
            self.accept()  # Cerrar el diálogo de forma exitosa
        except ValueError:
            self.text_edit.setPlaceholderText("Por favor, ingresa un número válido.")

    def get_respuesta(self):
        return self.__respuesta
    
    def keyPressEvent(self, event: QKeyEvent):
        """
        Maneja eventos de teclado, deshabilitando el cierre con la tecla Esc.
        """
        if event.key() == QtCore.Qt.Key.Key_Escape:
            event.ignore()  # Ignorar la tecla Esc
        else:
            super().keyPressEvent(event)  # Procesar otros eventos normalmente