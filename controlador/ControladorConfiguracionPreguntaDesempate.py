from vista.VistaConfiguracionPregunta import Ui_MainWindow
from PyQt6 import QtWidgets
from modelo.PreguntasABM import PreguntaABM
from modelo.TemaABM import TemaABM
from controlador.ControladorEstaSeguro import ControladorEstaSeguro
from controlador.ControladorEditarPreguntaDeDesempate import ControladorEditarPreguntaDeDesempate
from controlador.ControladorNuevaPreguntaDeDesempate import ControladorNuevaPreguntaDeDesempate
from controlador.ControladorVideo import ControladorVideo
import os
############################################ DESEMPATE NO ELIMINAR

class ControladorConfiguracionPreguntaDesempate():
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

        # Registrar la ventana en el controlador de audio y video
        ControladorVideo.registrar_ventana(self.MainWindow)

        #Aplicar estilos desde un archivo relativo
        self.__aplicar_estilos()

        # Obtener preguntas para el tema inicial
        self.__lista_preguntas = PreguntaABM().obtener_preguntas_desempate_tema(self.__idTemaActual)
        self.__preguntas_visibles = []  # Lista de referencias a las preguntas visibles

        # Conexiones con botones
        self.__vista.get_button_atras().clicked.connect(self.__volver)
        self.__vista.get_button_eliminar().clicked.connect(self.__eliminar)
        self.__vista.get_button_modificar().clicked.connect(self.__modificar)
        self.__vista.get_button_nueva().clicked.connect(self.__nueva)
    
        # Mostrar datos iniciales
        self.__vista.mostrar_lista_en_combobox()
        self.mostrar_preguntas()
        self.MainWindow.show()  # Mostrar ventana al iniciar

    def __aplicar_estilos(self):
        estilos_path = os.path.join(os.path.dirname(__file__),"../vista/estilos.qss")
        if os.path.exists(estilos_path):
            with open(estilos_path, "r") as f:
                self.MainWindow.setStyleSheet(f.read())
        else:
            print(f"Advertencia: No se encontró el archivo de estilos en {estilos_path}.")

    # Acciones de botones
    def __volver(self):
        self.MainWindow.hide()  # Oculta la ventana actual
        self.__controlador_anterior.MainWindow.show()  # Muestra la ventana anterior
    
    def __eliminar(self):
        for i in self.__preguntas_visibles:
            print(i.get_enunciado()) #si teine preguntas
        fila = self.__vista.tableWidget.currentRow()
        if fila < 0:
            self.__vista.aviso_seleccionar_pregunta()
        else:
            pregunta_a_eliminar = self.__preguntas_visibles[self.__vista.tableWidget.currentRow()]  # Obtener la pregunta seleccionada
            controlador_seguro = ControladorEstaSeguro("¿Está seguro de eliminar esta pregunta?")
            if controlador_seguro.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                # Eliminar la pregunta de la base de datos
                PreguntaABM().quitar_pregunta_desempate(pregunta_a_eliminar)
                self.mostrar_preguntas()  # Actualizar la tabla
    
    def __modificar(self):
        for i in self.__preguntas_visibles:
            print(i.get_enunciado()) #si teine preguntas
        fila = self.__vista.tableWidget.currentRow()
        if fila < 0:
            self.__vista.aviso_seleccionar_pregunta()
        else:
            pregunta_a_modificar = self.__preguntas_visibles[self.__vista.tableWidget.currentRow()]  # Obtener la pregunta seleccionada
            self.controlador_siguiente = ControladorEditarPreguntaDeDesempate(self, pregunta_a_modificar)
    
    def __nueva(self):
        for tema in self.__listaTemas:
            if self.__idTemaActual == tema.get_idTema():
                TemaActual = tema.get_idTema()
        self.controlador_siguiente = ControladorNuevaPreguntaDeDesempate(self, TemaActual)

    ###############################################################
    
    def __obtenerListaNombreTemas(self):  # Devuelve una lista con los nombres de los temas
        return [tema.get_nombreTema() for tema in self.__listaTemas]
    
    def __temaActual(self):  # Identifica el nombre actual del ComboBox y devuelve el ID del tema
        nombreTema = self.__vista.get_comboBox().currentText()
        for tema in self.__listaTemas:
            if nombreTema == tema.get_nombreTema():
                return tema.get_idTema()
        return None  # Devuelve None si no se encuentra un tema coincidente
    
    def mostrar_preguntas(self):
        self.__idTemaActual = self.__temaActual()  # Asegurarse de tener el tema actualizado
        if self.__idTemaActual is not None:
            self.__lista_preguntas = PreguntaABM().obtener_preguntas_desempate_tema(self.__idTemaActual)
            self.__llenar_tableview(self.__lista_preguntas)  # Llenar la tabla con las preguntas

    def __llenar_tableview(self, preguntas):
        self.__vista.tableWidget.setRowCount(0)  # Limpiar la tabla
        self.__preguntas_visibles = preguntas  # Actualizar la lista auxiliar de preguntas visibles

        for pregunta in preguntas:
            row_position = self.__vista.tableWidget.rowCount()
            self.__vista.tableWidget.insertRow(row_position)
            self.__vista.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(pregunta.get_enunciado()))
    
    def __actualizar_preguntas(self):  # Método conectado al ComboBox
        self.mostrar_preguntas()  # Llama a mostrar_preguntas() para actualizar la tabla
        
    def __buscar_pregunta(self, texto):
        texto_filtrado = texto.strip().lower()
        preguntas_filtradas = [
            pregunta for pregunta in self.__lista_preguntas
            if texto_filtrado in pregunta.get_enunciado().lower()
        ]
        self.__llenar_tableview(preguntas_filtradas)  # Mostrar solo las preguntas filtradas