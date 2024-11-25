from vista.VistaAudioVideo import Ui_ConfigWindow
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QScreen
from controlador.Sonido import Sonido
import os

class ControladorAudio:
    """Controlador para manejar las funcionalidades de audio."""
    _sonidos = None

    def __init__(self, vista):
        self.__vista = vista
        self.sonido = Sonido(
            r"C:\\Users\\Usuario\\Documents\\GitHub\\TF_LOS_8_ESCALONES\\musica\\menu_2.mp3"
        )
        # Conectar señales de la vista a métodos
        self.__vista.get_music_button().clicked.connect(self.__apagar_encender_musica)
        self.__vista.get_volume_slider().valueChanged.connect(self.__cambio_volumen)

        # Estado inicial de la música
        self.music_on = True

    def __apagar_encender_musica(self):
        """Alterna entre encender y apagar la música."""
        self.music_on = not self.music_on
        if self.music_on:
            self.sonido.toggle_music()
            self.__vista.get_music_button().setText("Apagar Música")
        else:
            self.sonido.toggle_music()
            self.__vista.get_music_button().setText("Encender Música")

    def __cambio_volumen(self, value):
        """Cambia el volumen de la música."""
        self.sonido.set_volume(value / 100)  # Convertir a rango 0.0-1.0
        
    
    @classmethod
    def cambiar_musica(cls, nueva_ruta):
        """Permite cambiar automáticamente la música al archivo especificado."""
        if cls._sonidos:
            if os.path.exists(nueva_ruta):
                cls._sonidos.cambiar_musica(nueva_ruta)
            else:
                print(f"Error: El archivo '{nueva_ruta}' no existe.")
        else:
            print("Error: El objeto 'Sonido' no ha sido inicializado.")


