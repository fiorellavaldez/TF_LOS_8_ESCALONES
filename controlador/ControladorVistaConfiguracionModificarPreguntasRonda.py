from vista.VistaConfiguracionModificarPreguntasDeRonda import Ui_MainWindow
from controlador.ControladorVistaConfiguracionPreguntasAgregarPreguntaDeRondaEspecifica import ControladorVistaConfiguracionPreguntasAgregarPreguntaDeRondaEspecifica
from modelo.PreguntasDAO import PreguntaDAO
from PyQt6 import QtWidgets
from PyQt6.QtCore import QStringListModel

class ControladorVistaConfiguracionModificarPreguntasRonda:
    def __init__(self, controlador_anterior, id_tema,nombre_tema):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__dao = PreguntaDAO()
        self.__id_tema = id_tema  # Almacenar el tema actual
        self.__nombre_tema= nombre_tema
        self.__vista.get_button_atras().clicked.connect(self.__volver)
        self.__vista.get_button_agregar_pregunta().clicked.connect(self.__agregar_pregunta)

        self.__llenar_listview()

    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __agregar_pregunta(self):
        self.MainWindow.hide()
        self.controlador_siguiente = ControladorVistaConfiguracionPreguntasAgregarPreguntaDeRondaEspecifica(self,self.__id_tema)

    def __llenar_listview(self):
        """Llena el QListView con las preguntas del tema."""
        preguntas = self.__dao.devolver_all_ronda(self.__id_tema)  # Consulta al DAO
        if not preguntas:
            print("No se encontraron preguntas para el tema.")
            return

        modelo = QStringListModel()
        lista_preguntas = [f"Pregunta: {pregunta[1]} - a): {pregunta[2]} - b): {pregunta[3]} - c): {pregunta[4]} - d): {pregunta[5]} - Correcta: {pregunta[6]}" for pregunta in preguntas]
        modelo.setStringList(lista_preguntas)
        self.__vista.listView.setModel(modelo)

