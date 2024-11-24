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
        with open("vista/estilos.qss") as f:
            self.MainWindow.setStyleSheet(f.read())
        
        self.__vista.get_button_aceptar().clicked.connect(self.__aceptar)
        self.__vista.get_button_cancelar().clicked.connect(self.__volver_seleccion_de_jugadores)

        self.filtrando_jugadores = self.__lista_jugadores.copy()

        # Configuración de búsqueda
        self.__vista.lineEdit.textChanged.connect(self.__buscar_jugador)


    def __aceptar(self):
        fila = self.__vista.tableWidget.currentRow() #devuelve el nro fila tupla selecc
        if fila >= 0:
            nombre = self.__vista.tableWidget.item(fila, 0).text() #el nombre del jugador
            
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
        self.__vista.tableWidget.clearContents()
        self.__vista.tableWidget.setRowCount(len(jugadores))

        self.__vista.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        
        for fila, (id_jugador,nombre_jugador, avatar_path) in enumerate(jugadores):
            item_nombre_jugador = QtWidgets.QTableWidgetItem(nombre_jugador)
            item_nombre_jugador.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            item_nombre_jugador.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.__vista.tableWidget.setItem(fila, 0, item_nombre_jugador)
            self.__vista.tableWidget.setRowHeight(fila, 60)
        # Columna 1: Avatar (centrado usando QLabel)
            label_avatar = QtWidgets.QLabel()
            pixmap = QPixmap(avatar_path).scaled(64, 64, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
            if not pixmap.isNull():
                label_avatar.setPixmap(pixmap)  # Establecer la imagen
            else:
                label_avatar.setText("Sin avatar")  # Texto alternativo
                label_avatar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            label_avatar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

            self.__vista.tableWidget.setCellWidget(fila, 1, label_avatar)
            
    def __buscar_jugador(self):
        """Filtra los jugadores según el texto ingresado en el cuadro de búsqueda."""
        texto = self.__vista.lineEdit.text().strip().lower()
        if texto:
            self.filtrando_jugadores = [
                (id_jugador,nombre_jugador ,avatar)
                for id_jugador, nombre_jugador,avatar in self.__lista_jugadores
                if nombre_jugador.lower().startswith(texto)
            ]
        else:
            self.filtrando_jugadores = self.__lista_jugadores
        self.__actualizar_tabla(self.filtrando_jugadores)
    
    
