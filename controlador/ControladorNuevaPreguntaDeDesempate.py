from vista.VistaNuevaPreguntaDeDesempate import Ui_MainWindow
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from modelo.PreguntasABM import PreguntaABM
from modelo.preguntaDesempate import preguntaDesempate
from controlador.ControladorEstaSeguro import ControladorEstaSeguro
from PyQt6.QtWidgets import QTextEdit
import os

class ControladorNuevaPreguntaDeDesempate(): 
    def __init__(self, controlador_anterior, id_tema):
        self.__id_tema = id_tema
        self.__pregunta = preguntaDesempate(id_tema, "", "")
        self.__controlador_anterior = controlador_anterior
        self.__vista = Ui_MainWindow() # Me parece que aca podria agregar el self.__id_tema para qeu la vista muestre el tema en el que va a gregar la preguta
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        #Aplicar estilos desde un archivo relativo
        self.__aplicar_estilos()

        self.__vista.get_button_cancelar().clicked.connect(self.__cancelar)
        self.__vista.get_button_aceptar().clicked.connect(self.__agregar_pregunta)
        
    def __cancelar(self): 
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __aplicar_estilos(self):
        estilos_path = os.path.join(os.path.dirname(__file__),"../vista/estilos.qss")
        if os.path.exists(estilos_path):
            with open(estilos_path, "r") as f:
                self.MainWindow.setStyleSheet(f.read())
        else:
            print(f"Advertencia: No se encontró el archivo de estilos en {estilos_path}.")


    def __agregar_pregunta(self):
        controlador_seguro = ControladorEstaSeguro("¿Está seguro de agregar esta pregunta?")
        if controlador_seguro.exec():  # `exec` con el usuario cierra el diálogo
            valor = self.__vista.lineEdit_7.text().strip()  # Usamos text() para QLineEdit
            enunciado = self.__vista.lineEdit_2.text().strip()  # Usamos text() para QLineEdit
            if valor and enunciado:
                if self.__es_entero(valor):
                    valor_int = int(valor)
                    enunciado = self.__vista.lineEdit_2.text()  # También se usa text() aquí
                    self.__pregunta.set_enunciado(enunciado)
                    self.__pregunta.set_respuestaCorrecta(valor_int)
                    PreguntaABM().agregar_pregunta_desempate(self.__pregunta)
                    self.__controlador_anterior.mostrar_preguntas()
                    self.MainWindow.hide()
                    self.__controlador_anterior.MainWindow.show()
                else:
                    self.__mostrar_error("La respuesta no es un número entero válido.")
            else:
                self.__mostrar_error("No puede haber campos vacios.")
                
    def __es_entero(self, valor):
        try:
            int(valor)
            return True
        except ValueError:
            return False
            
    def __mostrar_error(self, mensaje):
        """Muestra un mensaje de error en un cuadro de mensaje (QMessageBox)."""
        mensaje_box = QMessageBox()
        mensaje_box.setIcon(QMessageBox.Icon.Critical)
        mensaje_box.setWindowTitle("Error")
        mensaje_box.setText(mensaje)
        mensaje_box.exec()