from vista.VistaJuego import Ui_MainWindow
from vista.VistaPreguntaRonda import VistaPreguntaRonda
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMessageBox, QDialog, QLabel, QPushButton
from PyQt6.QtGui import QFont
from modelo.TemasDAO import TemasDAO
from modelo.JugadorDAO import JugadorDAO

class ControladorVistaJuego:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__temas = TemasDAO()
        self.__lista_temas = self.__temas.temas_partida() #trae 8 temas ya mezclados
        self.__asignar_temas() #¿le pasamos la lista por parámetro?

        # self.__jugadores = 
        
        self.__vista.get_button_atras().clicked.connect(self.__atras)

    def __atras(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()

    def __obtener_pregunta(self): #pasarlo a una vista y la llamamos acá
        vista_pregunta = VistaPreguntaRonda()
        vista_pregunta.exec()

    def setRespuestaCorrecta(self, boton, ):
        pass

    def __asignar_temas(self):
        lista_qlabels = self.__vista.get_lista_nombres_escalon()
        for i in range(0,8):
            lista_qlabels[i].setText((self.__lista_temas[i][1]).upper())