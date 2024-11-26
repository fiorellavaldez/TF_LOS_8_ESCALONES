from vista.VistaSeleccionarJugadoresABM import Ui_MainWindow
from controlador.ControladorVistaJugadorNuevoABM import ControladorVistaJugadorNuevoABM
from controlador.ControladorVistaModificarJugadorABM import ControladorVistaModificarJugadorABM
from controlador.ControladorEstaSeguro import ControladorEstaSeguro
from PyQt6 import QtWidgets,QtCore
from modelo.JugadoresABM import JugadorABM
from modelo.Jugador import Jugador
from PyQt6.QtGui import QIcon,QPixmap
from controlador.ControladorVideo import ControladorVideo
import os

class ControladorVistaSeleccionarJugadores:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__lista_jugadores = JugadorABM().obtener_jugadores() #armo la lista con todos los jugadores
        #self.__lista_jugadores_filtrados = [] ###quizas sea necesario para la barra de busqueda
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        #Aplicar estilos desde un archivo relativo
        self.__aplicar_estilos()

        # Registrar la ventana en el controlador de audio y video
        ControladorVideo.registrar_ventana(self.MainWindow)
        with open("vista/estilos.qss") as f:
            self.MainWindow.setStyleSheet(f.read())
        
        self.__vista.get_button_cancelar().clicked.connect(self.__volver)
        self.__vista.get_button_nuevo().clicked.connect(self.__nuevo)
        self.__vista.get_button_modificar().clicked.connect(self.__modificar)
        self.__vista.get_button_eliminar().clicked.connect(self.__eliminar)

        self.filtrando_jugadores = self.__lista_jugadores.copy()

        # Configuración de búsqueda
        self.__vista.lineEdit.textChanged.connect(self.__buscar_jugador)
        
        #Llenado de la tabla
        self.__vista.update_table(self.filtrando_jugadores)

    def __aplicar_estilos(self):
        estilos_path = os.path.join(os.path.dirname(__file__),"../vista/estilos.qss")
        if os.path.exists(estilos_path):
            with open(estilos_path, "r") as f:
                self.MainWindow.setStyleSheet(f.read())
        else:
            print(f"Advertencia: No se encontró el archivo de estilos en {estilos_path}.")


    def __nuevo(self):
        self.controlador_jugador_nuevo= ControladorVistaJugadorNuevoABM(self)
    
    def __modificar (self):
        fila = self.__vista.tableWidget.currentRow()
        if fila < 0:
            self.__vista.aviso_seleccionar_jugador()  # Si no se seleccionó ninguna fila
        else:
            # Obtener el contenido de la fila seleccionada en la columna 0 (nombre del jugador)
            nombre_jugador_a_modificar = self.__vista.tableWidget.item(fila, 0).text()
            jugador_a_modificar = None
            # Buscar el jugador en la lista filtrada de jugadores
            for i in self.filtrando_jugadores:
                if i.get_nombre_jugador() == nombre_jugador_a_modificar:
                    jugador_a_modificar = i
        self.controlador_jugador_nuevo= ControladorVistaModificarJugadorABM(self,jugador_a_modificar)
    
    def __eliminar(self):
        fila = self.__vista.tableWidget.currentRow()
        if fila < 0:
            self.__vista.aviso_seleccionar_jugador()  # Si no se seleccionó ninguna fila
        else:
            # Obtener el contenido de la fila seleccionada en la columna 0 (nombre del jugador)
            nombre_jugador_a_eliminar = self.__vista.tableWidget.item(fila, 0).text()
            # Confirmar si el usuario está seguro de eliminar al jugador
            controlador_seguro = ControladorEstaSeguro("¿Está seguro de eliminar este jugador?")
            if controlador_seguro.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                jugador_a_eliminar = None
                # Buscar el jugador en la lista filtrada de jugadores
                for i in self.filtrando_jugadores:
                    if i.get_nombre_jugador() == nombre_jugador_a_eliminar:
                        jugador_a_eliminar = i
                        break  # Salir del loop una vez encontrado el jugador
                if jugador_a_eliminar:
                    # Eliminar el jugador de la base de datos
                    JugadorABM().eliminar_jugador_por_nombre(jugador_a_eliminar)
                    self.actualizar_tabla()  # Actualizar la tabla con los jugadores restantes
    
    def __volver(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()
        
    def actualizar_tabla(self):
        jugadores = JugadorABM().obtener_jugadores()
        self.__vista.update_table(jugadores)
            
    def __buscar_jugador(self):
        """Filtra los jugadores según el texto ingresado en el cuadro de búsqueda."""
        texto = self.__vista.lineEdit.text().strip().lower()
        # Verificar que cada elemento sea un objeto de tipo Jugador
        if all(isinstance(jugador, Jugador) for jugador in self.__lista_jugadores):
            self.filtrando_jugadores = [
                jugador for jugador in self.__lista_jugadores
                if jugador.get_nombre_jugador().lower().startswith(texto)  # Filtrar por nombre
            ]
        else:
            # Si los elementos no son objetos Jugador, asignar lista vacía o manejar el error según sea necesario
            print("La lista de jugadores no contiene objetos de tipo Jugador.")
            self.filtrando_jugadores = []

        # Actualizar la tabla con los resultados filtrados
        self.__vista.update_table(self.filtrando_jugadores)

    
