from vista.VistaConfiguracion import Ui_MainWindow
from controlador.ControladorConfiguracionPreguntaRonda import ControladorConfiguracionPreguntaRonda
from controlador.ControladorConfiguracionPreguntaDesempate import ControladorConfiguracionPreguntaDesempate
from controlador.ControladorVistaConfiguracionTemaABM import ControladorVistaConfiguracionTemaABM
from controlador.ControladorVistaSeleccionarJugadoresABM import ControladorVistaSeleccionarJugadores
from controlador.ControladorAudioVideo import ControladorAudiovideo
from PyQt6 import QtWidgets
import os
import pygame

class ControladorVistaConfiguracion:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la configuración
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        
        # Registrar la ventana en el controlador de audio y video
        ControladorAudiovideo.registrar_ventana(self.MainWindow)

        #Aplicar estilos desde un archivo relativo
        self.__aplicar_estilos()

        # Conectar botones a sus métodos
        self.__vista.get_button_config_audio_video().clicked.connect(self.__audio_video)
        self.__vista.get_button_modificar_preguntas_ronda().clicked.connect(self.__preguntas_ronda_ABM)
        self.__vista.get_button_modificar_preguntas_desempate().clicked.connect(self.__preguntas_desempate_ABM)
        self.__vista.get_button_modificar_jugadores().clicked.connect(self.__jugadores)
        self.__vista.get_button_modificar_temas().clicked.connect(self.__modificar_temas)
        self.__vista.get_button_atras().clicked.connect(self.__volver_menu)

    def __audio_video(self):
        self.MainWindow.hide()
        self.ControladorAudioVideo = ControladorAudiovideo(self)
        self.ControladorAudioVideo.MainWindow.show()

    def __aplicar_estilos(self):
        estilos_path = os.path.join(os.path.dirname(__file__),"../vista/estilos.qss")
        if os.path.exists(estilos_path):
            with open(estilos_path, "r") as f:
                self.MainWindow.setStyleSheet(f.read())
        else:
            print(f"Advertencia: No se encontró el archivo de estilos en {estilos_path}.")

    def __preguntas_ronda_ABM(self):
        self.MainWindow.hide()
        self.ControladorConfiguracionPregunta = ControladorConfiguracionPreguntaRonda(self)
        self.ControladorConfiguracionPregunta.MainWindow.show()
        
    def __preguntas_desempate_ABM (self):
        self.MainWindow.hide()  # Ocultar la ventana actual
        self.ControladorConfiguracionPregunta = ControladorConfiguracionPreguntaDesempate(self)
        self.ControladorConfiguracionPregunta.MainWindow.show()
    
    def __modificar_temas(self):
        self.MainWindow.hide()
        self.controlador_modificar_temas = ControladorVistaConfiguracionTemaABM(self)
    
    def __jugadores (self):
        self.MainWindow.hide()  # Ocultar la ventana actual
        self.ControladorConfiguracionPregunta = ControladorVistaSeleccionarJugadores(self)
        self.ControladorConfiguracionPregunta.MainWindow.show()

    def __volver_menu(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()  # Muestra la ventana anterior