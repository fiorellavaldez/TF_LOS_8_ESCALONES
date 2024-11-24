from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
from controlador.ControladorPreguntaDesempateABM import ControladorVistaConfiguracionModificarPreguntasDesempate
from vista.VistaConfiguracionPreguntaNuevaDesempate import Ui_MainWindow  # Asegúrate de cambiar "tu_diseno" por el nombre correcto de tu archivo con el diseño.


class ControladorConfiguracionPreguntaNuevaDesempate:
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_controlador()

    def init_controlador(self):
        # Conectar los botones a las funciones correspondientes
        self.ui.get_button_aceptar().clicked.connect(self.aceptar)
        self.ui.get_button_atras().clicked.connect(self.cancelar)

    def aceptar(self):
        # Obtener los datos de las cajas de texto
        pregunta = self.ui.question_input.text()
        respuesta = self.ui.correct_answer_input.text()

        if not pregunta.strip() or not respuesta.strip():
            # Mostrar advertencia si falta información
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos.")
            return

        # Aquí podrías procesar la información (por ejemplo, guardar en una base de datos)
        QMessageBox.information(self, "Información", f"Pregunta: {pregunta}\nRespuesta: {respuesta}")

    def cancelar(self):
        # Confirmar salida o limpiar los campos
        respuesta = QMessageBox.question(self, "Cancelar", "¿Está seguro de que desea cancelar?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if respuesta == QMessageBox.StandardButton.Yes:
            self.close()  # Cierra la ventana


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ventana = MainWindowController()
#     ventana.show()
#     sys.exit(app.exec())
