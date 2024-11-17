from vista.VistaSeleccionarJugadores import Ui_MainWindow
from PyQt6 import QtWidgets
from modelo.JugadorDAO import JugadorDAO

class ControladorVistaSeleccionarJugadores:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__jugadores = JugadorDAO()
        self.__lista_jugadores = self.__jugadores.get_all_jugadores()
        self.__vista.setupUi(self.MainWindow, self.__lista_jugadores)
        self.MainWindow.show()
        
        self.__vista.get_button_aceptar().clicked.connect(self.__aceptar)
        self.__vista.get_button_cancelar().clicked.connect(self.__volver_seleccion_de_jugadores)

    def __aceptar(self):
        fila = self.__vista.get_tableWidget().currentRow() #devuelve el nro fila tupla selecc
        if fila >= 0:
            nombre = self.__vista.get_tableWidget().item(fila, 0).text() #el nombre del jugador
            
            if any(jugador[1]==nombre for jugador in self.__controlador_anterior.get_lista()): 
                self.__vista.aviso_repeticion_jugador(nombre)
                return
            #busca el indice del jugador en la lista
            indice = next((i for i, tupla in enumerate(self.__lista_jugadores) if str(tupla[1]) == nombre), None) #busca el nombre del jugador en la lista de jugadores y devuelve el indice
            if indice is not None:
                self.__controlador_anterior.add_jugador(self.__lista_jugadores[indice]) #le mando la tupla a la lista de la grilla, la tupla contiene el id_jugador, nombre y avatar del jugador
                self.MainWindow.close()
                self.__controlador_anterior.MainWindow.show()
            else:
                print(f"No se encontró a ningún jugador con el nombre {nombre}.") #esto no debería pasar tho
        else:
            print("No hay ninguna fila seleccionada")
        
    def __volver_seleccion_de_jugadores(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()

