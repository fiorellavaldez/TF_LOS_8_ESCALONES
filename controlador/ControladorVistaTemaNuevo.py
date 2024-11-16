from vista.VistaTemaNuevo import Ui_MainWindow
from PyQt6 import QtWidgets

class ControladorVistaTemaNuevo:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

#        self.__vista.get_button_siguiente().clicked.connect(self.__ir_siguiente)
        self.__vista.get_button_atras().clicked.connect(self.__volver_configuracion)

    # def __ir_siguente(self):
    #     pass

    def __volver_configuracion(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()