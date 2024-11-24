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
        self.__listaNombreTemas = self.__obtenerListaNombreTemas()
        
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow(self.__listaNombreTemas)
        self.__vista.setupUi(self.MainWindow)

        self.__vista.get_comboBox().currentTextChanged.connect(self.__actualizar_preguntas)  # Conecta el cambio en el ComboBox
        self.__idTemaActual = self.__temaActual()
        
        self.__vista.get_line_edit_busqueda().textChanged.connect(self.__buscar_pregunta) #conectra con la barra de busqueda

        
        # Obtener preguntas para el tema inicial
        self.__lista_preguntas = PreguntaABM().obtener_preguntas_ronda_tema(self.__idTemaActual)
        self.__preguntas_visibles = []  # Lista de referencias a las preguntas visibles

        # Conexiones con botones
        self.__vista.get_button_atras().clicked.connect(self.__volver)
        self.__vista.get_button_eliminar().clicked.connect(self.__eliminar)
        self.__vista.get_button_modificar().clicked.connect(self.__modificar)
        self.__vista.get_button_nueva().clicked.connect(self.__nueva)
    
        # Mostrar datos iniciales
        self.__vista.mostrar_lista_en_combobox()
        self.__mostrar_preguntas()
        self.MainWindow.show()  # Mostrar ventana al iniciar
    
    # Acciones de botones
    def __volver(self):
        self.MainWindow.hide()  # Oculta la ventana actual
        self.__controlador_anterior.MainWindow.show()  # Muestra la ventana anterior
    
    def __eliminar(self):
        fila = self.__vista.tableWidget.currentRow()
        if fila < 0:
            self.__vista.aviso_seleccionar_pregunta()
        else:
            pregunta_a_eliminar = self.__preguntas_visibles[fila]  # Obtener la pregunta seleccionada
            controlador_seguro = ControladorEstaSeguro("¿Está seguro de eliminar esta pregunta?")
            if controlador_seguro.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                PreguntaABM().quitar_pregunta_ronda(pregunta_a_eliminar)
                self.__mostrar_preguntas()  # Actualizar la tabla
    
    def __modificar(self):
        pass
    
    def __nueva(self):
        pass

    ###############################################################
    
    def __obtenerListaNombreTemas(self):  # Devuelve una lista con los nombres de los temas
        return [tema.get_nombreTema() for tema in self.__listaTemas]
    
    def __temaActual(self):  # Identifica el nombre actual del ComboBox y devuelve el ID del tema
        nombreTema = self.__vista.get_comboBox().currentText()
        for tema in self.__listaTemas:
            if nombreTema == tema.get_nombreTema():
                return tema.get_idTema()
        return None  # Devuelve None si no se encuentra un tema coincidente
    
    def __mostrar_preguntas(self):
        self.__idTemaActual = self.__temaActual()  # Asegurarse de tener el tema actualizado
        if self.__idTemaActual is not None:
            self.__lista_preguntas = PreguntaABM().obtener_preguntas_ronda_tema(self.__idTemaActual)
            self.__llenar_tableview(self.__lista_preguntas)  # Llenar la tabla con las preguntas

    def __llenar_tableview(self, preguntas):
        self.__vista.tableWidget.setRowCount(0)  # Limpiar la tabla
        self.__preguntas_visibles = preguntas  # Actualizar la lista auxiliar de preguntas visibles

        for pregunta in preguntas:
            row_position = self.__vista.tableWidget.rowCount()
            self.__vista.tableWidget.insertRow(row_position)
            self.__vista.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(pregunta.get_enunciado()))

    
    def __actualizar_preguntas(self):  # Método conectado al ComboBox
        self.__mostrar_preguntas()  # Llama a __mostrar_preguntas() para actualizar la tabla
        
    def __buscar_pregunta(self, texto):
        texto_filtrado = texto.strip().lower()
        preguntas_filtradas = [
            pregunta for pregunta in self.__lista_preguntas
            if texto_filtrado in pregunta.get_enunciado().lower()
        ]
        self.__llenar_tableview(preguntas_filtradas)  # Mostrar solo las preguntas filtradas


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    #

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #def __cargar_preguntas(self):
    #    nombreTema = self.__vista.get_comboBox().currentText()
    #    id_tema = None
    #    for tema in self.__listaTemas:
    #        if nombreTema == tema.get_nombreTema():
    #            id_tema = tema.get_idTema()
    #    return PreguntaABM().obtener_preguntas_desempate_tema(id_tema)
    #
    #
    #
    #
    #
    #
    #
    #def __buscar_pregunta(self):
    #    """Filtrar las preguntas según el texto ingresado en la barra de búsqueda"""
    #    texto_busqueda = self.__vista.get_line_edit_busqueda().text().lower()  # Obtener el texto de la barra de búsqueda
    #    preguntas_filtradas = [pregunta for pregunta in self.__lista_preguntas if texto_busqueda in pregunta.get_enunciado().lower()]
    #    self.__lista_preguntas_filtradas = preguntas_filtradas  # Guardamos las preguntas filtradas
    #    self.__llenar_tableview(preguntas_filtradas)  # Actualizar la tabla con las preguntas filtradas
#
    #
    #
    #
    #def __mostrar_preguntas(self):
    #    nombreTema = self.__vista.get_comboBox().currentText()
    #    id_tema = None
    #    for tema in self.__listaTemas:
    #        if nombreTema == tema.get_nombreTema():
    #            id_tema = tema.get_idTema()
    #    if id_tema:
    #        self.__lista_preguntas = PreguntaABM().obtener_preguntas_ronda_tema(id_tema)
    #    else:
    #        self.__lista_preguntas = PreguntaABM().obtener_preguntas_ronda()
#
    #    self.__lista_preguntas_filtradas = self.__lista_preguntas  # Resetear lista filtrada
    #    self.__llenar_tableview()  # Llenar la tabla con todas las preguntas
    #
    #def __LlenarlistaNobreTemas(self):
    #    listaNobreTemas = []
    #    for i in self.__listaTemas:
    #        listaNobreTemas.append(i.get_nombreTema())
    #    return listaNobreTemas
    
    #def actualizar_lista_preguntas(self):
    #    self.__vista.tableWidget.setRowCount(0)
    #    self.__lista_preguntas = PreguntaABM().obtener_preguntas_ronda_tema(self.__id_tema)
    #    self.__lista_preguntas_filtradas = self.__lista_preguntas  # Resetear lista filtrada a todas las preguntas
    #    self.__llenar_tableview()