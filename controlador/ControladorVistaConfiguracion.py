from vista.VistaConfiguracion import Ui_MainWindow
from controlador.ControladorVistaTemaNuevo import ControladorVistaTemaNuevo
from controlador.ControladorVistaConfiguracionModificarTemas import ControladorVistaConfiguracionModificarTemas
from controlador.ControladorVistaSeleccionTemaModificarPreguntasDesempate import ControladorVistaSeleccionTemaModificarPreguntasDesempate
from controlador.ControladorVistaSeleccionTemaModificarPreguntasRonda import ControladorVistaSeleccionTemaModificarPreguntasRonda

from PyQt6 import QtWidgets

class ControladorVistaConfiguracion:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la configuración
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__vista.get_button_modificar_preguntas_ronda().clicked.connect(self.__modificar_preguntas_ronda)
        self.__vista.get_button_modificar_preguntas_desempate().clicked.connect(self.__modificar_preguntas_desempate)
        self.__vista.get_button_modificar_temas().clicked.connect(self.__modificar_temas)
        self.__vista.get_button_tema_nuevo().clicked.connect(self.__tema_nuevo)
        self.__vista.get_button_atras().clicked.connect(self.__volver_menu)

    def __modificar_preguntas_ronda(self):
        self.MainWindow.hide()
        self.controlador_tema_preguntas_ronda = ControladorVistaSeleccionTemaModificarPreguntasRonda(self)

    def __modificar_preguntas_desempate(self):
        self.MainWindow.hide()
        self.controlador_tema_preguntas_desempate = ControladorVistaSeleccionTemaModificarPreguntasDesempate(self)

    def __modificar_temas(self):
        self.MainWindow.hide()
        self.controlador_modificar_temas = ControladorVistaConfiguracionModificarTemas(self)

    def __tema_nuevo(self):
        self.MainWindow.hide()
        self.controlador_tema_nuevo = ControladorVistaTemaNuevo(self)

    def __volver_menu(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()  # Muestra la ventana anterior
        #hide() permite volver a abrir la misma ventana (.show()) sin perder su estado o tener que volver a inicializarla
        #close() cierra la ventana y destruye el objeto asociado, no se le puede hacer .show(), usar cuando ya no se necesita la ventana y se quiere liberar recursos