from vista.VistaGrillaJugadores import Ui_MainWindow
from controlador.ControladorVistaSeleccionarJugadores import ControladorVistaSeleccionarJugadores
from controlador.ControladorVistaJugadorNuevo import ControladorVistaJugadorNuevo
from controlador.ControladorVistaJuego import ControladorVistaJuego
from controlador.ControladorVideo import ControladorVideo
from modelo.Jugador import Jugador
from functools import partial
from PyQt6 import QtWidgets

class ControladorVistaGrillaJugadores:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        # Registrar la ventana en el controlador de audio y video
        ControladorVideo.registrar_ventana(self.MainWindow)
        
        with open("vista/estilos.qss") as f:
            self.MainWindow.setStyleSheet(f.read())

        self.__lista_jugadores = ["","","","","","","","",""]
        self.__nro_seleccionado = None

        '''
        El ControladorVistaJuego llama a la clase de Escalon y con un Dao le trae los datos creo, entonces tiene una lista de jugadores. Esa lista de jugadores 
        debería enviarse desde este Controlador, acá voy a tener la lista final que le voy a pasar al Escalon que está en el siguiente controlador
        '''

        #Seleccion Jugador 1
        self.__vista.get_button_seleccionar_jugador1().clicked.connect(partial(self.__elegir_jugador, 0))
        #Seleccion Jugador 2        
        self.__vista.get_button_seleccionar_jugador2().clicked.connect(partial(self.__elegir_jugador, 1))   
        #Seleccion Jugador 3   
        self.__vista.get_button_seleccionar_jugador3().clicked.connect(partial(self.__elegir_jugador, 2))
        #Seleccion Jugador 4
        self.__vista.get_button_seleccionar_jugador4().clicked.connect(partial(self.__elegir_jugador, 3))
        #Seleccion Jugador 5
        self.__vista.get_button_seleccionar_jugador5().clicked.connect(partial(self.__elegir_jugador, 4))
        #Seleccion Jugador 6
        self.__vista.get_button_seleccionar_jugador6().clicked.connect(partial(self.__elegir_jugador, 5))
        #Seleccion Jugador 7
        self.__vista.get_button_seleccionar_jugador7().clicked.connect(partial(self.__elegir_jugador, 6))
        #Seleccion Jugador 8
        self.__vista.get_button_seleccionar_jugador8().clicked.connect(partial(self.__elegir_jugador, 7))
        #Seleccion Jugador 9
        self.__vista.get_button_seleccionar_jugador9().clicked.connect(partial(self.__elegir_jugador, 8))

        #OTROS BOTONES
        self.__vista.get_button_iniciar_partida().clicked.connect(self.__iniciar_partida)
        self.__vista.get_button_atras().clicked.connect(self.__volver_menu)
        self.__vista.get_button_jugador_nuevo().clicked.connect(self.__jugador_nuevo) #######

    def __elegir_jugador(self, numero_jugador):
        self.MainWindow.hide()
        self.controlador_elegir_jugador = ControladorVistaSeleccionarJugadores(self, numero_jugador)

    def __jugador_nuevo(self):
        #self.MainWindow.hide()
        self.controlador_jugador_nuevo= ControladorVistaJugadorNuevo(self)

    def __iniciar_partida(self):
        if all(isinstance(elemento, Jugador) for elemento in self.__lista_jugadores): #evalua si todos los elementos de la lista son jugadores
            self.MainWindow.hide()
            self.controlador_iniciar_partida = ControladorVistaJuego(self,self.__lista_jugadores)
        else:
            self.__vista.aviso_iniciar_partida()
        
    def __volver_menu(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()

    def ___set_nro_seleccionado(self, label):
        self.__nro_seleccionado = label
        #asigno el label del jugador que haya usado el elegir_jugador para asignarle el nombre del jugador

    def add_jugador(self, jugador, numero_jugador):
        self.__lista_jugadores[numero_jugador] = jugador
        metodo_cambiar_nombre = getattr(self.__vista, f"cambiar_nombre_jugador{numero_jugador}") #arma el metodo que voy a usar de la vista
        metodo_cambiar_nombre(jugador.get_nombre_jugador())
    
    def chequeo_jugador(self, id_jugador): #chequea si el jugador por el que se consulta ya está en la lista de jugadores
        for i in self.__lista_jugadores: # hay que hacer que si no es un elelemto jugador no le haga el get id
            if isinstance(i, Jugador):
                if id_jugador == i.get_idjugador():
                    return True
        return False
    
    def get_lista(self):
        if len(self.__lista_jugadores) == 9:
            self.__vista.get_button_iniciar_partida().setEnabled(True)
            self.__nro_seleccionado = None
        return self.__lista_jugadores

    def get_jugadores(self):
        return self.__lista_jugadores