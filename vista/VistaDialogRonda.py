from PyQt6 import QtWidgets, QtCore

class DialogRonda(QtWidgets.QDialog):
    def __init__(self, jugador, correcta: bool, respuesta_correcta: str):
        super().__init__()
        self.setWindowTitle("Resultado de la ronda")
        self.resize(400, 200)
        self.setup_ui(jugador, correcta, respuesta_correcta)

    def setup_ui(self, jugador, correcta: bool, respuesta_correcta: str):
        layout = QtWidgets.QVBoxLayout(self)

        # Mensaje principal
        if correcta:
            mensaje = f"¡{jugador} respondió correctamente! 🎉"
        else:
            mensaje = f"¡{jugador} respondió incorrectamente! 😔"

        lbl_mensaje = QtWidgets.QLabel(mensaje)
        lbl_mensaje.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lbl_mensaje)

        # Mostrar la respuesta correcta
        lbl_respuesta = QtWidgets.QLabel(f"Respuesta correcta: {respuesta_correcta}")
        lbl_respuesta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lbl_respuesta)

        # Botón de cierre
        btn_cerrar = QtWidgets.QPushButton("Cerrar")
        btn_cerrar.clicked.connect(self.accept)
        layout.addWidget(btn_cerrar)


