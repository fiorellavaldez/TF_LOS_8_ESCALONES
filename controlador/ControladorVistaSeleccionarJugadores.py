from vista.VistaSeleccionarJugadores import Ui_MainWindow
from PyQt6 import QtWidgets,QtCore
from modelo.JugadorDAO import JugadorDAO
from PyQt6.QtGui import QIcon,QPixmap
class ControladorVistaSeleccionarJugadores:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__jugadores = JugadorDAO()
        self.__lista_jugadores = self.__jugadores.get_all_jugadores()
        self.__vista.setupUi(self.MainWindow, self.__lista_jugadores)
        self.MainWindow.show()
        
        self.__vista.get_button_aceptar().clicked.connect(self.__aceptar)
        self.__vista.get_button_cancelar().clicked.connect(self.__volver_seleccion_de_jugadores)

        self.filtrando_jugadores = self.__lista_jugadores.copy()

        # Configuración de búsqueda
        self.__vista.lineEdit.textChanged.connect(self.__buscar_jugador)


    def __aceptar(self):
        fila = self.__vista.tableWidget().currentRow() #devuelve el nro fila tupla selecc
        if fila >= 0:
            nombre = self.__vista.tableWidget().item(fila, 0).text() #el nombre del jugador
            
            if any(jugador[1]==nombre for jugador in self.__controlador_anterior.get_lista()): 
                self.__vista.aviso_repeticion_jugador(nombre)
                return
            #busca el indice del jugador en la lista
            indice = next((i for i, tupla in enumerate(self.__lista_jugadores) if str(tupla[1]) == nombre), None) #busca el nombre del jugador en la lista de jugadores y devuelve el indice
            if indice is not None:
                self.__controlador_anterior.add_jugador(self.__lista_jugadores[indice]) #le mando la tupla a la lista de la grilla, la tupla contiene el id_jugador, nombre y avatar del jugador
                self.MainWindow.close()
                self.__controlador_anterior.MainWindow.show()
            else:
                print(f"No se encontró a ningún jugador con el nombre {nombre}.") #esto no debería pasar tho
        else:
            print("No hay ninguna fila seleccionada")
        
    def __volver_seleccion_de_jugadores(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()
        
        
    
    def __actualizar_tabla(self, jugadores):
        """Actualiza la tabla con los jugadores proporcionados."""
        self.__vista.tableWidget.setRowCount(len(jugadores))
        self.__vista.tableWidget.setColumnWidth(1,100)
        self.__vista.tableWidget.setIconSize(QtCore.QSize(64,64))
        
        for fila, (id_jugador,nombre_jugador, avatar_path) in enumerate(jugadores):
            item_nombre_jugador = QtWidgets.QTableWidgetItem(nombre_jugador)
            item_nombre_jugador.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            self.__vista.tableWidget.setItem(fila, 0, item_nombre_jugador)

            item_avatar = QtWidgets.QTableWidgetItem()  # Si es un texto o ruta
            pixmap = QPixmap(avatar_path).scaled(64,64)  # Cargar la imagen desde la ruta
            if not pixmap.isNull():  # Verificar que la imagen cargó correctamente
                icon = QIcon(pixmap.scaled(64, 64, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
                item_avatar.setIcon(icon)
            else:
                item_avatar.setText("Sin avatar")  # Texto alternativo si no se encuentra la imagen
        item_avatar.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.__vista.tableWidget.setItem(fila, 1, item_avatar)  # Segunda columna: Avatar (representación)

    def __buscar_jugador(self):
        """Filtra los jugadores según el texto ingresado en el cuadro de búsqueda."""
        texto = self.__vista.lineEdit.text().strip().lower()
        if texto:
            self.filtrando_jugadores = [
                (id_jugador,nombre_jugador ,avatar)
                for id_jugador, nombre_jugador,avatar in self.__lista_jugadores
                if texto in nombre_jugador.lower()
            ]
        else:
            self.filtrando_jugadores = self.__lista_jugadores
        self.__actualizar_tabla(self.filtrando_jugadores)
    '''
    def __obtener_jugador_seleccionado(self):
        """Obtiene el ID del tema seleccionado en la tabla."""
        fila_seleccionada = self.__vista.tableWidget.currentRow()
        if fila_seleccionada != -1:  # Si hay una fila seleccionada
            return self.filtered_temas[fila_seleccionada]  # Devuelve (id_tema, descripcion)
        return None
    '''
