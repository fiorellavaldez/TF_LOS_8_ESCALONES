from vista.VistaConfiguracionModificarPreguntasDeRonda import Ui_MainWindow
from controlador.ControladorVistaConfiguracionPreguntasEditarPreguntaDeRondaEspecifica import ControladorVistaConfiguracionPreguntasEditarPreguntaDeRondaEspecifica
from PyQt6 import QtWidgets

class ControladorVistaConfiguracionModificarPreguntasRonda:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__vista.get_button_atras().clicked.connect(self.__volver)
        self.__vista.get_button_agregar_pregunta().clicked.connect(self.__agregar_pregunta)

    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __agregar_pregunta(self):
        self.MainWindow.hide()
        self.controlador_siguiente = ControladorVistaConfiguracionPreguntasEditarPreguntaDeRondaEspecifica(self)