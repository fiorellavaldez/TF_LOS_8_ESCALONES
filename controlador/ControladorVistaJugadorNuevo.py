from vista.VistaJugadorNuevo import Ui_MainWindow
from PyQt6 import QtWidgets
from modelo.Jugador import Jugador
from modelo.JugadorDAO import JugadorDAO
#from Modelo.Jugador import Jugador

class ControladorVistaJugadorNuevo:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.lista_imagenes = ["vista/img/fa.jpg","vista/img/al.jpg","vista/img/jarr.jpg",
        "vista/img/ka.jpg","vista/img/avatar_azul.png","vista/img/ta.png", "vista/img/da.jpg",
        "vista/img/fi.jpg", "vista/img/edna.jpg","vista/img/aladdin.jpeg","vista/img/amore.jpg",
        "vista/img/avatar.png","vista/img/caradepapa.jpeg","vista/img/daria.jpg","vista/img/dory.jpeg",
        "vista/img/eugene.jpeg","vista/img/gohan.jpeg","vista/img/goku.jpeg""vista/img/jasmin.jpeg",
        "vista/img/kevin.jpg""vista/img/merida.jpeg","vista/img/moana.jpeg","vista/img/mulan.jpeg",
        "vista/img/tiana.jpeg"]
        
        self.imagen_actual = self.lista_imagenes[0]
        self.__vista.set_label_img(self.imagen_actual)

        #Este es el boton que estoy modificando:
        self.__vista.get_button_agregar_jugador().clicked.connect(self.__agregar_jugador_bd_)

        self.__vista.get_button_cancelar().clicked.connect(self.__volver_seleccion_de_jugadores)
        self.__vista.get_boton_deslizador_derecha().clicked.connect(self.__mostrar_siguiente_imagen)
        self.__vista.get_boton_deslizador_izquierda().clicked.connect(self.__mostrar_imagen_anterior)
        
    def __volver_seleccion_de_jugadores(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()
    

    def __crear_jugador(self):
        nombre_jugador = self.__vista.get_entrada_texto()
        
        jugador_dao = JugadorDAO()
        obtengo = jugador_dao.get_all_jugadores #me trae todos los jugadores 
        
        if any(jugador_dao[1]==nombre_jugador):
            self.__vista.aviso_nombre_repetido(nombre_jugador)
            return 
        
        
        # try:
        #     nombre_jugador = self.__vista.get_entrada_texto()
            
        #     if not nombre_jugador:
        #         raise ValueError("El nombre del jugador esta vacio")
        #     else:
        #         jugador_nuevo = Jugador()
        #         #comparo el nomnbre
        #         #jugador_nuevo.agrego_jugador(nombre_jugador)
        #         #Aca agrego a jugadorDAO
        #         self.__vista.notifico_insercion(nombre_jugador)
        #         self.MainWindow.close()
        # except:
        #         self.__vista.aviso_nombre_repetido()


    def __mostrar_siguiente_imagen(self):
        if len(self.imagen_actual) > 0:
            i = self.lista_imagenes.index(self.imagen_actual)
            i = (i + 1) % len(self.lista_imagenes)
            self.__vista.set_label_img(self.lista_imagenes[i])
            self.imagen_actual = self.lista_imagenes[i]

    def __mostrar_imagen_anterior(self):
        if len(self.lista_imagenes) > 0:
            i = self.lista_imagenes.index(self.imagen_actual)
            i = (i - 1) % len(self.lista_imagenes)
            self.__vista.set_label_img(self.lista_imagenes[i])
            self.imagen_actual = self.lista_imagenes[i]
