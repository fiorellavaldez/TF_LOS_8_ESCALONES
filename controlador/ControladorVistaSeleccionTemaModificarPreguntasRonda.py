# from vista.VistaSeleccionDeTemaModificarPreguntasDeRonda import Ui_MainWindow
# from controlador.ControladorVistaConfiguracionModificarPreguntasRonda import ControladorVistaConfiguracionModificarPreguntasRonda
# from modelo.TemasDAO import TemasDAO
# from PyQt6.QtCore import QStringListModel
# from PyQt6 import QtWidgets

# class ControladorVistaSeleccionTemaModificarPreguntasRonda:
#     def __init__(self, controlador_anterior):
#         self.__controlador_anterior = controlador_anterior
#         self.MainWindow = QtWidgets.QMainWindow()
#         self.__vista = Ui_MainWindow()
#         self.__vista.setupUi(self.MainWindow)
#         self.MainWindow.show()

#         # Conexión de botones existentes
#         self.__vista.get_button_atras().clicked.connect(self.__volver_configuracion)
#         self.__vista.get_button_seleccionar_pregunta().clicked.connect(self.__seleccionar_pregunta)

#         # Configuración de DAO, ListView y búsqueda
#         self.dao = TemasDAO()
#         self.temas = []
#         self.filtered_temas = []
#         self.model = QStringListModel()

#         # Configura el modelo en el ListView
#         self.__vista.listView.setModel(self.model)

#         # Conecta la entrada de texto para búsqueda
#         self.__vista.lineEdit.textChanged.connect(self.__buscar_temas)

#         # Carga inicial de temas
#         self.__cargar_temas()

#     def __volver_configuracion(self):
#         """Vuelve a la configuración anterior."""
#         self.MainWindow.hide()
#         self.__controlador_anterior.MainWindow.show()

#     def __seleccionar_pregunta(self):
#         """Selecciona el tema y pasa al siguiente controlador."""
#         index = self.__vista.listView.currentIndex()
#         if index.isValid():
#             tema_seleccionado = self.filtered_temas[index.row()]
#             print(f"Tema seleccionado: {tema_seleccionado}")
#             # Aquí se oculta la ventana actual y se inicia la siguiente
#             self.MainWindow.hide()
#             self.controlador_seleccionar_pregunta = ControladorVistaConfiguracionModificarPreguntasRonda(self)
#         else:
#             print("No se seleccionó ningún tema.")

#     def __cargar_temas(self):
#         """Carga los temas desde el DAO y los muestra en el ListView."""
#         try:
#             self.temas = [tema[1] for tema in self.dao.get_all_temas()]  # Asume que el nombre del tema está en la segunda columna
#             self.filtered_temas = self.temas
#             self.__actualizar_list_view()
#         except Exception as e:
#             print(f"Error al cargar temas: {e}")

#     def __buscar_temas(self):
#         """Filtra los temas según el texto ingresado en la caja de búsqueda."""
#         texto = self.__vista.lineEdit.text().lower()
#         self.filtered_temas = [tema for tema in self.temas if texto in tema.lower()]
#         self.__actualizar_list_view()

#     def __actualizar_list_view(self):
#         """Actualiza el modelo del ListView con los temas filtrados."""
#         self.model.setStringList(self.filtered_temas)

# from vista.VistaSeleccionDeTemaModificarPreguntasDeRonda import Ui_MainWindow
# from controlador.ControladorVistaConfiguracionModificarPreguntasRonda import ControladorVistaConfiguracionModificarPreguntasRonda
# from modelo.TemasDAO import TemasDAO
# from PyQt6.QtCore import QStringListModel
# from PyQt6 import QtWidgets

# class ControladorVistaSeleccionTemaModificarPreguntasRonda:
#     def __init__(self, controlador_anterior):
#         self.__controlador_anterior = controlador_anterior
#         self.MainWindow = QtWidgets.QMainWindow()
#         self.__vista = Ui_MainWindow()
#         self.__vista.setupUi(self.MainWindow)
#         self.MainWindow.show()

#         # Conexión de botones existentes
#         self.__vista.get_button_atras().clicked.connect(self.__volver_configuracion)
#         self.__vista.get_button_seleccionar_pregunta().clicked.connect(self.__seleccionar_pregunta)

#         # Configuración de DAO, ListView y búsqueda
#         self.dao = TemasDAO()
#         self.temas = []
#         self.filtered_temas = []
#         self.model = QStringListModel()

#         # Configura el modelo en el ListView
#         self.__vista.listView.setModel(self.model)
#         self.__vista.listView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)  # Bloquea edición

#         # Conecta la entrada de texto para búsqueda
#         self.__vista.lineEdit.textChanged.connect(self.__buscar_temas)

#         # Carga inicial de temas
#         self.__cargar_temas()

#     def __volver_configuracion(self):
#         """Vuelve a la configuración anterior."""
#         self.MainWindow.hide()
#         self.__controlador_anterior.MainWindow.show()

#     def __seleccionar_pregunta(self):
#         """Selecciona el tema y pasa al siguiente controlador."""
#         index = self.__vista.listView.currentIndex()
#         if index.isValid():
#             tema_seleccionado = self.filtered_temas[index.row()]
#             print(f"Tema seleccionado: {tema_seleccionado}")
#             # Aquí se oculta la ventana actual y se inicia la siguiente
#             self.MainWindow.hide()
#             self.controlador_seleccionar_pregunta = ControladorVistaConfiguracionModificarPreguntasRonda(self)
#         else:
#             print("No se seleccionó ningún tema.")

#     def __cargar_temas(self):
#         """Carga los temas desde el DAO y los muestra en el ListView."""
#         try:
#             self.temas = [tema[1] for tema in self.dao.get_all_temas()]  # Asume que el nombre del tema está en la segunda columna
#             self.filtered_temas = self.temas
#             self.__actualizar_list_view()
#         except Exception as e:
#             print(f"Error al cargar temas: {e}")

#     def __buscar_temas(self):
#         """Filtra los temas según el texto ingresado en la caja de búsqueda."""
#         texto = self.__vista.lineEdit.text().lower()
#         self.filtered_temas = [tema for tema in self.temas if texto in tema.lower()]
#         self.__actualizar_list_view()

#     def __actualizar_list_view(self):
#         """Actualiza el modelo del ListView con los temas filtrados."""
#         self.model.setStringList(self.filtered_temas)

from vista.VistaSeleccionDeTemaModificarPreguntasDeRonda import Ui_MainWindow
from controlador.ControladorVistaConfiguracionModificarPreguntasRonda import ControladorVistaConfiguracionModificarPreguntasDeDesempate
from modelo.TemaABM import TemaABM
from PyQt6.QtCore import QStringListModel
from PyQt6 import QtWidgets

class ControladorVistaSeleccionTemaModificarPreguntasRonda:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()


        # Configuración de ABM, ListView y búsqueda
        self.dao = TemaABM().lista_temas
        self.temas = []  # [(id_tema, nombre_tema)]
        self.filtered_temas = []  # Filtrados para mostrar
        self.model = QStringListModel()
        
        # Configuración de DAO, ListView y búsqueda
        self.temas = TemaABM().lista_temas
        self.filtered_temas = []
        self.model = QStringListModel()
        
        # Configura el modelo en el ListView
        self.__vista.listView.setModel(self.model)
        self.__vista.listView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)  # Bloquea edición

        # Conecta la entrada de texto para búsqueda
        self.__vista.lineEdit.textChanged.connect(self.__buscar_temas)

        # Atributo para guardar el tema seleccionado
        self.tema_seleccionado = None

        # Carga inicial de temas
        self.__cargar_temas()
        #self.__actualizar_list_view()
        
        self.__vista.get_button_atras().clicked.connect(self.__volver_configuracion)
        self.__vista.get_button_seleccionar_pregunta().clicked.connect(self.__seleccionar_tema)
        
    def __cargar_temas(self):
        """Carga los temas desde el DAO y los muestra en el ListView."""
        try:
            # Obtener temas desde la base de datos
            self.filtered_temas = self.temas
            self.__actualizar_list_view()
        except Exception as e:
            print(f"Error al cargar temas: {e}")
            

    def __volver_configuracion(self):
        """Vuelve a la configuración anterior."""
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __seleccionar_tema(self):
        """Selecciona el tema y pasa al siguiente controlador."""
        index = self.__vista.listView.currentIndex()
        if index.isValid():
            # Obtiene el tema seleccionado
            tema_seleccionado_index = index.row()
            self.tema_seleccionado = self.temas[tema_seleccionado_index]
            id_tema = self.tema_seleccionado.get_idTema()
            nombre_tema = self.tema_seleccionado.get_nombreTema()
            
            # Oculta esta ventana y pasa al siguiente controlador
            self.MainWindow.hide()
            self.controlador_seleccionar_pregunta = ControladorVistaConfiguracionModificarPreguntasRonda(self, id_tema, nombre_tema)
        else:
            if not self.tema_seleccionado:  
                self.__vista.aviso_seleccionar_pregunta_ronda()
            print("No se seleccionó ningún tema.")

    def __buscar_temas(self):
        """Filtra los temas según el texto ingresado en la caja de búsqueda."""
        texto = self.__vista.lineEdit.text().lower()
        self.filtered_temas = [tema for tema in self.temas if texto in tema.get_nombreTema().lower()]
        self.__actualizar_list_view()

    def __actualizar_list_view(self):
        """Actualiza el modelo del ListView con los temas filtrados."""
        nombres = []
        for tema in self.filtered_temas:
            nombres.append(tema.get_nombreTema())
        self.model.setStringList(nombres)
        
    
    #     # Conecta la entrada de texto para búsqueda
    #     self.__vista.lineEdit.textChanged.connect(self.__buscar_temas)

    #     # Atributo para guardar el tema seleccionado
    #     self.tema_seleccionado = None

    #     # Carga inicial de temas
    #     self.__cargar_temas()

    # def __volver_configuracion(self):
    #     """Vuelve a la configuración anterior."""
    #     self.MainWindow.hide()
    #     self.__controlador_anterior.MainWindow.show()

    # def __seleccionar_pregunta(self):
    #     """Selecciona el tema, guarda los datos y pasa al siguiente controlador."""
    #     index = self.__vista.listView.currentIndex()
    #     if index.isValid():
    #         # Obtiene el tema seleccionado
    #         tema_seleccionado_index = index.row()
    #         self.tema_seleccionado = self.filtered_temas[tema_seleccionado_index]

    #         id_tema, nombre_tema, estado = self.tema_seleccionado
    #         print(f"Tema seleccionado: ID={id_tema}, Nombre={nombre_tema}")

    #         # Oculta esta ventana y pasa al siguiente controlador
    #         self.MainWindow.hide()
    #         self.controlador_seleccionar_pregunta = ControladorVistaConfiguracionModificarPreguntasRonda(self, id_tema, nombre_tema)
    #     else:
    #         print("No se seleccionó ningún tema.")

    # def __cargar_temas(self):
    #     """Carga los temas desde el DAO y los muestra en el ListView."""
    #     try:
    #         # Obtener temas desde la base de datos
    #         self.temas = self.dao.get_all_temas()  # [(id_tema, nombre_tema)]
    #         self.filtered_temas = self.temas
    #         self.__actualizar_list_view()
    #     except Exception as e:
    #         print(f"Error al cargar temas: {e}")

    # def __buscar_temas(self):
    #     """Filtra los temas según el texto ingresado en la caja de búsqueda."""
    #     texto = self.__vista.lineEdit.text().lower()
    #     self.filtered_temas = [
    #         tema for tema in self.temas if texto in tema[1].lower()
    #     ]  # Busca por nombre_tema
    #     self.__actualizar_list_view()

    # def __actualizar_list_view(self):
    #     """Actualiza el modelo del ListView con los temas filtrados."""
    #     # Solo muestra los nombres de los temas en el ListView
    #     nombres_temas = [tema[1] for tema in self.filtered_temas]
    #     self.model.setStringList(nombres_temas)

