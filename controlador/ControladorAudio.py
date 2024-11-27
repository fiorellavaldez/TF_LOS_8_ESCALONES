import pygame
import os
from controlador.Audiovariables import DEFAULT_SOUND_PATH, DEFAULT_VOLUME

class ControladorAudio:
    """Controlador para manejar las funcionalidades de audio."""
    def __init__(self, ruta_inicial=None, vista=None):
        """Inicializa el controlador con una ruta opcional y una vista."""
        self.__vista = vista
        self.__music_on = True  # Música está encendida inicialmente
        self.__volume = DEFAULT_VOLUME  # Configuración inicial de volumen
        self.__ruta_actual = ruta_inicial or DEFAULT_SOUND_PATH  # Ruta de audio predeterminada

        # Inicializamos pygame.mixer si no está ya inicializado
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        # Cargar y reproducir música
        self.__cargar_musica(self.__ruta_actual)
        #pygame.mixer.music.set_volume(self.__volume / 100)  # Configurar volumen inicial

        # Conectar señales si se proporciona una vista
        if self.__vista:
            #self.__vista.get_music_button().clicked.connect(self.apagar_encender_musica)
            self.__vista.get_volume_slider().setValue(int(self.__volume * 100))  # Configurar valor inicial
            self.__vista.get_volume_slider().valueChanged.connect(self.cambio_volumen)

    def __cargar_musica(self, ruta):
        """Carga la música desde una ruta."""
        if os.path.exists(ruta):
            try:
                pygame.mixer.music.load(ruta)
                if self.__music_on:
                    pygame.mixer.music.play(-1)  # Reproducir en bucle
            except pygame.error as e:
                print(f"Error al cargar la música: {str(e)}")
        else:
            print(f"Error: El archivo de música '{ruta}' no se encuentra.")

           
    def cambio_volumen(self, value):
        """Cambia el volumen de la música."""
        self.__volume = value
        
        pygame.mixer.music.set_volume(self.__volume / 100)  # Ajustar rango a 0.0-1.0

    # def apagar_encender_musica(self):
    #     """Alterna entre encender y apagar la música."""
    #     self.__music_on = not self.__music_on
    #     if self.__music_on:
    #         self.volumne = 0.5
    #         pygame.mixer.music.play(-1)  # Reproducir en bucle
    #         self.__vista.get_music_button().setText(MUSIC_BUTTON_TEXT_ON)
    #     else:
    #         self.__volume = 0.0
    #         pygame.mixer.music.stop()
    #         self.__vista.get_music_button().setText(MUSIC_BUTTON_TEXT_OFF)


    def cambiar_musica(self, nueva_ruta):
        """Cambia la música al archivo especificado."""
        if not isinstance(nueva_ruta, str):
            raise ValueError("La ruta proporcionada debe ser una cadena de texto.")
        if os.path.exists(nueva_ruta):
            self.__ruta_actual = nueva_ruta
            self.__cargar_musica(nueva_ruta)
        else:
            print(f"Error: El archivo '{nueva_ruta}' no se encuentra.")

    def detener_musica(self):
        """Detiene la música actual."""
        pygame.mixer.music.stop()

