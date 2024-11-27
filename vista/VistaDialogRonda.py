from PyQt6 import QtWidgets,QtGui, QtCore

class DialogRonda(QtWidgets.QDialog):
    def __init__(self, jugador, opciones, correcta: bool, respuesta_correcta: str):
        super().__init__()
        self.setWindowTitle("Resultado de la ronda")
        self.resize(400, 200)
        self.setup_ui(jugador, opciones, correcta, respuesta_correcta)

    def setup_ui(self, jugador, opciones, correcta: bool, respuesta_correcta: str):
        layout = QtWidgets.QVBoxLayout(self)

        # Mensaje principal
        if correcta:
            mensaje = f"¡{jugador} respondió BIEN! 🎉"
            self.setWindowIcon(QtGui.QIcon('vista/img/icono_resultado_correcto.png'))
        else:
            mensaje = f"¡{jugador} respondió MAL! 😔"
            self.setWindowIcon(QtGui.QIcon('vista/img/icono_resultado_incorrecto.png'))

        lbl_mensaje = QtWidgets.QLabel(mensaje)
        lbl_mensaje.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        lbl_mensaje.setFont(font)
        layout.addWidget(lbl_mensaje)

        # Mostrar la respuesta correcta
        if respuesta_correcta== "A":
            correcta_texto = opciones[0]
        elif respuesta_correcta=="B":
            correcta_texto = opciones[1]
        elif respuesta_correcta=="C":
            correcta_texto = opciones[2]
        elif respuesta_correcta=="D":
            correcta_texto = opciones[3]
            
        lbl_respuesta = QtWidgets.QLabel(f"Respuesta correcta: {respuesta_correcta}) {correcta_texto}")
        lbl_respuesta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lbl_respuesta)

        # Botón de cierre
        btn_cerrar = QtWidgets.QPushButton("Cerrar")
        btn_cerrar.clicked.connect(self.accept)
        layout.addWidget(btn_cerrar)


