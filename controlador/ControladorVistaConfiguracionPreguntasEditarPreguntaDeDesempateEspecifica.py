from vista.VistaConfiguracionPreguntasEditarPreguntaDeDesempate import Ui_MainWindow
from PyQt6 import QtWidgets

class ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__vista.get_button_atras().clicked.connect(self.__volver)
        #self.__vista.get_button_aceptar().clicked.connect(self.__guardar) #??

    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    # def __guardar(self):
    #     pass