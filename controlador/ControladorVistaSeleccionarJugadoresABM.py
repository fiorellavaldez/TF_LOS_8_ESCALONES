from vista.VistaSeleccionarJugadoresABM import Ui_MainWindow
from controlador.ControladorVistaJugadorNuevoABM import ControladorVistaJugadorNuevoABM
from PyQt6 import QtWidgets,QtCore
from modelo.JugadoresABM import JugadorABM
from modelo.Jugador import Jugador
from PyQt6.QtGui import QIcon,QPixmap
from controlador.ControladorAudioVideo import ControladorAudiovideo

class ControladorVistaSeleccionarJugadores:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__lista_jugadores = JugadorABM().obtener_jugadores() #armo la lista con todos los jugadores
        #self.__lista_jugadores_filtrados = [] ###quizas sea necesario para la barra de busqueda
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        # Registrar la ventana en el controlador de audio y video
        ControladorAudiovideo.registrar_ventana(self.MainWindow)
        with open("vista/estilos.qss") as f:
            self.MainWindow.setStyleSheet(f.read())
        
        self.__vista.get_button_cancelar().clicked.connect(self.__volver)
        self.__vista.get_button_nuevo().clicked.connect(self.__nuevo)
        self.__vista.get_button_modificar().clicked.connect(self.__modificar)
        self.__vista.get_button_eliminar().clicked.connect(self.__eliminar)

        self.filtrando_jugadores = self.__lista_jugadores.copy()

        # Configuración de búsqueda
        self.__vista.lineEdit.textChanged.connect(self.__buscar_jugador)
        
        #Llenado de la tabla
        self.__vista.update_table(self.filtrando_jugadores)
    
    def __nuevo(self):
        self.controlador_jugador_nuevo= ControladorVistaJugadorNuevoABM(self)
    
    def __modificar (self):
        pass
    
    def __eliminar (self):
        pass
    
    def __volver(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()
        
    def actualizar_tabla(self):
        jugadores = JugadorABM().obtener_jugadores()
        self.__vista.update_table(jugadores)
            
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

    
