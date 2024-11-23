from vista.VistaConfiguracion import Ui_MainWindow
from controlador.ControladorVistaTemaNuevo import ControladorVistaTemaNuevo
from controlador.ControladorConfiguracionPregunta import ControladorConfiguracionPreguntaRonda
from controlador.ControladorSeleccionTemaPreguntaABM import ControladorSeleccionTemaPreguntaABM
from controlador.ControladorVistaConfiguracionTemaABM import ControladorVistaConfiguracionTemaABM
from PyQt6 import QtWidgets

class ControladorVistaConfiguracion:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la configuración
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__vista.get_button_modificar_preguntas_ronda().clicked.connect(self.__preguntas_ronda_ABM)
        self.__vista.get_button_modificar_preguntas_desempate().clicked.connect(self.__desempateSeleccionarTema)
        self.__vista.get_button_modificar_temas().clicked.connect(self.__modificar_temas)
        self.__vista.get_button_atras().clicked.connect(self.__volver_menu)
    
    def __preguntas_ronda_ABM (self):
        self.MainWindow.hide() 
        self.ControladorConfiguracionPregunta = ControladorConfiguracionPreguntaRonda(self)
        
    def __desempateSeleccionarTema (self):
        self.MainWindow.hide() 
        self.controladorSeleccionTemaPreguntaABM = ControladorSeleccionTemaPreguntaABM(self, "desempate")
    
    def __modificar_temas(self):
        self.MainWindow.hide()
        self.controlador_modificar_temas = ControladorVistaConfiguracionTemaABM(self)

    def __volver_menu(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()  # Muestra la ventana anterior