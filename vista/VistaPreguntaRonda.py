from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt6.QtGui import QFont

class VistaPreguntaRonda(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pregunta!")
        self.resize(600, 500)

        # Fonts
        font_14b = QFont()
        font_14b.setPointSize(14)
        font_14b.setBold(True)

        font_14 = QFont()
        font_14.setPointSize(14)

        font_11b = QFont()
        font_11b.setPointSize(11)
        font_11b.setBold(True)

        font_11 = QFont()
        font_11.setPointSize(11)

        # Layout principal
        main_layout = QVBoxLayout(self)

        # Información general
        info_layout = QGridLayout()
        self.num_escalon = QLabel("0")
        self.num_escalon.setFont(font_14b)
        info_layout.addWidget(QLabel("Escalón N°:", font=font_14b), 0, 0)
        info_layout.addWidget(self.num_escalon, 0, 1)

        self.nombre_tematica = QLabel("Temática")
        self.nombre_tematica.setFont(font_14)
        info_layout.addWidget(QLabel("Temática:", font=font_14b), 0, 2)
        info_layout.addWidget(self.nombre_tematica, 0, 3)

        self.nombre_jugador = QLabel("Jugador")
        self.nombre_jugador.setFont(font_14)
        info_layout.addWidget(QLabel("Jugador:", font=font_14b), 1, 0)
        info_layout.addWidget(self.nombre_jugador, 1, 1)

        main_layout.addLayout(info_layout)

        # Pregunta
        self.pregunta_label = QLabel("Pregunta")
        self.pregunta_label.setFont(font_14b)
        self.pregunta_label.setWordWrap(True)
        self.pregunta_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        main_layout.addWidget(self.pregunta_label)

        # Selección de respuesta
        seleccione_label = QLabel("Seleccione una respuesta:")
        seleccione_label.setFont(font_11b)
        main_layout.addWidget(seleccione_label)

        # Respuestas con botones
        respuestas_layout = QGridLayout()

        self.opcion_a = QPushButton("A")
        self.opcion_b = QPushButton("B")
        self.opcion_c = QPushButton("C")
        self.opcion_d = QPushButton("D")

        self.respuesta_a = QLabel("Respuesta A")
        self.respuesta_b = QLabel("Respuesta B")
        self.respuesta_c = QLabel("Respuesta C")
        self.respuesta_d = QLabel("Respuesta D")

        for label in [self.respuesta_a, self.respuesta_b, self.respuesta_c, self.respuesta_d]:
            label.setFont(font_11)
            label.setWordWrap(True)

        respuestas_layout.addWidget(self.opcion_a, 0, 0)
        respuestas_layout.addWidget(self.respuesta_a, 0, 1)
        respuestas_layout.addWidget(self.opcion_b, 1, 0)
        respuestas_layout.addWidget(self.respuesta_b, 1, 1)
        respuestas_layout.addWidget(self.opcion_c, 0, 2)
        respuestas_layout.addWidget(self.respuesta_c, 0, 3)
        respuestas_layout.addWidget(self.opcion_d, 1, 2)
        respuestas_layout.addWidget(self.respuesta_d, 1, 3)

        main_layout.addLayout(respuestas_layout)

        # Conectar señales
        self.opcion_a.clicked.connect(lambda: self.seleccionar_respuesta("A"))
        self.opcion_b.clicked.connect(lambda: self.seleccionar_respuesta("B"))
        self.opcion_c.clicked.connect(lambda: self.seleccionar_respuesta("C"))
        self.opcion_d.clicked.connect(lambda: self.seleccionar_respuesta("D"))

    def actualizar_pregunta(self, jugador, escalon, tematica, pregunta, respuestas):
        """
        Actualiza los datos de la ventana emergente.
        """
        self.nombre_jugador.setText(jugador)
        self.num_escalon.setText(str(escalon))
        self.nombre_tematica.setText(tematica)
        self.pregunta_label.setText(pregunta)
        self.respuesta_a.setText(respuestas[0])
        self.respuesta_b.setText(respuestas[1])
        self.respuesta_c.setText(respuestas[2])
        self.respuesta_d.setText(respuestas[3])

    def seleccionar_respuesta(self, opcion):
        """
        Maneja la respuesta seleccionada por el jugador.
        """
        print(f"El jugador seleccionó la respuesta {opcion}")
        self.done(int(ord(opcion.upper())-64))  # Devuelve la opción seleccionada y cierra el diálogo