from vista.VistaSeleccionDeJugadores import Ui_MainWindow
from controlador.ControladorVistaSeleccionarJugadores import ControladorVistaSeleccionarJugadores
from controlador.ControladorVistaJugadorNuevo import ControladorVistaJugadorNuevo
from controlador.ControladorVistaJuego import ControladorVistaJuego
from PyQt6 import QtWidgets

class ControladorVistaSeleccionDeJugadores:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__vista.get_button_seleccionar_jugador1().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_jugador_nuevo1().clicked.connect(self.__jugador_nuevo)
        self.__vista.get_button_seleccionar_jugador2().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_jugador_nuevo2().clicked.connect(self.__jugador_nuevo)
        self.__vista.get_button_seleccionar_jugador3().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_jugador_nuevo3().clicked.connect(self.__jugador_nuevo)
        self.__vista.get_button_seleccionar_jugador4().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_jugador_nuevo4().clicked.connect(self.__jugador_nuevo)
        self.__vista.get_button_seleccionar_jugador5().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_jugador_nuevo5().clicked.connect(self.__jugador_nuevo)
        self.__vista.get_button_seleccionar_jugador6().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_jugador_nuevo6().clicked.connect(self.__jugador_nuevo)
        self.__vista.get_button_seleccionar_jugador7().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_jugador_nuevo7().clicked.connect(self.__jugador_nuevo)
        self.__vista.get_button_seleccionar_jugador8().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_jugador_nuevo8().clicked.connect(self.__jugador_nuevo)
        self.__vista.get_button_seleccionar_jugador9().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_jugador_nuevo9().clicked.connect(self.__jugador_nuevo)

        self.__vista.get_button_iniciar_partida().clicked.connect(self.__iniciar_partida)
        self.__vista.get_button_atras().clicked.connect(self.__volver_menu)

    def __elegir_jugador(self):
        self.MainWindow.hide()
        self.controlador_elegir_jugador = ControladorVistaSeleccionarJugadores(self)

    def __jugador_nuevo(self):
        self.MainWindow.hide()
        self.controlador_jugador_nuevo= ControladorVistaJugadorNuevo(self)

    def __iniciar_partida(self):
        self.MainWindow.hide()
        self.controlador_iniciar_partida = ControladorVistaJuego(self)

    def __volver_menu(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()  # Muestra la ventana anterior
        #hide() permite volver a abrir la misma ventana (.show()) sin perder su estado o tener que volver a inicializarla
        #close() cierra la ventana y destruye el objeto asociado, no se le puede hacer .show(), usar cuando ya no se necesita la ventana y se quiere liberar recursos
        
    