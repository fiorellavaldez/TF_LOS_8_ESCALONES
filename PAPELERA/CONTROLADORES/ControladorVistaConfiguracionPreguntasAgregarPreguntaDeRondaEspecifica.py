from vista.VistaConfiguracionPreguntasAgregarPreguntaDeRondaEspecifica import Ui_MainWindow
from PyQt6 import QtWidgets

class ControladorVistaConfiguracionPreguntasAgregarPreguntaDeRondaEspecifica:
    def __init__(self, controlador_anterior, id_tema):
        self.__controlador_anterior = controlador_anterior
        self.__id_tema = id_tema
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__vista.get_button_atras().clicked.connect(self.__volver)
        #self.__vista.get_button_aceptar().clicked.connect(self.__guardar) #??

    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def imprimir(self):
        print(f"id tema: {self.__id_tema}")
