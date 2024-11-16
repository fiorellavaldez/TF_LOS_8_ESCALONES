from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMessageBox, QDialog, QLabel, QPushButton
from PyQt6.QtGui import QFont

class VistaPreguntaRonda(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(599, 444)
        self.setWindowTitle("Pregunta!")

        #fonts
        font_14b = QFont()
        font_14b.setPointSize(14)
        font_14b.setBold(True)

        font_14 = QFont()
        font_14b.setPointSize(14)

        font_15b = QFont()
        font_15b.setPointSize(15)
        font_15b.setBold(True)

        font_11b = QFont()
        font_11b.setPointSize(11)
        font_11b.setBold(True)

        font_11 = QFont()
        font_11.setPointSize(11)

        #pregunta
        pregunta = QLabel("Pregunta", self) #necesita setText
        pregunta.setGeometry(QtCore.QRect(20, 110, 561, 71))
        pregunta.setFont(font_15b)
        pregunta.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        pregunta.setWordWrap(True)

        #jugador
        jugador_label = QLabel("Jugador:", self)
        jugador_label.setGeometry(QtCore.QRect(310, 50, 91, 31))   
        jugador_label.setFont(font_14b)
        nombre_jugador = QLabel("Nombre",self) #necesita setText
        nombre_jugador.setFont(font_14)
        nombre_jugador.setGeometry(QtCore.QRect(400, 60, 121, 16))

        #escalon
        escalon_label = QLabel("Escalón N°",self)
        escalon_label.setFont(font_14b)
        escalon_label.setGeometry(QtCore.QRect(210, 20, 101, 16))
        num_escalon = QLabel("0",self) #necesita setText
        num_escalon.setFont(font_14b)
        num_escalon.setGeometry(QtCore.QRect(310, 20, 41, 16))

        #tematica
        tematica_label = QLabel("Temática:",self)
        tematica_label.setFont(font_14b)
        tematica_label.setGeometry(QtCore.QRect(70, 60, 91, 16))
        nombre_tematica = QLabel("Temática",self) #necesita un setText
        nombre_tematica.setFont(font_14)
        nombre_tematica.setGeometry(QtCore.QRect(160, 60, 101, 16))

        #Seleccionar
        seleccione = QLabel("Seleccione respuesta",self)
        seleccione.setFont(font_11b)
        seleccione.setGeometry(QtCore.QRect(210, 170, 151, 51))

        #Respuestas
        respuesta_a = QLabel("Respuesta a", self)
        respuesta_a.setGeometry(QtCore.QRect(70, 230, 231, 81))
        respuesta_a.setFont(font_11)
        respuesta_a.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        respuesta_a.setWordWrap(True)

        respuesta_b = QLabel("Respuesta b", self)
        respuesta_b.setGeometry(QtCore.QRect(70, 340, 231, 81))
        respuesta_b.setFont(font_11)
        respuesta_b.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        respuesta_b.setWordWrap(True)

        respuesta_c = QLabel("Respuesta c", self)
        respuesta_c.setGeometry(QtCore.QRect(360, 230, 231, 81))
        respuesta_c.setFont(font_11)
        respuesta_c.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        respuesta_c.setWordWrap(True)

        respuesta_d = QLabel("Respuesta d", self)
        respuesta_d.setGeometry(QtCore.QRect(360, 340, 231, 81))
        respuesta_d.setFont(font_11)
        respuesta_d.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        respuesta_d.setWordWrap(True)

        #opciones
        opcion_a = QPushButton("A", self)
        opcion_a.setGeometry(QtCore.QRect(20, 230, 41, 31))
        opcion_b = QPushButton("B",self)
        opcion_b.setGeometry(QtCore.QRect(20, 340, 41, 31))
        opcion_c = QPushButton("C",self)
        opcion_c.setGeometry(QtCore.QRect(310, 230, 41, 31))
        opcion_d = QPushButton("D",self)
        opcion_d.setGeometry(QtCore.QRect(310, 340, 41, 31))

        #self.exec()