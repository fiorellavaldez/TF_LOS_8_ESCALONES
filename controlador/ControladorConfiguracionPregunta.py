from vista.VistaConfiguracionPregunta import Ui_MainWindow
from PyQt6 import QtWidgets
from modelo.PreguntasABM import PreguntaABM
from modelo.TemaABM import TemaABM
from controlador.ControladorEstaSeguro import ControladorEstaSeguro

############################################ RONDA

class ControladorConfiguracionPreguntaRonda():
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.__listaTemas = TemaABM().obtener_temas()
        self.__listaNobreTemas = self.__LlenarlistaNobreTemas()
        self.__lista_preguntas = []  # Inicializamos la lista de preguntas
        self.__lista_preguntas_filtradas = []  # Lista filtrada
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow(self.__listaNobreTemas)
        self.__vista.setupUi(self.MainWindow)

        self.__vista.get_line_edit_busqueda().textChanged.connect(self.__buscar_pregunta)
        self.__vista.get_button_atras().clicked.connect(self.__volver)
        self.__vista.get_button_eliminar().clicked.connect(self.__eliminar)
        self.__vista.get_button_modificar().clicked.connect(self.__modificar)
        self.__vista.get_button_nueva().clicked.connect(self.__nueva)

        self.__vista.mostrar_lista_en_combobox()
        self.__vista.get_comboBox().currentTextChanged.connect(self.__mostrar_preguntas) #####

        
        self.__mostrar_preguntas()
        self.MainWindow.show()

    def __LlenarlistaNobreTemas(self):
        listaNobreTemas = []
        for i in self.__listaTemas:
            listaNobreTemas.append(i.get_nombreTema())
        return listaNobreTemas
    
    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.show()
    
    def __eliminar(self):
        fila = self.__vista.tableWidget.currentRow()
        if fila < 0:
            self.__vista.aviso_seleccionar_pregunta()
        else:
            # Instanciamos el controlador de confirmación
            controlador_seguro = ControladorEstaSeguro("¿Está seguro de eliminar esta pregunta?")
            
            if controlador_seguro.exec() == QtWidgets.QMessageBox.StandardButton.Yes:  # Verificamos si el usuario confirma
                pregunta_a_eliminar = self.__lista_preguntas_filtradas[fila]  # Usamos la lista filtrada
                PreguntaABM().quitar_pregunta_ronda(pregunta_a_eliminar)
                self.__mostrar_preguntas()  # Actualizamos la tabla después de eliminar la pregunta
    
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

    
    def __llenar_tableview(self, preguntas=None):
        """Llenar la tabla con preguntas filtradas o todas las preguntas si no se pasa ninguna."""
        self.__vista.tableWidget.setRowCount(0)  # Limpiar la tabla antes de agregar los nuevos datos
        preguntas = preguntas or self.__lista_preguntas_filtradas  # Si no hay preguntas filtradas, usar todas las preguntas
        for pregunta in preguntas:
            row_position = self.__vista.tableWidget.rowCount()
            self.__vista.tableWidget.insertRow(row_position)
            self.__vista.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(pregunta.get_enunciado()))
    
    def __mostrar_preguntas(self):
        comboBox = self.__vista.get_comboBox()
        nombreTema = comboBox.currentText()
        id_tema = None
        for tema in self.__listaTemas:
            if nombreTema == tema.get_nombreTema():
                id_tema = tema.get_idTema()
        if id_tema:
            self.__lista_preguntas = PreguntaABM().obtener_preguntas_ronda_tema(id_tema)
        else:
            self.__lista_preguntas = PreguntaABM().obtener_preguntas_ronda()

        self.__lista_preguntas_filtradas = self.__lista_preguntas  # Resetear lista filtrada
        self.__llenar_tableview()  # Llenar la tabla con todas las preguntas
    
    #def actualizar_lista_preguntas(self):
    #    self.__vista.tableWidget.setRowCount(0)
    #    self.__lista_preguntas = PreguntaABM().obtener_preguntas_ronda_tema(self.__id_tema)
    #    self.__lista_preguntas_filtradas = self.__lista_preguntas  # Resetear lista filtrada a todas las preguntas
    #    self.__llenar_tableview()