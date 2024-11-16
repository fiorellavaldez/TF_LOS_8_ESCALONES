from vista.VistaSeleccionDeTemaModificarPreguntasDeRonda import Ui_MainWindow
from controlador.ControladorVistaConfiguracionModificarPreguntasRonda import ControladorVistaConfiguracionModificarPreguntasRonda
from PyQt6 import QtWidgets

class ControladorVistaSeleccionTemaModificarPreguntasRonda:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        
        self.__vista.get_button_atras().clicked.connect(self.__volver_configuracion)
        self.__vista.get_button_seleccionar_pregunta().clicked.connect(self.__seleccionar_pregunta)

    def __volver_configuracion(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __seleccionar_pregunta(self):
        self.MainWindow.hide()
        self.controlador_seleccionar_pregunta = ControladorVistaConfiguracionModificarPreguntasRonda(self)