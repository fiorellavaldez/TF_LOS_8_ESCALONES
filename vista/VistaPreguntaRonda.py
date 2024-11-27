from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QFont, QKeyEvent
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QPixmap, QPainter, QMovie
from PyQt6.QtCore import Qt

class VistaPreguntaRonda(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pregunta!")
        self.resize(600, 500)
        # Deshabilitar el botón de cerrar (X)
        #self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint, False)

        palette = self.palette()
        pixmap = QtGui.QPixmap("vista/img/fondo_preguntas.png").scaled(self.size(), QtCore.Qt.AspectRatioMode.IgnoreAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(pixmap))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # Variable para controlar si se ha respondido
        self.respuesta_seleccionada = False

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

        self.num_ronda = QLabel("Ronda")
        self.num_ronda.setFont(font_14)
        info_layout.addWidget(QLabel("Ronda:", font=font_14b), 1, 2)
        info_layout.addWidget(self.num_ronda, 1, 3)

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

        self.opcion_a.setObjectName("bt_respuesta_ronda")
        self.opcion_b.setObjectName("bt_respuesta_ronda")
        self.opcion_c.setObjectName("bt_respuesta_ronda")
        self.opcion_d.setObjectName("bt_respuesta_ronda")


        self.opcion_a.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.50965, y1:0.284, x2:0.491051, y2:1, stop:0 rgba(14, 72, 128, 255), stop:1 rgba(0, 0, 208, 255));height: 35px; width: 100px; font-size: 15px; color:#ffffff; font-weight:bold;border-radius: 3px;")

        self.opcion_b.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.50965, y1:0.284, x2:0.491051, y2:1, stop:0 rgba(14, 72, 128, 255), stop:1 rgba(0, 0, 208, 255));height: 35px; width: 100px; font-size: 15px; color:#ffffff; font-weight:bold;border-radius: 3px;")

        self.opcion_c.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.50965, y1:0.284, x2:0.491051, y2:1, stop:0 rgba(14, 72, 128, 255), stop:1 rgba(0, 0, 208, 255));height: 35px; width: 100px; font-size: 15px; color:#ffffff; font-weight:bold;border-radius: 3px;")

        self.opcion_d.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.50965, y1:0.284, x2:0.491051, y2:1, stop:0 rgba(14, 72, 128, 255), stop:1 rgba(0, 0, 208, 255));height: 35px; width: 100px; font-size: 15px; color:#ffffff; font-weight:bold;border-radius: 3px;")
        
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

    def actualizar_pregunta(self, jugador, escalon, tematica, ronda_actual, pregunta, respuestas):
        """
        Actualiza los datos de la ventana emergente.
        """
        self.nombre_jugador.setText(jugador)
        self.num_escalon.setText(str(escalon))
        self.nombre_tematica.setText(tematica)
        self.num_ronda.setText(str(ronda_actual))
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
        self.respuesta_seleccionada = True
        self.done(int(ord(opcion.upper()) - 64))  # Devuelve la opción seleccionada y cierra el diálogo

    def closeEvent(self, event):
        """
        Maneja el evento de cierre de la ventana.
        """
        if not self.respuesta_seleccionada:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Debe seleccionar una respuesta antes de cerrar.")
            event.ignore()  # Evita el cierre del diálogo
        else:
            event.accept()  # Permite el cierre si se ha respondido
    
    def keyPressEvent(self, event: QKeyEvent):
        """
        Maneja eventos de teclado, deshabilitando el cierre con la tecla Esc.
        """
        if event.key() == QtCore.Qt.Key.Key_Escape:
            event.ignore()  # Ignorar la tecla Esc
        else:
            super().keyPressEvent(event)  # Procesar otros eventos normalmente
