from vista.VistaConfiguracionModificarTema import Ui_MainWindow
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt

from modelo.TemasDAO import TemasDAO

class ControladorVistaConfiguracionModificarTemas:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        # Configuración del botón "Atrás"
        self.__vista.get_button_atras().clicked.connect(self.__volver_configuracion)

        # Inicialización de la tabla
        self.__vista.tableWidget.setColumnCount(1)  # Solo una columna para la descripción
        self.__vista.tableWidget.setColumnWidth(0, 180)  # Ajuste del ancho de la columna
        self.__vista.tableWidget.setHorizontalHeaderLabels(['Descripción Tema'])  # Título de la columna

        # Configuración de DAO y temas
        self.dao = TemasDAO()
        self.temas = self.dao.get_all_temas()  # Inicializa con todos los temas
        self.filtered_temas = self.temas.copy()  # Copia inicial para el filtrado

        # Configuración de búsqueda
        self.__vista.lineEdit.textChanged.connect(self.__buscar_temas)

        # Cargar la tabla inicialmente
        self.__actualizar_tabla(self.temas)

    def __volver_configuracion(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __actualizar_tabla(self, temas):
        """Actualiza la tabla con los temas proporcionados."""
        self.__vista.tableWidget.setRowCount(len(temas))  # Establece el número de filas
        for fila, (id_tema, descripcion) in enumerate(temas):
            item_descripcion = QTableWidgetItem(descripcion)  # Coloca solo la descripción en la celda
            item_descripcion.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # No editable
            self.__vista.tableWidget.setItem(fila, 0, item_descripcion)  # Asigna a la primera columna

    def __buscar_temas(self):
        """Filtra los temas según el texto ingresado en el cuadro de búsqueda."""
        texto = self.__vista.lineEdit.text().strip().lower()
        if texto:
            self.filtered_temas = [
                (id_tema, descripcion)
                for id_tema, descripcion in self.temas
                if texto in descripcion.lower()
            ]
        else:
            self.filtered_temas = self.temas  # Si no hay texto, mostrar todos los temas
        self.__actualizar_tabla(self.filtered_temas)



##################################################################################
##El primer cambio

# from vista.VistaConfiguracionModificarTema import Ui_MainWindow
# from PyQt6 import QtWidgets
# from PyQt6.QtWidgets import QTableWidgetItem
# from PyQt6.QtCore import QStringListModel
# from PyQt6.QtCore import Qt

# from modelo.TemasDAO import TemasDAO

# class ControladorVistaConfiguracionModificarTemas:
#     def __init__(self, controlador_anterior):
#         self.__controlador_anterior = controlador_anterior
#         self.MainWindow = QtWidgets.QMainWindow()
#         self.__vista = Ui_MainWindow()
#         self.__vista.setupUi(self.MainWindow)
#         self.MainWindow.show()

#         # Configuración del botón "Atrás"
#         self.__vista.get_button_atras().clicked.connect(self.__volver_configuracion)

#         # Inicialización de la tabla
#         self.__vista.tableWidget.setColumnCount(2)   
#         self.__vista.tableWidget.setColumnWidth(0, 80)
#         self.__vista.tableWidget.setColumnWidth(1, 180)
#         self.__vista.tableWidget.setHorizontalHeaderLabels(['Nro Tema', 'Descripcion Tema'])

        
#         # Configuración de DAO, ListView y búsqueda
#         self.dao = TemasDAO()
#         self.temas = []
#         self.filtered_temas = []
#         self.model = QStringListModel()

#         self.__vista.tableWidget.setRowCount(len(lista_temas))
#         for linea, (id_tema, nombre_tema) in enumerate(lista_temas):  
#             item_id = QTableWidgetItem(str(id_tema))
#             item_id.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # No editable
#             self.__vista.tableWidget.setItem(linea, 0, item_id)

#             item_nombre = QTableWidgetItem(nombre_tema)
#             item_nombre.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # No editable
#             self.__vista.tableWidget.setItem(linea, 1, item_nombre)

#     def __volver_configuracion(self):
#         self.MainWindow.hide()
#         self.__controlador_anterior.MainWindow.show()

#     def __actualizar_tabla(self, temas):
#         """Actualiza la tabla con los temas proporcionados."""
#         self.__vista.tableWidget.setRowCount(len(temas))
#         for fila, (id_tema, descripcion) in enumerate(temas):
#             item_id = QTableWidgetItem(str(id_tema))
#             item_id.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # No editable
#             self.__vista.tableWidget.setItem(fila, 0, item_id)

#             item_descripcion = QTableWidgetItem(descripcion)
#             item_descripcion.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # No editable
#             self.__vista.tableWidget.setItem(fila, 1, item_descripcion)

#     def __buscar_temas(self):
#         """Filtra los temas según el texto ingresado en el cuadro de búsqueda."""
#         texto = self.__vista.lineEdit.text().strip().lower()
#         if texto:
#             temas_filtrados = self.dao.get_tema(texto)
#         else:
#             temas_filtrados = self.filtered_temas  # Si no hay texto, mostrar todos los temas
#         self.__actualizar_tabla(temas_filtrados)

########################################################################################################

###El primer codigo original

# from vista.VistaConfiguracionModificarTema import Ui_MainWindow

# from PyQt6 import QtWidgets
# from PyQt6.QtWidgets import QTableWidgetItem
# from  modelo.TemasDAO import TemasDAO

# class ControladorVistaConfiguracionModificarTemas:
#     def __init__(self, controlador_anterior):
#         self.__controlador_anterior = controlador_anterior
#         self.MainWindow = QtWidgets.QMainWindow()
#         self.__vista = Ui_MainWindow()
#         self.__vista.setupUi(self.MainWindow)
#         self.MainWindow.show()
        
#         self.__vista.get_button_atras().clicked.connect(self.__volver_configuracion)
#         # Para botones u otros se agregan acá
#         # self.MainWindow.

#         # Esto deberia estar en la Vista:
#         self.__vista.tableWidget.setColumnCount(2)   
#         self.__vista.tableWidget.setColumnWidth(0,80)
#         self.__vista.tableWidget.setColumnWidth(1,180)
#         self.__vista.tableWidget.setHorizontalHeaderLabels(['Nro Tema','Descripcion Tema'])
        
#         # Probando lista
#         """lista_temas = []
#         for i in range(1,30):
#             reg=(str(i),"Tema "+str(i))
#             lista_temas.append(reg)
#         """

#         temas = TemasDAO()
#         lista_temas = temas.get_all_temas()
#         print(lista_temas)

#         self.__vista.tableWidget.setRowCount(len(lista_temas))
#         for linea, (id_tema, nombre_tema) in enumerate(lista_temas):  
#             self.__vista.tableWidget.setItem(linea, 0, QTableWidgetItem(str(id_tema)))  
#             self.__vista.tableWidget.setItem(linea, 1, QTableWidgetItem(nombre_tema))  

#     def __volver_configuracion(self):
#         self.MainWindow.hide()
#         self.__controlador_anterior.MainWindow.show()
        