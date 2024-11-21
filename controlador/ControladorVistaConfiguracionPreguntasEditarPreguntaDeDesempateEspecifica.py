from vista.VistaConfiguracionPreguntasEditarPreguntaDeDesempate import Ui_MainWindow
from PyQt6 import QtWidgets

class ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica:
    def __init__(self, controlador_anterior, pregunta):
        self.__pregunta = pregunta
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow,self.__pregunta.get_enunciado(), self.__pregunta.get_respuestaCorrecta())
        self.MainWindow.show()

        self.__vista.get_button_atras().clicked.connect(self.__volver)

    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()