from vista.EDITARVistaConfiguracionPreguntasEditarPreguntaDeRonda import Ui_MainWindow
from PyQt6 import QtWidgets


class EDITARControladorConfiguracionPreguntasEditarPreguntaDeRonda():
    def __init__(self, controlador_anterior, pregunta_desempate):
        self.__pregunta = pregunta_desempate
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow(self.__pregunta.get_enunciado(),self.__pregunta.get_opcionA(), self.__pregunta.get_opcionB(), self.__pregunta.get_opcionC(), self.__pregunta.get_opcionD(), self.__pregunta.get_opcionCorrecta())
        self.__vista.setupUi(self.MainWindow, self.__pregunta.get_enunciado(), self.__pregunta.get_respuestaCorrecta())
        self.MainWindow.show()

        self.__vista.get_button_atras().clicked.connect(self.__volver)
        self.__vista.get_button_aceptar().clicked.connect(lambda: self.__guardar(self.__pregunta))
        
        
    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()
    
    def __guardar():
        pass