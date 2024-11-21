from vista.VistaConfiguracionModificarPreguntasDeDesempate import Ui_MainWindow
from controlador.ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica import ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica
from controlador.ControladorConfiguracionPreguntasAgregarPreguntaDeDesempate import ControladorConfiguracionPreguntasAgregarPreguntaDeDesempate
from modelo.PreguntasABM import PreguntaABM
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

class ControladorVistaConfiguracionModificarPreguntasDeDesempate:
    def __init__(self, controlador_anterior, id_tema, nombre_tema):
        self.__controlador_anterior = controlador_anterior
        self.__id_tema = id_tema
        self.__nombre_tema = nombre_tema # hay que mandarlo para que la vista muestre el tema en el que se esta trabajando
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        
        self.__lista_preguntas = PreguntaABM().obtener_preguntas_desempate_tema(id_tema) #aca esta la lista con todos los objetos pregunta
        self.__vista.setupUi(self.MainWindow)
        self.__llenar_tableview()
        self.MainWindow.show()
        self.__vista.get_button_atras().clicked.connect(self.__volver)
        self.__vista.get_button_agregar_pregunta().clicked.connect(self.__agregar_pregunta)
        self.__vista.get_button_eliminar_pregunta().clicked.connect(self.__eliminar_pregunta)
        self.__vista.get_button_modificar_pregunta().clicked.connect(self.__modificar_pregunta)

    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __agregar_pregunta (self):
        self.controlador_siguiente = ControladorConfiguracionPreguntasAgregarPreguntaDeDesempate(self, self.__id_tema)
    
    def __modificar_pregunta(self):
        self.MainWindow.hide()
        self.controlador_siguiente = ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica(self, 1)

    def __llenar_tableview(self):
        for pregunta in self.__lista_preguntas:
            row_position = self.__vista.tableWidget.rowCount()  # Obtener el número actual de filas, que en realidad no se que tan necesario es
            self.__vista.tableWidget.insertRow(row_position)    # Insertar una nueva fila al final
            # Insertar la palabra en la primera columna de la fila recién agregada
            self.__vista.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(pregunta.get_enunciado()))
    
    def actualizar_lista_preguntas(self):  # Lo usa la pantalla de agregar nueva pregunta
        self.__vista.tableWidget.setRowCount(0)
        self.__lista_preguntas = PreguntaABM().obtener_preguntas_desempate_tema(self.__id_tema)
        self.__llenar_tableview()

    def __eliminar_pregunta(self): # le falta el dialog de "Esta seguro?"
        fila = self.__vista.tableWidget.currentRow()
        if fila != -1:
            PreguntaABM().quitar_pregunta_desempate(self.__lista_preguntas[fila])
            self.actualizar_lista_preguntas()

    def __modificar_pregunta(self):
        fila = self.__vista.tableWidget.currentRow()
        if fila != -1:
            pregunta = self.__lista_preguntas[fila]
            self.controlador_siguiente = ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica(self, pregunta)