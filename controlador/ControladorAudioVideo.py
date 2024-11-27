from vista.VistaAudioVideo import Ui_ConfigWindow
from PyQt6.QtWidgets import QMainWindow
from controlador.ControladorAudio import ControladorAudio
from controlador.ControladorVideo import ControladorVideo

class ControladorAudioVideo:
    def __init__(self, controlador_anterior, ruta_musica=None):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QMainWindow()


        # Configurar la vista en la ventana principal, pasando el controlador de audio
        self.__vista = Ui_ConfigWindow()
        self.__vista.setupUi(self.MainWindow)

        # Mostrar la ventana principal
        self.MainWindow.show()

        # Registrar la ventana con el controlador de video
        self.controlador_audio = ControladorAudio(ruta_inicial=ruta_musica, vista=self.__vista) 
        self.controlador_video = ControladorVideo(self.MainWindow, self.__vista)  # Pasar ventana y vista
        ControladorVideo.registrar_ventana(self.MainWindow)

        # Conectar el botón "Atrás" a su función
        self.__vista.get_back_button().clicked.connect(self.__volver_atras)

    def __volver_atras(self):
        """Vuelve a la ventana anterior."""
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

