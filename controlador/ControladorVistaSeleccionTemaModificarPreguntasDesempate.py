from vista.VistaSeleccionDeTemaModificarPreguntasDeDesempate import Ui_MainWindow
from controlador.ControladorVistaConfiguracionModificarPreguntasDesempate import ControladorVistaConfiguracionModificarPreguntasDeDesempate
from modelo.TemasDAO import TemasDAO
from PyQt6.QtCore import QStringListModel
from PyQt6 import QtWidgets

class ControladorVistaSeleccionTemaModificarPreguntasDesempate:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        # Configuración de DAO, ListView y búsqueda
        self.dao = TemasDAO()
        self.temas = []
        self.filtered_temas = []
        self.model = QStringListModel()
        
        # Configura el modelo en el ListView
        self.__vista.listView.setModel(self.model)
        self.__vista.listView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)  # Bloquea edición

        # Conecta la entrada de texto para búsqueda
        self.__vista.lineEdit.textChanged.connect(self.__buscar_temas)

        # Carga inicial de temas
        self.__cargar_temas()
        
        self.__vista.get_button_atras().clicked.connect(self.__volver_configuracion)
        self.__vista.get_button_seleccionar_pregunta().clicked.connect(self.__seleccionar_pregunta)

    def __volver_configuracion(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __seleccionar_pregunta(self):
        self.MainWindow.hide()
        self.controlador_seleccionar_pregunta = ControladorVistaConfiguracionModificarPreguntasDeDesempate(self)
        
    def __volver_configuracion(self):
        """Vuelve a la configuración anterior."""
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __seleccionar_pregunta(self):
        """Selecciona el tema y pasa al siguiente controlador."""
        index = self.__vista.listView.currentIndex()
        if index.isValid():
            tema_seleccionado = self.filtered_temas[index.row()]
            print(f"Tema seleccionado: {tema_seleccionado}")
            # Aquí se oculta la ventana actual y se inicia la siguiente
            self.MainWindow.hide()
            self.controlador_seleccionar_pregunta = ControladorVistaConfiguracionModificarPreguntasDeDesempate(self)
        else:
            print("No se seleccionó ningún tema.")

    def __cargar_temas(self):
        """Carga los temas desde el DAO y los muestra en el ListView."""
        try:
            self.temas = [tema[1] for tema in self.dao.get_all_temas()]  # Asume que el nombre del tema está en la segunda columna
            self.filtered_temas = self.temas
            self.__actualizar_list_view()
        except Exception as e:
            print(f"Error al cargar temas: {e}")

    def __buscar_temas(self):
        """Filtra los temas según el texto ingresado en la caja de búsqueda."""
        texto = self.__vista.lineEdit.text().lower()
        self.filtered_temas = [tema for tema in self.temas if texto in tema.lower()]
        self.__actualizar_list_view()

    def __actualizar_list_view(self):
        """Actualiza el modelo del ListView con los temas filtrados."""
        self.model.setStringList(self.filtered_temas)
