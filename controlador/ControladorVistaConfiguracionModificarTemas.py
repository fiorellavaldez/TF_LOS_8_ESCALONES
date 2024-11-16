from vista.VistaConfiguracionModificarTema import Ui_MainWindow

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
from  modelo.TemasDAO import TemasDAO

class ControladorVistaConfiguracionModificarTemas:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        
        self.__vista.get_button_atras().clicked.connect(self.__volver_configuracion)
        # Para botones u otros se agregan acá
        # self.MainWindow.

        # Esto deberia estar en la Vista:
        self.__vista.tableWidget.setColumnCount(2)   
        self.__vista.tableWidget.setColumnWidth(0,80)
        self.__vista.tableWidget.setColumnWidth(1,180)
        self.__vista.tableWidget.setHorizontalHeaderLabels(['Nro Tema','Descripcion Tema'])
        
        # Probando lista
        """lista_temas = []
        for i in range(1,30):
            reg=(str(i),"Tema "+str(i))
            lista_temas.append(reg)
        """

        temas = TemasDAO()
        lista_temas = temas.get_all_temas()
        print(lista_temas)

        self.__vista.tableWidget.setRowCount(len(lista_temas))
        for linea, (id_tema, nombre_tema) in enumerate(lista_temas):  
            self.__vista.tableWidget.setItem(linea, 0, QTableWidgetItem(str(id_tema)))  
            self.__vista.tableWidget.setItem(linea, 1, QTableWidgetItem(nombre_tema))  

    def __volver_configuracion(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()