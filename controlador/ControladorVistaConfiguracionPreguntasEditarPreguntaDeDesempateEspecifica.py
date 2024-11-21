from vista.VistaConfiguracionPreguntasEditarPreguntaDeDesempate import Ui_MainWindow
from PyQt6 import QtWidgets
from modelo.PreguntasABM import PreguntaABM
from PyQt6.QtWidgets import QMessageBox

class ControladorVistaConfiguracionPreguntasEditarPreguntaDeDesempateEspecifica():
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
        valor = self.__vista.textEdit.toPlainText().strip()  # Elimina espacios en blanco al principio y al final
        if valor:  # Verifica si no está vacío
            if self.__es_entero(valor):  # Verifica si el valor es un número entero válido
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
        """Verifica si un valor puede ser convertido a entero."""
        try:
            int(valor)  # Intenta convertirlo a entero
            return True  # Si no lanza excepción, es un número entero válido
        except ValueError:
            return False  # Si lanza excepción, no es un entero

    def __mostrar_error(self, mensaje):
        """Muestra un mensaje de error en un cuadro de mensaje (QMessageBox)."""
        mensaje_box = QMessageBox()
        mensaje_box.setIcon(QMessageBox.Icon.Critical)
        mensaje_box.setWindowTitle("Error")
        mensaje_box.setText(mensaje)
        mensaje_box.exec()
