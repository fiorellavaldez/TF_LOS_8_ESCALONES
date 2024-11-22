from vista.VistaJugadorNuevo import Ui_MainWindow
from PyQt6 import QtWidgets
from modelo.Jugador import Jugador
#from modelo.JugadorDAO import JugadorDAO
from modelo.JugadoresABM import JugadorABM
import re
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
        self.__vista.get_button_agregar_jugador().clicked.connect(self.__crear_jugador) #<----aca decia ._bd despues de .__crear_jugador

        self.__vista.get_button_cancelar().clicked.connect(self.__volver_seleccion_de_jugadores)
        self.__vista.get_boton_deslizador_derecha().clicked.connect(self.__mostrar_siguiente_imagen)
        self.__vista.get_boton_deslizador_izquierda().clicked.connect(self.__mostrar_imagen_anterior)
        
    def __volver_seleccion_de_jugadores(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()
    

    def __crear_jugador(self):
        """
        Crea un nuevo jugador en la base de datos, verificando que el nombre no se repita
        y que el campo este lleno.
        """
        # Obtener el nombre del jugador desde la vista
        nombre_jugador = self.__vista.get_entrada_texto()

        # Validar si el campo de nombre está vacío
        if not nombre_jugador:
            self.__vista.imprimo_alerta()
            return
        
        # Validar que el nombre no contenga caracteres no deseados (si es necesario)
        if not re.match("^[A-Za-z0-9 ]*$", nombre_jugador):  # Permite letras, números y espacios
            self.__vista.imprimo_alerta()
            return
        
        
        jugador_bd = JugadorABM()
        
        # Consultar jugadores existentes en la base de datos
        if jugador_bd.existe_jugador(Jugador(nombre_jugador, None)):  # El avatar es opcional para la validación
            self.__vista.aviso_nombre_repetido(nombre_jugador)
            return

        avatar_elegido=self.imagen_actual
        if not avatar_elegido:  #puse porque tengo un avatara vacio, que es el verde
            self.__vista.aviso_seleccionar_avatar()
            return
        
        try:
            # Crear el nuevo jugador
            jugador_nuevo = Jugador(nombre=nombre_jugador, avatar=avatar_elegido)

            # Agregar a la base de datos
            jugador_bd.agregar_jugador(jugador_nuevo)  # aca tendria que ser agregar jugador

            # Notificar al usuario
            self.__vista.notifico_insercion(nombre_jugador)
            
            print(f"Jugador '{nombre_jugador}' agregado exitosamente.")
            
        except Exception as e:
            # Manejo de errores
            self.__vista.aviso_nombre_repetido(nombre_jugador)

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
