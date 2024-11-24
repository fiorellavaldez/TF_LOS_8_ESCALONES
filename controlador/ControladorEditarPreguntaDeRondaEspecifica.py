from vista.VistaEditarPreguntaDeRondaEspecifica import Ui_MainWindow
from controlador.ControladorEstaSeguro import ControladorEstaSeguro
from modelo.PreguntasABM import PreguntaABM
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtWidgets

class ControladorEditarPreguntaDeRondaEspecifica():
    def __init__(self, controlador_anterior, pregunta_desempate):
        self.__pregunta = pregunta_desempate
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow(self.__pregunta.get_enunciado(),self.__pregunta.get_opcionA(), self.__pregunta.get_opcionB(), self.__pregunta.get_opcionC(), self.__pregunta.get_opcionD(), self.__pregunta.get_opcionCorrecta())
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__vista.get_button_atras().clicked.connect(self.__volver)
        self.__vista.get_button_aceptar().clicked.connect(lambda: self.__guardar(self.__pregunta))
        
        
    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()
    
    def __guardar(self, pregunta): #ESTOY ACÁ
        controlador_seguro = ControladorEstaSeguro("¿Está seguro de cambiar esta pregunta?")
        if controlador_seguro.exec():  # `exec` con el usuario cierra el diálogo
            self.__pregunta.set_enunciado(self.__vista.textEdit_2.toPlainText())
            self.__pregunta.set_opcionA(self.__vista.textEdit_4.toPlainText())
            self.__pregunta.set_opcionB(self.__vista.textEdit_5.toPlainText())
            self.__pregunta.set_opcionC(self.__vista.textEdit_3.toPlainText())
            self.__pregunta.set_opcionD(self.__vista.textEdit_6.toPlainText())
            valor = self.__vista.comboBox.currentIndex()
            mapa_opciones = {0: "A", 1: "B", 2: "C", 3: "D"}
            correcta = mapa_opciones.get(valor, None)
            self.__pregunta.set_opcionCorrecta(correcta)
            PreguntaABM().actualizar_preguntas_ronda(self.__pregunta)
            self.__controlador_anterior.mostrar_preguntas()
            self.MainWindow.hide()
            self.__controlador_anterior.MainWindow.show()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
"""
            valor = self.__vista.textEdit.toPlainText().strip()  # Elimina espacios en blanco
            if valor:
                if self.__es_entero(valor):
                    valor_int = int(valor)
                    enunciado = self.__vista.textEdit_2.toPlainText()
                    pregunta.set_enunciado(enunciado)
                    pregunta.set_respuestaCorrecta(valor_int)
                    PreguntaABM().actualizar_preguntas_desempate(self.__pregunta)
                    self.__controlador_anterior.actualizar_lista_preguntas()
                    self.MainWindow.hide()
                    self.__controlador_anterior.MainWindow.show()
                else:
                    self.__mostrar_error("La respuesta no es un número entero válido.")
            else:
                self.__mostrar_error("El campo de respuesta está vacío.")
    def __es_entero(self, valor):
        try:
            int(valor)
            return True
        except ValueError:
            return False
        
    def __mostrar_error(self, mensaje):
            #### Muestra un mensaje de error en un cuadro de mensaje (QMessageBox)
        mensaje_box = QMessageBox()
        mensaje_box.setIcon(QMessageBox.Icon.Critical)
        mensaje_box.setWindowTitle("Error")
        mensaje_box.setText(mensaje)
        mensaje_box.exec() """