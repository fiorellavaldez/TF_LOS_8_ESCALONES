from vista.VistaConfiguracionModificarPreguntasDeDesempate import Ui_MainWindow
from controlador.ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica import ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica
from PyQt6 import QtWidgets

class ControladorVistaConfiguracionModificarPreguntasDeDesempate:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        
        self.__vista.get_button_atras().clicked.connect(self.__volver_modificacion)
        self.__vista.get_button_agregar_pregunta().clicked.connect(self.__siguiente)

    def __volver_modificacion(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __siguiente(self):
        self.MainWindow.hide()
        self.__controlador_siguiente = ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica(self)