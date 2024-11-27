from vista.VistaJugadorNuevo import Ui_MainWindow
from PyQt6 import QtWidgets
from modelo.Jugador import Jugador
from modelo.JugadoresABM import JugadorABM
import re
import os

class ControladorVistaModificarJugadorABM:

    def __init__(self, controlador_anterior, jugador):
        self.__controlador_anterior = controlador_anterior
        self.__jugador = jugador
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        #Aplicar estilos
        self.__aplicar_estilos()

        # Corregir lista de imágenes (faltaban comas entre algunas cadenas)
        self.lista_imagenes = [
            "vista/img/fa.jpg", "vista/img/al.jpg", "vista/img/jarr.jpg",
            "vista/img/ka.jpg", "vista/img/avatar_azul.png", "vista/img/ta.png", "vista/img/da.jpg",
            "vista/img/fi.jpg", "vista/img/edna.jpg", "vista/img/aladdin.jpeg", "vista/img/amore.jpg",
            "vista/img/avatar.png", "vista/img/caradepapa.jpeg", "vista/img/daria.jpg", "vista/img/dory.jpeg",
            "vista/img/eugene.jpeg", "vista/img/gohan.jpeg", "vista/img/goku.jpeg",
            "vista/img/kevin.jpg", "vista/img/merida.jpeg", "vista/img/moana.jpeg", "vista/img/mulan.jpeg",
            "vista/img/tiana.jpeg"
        ]

        # Inicializar imagen_actual y jugador
        self.imagen_actual = self.lista_imagenes[0]  # Inicializa con la primera imagen (puedes cambiar esto según necesites)
        self.__imagen_jugador = self.__jugador.get_avatar()
        self.__nombre_jugador = self.__jugador.get_nombre_jugador()  
        
        # Asignar imagen y texto en la vista
        self.__vista.set_label_img(self.__imagen_jugador)
        self.__vista.lineEdit.setText(self.__nombre_jugador)

        # Botones y conexiones
        self.__vista.get_button_agregar_jugador().clicked.connect(self.__actualizar_jugador)
        self.__vista.get_button_cancelar().clicked.connect(self.__volver_seleccion_de_jugadores)
        self.__vista.get_boton_deslizador_derecha().clicked.connect(self.__mostrar_siguiente_imagen)
        self.__vista.get_boton_deslizador_izquierda().clicked.connect(self.__mostrar_imagen_anterior)

    def __aplicar_estilos(self):
        estilos_path = os.path.join(os.path.dirname(__file__),"../vista/estilos.qss")
        if os.path.exists(estilos_path):
            with open(estilos_path, "r") as f:
                self.MainWindow.setStyleSheet(f.read())
        else:
            print(f"Advertencia: No se encontró el archivo de estilos en {estilos_path}.")

    def __volver_seleccion_de_jugadores(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()

    def __actualizar_jugador(self):
        """
        Actualiza los datos del jugador en la base de datos, verificando que el nombre no se repita
        y que el campo esté lleno.
        """
        # Obtener el nombre del jugador desde la vista
        nombre_jugador = self.__vista.lineEdit.text()  # Obtener texto del QLineEdit

        # Validar si el campo de nombre está vacío
        if not nombre_jugador:
            self.__vista.imprimo_alerta()
            return

        # Validar que el nombre no contenga caracteres no deseados (si es necesario)
        if not re.match("^[A-Za-z0-9 ]*$", nombre_jugador):  # Permite letras, números y espacios
            self.__vista.imprimo_alerta()
            return

        jugador_bd = JugadorABM()

        try:
            # Actualizar el jugador con el nuevo nombre y avatar
            self.__jugador.set_nombre(nombre_jugador)
            self.__jugador.set_avatar(self.__imagen_jugador)

            # Actualizar en la base de datos
            jugador_bd.actualizar_jugador(self.__jugador)  # Actualiza el jugador

            # Notificar al usuario si es necesario
            self.__controlador_anterior.actualizar_tabla()

            # Cerrar la ventana actual y regresar a la anterior
            self.MainWindow.close()
            self.__controlador_anterior.MainWindow.show()

        except Exception as e:
            # Manejo de errores
            print(f"Error al actualizar jugador: {e}")
            self.__vista.aviso_nombre_repetido(nombre_jugador)

    def __mostrar_siguiente_imagen(self):
        if len(self.lista_imagenes) > 0:
            i = self.lista_imagenes.index(self.__imagen_jugador)
            i = (i + 1) % len(self.lista_imagenes)
            self.__vista.set_label_img(self.lista_imagenes[i])
            self.__imagen_jugador = self.lista_imagenes[i]

    def __mostrar_imagen_anterior(self):
        if len(self.lista_imagenes) > 0:
            i = self.lista_imagenes.index(self.__imagen_jugador)
            i = (i - 1) % len(self.lista_imagenes)
            self.__vista.set_label_img(self.lista_imagenes[i])
            self.__imagen_jugador = self.lista_imagenes[i]
