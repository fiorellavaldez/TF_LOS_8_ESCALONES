#from vista.VistaConfiguracioSeleccionarPregunta import Ui_MainWindow
from vista.VistaPreguntaABM import Ui_MainWindow
from controlador.EDITARControladorConfiguracionPreguntasEditarPreguntaDeRonda import EDITARControladorConfiguracionPreguntasEditarPreguntaDeRonda
from controlador.NUEVAControladorConfiguracionPreguntasEditarPreguntaDeRonda import NUEVAControladorConfiguracionPreguntasEditarPreguntaDeRonda
from modelo.PreguntasABM import PreguntaABM
from PyQt6 import QtWidgets
#from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

class ControladorPreguntaRondaABM:  
    def __init__(self, controlador_anterior, id_tema, nombre_tema):
        self.__controlador_anterior = controlador_anterior
        self.__id_tema = id_tema
        self.__nombre_tema = nombre_tema
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()

        self.__lista_preguntas = PreguntaABM().obtener_preguntas_ronda_tema(id_tema)  # Obtén todas las preguntas
        self.__vista.setupUi(self.MainWindow)

        self.__lista_preguntas_filtradas = self.__lista_preguntas  # Inicializamos la lista filtrada con todas las preguntas

        self.__llenar_tableview()  # Llenamos la tabla inicialmente
        self.MainWindow.show()

        # Conectar botones
        self.__vista.get_button_atras().clicked.connect(self.__volver)
        self.__vista.get_button_agregar_pregunta().clicked.connect(self.__agregar_pregunta)
        self.__vista.get_button_eliminar_pregunta().clicked.connect(self.__eliminar_pregunta)
        self.__vista.get_button_modificar_pregunta().clicked.connect(self.__modificar_pregunta)

        # Conectar barra de búsqueda
        self.__vista.get_line_edit_busqueda().textChanged.connect(self.__buscar_pregunta)  # Conectar la barra de búsqueda al método de búsqueda

    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __agregar_pregunta(self):
        self.controlador_siguiente = NUEVAControladorConfiguracionPreguntasEditarPreguntaDeRonda(self, self.__id_tema)

    def __llenar_tableview(self, preguntas=None):
        """Llenar la tabla con preguntas filtradas o todas las preguntas si no se pasa ninguna."""
        self.__vista.tableWidget.setRowCount(0)  # Limpiar la tabla antes de agregar los nuevos datos
        preguntas = preguntas or self.__lista_preguntas_filtradas  # Si no hay preguntas filtradas, usar todas las preguntas
        for pregunta in preguntas:
            row_position = self.__vista.tableWidget.rowCount()
            self.__vista.tableWidget.insertRow(row_position)
            self.__vista.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(pregunta.get_enunciado()))

    def actualizar_lista_preguntas(self):
        self.__vista.tableWidget.setRowCount(0)
        self.__lista_preguntas = PreguntaABM().obtener_preguntas_ronda_tema(self.__id_tema)
        self.__lista_preguntas_filtradas = self.__lista_preguntas  # Resetear lista filtrada a todas las preguntas
        self.__llenar_tableview()

    def __eliminar_pregunta(self):
        fila = self.__vista.tableWidget.currentRow()
        if fila < 0:
            self.__vista.aviso_seleccionar_pregunta()
        else:
            pregunta_a_eliminar = self.__lista_preguntas_filtradas[fila]  # Usamos la lista filtrada
            PreguntaABM().quitar_pregunta_ronda(pregunta_a_eliminar)
            self.actualizar_lista_preguntas()

    def __modificar_pregunta(self):
        fila = self.__vista.tableWidget.currentRow()
        if fila < 0:
            self.__vista.aviso_seleccionar_pregunta()
        else:
            pregunta_a_modificar = self.__lista_preguntas_filtradas[fila]  # Usamos la lista filtrada
            self.controlador_siguiente = EDITARControladorConfiguracionPreguntasEditarPreguntaDeRonda(self, pregunta_a_modificar)

    def __buscar_pregunta(self):
        """Filtrar las preguntas según el texto ingresado en la barra de búsqueda"""
        texto_busqueda = self.__vista.get_line_edit_busqueda().text().lower()  # Obtener el texto de la barra de búsqueda
        preguntas_filtradas = [pregunta for pregunta in self.__lista_preguntas if texto_busqueda in pregunta.get_enunciado().lower()]
        self.__lista_preguntas_filtradas = preguntas_filtradas  # Guardamos las preguntas filtradas
        self.__llenar_tableview(preguntas_filtradas)  # Actualizar la tabla con las preguntas filtradas
