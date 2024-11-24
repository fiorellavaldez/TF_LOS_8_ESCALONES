from vista.VistaEditarPreguntaDeDesempate import Ui_MainWindow
from modelo.PreguntasABM import PreguntaABM
from controlador.ControladorEstaSeguro import ControladorEstaSeguro
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtWidgets

class ControladorEditarPreguntaDeDesempate(): 
    def __init__(self, controlador_anterior, pregunta_desempate):
        self.__pregunta = pregunta_desempate
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow, self.__pregunta.get_enunciado(), self.__pregunta.get_respuestaCorrecta())
        self.MainWindow.show()

        self.__vista.get_button_atras().clicked.connect(self.__volver)
        self.__vista.get_button_aceptar().clicked.connect(lambda: self.__guardar(self.__pregunta))

    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __guardar(self, pregunta):
        controlador_seguro = ControladorEstaSeguro("¿Está seguro de cambiar esta pregunta?")
        if controlador_seguro.exec():  # `exec` con el usuario cierra el diálogo
            valor = self.__vista.textEdit.toPlainText().strip()  # Elimina espacios en blanco
            if valor:
                if self.__es_entero(valor):
                    valor_int = int(valor)
                    enunciado = self.__vista.textEdit_2.toPlainText()
                    pregunta.set_enunciado(enunciado)
                    pregunta.set_respuestaCorrecta(valor_int)
                    PreguntaABM().actualizar_preguntas_desempate(self.__pregunta)
                    self.__controlador_anterior.mostrar_preguntas()
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
        """Muestra un mensaje de error en un cuadro de mensaje (QMessageBox)."""
        mensaje_box = QMessageBox()
        mensaje_box.setIcon(QMessageBox.Icon.Critical)
        mensaje_box.setWindowTitle("Error")
        mensaje_box.setText(mensaje)
        mensaje_box.exec()
