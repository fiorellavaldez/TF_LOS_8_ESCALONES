from vista.VistaSeleccionarJugadores import Ui_MainWindow
from PyQt6 import QtWidgets,QtCore
from modelo.JugadoresABM import JugadorABM
from PyQt6.QtGui import QIcon,QPixmap
from controlador.ControladorVideo import ControladorVideo
from modelo.Jugador import Jugador

class ControladorVistaSeleccionarJugadores:
    def __init__(self, controlador_anterior, numero_jugador):
        self.__numero_jugador = numero_jugador
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__jugadores = JugadorABM()
        self.__lista_jugadores = self.__jugadores.obtener_jugadores()
        self.__vista.setupUi(self.MainWindow, self.__lista_jugadores)
        self.MainWindow.show()
        # Registrar la ventana en el controlador de audio y video
        ControladorVideo.registrar_ventana(self.MainWindow)
        
        with open("vista/estilos.qss") as f:
            self.MainWindow.setStyleSheet(f.read())
        
        self.__vista.get_button_aceptar().clicked.connect(self.__aceptar)
        self.__vista.get_button_cancelar().clicked.connect(self.__volver_seleccion_de_jugadores)
        self.__vista.tableWidget.doubleClicked.connect(self.__aceptar)
    
        self.filtrando_jugadores = self.__lista_jugadores.copy()

        # Configuración de búsqueda
        self.__vista.lineEdit.textChanged.connect(self.__buscar_jugador)
        
        #Llenado de la tabla
        self.__vista.update_table(self.filtrando_jugadores)
        
    def __aceptar (self):
        indice = self.__vista.tableWidget.currentRow()
        if indice < 0:
            self.__vista.aviso_seleccionar_jugador()  # Si no se seleccionó ninguna fila
        else:
            jugador_a_agregar = self.filtrando_jugadores[indice]
            if self.__controlador_anterior.chequeo_jugador(jugador_a_agregar.get_idjugador()) == True:
                self.__vista.aviso_repeticion_jugador(jugador_a_agregar.get_nombre_jugador())
            else:
                self.__controlador_anterior.add_jugador(self.filtrando_jugadores[indice], self.__numero_jugador) ### añade jugador
                self.MainWindow.close()
                self.__controlador_anterior.MainWindow.show()
        
    def __volver_seleccion_de_jugadores(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()
    
    def __buscar_jugador(self):
        """Filtra los jugadores según el texto ingresado en el cuadro de búsqueda."""
        texto = self.__vista.lineEdit.text().strip().lower()
        # Verificar que cada elemento sea un objeto de tipo Jugador
        if all(isinstance(jugador, Jugador) for jugador in self.__lista_jugadores):
            self.filtrando_jugadores = [
                jugador for jugador in self.__lista_jugadores
                if jugador.get_nombre_jugador().lower().startswith(texto)  # Filtrar por nombre
            ]
        else:
            # Si los elementos no son objetos Jugador, asignar lista vacía o manejar el error según sea necesario
            print("La lista de jugadores no contiene objetos de tipo Jugador.")
            self.filtrando_jugadores = []

        # Actualizar la tabla con los resultados filtrados
        self.__vista.update_table(self.filtrando_jugadores)