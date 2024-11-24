from vista.VistaAudioVideo import Ui_ConfigWindow
from PyQt6.QtWidgets import QMessageBox, QMainWindow

class ControladorAudiovideo:
    """Controlador para la configuración de audio y video."""

    # Variable de clase para el estado de pantalla completa
    is_fullscreen = True
    ventanas_registradas = []

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QMainWindow()  # Nueva ventana para la configuración
        self.__vista = Ui_ConfigWindow()
        self.__vista.setupUi(self.MainWindow)

        # Registrar esta ventana en la lista de ventanas
        self.registrar_ventana(self.MainWindow)

        self.music_on = False  # Inicialmente la música está apagada

        # Conectar señales a funciones
        self.__vista.get_music_button().clicked.connect(self.__apagar_encender_musica)
        self.__vista.get_volume_slider().valueChanged.connect(self.__cambio_volumen)
        self.__vista.get_screen_button().clicked.connect(self.__alternar_pantalla_completa)
        self.__vista.get_back_button().clicked.connect(self.__volver_atras)

    @classmethod
    def registrar_ventana(cls, ventana):
        """Registra una ventana para sincronizar el estado de pantalla completa."""
        if ventana not in cls.ventanas_registradas:
            cls.ventanas_registradas.append(ventana)
            # Aplica el estado actual a la ventana registrada
            if cls.is_fullscreen:
                ventana.showFullScreen()
            else:
                ventana.showNormal()

    @classmethod
    def aplicar_pantalla_completa(cls):
        """Aplica el estado de pantalla completa a todas las ventanas registradas."""
        for ventana in cls.ventanas_registradas:
            if cls.is_fullscreen:
                ventana.showFullScreen()
            else:
                ventana.showNormal()

    def __apagar_encender_musica(self):
        """Alterna entre encender y apagar la música."""
        self.music_on = not self.music_on
        if self.music_on:
            self.__vista.get_music_button().setText("Apagar Música")
            QMessageBox.information(self.MainWindow, "Música", "La música está encendida.")
        else:
            self.__vista.get_music_button().setText("Encender Música")
            QMessageBox.information(self.MainWindow, "Música", "La música está apagada.")

    def __cambio_volumen(self, value):
        """Cambia el volumen de la música."""
        QMessageBox.information(self.MainWindow, "Volumen", f"Volumen ajustado a: {value}%")

    def __alternar_pantalla_completa(self):
        """Alterna entre pantalla completa y modo ventana normal."""
        # Cambiar el estado global
        ControladorAudiovideo.is_fullscreen = not ControladorAudiovideo.is_fullscreen
        # Aplicar el nuevo estado a todas las ventanas registradas
        ControladorAudiovideo.aplicar_pantalla_completa()

        # Cambiar el texto del botón en la ventana actual
        if ControladorAudiovideo.is_fullscreen:
            self.__vista.get_screen_button().setText("Modo Ventana")
        else:
            self.__vista.get_screen_button().setText("Pantalla Completa")

    def __volver_atras(self):
        """Vuelve a la ventana anterior."""
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()