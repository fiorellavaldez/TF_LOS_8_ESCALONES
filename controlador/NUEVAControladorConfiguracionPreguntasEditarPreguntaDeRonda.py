from vista.NUEVAVistaConfiguracionPreguntasNuevaPreguntaDeRonda  import Ui_MainWindow
from modelo.PreguntasABM import PreguntaABM
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtWidgets
from modelo.preguntaRonda import preguntaRonda

class NUEVAControladorConfiguracionPreguntasEditarPreguntaDeRonda(): #### FALTA EDITAR TODO DE ESTE ES UAN COPIA DE EDITAR
    def __init__(self, controlador_anterior, id_tema):
        self.__pregunta = preguntaRonda(id_tema, "", "", "", "", "", "")
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
    
        self.__vista.get_button_atras().clicked.connect(self.__volver)
        self.__vista.get_button_aceptar().clicked.connect(self.__guardar)
        
    def __volver(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()
    
    def __guardar(self):
        enunciado = self.__vista.textEdit_2.toPlainText()
        rtaA = self.__vista.textEdit_4.toPlainText()
        rtaB = self.__vista.textEdit_5.toPlainText()
        rtaC = self.__vista.textEdit_3.toPlainText()
        rtaD = self.__vista.textEdit_6.toPlainText()
        
        if not enunciado or not rtaA or not rtaB or not rtaC or not rtaD:
            # Mostrar mensaje de error al usuario
            self.mostrar_mensaje("Todos los campos deben estar llenos para guardar la pregunta.")
            return  # Salir del método si hay campos vacíos
        valor = self.__vista.comboBox.currentIndex()
        mapa_opciones = {0: "A", 1: "B", 2: "C", 3: "D"}
        self.__pregunta.set_enunciado( enunciado)
        self.__pregunta.set_opcionA(rtaA)
        self.__pregunta.set_opcionB(rtaB)
        self.__pregunta.set_opcionC(rtaC)
        self.__pregunta.set_opcionD(rtaD)
        correcta = mapa_opciones.get(valor, None)
        self.__pregunta.set_opcionCorrecta(correcta)
        PreguntaABM().agregar_pregunta_ronda(self.__pregunta)
        self.__controlador_anterior.actualizar_lista_preguntas()
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()
    
    def mostrar_mensaje(self, mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(mensaje)
        msg.setWindowTitle("Error")
        msg.exec()
