from vista.VistaGrillaJugadores import Ui_MainWindow
from controlador.ControladorVistaSeleccionarJugadores import ControladorVistaSeleccionarJugadores
from controlador.ControladorVistaJugadorNuevo import ControladorVistaJugadorNuevo
from controlador.ControladorVistaJuego import ControladorVistaJuego
from PyQt6 import QtWidgets

class ControladorVistaGrillaJugadores:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__lista_jugadores = []
        self.__nro_seleccionado = None

        '''
        El ControladorVistaJuego llama a la clase de Escalon y con un Dao le trae los datos creo, entonces tiene una lista de jugadores. Esa lista de jugadores 
        debería enviarse desde este Controlador, acá voy a tener la lista final que le voy a pasar al Escalon que está en el siguiente controlador
        '''

        #Seleccion Jugador 1
        self.__vista.get_button_seleccionar_jugador1().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_seleccionar_jugador1().clicked.connect(lambda: self.___set_nro_seleccionado(self.__vista.get_nombre_jugador1()))
        self.__vista.get_button_jugador_nuevo1().clicked.connect(self.__jugador_nuevo)
        #Seleccion Jugador 2        
        self.__vista.get_button_seleccionar_jugador2().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_seleccionar_jugador2().clicked.connect(lambda: self.___set_nro_seleccionado(self.__vista.get_nombre_jugador2()))     
        self.__vista.get_button_jugador_nuevo2().clicked.connect(self.__jugador_nuevo)
        #Seleccion Jugador 3   
        self.__vista.get_button_seleccionar_jugador3().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_seleccionar_jugador3().clicked.connect(lambda: self.___set_nro_seleccionado(self.__vista.get_nombre_jugador3()))
        self.__vista.get_button_jugador_nuevo3().clicked.connect(self.__jugador_nuevo)
        #Seleccion Jugador 4
        self.__vista.get_button_seleccionar_jugador4().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_seleccionar_jugador4().clicked.connect(lambda: self.___set_nro_seleccionado(self.__vista.get_nombre_jugador4()))
        self.__vista.get_button_jugador_nuevo4().clicked.connect(self.__jugador_nuevo)
        #Seleccion Jugador 5
        self.__vista.get_button_seleccionar_jugador5().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_seleccionar_jugador5().clicked.connect(lambda: self.___set_nro_seleccionado(self.__vista.get_nombre_jugador5()))
        self.__vista.get_button_jugador_nuevo5().clicked.connect(self.__jugador_nuevo)
        #Seleccion Jugador 6
        self.__vista.get_button_seleccionar_jugador6().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_seleccionar_jugador6().clicked.connect(lambda: self.___set_nro_seleccionado(self.__vista.get_nombre_jugador6()))
        self.__vista.get_button_jugador_nuevo6().clicked.connect(self.__jugador_nuevo)
        #Seleccion Jugador 7
        self.__vista.get_button_seleccionar_jugador7().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_seleccionar_jugador7().clicked.connect(lambda: self.___set_nro_seleccionado(self.__vista.get_nombre_jugador7()))
        self.__vista.get_button_jugador_nuevo7().clicked.connect(self.__jugador_nuevo)
        #Seleccion Jugador 8
        self.__vista.get_button_seleccionar_jugador8().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_seleccionar_jugador8().clicked.connect(lambda: self.___set_nro_seleccionado(self.__vista.get_nombre_jugador8()))
        self.__vista.get_button_jugador_nuevo8().clicked.connect(self.__jugador_nuevo)
        #Seleccion Jugador 9
        self.__vista.get_button_seleccionar_jugador9().clicked.connect(self.__elegir_jugador)
        self.__vista.get_button_seleccionar_jugador9().clicked.connect(lambda: self.___set_nro_seleccionado(self.__vista.get_nombre_jugador9()))
        self.__vista.get_button_jugador_nuevo9().clicked.connect(self.__jugador_nuevo)

        #OTROS BOTONES
        self.__vista.get_button_iniciar_partida().clicked.connect(self.__iniciar_partida)
        self.__vista.get_button_atras().clicked.connect(self.__volver_menu)

    def __elegir_jugador(self):
        self.MainWindow.hide()
        self.controlador_elegir_jugador = ControladorVistaSeleccionarJugadores(self)

    def __jugador_nuevo(self):
        self.MainWindow.hide()
        self.controlador_jugador_nuevo= ControladorVistaJugadorNuevo(self)

    def __iniciar_partida(self):
        if len(self.__lista_jugadores) <9:
            self.__vista.aviso_iniciar_partida()
        else:
            self.MainWindow.hide()
            #acá usamos un método del siguiente controlador usando la referencia para setearle al escalon 1 la lista de jugadores 
            self.controlador_iniciar_partida = ControladorVistaJuego(self,self.__lista_jugadores) ###############################################################3

    def __volver_menu(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()

    def ___set_nro_seleccionado(self, label):
        self.__nro_seleccionado = label
        #asigno el label del jugador que haya usado el elegir_jugador para asignarle el nombre del jugador

    def add_jugador(self, jugador):
        self.__nro_seleccionado.setText(jugador[1])
        self.__lista_jugadores.append(jugador)
        print(f"Añadiste a jugador {jugador[1]}")
        self.__nro_seleccionado=None
        
    def get_lista(self):
        if len(self.__lista_jugadores) == 9: #9
            self.__vista.get_button_iniciar_partida().setEnabled(True)
            self.__nro_seleccionado = None
        return self.__lista_jugadores

    def get_jugadores(self):
        return self.__lista_jugadores