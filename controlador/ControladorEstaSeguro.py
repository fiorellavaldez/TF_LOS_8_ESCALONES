from vista.VistaEstaSeguro import VistaEstaSeguro
from PyQt6 import QtWidgets


class ControladorEstaSeguro(QtWidgets.QDialog):
    def __init__(self, mensaje):
        super().__init__()
        self.__vista = VistaEstaSeguro()
        self.__aceptado = None
        self.__vista.setupUi(self, mensaje)

        self.__vista.pushButton_12.clicked.connect(self.__accion_aceptar)
        self.__vista.pushButton_13.clicked.connect(self.__accion_cancelar)

    def __accion_aceptar(self):
        self.__aceptado = True
        self.accept()

    def __accion_cancelar(self):
        self.__aceptado = False
        self.reject()

    def fue_aceptado(self):
        return self.__aceptado
