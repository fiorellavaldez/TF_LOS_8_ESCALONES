from vista.VistaConfiguracionTemaABMEdit import Ui_Widget
from modelo.Tema import Tema
from modelo.TemaABM import TemaABM
from PyQt6 import QtWidgets

class ControladorVistaConfiguracionTemaABMEdit:
    def __init__(self, controlador_anterior=None,tema:Tema=None,temas:TemaABM=None):   # Se ingresa la lista de temas como parametro para consistencia
        self._controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QWidget()
        self._vista = Ui_Widget()
        self._vista.setupUi(self.MainWindow)
        self._vista.label_Titulo.setText("")
        self._vista.label_Mensaje.setText("")
        self._vista.lineEdit_Tema.setText(tema.get_nombreTema())
        self._tema = tema
        self._temas = temas
  
        self._vista.buttonBox_Confirmar.rejected.connect(self._volver_configuracion)

    def _volver_configuracion(self):
        self.MainWindow.hide()
        self._controlador_anterior.MainWindow.show()




        