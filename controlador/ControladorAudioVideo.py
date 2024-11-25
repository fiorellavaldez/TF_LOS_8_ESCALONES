from vista.VistaAudioVideo import Ui_ConfigWindow
from PyQt6.QtWidgets import QMainWindow
from controlador.ControladorAudio import ControladorAudio
from controlador.ControladorVideo import ControladorVideo
class ControladorAudioVideo:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior

        # Inicializar la ventana principal como instancia de QMainWindow
        self.MainWindow = QMainWindow()

        # Configurar la vista en la ventana principal
        self.__vista = Ui_ConfigWindow()
        self.__vista.setupUi(self.MainWindow)

        # Inicializar controladores secundarios
        self.controlador_audio = ControladorAudio(self.__vista)  # Pasar la vista
        self.controlador_video = ControladorVideo(self.MainWindow, self.__vista)  # Pasar ventana y vista

        # Conectar el botón "Atrás" a su función
        self.__vista.get_back_button().clicked.connect(self.__volver_atras)

    def __volver_atras(self):
        """Vuelve a la ventana anterior."""
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()


##___________________________-----------------------------------------------------

# from vista.VistaAudioVideo import Ui_ConfigWindow
# from PyQt6.QtWidgets import QMainWindow
# from PyQt6.QtGui import QScreen
# from controlador.Sonido import Sonido
# import os


# class ControladorAudiovideo:
#     """Controlador para la configuración de audio y video."""

#     # Variables de clase para manejar el estado global
#     is_fullscreen = True
#     ventanas_registradas = []
#     music_on = True  # Estado global de la música, por defecto encendida
#     __instancia_unica = None  # Singleton para manejar la música

#     def __new__(cls, *args, **kwargs):
#         """Implementación del patrón Singleton."""
#         if not cls.__instancia_unica:
#             cls.__instancia_unica = super().__new__(cls)
#         return cls.__instancia_unica

#     def __init__(self, controlador_anterior):
#         if not hasattr(self, "MainWindow"):  # Evitar re-ejecutar la inicialización
#             self.__controlador_anterior = controlador_anterior
#             self.MainWindow = QMainWindow()  # Nueva ventana para la configuración
#             self.__vista = Ui_ConfigWindow()
#             self.__vista.setupUi(self.MainWindow)

#             # Instanciar la clase Sonido
#             self.sonido = Sonido(
#                 r"C:\Users\Usuario\Documents\GitHub\TF_LOS_8_ESCALONES\musica\menu_2.mp3"
#             )

#             # Registrar esta ventana en la lista de ventanas
#             self.registrar_ventana(self.MainWindow)

#             # Conectar señales a funciones
#             self.__vista.get_music_button().clicked.connect(self.__apagar_encender_musica)
#             self.__vista.get_volume_slider().valueChanged.connect(self.__cambio_volumen)
#             self.__vista.get_screen_button().clicked.connect(self.__alternar_pantalla_completa)
#             self.__vista.get_back_button().clicked.connect(self.__volver_atras)

#             # Establecer el estado de la música globalmente
#             if not ControladorAudiovideo.music_on:
#                 self.sonido.toggle_music()

#     @classmethod
#     def centrar_ventana(cls, ventana):
#         """Centra la ventana en la pantalla principal."""
#         screen = QScreen.availableGeometry(ventana.screen())
#         window_size = ventana.size()
#         x = (screen.width() - window_size.width()) // 2
#         y = (screen.height() - window_size.height()) // 2
#         ventana.move(x, y)

#     @classmethod
#     def registrar_ventana(cls, ventana):
#         """Registra una ventana para sincronizar el estado de pantalla completa."""
#         if ventana not in cls.ventanas_registradas:
#             cls.ventanas_registradas.append(ventana)
#             # Aplica el estado actual a la ventana registrada
#             if cls.is_fullscreen:
#                 ventana.showFullScreen()
#             else:
#                 ventana.showNormal()
#                 cls.centrar_ventana(ventana)

#     @classmethod
#     def aplicar_pantalla_completa(cls):
#         """Aplica el estado de pantalla completa a todas las ventanas registradas."""
#         for ventana in cls.ventanas_registradas:
#             if cls.is_fullscreen:
#                 ventana.showFullScreen()
#             else:
#                 ventana.showNormal()
#                 cls.centrar_ventana(ventana)

#     def __apagar_encender_musica(self):
#         """Alterna entre encender y apagar la música globalmente."""
#         ControladorAudiovideo.music_on = not ControladorAudiovideo.music_on
#         if ControladorAudiovideo.music_on:
#             self.sonido.toggle_music()  # Enciende la música
#             self.__vista.get_music_button().setText("Apagar Música")
#         else:
#             self.sonido.toggle_music()  # Apaga la música
#             self.__vista.get_music_button().setText("Encender Música")

#     def __cambio_volumen(self, value):
#         """Cambia el volumen de la música."""
#         self.sonido.set_volume(value / 100)  # Convertir a rango 0.0-1.0

#     def __alternar_pantalla_completa(self):
#         """Alterna entre pantalla completa y modo ventana normal."""
#         # Cambiar el estado global
#         ControladorAudiovideo.is_fullscreen = not ControladorAudiovideo.is_fullscreen
#         # Aplicar el nuevo estado a todas las ventanas registradas
#         ControladorAudiovideo.aplicar_pantalla_completa()

#         # Cambiar el texto del botón en la ventana actual
#         if ControladorAudiovideo.is_fullscreen:
#             self.__vista.get_screen_button().setText("Modo Ventana")
#         else:
#             self.__vista.get_screen_button().setText("Pantalla Completa")

#     def __volver_atras(self):
#         """Vuelve a la ventana anterior."""
#         self.MainWindow.hide()
#         self.__controlador_anterior.MainWindow.show()

####################################################_____________________________--------------------
############------------------------------------------------------



# from vista.VistaAudioVideo import Ui_ConfigWindow
# from PyQt6.QtWidgets import QMainWindow
# import pygame
# import os

# class ControladorAudiovideo:
#     """Controlador para la configuración de audio y video."""

#     # Variable de clase para el estado de pantalla completa
#     is_fullscreen = True
#     ventanas_registradas = []

#     def __init__(self, controlador_anterior):
#         self.__controlador_anterior = controlador_anterior
#         self.MainWindow = QMainWindow()  # Nueva ventana para la configuración
#         self.__vista = Ui_ConfigWindow()
#         self.__vista.setupUi(self.MainWindow)

#         # Registrar esta ventana en la lista de ventanas
#         self.registrar_ventana(self.MainWindow)

#         self.music_on = True  # Inicialmente la música está encendida
#         self.volume = 1.0  # Volumen inicial al máximo
#         self.music_file = r"C:\Users\Usuario\Documents\GitHub\TF_LOS_8_ESCALONES\musica\menu.mp3"  # Ruta del archivo de música

#         # Inicializar pygame y cargar la música
#         pygame.mixer.init()
#         if os.path.exists(self.music_file):
#             try:
#                 pygame.mixer.music.load(self.music_file)
#                 pygame.mixer.music.set_volume(self.volume)  # Ajustar volumen inicial al máximo
#                 pygame.mixer.music.play(-1)  # Reproducir música en bucle automáticamente
#             except pygame.error as e:
#                 print(f"Error al cargar la música: {str(e)}")
#         else:
#             print("El archivo de música no se encuentra en la ruta especificada.")

#         # Configurar el control deslizante de volumen al máximo
#         self.__vista.get_volume_slider().setValue(100)  # Establece el slider en 100 (máximo)

#         # Cambiar el texto del botón de música para reflejar el estado inicial
#         self.__vista.get_music_button().setText("Apagar Música")

#         # Conectar señales a funciones
#         self.__vista.get_music_button().clicked.connect(self.__apagar_encender_musica)
#         self.__vista.get_volume_slider().valueChanged.connect(self.__cambio_volumen)
#         self.__vista.get_screen_button().clicked.connect(self.__alternar_pantalla_completa)
#         self.__vista.get_back_button().clicked.connect(self.__volver_atras)

#     @classmethod
#     def registrar_ventana(cls, ventana):
#         """Registra una ventana para sincronizar el estado de pantalla completa."""
#         if ventana not in cls.ventanas_registradas:
#             cls.ventanas_registradas.append(ventana)
#             # Aplica el estado actual a la ventana registrada
#             if cls.is_fullscreen:
#                 ventana.showFullScreen()
#             else:
#                 ventana.showNormal()

#     @classmethod
#     def aplicar_pantalla_completa(cls):
#         """Aplica el estado de pantalla completa a todas las ventanas registradas."""
#         for ventana in cls.ventanas_registradas:
#             if cls.is_fullscreen:
#                 ventana.showFullScreen()
#             else:
#                 ventana.showNormal()

#     def __apagar_encender_musica(self):
#         """Alterna entre encender y apagar la música."""
#         self.music_on = not self.music_on
#         if self.music_on:
#             try:
#                 pygame.mixer.music.play(-1)  # Reproducir música en bucle
#                 self.__vista.get_music_button().setText("Apagar Música")
#             except pygame.error as e:
#                 print(f"Error al reproducir la música: {str(e)}")
#         else:
#             pygame.mixer.music.stop()
#             self.__vista.get_music_button().setText("Encender Música")

#     def __cambio_volumen(self, value):
#         """Cambia el volumen de la música."""
#         self.volume = value / 100  # Convertir el valor del slider (0-100) a rango (0.0-1.0)
#         pygame.mixer.music.set_volume(self.volume)

#     def __alternar_pantalla_completa(self):
#         """Alterna entre pantalla completa y modo ventana normal."""
#         # Cambiar el estado global
#         ControladorAudiovideo.is_fullscreen = not ControladorAudiovideo.is_fullscreen
#         # Aplicar el nuevo estado a todas las ventanas registradas
#         ControladorAudiovideo.aplicar_pantalla_completa()

#         # Cambiar el texto del botón en la ventana actual
#         if ControladorAudiovideo.is_fullscreen:
#             self.__vista.get_screen_button().setText("Modo Ventana")
#         else:
#             self.__vista.get_screen_button().setText("Pantalla Completa")

#     def __volver_atras(self):
#         """Vuelve a la ventana anterior."""
#         self.MainWindow.hide()
#         self.__controlador_anterior.MainWindow.show()


# from vista.VistaAudioVideo import Ui_ConfigWindow
# from PyQt6.QtWidgets import QMessageBox, QMainWindow

# class ControladorAudiovideo:
#     """Controlador para la configuración de audio y video."""

#     # Variable de clase para el estado de pantalla completa
#     is_fullscreen = True
#     ventanas_registradas = []

#     def __init__(self, controlador_anterior):
#         self.__controlador_anterior = controlador_anterior
#         self.MainWindow = QMainWindow()  # Nueva ventana para la configuración
#         self.__vista = Ui_ConfigWindow()
#         self.__vista.setupUi(self.MainWindow)

#         # Registrar esta ventana en la lista de ventanas
#         self.registrar_ventana(self.MainWindow)

#         self.music_on = False  # Inicialmente la música está apagada

#         # Conectar señales a funciones
#         self.__vista.get_music_button().clicked.connect(self.__apagar_encender_musica)
#         self.__vista.get_volume_slider().valueChanged.connect(self.__cambio_volumen)
#         self.__vista.get_screen_button().clicked.connect(self.__alternar_pantalla_completa)
#         self.__vista.get_back_button().clicked.connect(self.__volver_atras)

#     @classmethod
#     def registrar_ventana(cls, ventana):
#         """Registra una ventana para sincronizar el estado de pantalla completa."""
#         if ventana not in cls.ventanas_registradas:
#             cls.ventanas_registradas.append(ventana)
#             # Aplica el estado actual a la ventana registrada
#             if cls.is_fullscreen:
#                 ventana.showFullScreen()
#             else:
#                 ventana.showNormal()

#     @classmethod
#     def aplicar_pantalla_completa(cls):
#         """Aplica el estado de pantalla completa a todas las ventanas registradas."""
#         for ventana in cls.ventanas_registradas:
#             if cls.is_fullscreen:
#                 ventana.showFullScreen()
#             else:
#                 ventana.showNormal()

#     def __apagar_encender_musica(self):
#         """Alterna entre encender y apagar la música."""
#         self.music_on = not self.music_on
#         if self.music_on:
#             self.__vista.get_music_button().setText("Apagar Música")
#             QMessageBox.information(self.MainWindow, "Música", "La música está encendida.")
#         else:
#             self.__vista.get_music_button().setText("Encender Música")
#             QMessageBox.information(self.MainWindow, "Música", "La música está apagada.")

#     def __cambio_volumen(self, value):
#         """Cambia el volumen de la música."""
#         QMessageBox.information(self.MainWindow, "Volumen", f"Volumen ajustado a: {value}%")

#     def __alternar_pantalla_completa(self):
#         """Alterna entre pantalla completa y modo ventana normal."""
#         # Cambiar el estado global
#         ControladorAudiovideo.is_fullscreen = not ControladorAudiovideo.is_fullscreen
#         # Aplicar el nuevo estado a todas las ventanas registradas
#         ControladorAudiovideo.aplicar_pantalla_completa()

#         # Cambiar el texto del botón en la ventana actual
#         if ControladorAudiovideo.is_fullscreen:
#             self.__vista.get_screen_button().setText("Modo Ventana")
#         else:
#             self.__vista.get_screen_button().setText("Pantalla Completa")

#     def __volver_atras(self):
#         """Vuelve a la ventana anterior."""
#         self.MainWindow.hide()
#         self.__controlador_anterior.MainWindow.show()