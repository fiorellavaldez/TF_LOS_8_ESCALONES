from controlador.ControladorConfiguracion import ControladorVistaConfiguracion
from controlador.ControladorVistaGrillaJugadores import ControladorVistaGrillaJugadores
from vista.VistaPantallaInicio import Ui_MainWindow
from controlador.ControladorAudioVideo import ControladorAudiovideo
from PyQt6 import QtWidgets

class ControladorPantallaInicio:

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        
        # Registrar la ventana en el controlador de audio y video
        ControladorAudiovideo.registrar_ventana(self.MainWindow)
        
        with open("vista/estilos.qss") as f:
            self.MainWindow.setStyleSheet(f.read())
        
        self.__vista.get_button_nueva_partida().clicked.connect(self.__nueva_partida)
        #self.__vista.get_button_continuar().clicked.connect(self.__continuar)
        self.__vista.get_button_configuracion().clicked.connect(self.__configuracion) #Clickear el boton (Es un evento) ?
        self.__vista.get_button_salir().clicked.connect(self.__salir)
        
    def __nueva_partida(self):
        self.MainWindow.close()
        self.controlador_nueva_partida=ControladorVistaGrillaJugadores(self)

    def __configuracion(self):
        self.MainWindow.hide()
        self.controlador_configuracion = ControladorVistaConfiguracion(self)
    
    def __salir(self):
        self.MainWindow.close() #si es la última ventana abierta y hacemos .close(), se cierra el programa y termina la ejecución del bucle de Qt (que está en el main)