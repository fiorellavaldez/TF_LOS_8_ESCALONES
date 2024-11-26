from vista.VistaAudioVideo import Ui_ConfigWindow
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QScreen
from controlador.Sonido import Sonido

class ControladorAudio:
    """Controlador para manejar las funcionalidades de audio."""

    def __init__(self, ruta_inicial=None, vista=None):
        """Inicializa el controlador con una ruta opcional y una vista."""
        self.__vista = vista
        # Asegúrate de que ruta_inicial sea una cadena, si no se pasa, no se inicializa Sonido
        if ruta_inicial and isinstance(ruta_inicial, str):
            self.__sonido = Sonido(ruta_inicial)  # Usa la ruta si se proporciona
        else:
            self.__sonido = Sonido()  # Si no hay ruta, inicializa sin música

        self.__music_on = True  # Música está encendida inicialmente

        # Conectar señales si se proporciona una vista
        if self.__vista:
            self.__vista.get_music_button().clicked.connect(self.__apagar_encender_musica)
            self.__vista.get_volume_slider().valueChanged.connect(self.__cambio_volumen)

    def __apagar_encender_musica(self):
        """Alterna entre encender y apagar la música."""
        self.music_on = not self.__music_on
        if self.music_on:
            self.__sonido.toggle_music()
            self.__vista.get_music_button().setText("Encender/Apagar Música")
        else:
            self.__sonido.toggle_music()
            self.__vista.get_music_button().setText("Encender/Apagar Música")

    def __cambio_volumen(self, value):
        """Cambia el volumen de la música."""
        self.__sonido.set_volume(value / 100)  # Convertir a rango 0.0-1.0

    def cambiar_musica(self, nueva_ruta):
        """Permite cambiar automáticamente la música al archivo especificado."""
        if not isinstance(nueva_ruta, str):
            raise ValueError("La ruta proporcionada debe ser una cadena de texto.")
        
        if not self.__sonido:
            raise ValueError("El objeto 'Sonido' no está inicializado.")
        self.__sonido.cambiar_musica(nueva_ruta)


# class ControladorAudio:
#     """Controlador para manejar las funcionalidades de audio."""
#     _sonidos = None

#     def __init__(self, vista = None):
#         self.__vista = vista
#         self.sonido = Sonido(
#             r"musica\\menu_2.mp3"
#         )
        
#         # Solo conecta señales si hay una vista
#         if self.__vista:
#             self.__vista.get_music_button().clicked.connect(self.__apagar_encender_musica)
#             self.__vista.get_volume_slider().valueChanged.connect(self.__cambio_volumen)


#         # Estado inicial de la música
#         self.music_on = True

#     def __apagar_encender_musica(self):
#         """Alterna entre encender y apagar la música."""
#         self.music_on = not self.music_on
#         if self.music_on:
#             self.sonido.toggle_music()
#             self.__vista.get_music_button().setText("Apagar Música")
#         else:
#             self.sonido.toggle_music()
#             self.__vista.get_music_button().setText("Encender Música")

#     def __cambio_volumen(self, value):
#         """Cambia el volumen de la música."""
#         self.sonido.set_volume(value / 100)  # Convertir a rango 0.0-1.0
        
#     @classmethod
#     def inicializar_sonido(cls, ruta_inicial):
#         """Inicializa el objeto Sonido para toda la clase."""
#         if cls._sonidos is None:
#             cls._sonidos = Sonido(ruta_inicial)
#         else:
#             print("El sonido ya fue inicializado.")
    
#     @classmethod
#     def cambiar_musica(cls, nueva_ruta):
#         """Permite cambiar automáticamente la música al archivo especificado."""
#         if cls._sonidos:
#             if os.path.exists(nueva_ruta):
#                 cls._sonidos.cambiar_musica(nueva_ruta)
#             else:
#                 print(f"Error: El archivo '{nueva_ruta}' no existe.")
#         else:
#             print("Error: El objeto 'Sonido' no ha sido inicializado.")


