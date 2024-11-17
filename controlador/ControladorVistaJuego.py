from vista.VistaJuego import Ui_MainWindow
from vista.VistaPreguntaRonda import VistaPreguntaRonda
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMessageBox, QDialog, QLabel, QPushButton
from PyQt6 import QtWidgets
from modelo.TemasDAO import TemasDAO
from modelo.JugadorDAO import JugadorDAO
from modelo.Escalon import Escalon
from vista.WidgetJugador import WidgetJugador

class ControladorVistaJuego:

    def __init__(self, controlador_anterior, lista_jugadores):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow() #Aca se crea la vista 
        self.__temas = TemasDAO()
        self.__lista_temas = self.__temas.temas_partida() #trae 8 temas ya mezclados
        self.__asignar_temas() #¿le pasamos la lista por parámetro?
        self.__escalon1 = Escalon(1)
        self.__lista_jugadores_widget = []
        self.__lista = lista_jugadores
        self.__asignar_jugadores(self.__escalon1)
        self.__vista.setupUi(self.MainWindow, self.__lista_jugadores_widget)
        self.MainWindow.show()
        
        self.__vista.get_button_atras().clicked.connect(self.__atras)
        

    def __atras(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()

    def __obtener_pregunta(self): #pasarlo a una vista y la llamamos acá
        vista_pregunta = VistaPreguntaRonda()
        vista_pregunta.exec()

    def setRespuestaCorrecta(self, boton):
        pass

    def __asignar_temas(self):
        lista_qlabels = []
        lista_qlabels = self.__vista.lista_nombres_escalon()
        for i in range(0,8):
            lista_qlabels[i].setText((self.__lista_temas[i][1]).upper())

    def __asignar_jugadores(self, escalon): #Acá asigno al escalon
        self.__convertir_widget()
        # for i in self.__lista:
        #     layout.addWidget(i)
        escalon.set_jugadores(self.__lista)
        self.__escalon1.set_jugadores(self.__lista)

    def __convertir_widget(self):
        for i in self.__lista:
            self.__lista_jugadores_widget.append(WidgetJugador((i)[1],(i)[2]))
            #self.__vista.ly_escalon1.addWidget(self.__lista_jugadores_widget(i))
            
    # def agregar_ly1 (self):
    #     for i in self.__lista_jugadores_widget:
    #         self.__vista.ly_escalon1.addWidget(i)
            