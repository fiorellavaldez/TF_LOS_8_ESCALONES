import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

#Solucion para controlar el cierre de ventana. Fueza a hacerlo con el boton Volver.
#Se debe reemplazar en los controladores la instanciación del QMainWindow
class ControladorVentanaMain(QMainWindow):
    def __init__(self):
        super().__init__()

    def closeEvent(self, event):
        respuesta = QMessageBox.information(self, 'Atencion!', 'Utilice el boton VOLVER')
        event.ignore()
