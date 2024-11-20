from vista.VistaConfiguracionPreguntasAgregarPreguntaDeDesempate import Ui_MainWindow
from PyQt6 import QtWidgets
from modelo.PreguntasABM import PreguntaABM
from modelo.preguntaDesempate import preguntaDesempate


class ControladorConfiguracionPreguntasAgregarPreguntaDeDesempate():
    def __init__(self, controlador_anterior, id_tema):
        self.__id_tema = id_tema
        self.__controlador_anterior = controlador_anterior
        self.__vista = Ui_MainWindow() # Me parece que aca podria agregar el self.__id_tema para qeu la vista muestre el tema en el que va a gregar la preguta
        self.MainWindow = QtWidgets.QMainWindow()
        
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.__vista.get_button_cancelar().clicked.connect(self.__cancelar)
        self.__vista.get_button_aceptar().clicked.connect(self.__agregar_pregunta)
        
    def __cancelar(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()
    
    def __agregar_pregunta(self):
        #Armo el objeto pregunta
        enunciado = self.__vista.lineEdit_2.text()
        respuesta = self.__vista.lineEdit_7.text()
        pregunta = preguntaDesempate(self.__id_tema, enunciado, respuesta)
        PreguntaABM().agregar_pregunta_desempate(pregunta)
        # Vuelve a la pantalla anterior pero tengo que ver si funciona bien
        self.__controlador_anterior(self.__id_tema)
        
        
        #self.MainWindow.hide()
        #self.__controlador_anterior.MainWindow.show()