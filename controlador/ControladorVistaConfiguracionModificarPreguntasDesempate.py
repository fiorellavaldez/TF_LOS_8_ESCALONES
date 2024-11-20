from vista.VistaConfiguracionModificarPreguntasDeDesempate import Ui_MainWindow
from controlador.ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica import ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica
from modelo.PreguntasABM import PreguntaABM
from PyQt6 import QtWidgets
from PyQt6.QtCore import QStringListModel

class ControladorVistaConfiguracionModificarPreguntasDeDesempate:
    def __init__(self, controlador_anterior, id_tema, nombre_tema):
        self.__controlador_anterior = controlador_anterior
        self.__id_tema = id_tema
        self.__nombre_tema = nombre_tema
        self.model = QStringListModel()
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.filtered_preguntas = []
        self.__lista_preguntas = PreguntaABM().preguntas_desempate_tema(self.__id_tema) #aca esta la lista con todos los objetos pregunta
        self.__vista.get_button_atras().clicked.connect(self.__volver)
        self.__vista.get_button_agregar_pregunta().clicked.connect(self.__agregar_pregunta)
        self.__vista.get_button_eliminar_pregunta().clicked.connect(self.__eliminar_pregunta)
        self.__vista.get_button_modificar_pregunta().clicked.connect(self.__modificar_pregunta)

        self.__llenar_listview()
        self.__actualizar_list_view()

    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __agregar_pregunta(self):
        self.MainWindow.hide()
        self.controlador_siguiente = ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica(self)

    def __eliminar_pregunta(self):
        pass #aca va el dialog que todavia no tenemos
    
    def __modificar_pregunta(self):
        self.MainWindow.hide()
        self.controlador_siguiente = ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica(self, 1)

    def __llenar_listview(self):
        """Llena el QListView con las preguntas del tema."""
        try:
            # Obtener preguntas desde la base de datos
            self.filtered_preguntas = self.__lista_preguntas
            self.__actualizar_list_view()
        except Exception as e:
            print(f"Error al cargar preguntas: {e}")
    
    def __actualizar_list_view(self):
        """Actualiza el modelo del ListView con las preguntas filtradas."""
        enunciados = []
        for pregunta in self.filtered_preguntas:
            enunciados.append(pregunta.get_enunciado())
        self.model.setStringList(enunciados)
    
            
        #################################
    # def __volver_atras(self):
    #     self.MainWindow.hide()
    #     self.__controlador_anterior.MainWindow.show()

    # def __seleccionar_pregunta(self):
    #     """Selecciona el tema y pasa al siguiente controlador."""
    #     index = self.__vista.listView.currentIndex()
    #     if index.isValid():
    #         # Obtiene el tema seleccionado
    #         tema_seleccionado_index = index.row()
    #         self.tema_seleccionado = self.temas[tema_seleccionado_index]
    #         id_tema = self.tema_seleccionado.get_idTema()
    #         nombre_tema = self.tema_seleccionado.get_nombreTema()
            
    #         # Oculta esta ventana y pasa al siguiente controlador
    #         self.MainWindow.hide()
    #         self.controlador_seleccionar_pregunta = ControladorVistaConfiguracionModificarPreguntasDeDesempate(self, id_tema, nombre_tema)
    #     else:
    #         print("No se seleccionó ningún tema.")

    # def __buscar_temas(self):
    #     """Filtra los temas según el texto ingresado en la caja de búsqueda."""
    #     texto = self.__vista.lineEdit.text().lower()
    #     self.filtered_temas = [tema for tema in self.temas if texto in tema.get_nombreTema().lower()]
    #     self.__actualizar_list_view()

    
