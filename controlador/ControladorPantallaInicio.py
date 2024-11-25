from controlador.ControladorAudioVideo import ControladorAudiovideo
from controlador.ControladorConfiguracion import ControladorVistaConfiguracion
from controlador.ControladorVistaGrillaJugadores import ControladorVistaGrillaJugadores
from vista.VistaPantallaInicio import Ui_MainWindow
from PyQt6 import QtWidgets
import os
import pygame


class ControladorPantallaInicio:

    def __init__(self):
        # Inicializa la ventana principal
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)

        # Registrar la ventana en el controlador de audio y video
        ControladorAudiovideo.registrar_ventana(self.MainWindow)

        # Iniciar la música sin abrir ventanas adicionales
        self.__inicializar_audio()
        self.MainWindow.show()

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

    def __inicializar_audio(self):
        """Inicializa el sistema de audio y configura la música."""
        self.music_on = True  # Inicialmente la música está encendida
        self.volume = 1.0  # Volumen inicial al máximo

        # Establecer la ruta relativa al archivo de música
        base_dir = os.path.dirname(__file__)
        self.music_file = os.path.join(base_dir, "../musica/menu_2.mp3")

        # Inicializar pygame y cargar la música
        pygame.mixer.init()
        self.__cargar_musica(self.music_file)

        # Reproducir música automáticamente al iniciar
        if self.music_on:
            pygame.mixer.music.play(-1)  # Reproducir música en bucle

    def __cargar_musica(self, archivo):
        """Carga y reproduce una nueva canción."""
        if os.path.exists(archivo):
            try:
                pygame.mixer.music.load(archivo)
                pygame.mixer.music.set_volume(self.volume)  # Ajustar volumen al actual
                if self.music_on:
                    pygame.mixer.music.play(-1)  # Reproducir música en bucle
            except pygame.error as e:
                print(f"Error al cargar la música: {str(e)}")
        else:
            print(f"Error: El archivo de música {archivo} no se encuentra en la ruta especificada.")

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

##########################################################################

# from controlador.ControladorAudioVideo import ControladorAudiovideo
# from controlador.ControladorConfiguracion import ControladorVistaConfiguracion
# from controlador.ControladorVistaGrillaJugadores import ControladorVistaGrillaJugadores
# from vista.VistaPantallaInicio import Ui_MainWindow
# from PyQt6 import QtWidgets
# import os
# import pygame


# class ControladorPantallaInicio:

#     def __init__(self):
#         self.MainWindow = QtWidgets.QMainWindow()
#         self.__vista = Ui_MainWindow()
#         self.__vista.setupUi(self.MainWindow)

        
#         # Registrar la ventana en el controlador de audio y video
#         ControladorAudiovideo.registrar_ventana(self.MainWindow)
        
#         # Iniciar la música sin abrir ventanas adicionales
#         self.__inicializar_audio()
#         self.MainWindow.show()


#         # Aplicar estilos
#         with open("vista/estilos.qss") as f:
#             self.MainWindow.setStyleSheet(f.read())
        
#         # Conectar botones a eventos
#         self.__vista.get_button_nueva_partida().clicked.connect(self.__nueva_partida)
#         self.__vista.get_button_configuracion().clicked.connect(self.__configuracion)
#         self.__vista.get_button_salir().clicked.connect(self.__salir)
    
#     # Garantiza que la música se inicie (Singleton)

#     def __cargar_musica(self, archivo):
#         """Carga y reproduce una nueva canción."""
#         if os.path.exists(archivo):
#             try:
#                 pygame.mixer.music.load(archivo)
#                 pygame.mixer.music.set_volume(self.volume)  # Ajustar volumen al actual
#                 if self.music_on:
#                     pygame.mixer.music.play(-1)  # Reproducir música en bucle
#             except pygame.error as e:
#                 print(f"Error al cargar la música: {str(e)}")
#         else:
#             print(f"El archivo de música {archivo} no se encuentra en la ruta especificada.")
    
    
#     def __inicializar_audio(self):
#         """Inicializa el sistema de audio y configura la música."""
#         self.music_on = True  # Inicialmente la música está encendida
#         self.volume = 1.0  # Volumen inicial al máximo
#         self.music_file = r"C:\Users\Usuario\Documents\GitHub\TF_LOS_8_ESCALONES\musica\menu_2.mp3"  # Ruta del archivo de música

#         #Inicializar pygame y cargar la música
#         pygame.mixer.init()
#         self.__cargar_musica(self.music_file)

#         # Reproducir música automáticamente al iniciar
#         if self.music_on:
#             pygame.mixer.music.play(-1)  # Reproducir música en bucle
    
    
#     def __nueva_partida(self):
#         self.MainWindow.close()
#         self.controlador_nueva_partida = ControladorVistaGrillaJugadores(self)

#     def __configuracion(self):
#         self.MainWindow.hide()
#         self.controlador_configuracion = ControladorVistaConfiguracion(self)
    
#     def __salir(self):
#         self.MainWindow.close()


###################################################################################################

# from controlador.ControladorConfiguracion import ControladorVistaConfiguracion
# from controlador.ControladorVistaGrillaJugadores import ControladorVistaGrillaJugadores
# from vista.VistaPantallaInicio import Ui_MainWindow
# from controlador.ControladorAudioVideo import ControladorAudiovideo
# from PyQt6 import QtWidgets

# class ControladorPantallaInicio:

#     def __init__(self):
#         self.MainWindow = QtWidgets.QMainWindow()
#         self.__vista = Ui_MainWindow()
#         self.__vista.setupUi(self.MainWindow)
        
#         # Registrar la ventana en el controlador de audio y video
#         ControladorAudiovideo.registrar_ventana(self.MainWindow)
#         self.MainWindow.show()


        
#         with open("vista/estilos.qss") as f:
#             self.MainWindow.setStyleSheet(f.read())
        
#         self.__vista.get_button_nueva_partida().clicked.connect(self.__nueva_partida)
#         #self.__vista.get_button_continuar().clicked.connect(self.__continuar)
#         self.__vista.get_button_configuracion().clicked.connect(self.__configuracion) #Clickear el boton (Es un evento) ?
#         self.__vista.get_button_salir().clicked.connect(self.__salir)
        
    
#     def ajustar_volumen_musica(self, volumen):
#         # Cambiar el volumen de la música
#         ControladorAudiovideo.ajustar_volumen(volumen)

#     def detener_musica(self):
#         # Detener música desde este controlador
#         if ControladorAudiovideo().music_on:
#             ControladorAudiovideo.alternar_musica()
#         # Registrar la ventana en el controlador de audio y video
#         ControladorAudiovideo.registrar_ventana(self.MainWindow)
        
#     def __nueva_partida(self):
#         self.MainWindow.close()
#         self.controlador_nueva_partida=ControladorVistaGrillaJugadores(self)

#     def __configuracion(self):
#         self.MainWindow.hide()
#         self.controlador_configuracion = ControladorVistaConfiguracion(self)
    
#     def __salir(self):
#         self.MainWindow.close() #si es la última ventana abierta y hacemos .close(), se cierra el programa y termina la ejecución del bucle de Qt (que está en el main)