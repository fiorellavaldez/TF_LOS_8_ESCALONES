from vista.VistaConfiguracionTemaABM import Ui_MainWindow
from controlador.ControladorVistaTemaNuevo import ControladorVistaTemaNuevo
from controlador.ControladorVistaConfiguracinTemaABMEdit import ControladorVistaConfiguracionTemaABMEdit

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
from  Modelo.TemasDAO import TemasDAO

class ControladorVistaConfiguracionTemaABM:
    #def __init__(self):
    def __init__(self, controlador_anterior=None):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        
        #self.Widget = QtWidgets.QWidget()
        #self.__vistaWidget = QtWidgets()

        #self.__vista.get_button_atras().clicked.connect(self.__volver_configuracion)
        self.__vista.pushButton_Volver.clicked.connect(self.__volver_configuracion)
        #self.__vista.pushButton_Nuevo.clicked.connect()
        self.__vista.pushButton_Modificar.clicked.connect(self.__modificarTema)

        # Para botones u otros se agregan acá
        # self.MainWindow.

        self.__vista.QTable_Temas.setColumnCount(2)
        self.__vista.QTable_Temas.setColumnHidden(0,True)
        self.__vista.QTable_Temas.setColumnWidth(1,400)
        self.__vista.QTable_Temas.setHorizontalHeaderLabels(["Id_tema","Tema"]) #El parametro para los nombres de los encabezados debe ser un iterable
        self.__vista.QTable_Temas.setVerticalHeaderLabels([""])
        self.__vista.QTable_Temas.verticalHeader().hide()

        self.__lista_temas = []
        self.__temas = TemasDAO()
        
        @property
        def lista_temas(self):
            return self.__lista_temas
 

        lista_temas = self.__temas.get_all_temas()
        
        #lista_temas = [TemasDAO().get_all_temas()]

        self.__vista.QTable_Temas.setRowCount(len(lista_temas))
        
        
        for linea, (id_tema, nombre_tema) in enumerate(lista_temas):  
            self.__vista.QTable_Temas.setItem(linea, 0, QTableWidgetItem(str(id_tema)))  
            self.__vista.QTable_Temas.setItem(linea, 1, QTableWidgetItem(nombre_tema))  

      
    def __volver_configuracion(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __modificarTema(self):
        #print(self.__vista.QTable_Temas.currentItem())
        self.MainWindow.hide()
        #self.ControladorVistaTemaNuevo = ControladorVistaTemaNuevo(self)
        self.ControladorVistaTemaNuevo = ControladorVistaConfiguracionTemaABMEdit(self)

        
        #self.__obtener_celda_seleccionada()
        #self.__obtener_tupla_seleccionada()

    def __obtener_celda_seleccionada(self):  
        item = self.__vista.QTable_Temas.currentItem()  
        if item is not None:  
            print("Contenido de la celda seleccionada:", item.text())  
        else:  
            print("No hay ninguna celda seleccionada.") 

    def __obtener_tupla_seleccionada(self):
        fila_actual = self.__vista.QTable_Temas.currentRow()  # Obtiene la fila seleccionada  
        if fila_actual != -1:  # Verifica que haya una fila seleccionada  
            datos_tupla = []  
            for columna in range(self.__vista.QTable_Temas.columnCount()):  
                item = self.__vista.QTable_Temas.item(fila_actual, columna)  
                if item is not None:  
                    datos_tupla.append(item.text())  
            print(datos_tupla)  # Imprime los datos de la tupla seleccionada

    """def __bloqueo_modif_tabla(self):
        for 
        self.__vista.QTable_Temas.item(row, column).setFlags(Qt.ItemFlag.ItemIsEnabled)
        """