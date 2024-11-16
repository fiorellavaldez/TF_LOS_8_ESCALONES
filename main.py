from controlador.ControladorPantallaInicio import ControladorPantallaInicio
from PyQt6 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controlador = ControladorPantallaInicio()
    sys.exit(app.exec())

