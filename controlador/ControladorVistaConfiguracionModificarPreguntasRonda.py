# from vista.VistaConfiguracionModificarPreguntasDeRonda import Ui_MainWindow
# from controlador.ControladorVistaConfiguracionPreguntasEditarPreguntaDeRondaEspecifica import ControladorVistaConfiguracionPreguntasEditarPreguntaDeRondaEspecifica
# from PyQt6 import QtWidgets

# class ControladorVistaConfiguracionModificarPreguntasRonda:
#     def __init__(self, controlador_anterior):
#         self.__controlador_anterior = controlador_anterior
#         self.MainWindow = QtWidgets.QMainWindow()
#         self.__vista = Ui_MainWindow()
#         self.__vista.setupUi(self.MainWindow)
#         self.MainWindow.show()

#         self.__vista.get_button_atras().clicked.connect(self.__volver)
#         self.__vista.get_button_agregar_pregunta().clicked.connect(self.__agregar_pregunta)

#     def __volver(self):
#         self.MainWindow.hide()
#         self.__controlador_anterior.MainWindow.show()

#     def __agregar_pregunta(self):
#         self.MainWindow.hide()
#         self.controlador_siguiente = ControladorVistaConfiguracionPreguntasEditarPreguntaDeRondaEspecifica(self)

# from vista.VistaConfiguracionModificarPreguntasDeRonda import Ui_MainWindow
# from controlador.ControladorVistaConfiguracionPreguntasEditarPreguntaDeRondaEspecifica import ControladorVistaConfiguracionPreguntasEditarPreguntaDeRondaEspecifica
# from PyQt6 import QtWidgets
# from modelo.PreguntasDAO import PreguntaDAO  # Importa el DAO

# class ControladorVistaConfiguracionModificarPreguntasRonda:
#     def __init__(self, controlador_anterior, id_tema, nombre_tema):
#         self.__controlador_anterior = controlador_anterior
#         self.__id_tema = id_tema  # ID del tema
#         self.__nombre_tema = nombre_tema  # Nombre del tema
#         self.__pregunta_dao = PreguntaDAO()  # Instancia del DAO

#         self.MainWindow = QtWidgets.QMainWindow()
#         self.__vista = Ui_MainWindow()
#         self.__vista.setupUi(self.MainWindow)
#         self.MainWindow.show()

#         # Configurar la vista con el nombre del tema
#         self.__vista.label.setText(
#             f"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Preguntas de ronda: {self.__nombre_tema}</span></p></body></html>"
#         )

#         # Conexiones de botones
#         self.__vista.get_button_atras().clicked.connect(self.__volver)
#         self.__vista.get_button_agregar_pregunta().clicked.connect(self.__agregar_pregunta)

#         # Cargar preguntas en la tabla
#         self.__cargar_preguntas()

#     def __volver(self):
#         self.MainWindow.hide()
#         self.__controlador_anterior.MainWindow.show()

#     def __agregar_pregunta(self):
#         self.MainWindow.hide()
#         self.controlador_siguiente = ControladorVistaConfiguracionPreguntasEditarPreguntaDeRondaEspecifica(self)

#     def __cargar_preguntas(self):
#         """
#         Consulta las preguntas de la base de datos y las carga en la tabla.
#         """
#         try:
#             preguntas = self.__pregunta_dao.devolver_all_ronda(self.__id_tema)

#             # Limpiar la tabla antes de cargar datos
#             self.__vista.tableWidget.setRowCount(0)

#             for pregunta in preguntas:
#                 row_position = self.__vista.tableWidget.rowCount()
#                 self.__vista.tableWidget.insertRow(row_position)

#                 # Insertar datos en cada columna de la tabla
#                 self.__vista.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(pregunta['enunciado_pregunta']))
#                 self.__vista.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(pregunta['rta_a']))
#                 self.__vista.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(pregunta['rta_b']))
#                 self.__vista.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(pregunta['rta_c']))
#                 self.__vista.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(pregunta['rta_d']))
#                 self.__vista.tableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(pregunta['rta_correcta']))
#         except Exception as e:
#             print(f"Error al cargar preguntas: {e}")

from vista.VistaConfiguracionModificarPreguntasDeRonda import Ui_MainWindow
from controlador.ControladorVistaConfiguracionPreguntasEditarPreguntaDeRondaEspecifica import ControladorVistaConfiguracionPreguntasEditarPreguntaDeRondaEspecifica
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
        self.controlador_siguiente = ControladorVistaConfiguracionPreguntasEditarPreguntaDeRondaEspecifica(self)

    def __llenar_listview(self):
        """Llena el QListView con las preguntas del tema."""
        preguntas = self.__dao.devolver_all_ronda(self.__id_tema)  # Consulta al DAO

        if not preguntas:
            print("No se encontraron preguntas para el tema.")
            return

        modelo = QStringListModel()
        lista_preguntas = [f"Pregunta: {pregunta['enunciado_pregunta']} - Correcta: {pregunta['rta_correcta']}" for pregunta in preguntas]
        modelo.setStringList(lista_preguntas)
        self.__vista.listView.setModel(modelo)

