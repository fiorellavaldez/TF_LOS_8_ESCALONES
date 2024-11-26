from controlador.ControladorVideo import ControladorVideo
from controlador.ControladorConfiguracion import ControladorVistaConfiguracion
from controlador.ControladorVistaGrillaJugadores import ControladorVistaGrillaJugadores
from vista.VistaPantallaInicio import Ui_MainWindow
from controlador.Sonido import Sonido
from PyQt6 import QtWidgets
import os
import pygame


class ControladorPantallaInicio:

    def __init__(self):
        # Inicializa la ventana principal
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        # Registrar la ventana en el controlador de audio y video
        ControladorVideo.registrar_ventana(self.MainWindow)

        # Iniciar la música sin abrir ventanas adicionales
        
        # Configurar la música
        self.__sonido = Sonido(r"musica\menu_2.mp3")
        #self.__sonido = Sonido(r"C:\Users\Usuario\Documents\GitHub\TF_LOS_8_ESCALONES\musica\menu_2.mp3")
        if not pygame.mixer.get_init():
            pygame.mixer.init()  # Asegúrate de inicializar pygame.mixer
        if not pygame.mixer.music.get_busy():
            self.__sonido.toggle_music()  
        

        # Aplicar estilos desde un archivo relativo
        self.__aplicar_estilos()

        # Conectar botones a eventos
        self.__vista.get_button_nueva_partida().clicked.connect(self.__nueva_partida)
        self.__vista.get_button_configuracion().clicked.connect(self.__configuracion)
        self.__vista.get_button_salir().clicked.connect(self.__salir)

    def __aplicar_estilos(self):
        """Aplica los estilos desde un archivo QSS en el directorio del proyecto."""
        estilos_path = os.path.join(os.path.dirname(__file__), "../vista/estilos.qss")
        if os.path.exists(estilos_path):
            with open(estilos_path, "r") as f:
                self.MainWindow.setStyleSheet(f.read())
        else:
            print(f"Advertencia: No se encontró el archivo de estilos en {estilos_path}.")

    def __nueva_partida(self):
        """Inicia una nueva partida."""
        self.MainWindow.close()
        self.controlador_nueva_partida = ControladorVistaGrillaJugadores(self)

    def __configuracion(self):
        """Abre la configuración."""
        self.MainWindow.hide()
        self.controlador_configuracion = ControladorVistaConfiguracion(self)

    def __salir(self):
        """Cierra la aplicación."""
        self.MainWindow.close()