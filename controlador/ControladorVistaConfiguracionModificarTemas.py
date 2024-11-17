from vista.VistaConfiguracionModificarTema import Ui_MainWindow
from vista.VistaTemaNuevo import Ui_MainWindow
from vista.VistaEliminarTema import VistaEliminarTema
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt6.QtCore import Qt

from modelo.TemasDAO import TemasDAO

class ControladorVistaConfiguracionModificarTemas:
    def __init__(self, controlador_anterior, controlador_eliminar_tema, controlador_crear_tema, controlador_cambiar_tema):
        self.__controlador_eliminar_tema = controlador_eliminar_tema
        self.__controlador_crear_tema = controlador_crear_tema
        self.__controlador_cambiar_tema = controlador_cambiar_tema
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        # Configuración de botones
        self.__vista.get_button_atras().clicked.connect(self.__volver_configuracion)
        self.__vista.get_button_eliminar().clicked.connect(self.__eliminar_tema)
        self.__vista.get_button_cambiar().clicked.connect(self.__cambiar_tema)
        self.__vista.get_button_agregar().clicked.connect(self.__crear_tema)

        # Inicialización de la tabla
        self.__vista.tableWidget.setColumnCount(1)
        self.__vista.tableWidget.setColumnWidth(0, 180)
        self.__vista.tableWidget.setHorizontalHeaderLabels(['Descripción Tema'])

        # Configuración del DAO
        self.dao = TemasDAO()
        self.temas = self.dao.get_all_temas()
        self.filtered_temas = self.temas.copy()

        # Configuración de búsqueda
        self.__vista.lineEdit.textChanged.connect(self.__buscar_temas)

        # Cargar tabla y deshabilitar botones
        self.__actualizar_tabla(self.temas)
        self.__vista.get_button_eliminar().setEnabled(False)
        self.__vista.get_button_cambiar().setEnabled(False)

        # Conectar la selección de la tabla a la actualización de botones
        self.__vista.tableWidget.itemSelectionChanged.connect(self.__actualizar_botones)

    def __volver_configuracion(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __eliminar_tema(self):
        tema_seleccionado = self.__obtener_tema_seleccionado()
        if tema_seleccionado:
            self.MainWindow.hide()
            self.__controlador_eliminar_tema.set_tema(tema_seleccionado)
            self.__controlador_eliminar_tema.MainWindow.show()
        else:
            QMessageBox.warning(self.MainWindow, "Advertencia", "Debe seleccionar un tema para eliminar.")

    def __cambiar_tema(self):
        tema_seleccionado = self.__obtener_tema_seleccionado()
        if tema_seleccionado:
            self.MainWindow.hide()
            self.__controlador_cambiar_tema.set_tema(tema_seleccionado)
            self.__controlador_cambiar_tema.MainWindow.show()
        else:
            QMessageBox.warning(self.MainWindow, "Advertencia", "Debe seleccionar un tema para cambiar.")

    def __crear_tema(self):
        self.MainWindow.hide()
        self.__controlador_crear_tema.MainWindow.show()

    def __actualizar_tabla(self, temas):
        """Actualiza la tabla con los temas proporcionados."""
        self.__vista.tableWidget.setRowCount(len(temas))
        for fila, (id_tema, descripcion) in enumerate(temas):
            item_descripcion = QTableWidgetItem(descripcion)
            item_descripcion.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.__vista.tableWidget.setItem(fila, 0, item_descripcion)

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
            self.filtered_temas = self.temas
        self.__actualizar_tabla(self.filtered_temas)

    def __obtener_tema_seleccionado(self):
        """Obtiene el ID del tema seleccionado en la tabla."""
        fila_seleccionada = self.__vista.tableWidget.currentRow()
        if fila_seleccionada != -1:  # Si hay una fila seleccionada
            return self.filtered_temas[fila_seleccionada]  # Devuelve (id_tema, descripcion)
        return None

    def __actualizar_botones(self):
        """Habilita o deshabilita los botones según la selección en la tabla."""
        tema_seleccionado = self.__obtener_tema_seleccionado()
        habilitar = tema_seleccionado is not None
        self.__vista.get_button_eliminar().setEnabled(habilitar)
        self.__vista.get_button_cambiar().setEnabled(habilitar)


####################################################################

# from vista.VistaConfiguracionModificarTema import Ui_MainWindow
# from vista.VistaTemaNuevo import Ui_MainWindow
# from vista.VistaEliminarTema import Ui_MainWindow
# from PyQt6 import QtWidgets
# from PyQt6.QtWidgets import QTableWidgetItem
# from PyQt6.QtCore import Qt

# from modelo.TemasDAO import TemasDAO

# class ControladorVistaConfiguracionModificarTemas:
#     def __init__(self, controlador_anterior,contolador_eliminar_tema,controlador_crear_tema,controlador_cambiar_tema):
#         self.__controlador_eliminar_tema = contolador_eliminar_tema
#         self.__controlador_crear_tema = controlador_crear_tema
#         self.__controlador_cambiar_tema = controlador_cambiar_tema
#         self.__controlador_anterior = controlador_anterior
#         self.MainWindow = QtWidgets.QMainWindow()
#         self.__vista = Ui_MainWindow()
#         self.__vista.setupUi(self.MainWindow)
#         self.MainWindow.show()

#         # Configuración del botón "Atrás"
#         self.__vista.get_button_atras().clicked.connect(self.__volver_configuracion)

#         #configuracion del boton "Eliminar Tema"
#         self.__vista.get_button_eliminar().clicked.connect(self.__eliminar_tema)
        
#         #Configuracion del boton "Cambiar Nombre"
#         self.__vista.get_button_cambiar().clicked.connect(self.__cambiar_tema)
        
#         #Configuracion del boton "Crear nuevo tema"
#         self.__vista.get_button_agregar().clicked.connect(self.__crear_tema)
        
#         # Inicialización de la tabla
#         self.__vista.tableWidget.setColumnCount(1)  # Solo una columna para la descripción
#         self.__vista.tableWidget.setColumnWidth(0, 180)  # Ajuste del ancho de la columna
#         self.__vista.tableWidget.setHorizontalHeaderLabels(['Descripción Tema'])  # Título de la columna

#         # Configuración de DAO y temas
#         self.dao = TemasDAO()
#         self.temas = self.dao.get_all_temas()  # Inicializa con todos los temas
#         self.filtered_temas = self.temas.copy()  # Copia inicial para el filtrado

#         # Configuración de búsqueda
#         self.__vista.lineEdit.textChanged.connect(self.__buscar_temas)

#         # Cargar la tabla inicialmente
#         self.__actualizar_tabla(self.temas)

#     def __volver_configuracion(self):
#         self.MainWindow.hide()
#         self.__controlador_anterior.MainWindow.show()
        
#     def __eliminar_tema(self):
#         self.MainWindow.hide()
#         self.__controlador_eliminar_tema.MainWindow.show()
        
#     def crear_tema(self):
#         self.MainWindow.hide()
#         self.__controlador_crear_tema.MainWindow.show()
        


#     def __actualizar_tabla(self, temas):
#         """Actualiza la tabla con los temas proporcionados."""
#         self.__vista.tableWidget.setRowCount(len(temas))  # Establece el número de filas
#         for fila, (id_tema, descripcion) in enumerate(temas):
#             item_descripcion = QTableWidgetItem(descripcion)  # Coloca solo la descripción en la celda
#             item_descripcion.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # No editable
#             self.__vista.tableWidget.setItem(fila, 0, item_descripcion)  # Asigna a la primera columna

#     def __buscar_temas(self):
#         """Filtra los temas según el texto ingresado en el cuadro de búsqueda."""
#         texto = self.__vista.lineEdit.text().strip().lower()
#         if texto:
#             self.filtered_temas = [
#                 (id_tema, descripcion)
#                 for id_tema, descripcion in self.temas
#                 if texto in descripcion.lower()
#             ]
#         else:
#             self.filtered_temas = self.temas  # Si no hay texto, mostrar todos los temas
#         self.__actualizar_tabla(self.filtered_temas)



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
        