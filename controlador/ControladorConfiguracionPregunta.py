from vista.VistaConfiguracionPregunta import Ui_MainWindow
from PyQt6 import QtWidgets
from modelo.PreguntasABM import PreguntaABM

class ControladorConfiguracionPreguntaRonda:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()

    
        self.__vista.get_line_edit_busqueda().textChanged.connect(self.__buscar_pregunta)  # Conectar la barra de búsqueda al método de búsqueda
    
        self.__vista.get_button_atras().clicked.connect(self.__volver)
        self.__vista.get_button_eliminar().clicked.connect(self.__eliminar)
        self.__vista.get_button_modificar().clicked.connect(self.__modificar)
        self.__vista.get_button_nueva().clicked.connect(self.__nueva)

    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()
    
    def __eliminar(self):
        pass
    
    def __modificar(self):
        pass
    
    def __nueva(self):
        pass
    
    def __buscar_pregunta(self):
        """Filtrar las preguntas según el texto ingresado en la barra de búsqueda"""
        texto_busqueda = self.__vista.get_line_edit_busqueda().text().lower()  # Obtener el texto de la barra de búsqueda
        preguntas_filtradas = [pregunta for pregunta in self.__lista_preguntas if texto_busqueda in pregunta.get_enunciado().lower()]
        self.__lista_preguntas_filtradas = preguntas_filtradas  # Guardamos las preguntas filtradas
        self.__llenar_tableview(preguntas_filtradas)  # Actualizar la tabla con las preguntas filtradas
    