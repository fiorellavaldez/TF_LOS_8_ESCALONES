from vista.VistaConfiguracionTemaABMEdit import Ui_Widget
from controlador.ControladorVistaTemaNuevo import ControladorVistaTemaNuevo

from PyQt6 import QtWidgets
#from PyQt6.QtWidgets import QTableWidgetItem
#from  Modelo.TemasDAO import TemasDAO

class ControladorVistaConfiguracionTemaABMEdit:
    #def __init__(self):
    def __init__(self, controlador_anterior=None):
        self.__controlador_anterior = controlador_anterior
        #self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow = QtWidgets.QWidget()
        self.__vista = Ui_Widget()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        
  
        self.__vista.buttonBox_Confirmar.clicked.connect(self.__volver_configuracion)
        
    def __volver_configuracion(self):
        #self.__consistir()
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    #def __consistir(self)
        