from PyQt6 import QtWidgets, QtCore
class DialogDesempate(QtWidgets.QDialog):
    def __init__(self, jugadores_empate: list, jugador_eliminado: str, distancias: dict, respuesta_correcta: str):
        super().__init__()
        self.setWindowTitle("Resultado del desempate")
        self.resize(500, 300)
        self.setup_ui(jugadores_empate, jugador_eliminado, distancias, respuesta_correcta)

    def setup_ui(self, jugadores_empate: list, jugador_eliminado: str, distancias: dict, respuesta_correcta: str):
        layout = QtWidgets.QVBoxLayout(self)

        # Título
        lbl_titulo = QtWidgets.QLabel("Resultado del desempate")
        lbl_titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = lbl_titulo.font()
        font.setPointSize(12)
        lbl_titulo.setFont(font)
        layout.addWidget(lbl_titulo)

        # Respuesta correcta
        lbl_respuesta_correcta = QtWidgets.QLabel(f"La respuesta correcta es: {respuesta_correcta}")
        lbl_respuesta_correcta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font_respuesta_correcta = lbl_respuesta_correcta.font()
        font_respuesta_correcta.setBold(True)
        lbl_respuesta_correcta.setFont(font_respuesta_correcta)
        layout.addWidget(lbl_respuesta_correcta)

        # Distancias de los jugadores
        lbl_distancias = QtWidgets.QLabel("Distancias de los jugadores:")
        layout.addWidget(lbl_distancias)

        for jugador, distancia in distancias.items():
            lbl_jugador = QtWidgets.QLabel(f"{jugador.get_nombre_jugador()}: {distancia} de distancia")
            layout.addWidget(lbl_jugador)

        # Mostrar el jugador eliminado
        lbl_eliminado = QtWidgets.QLabel(f"Jugador eliminado: {jugador_eliminado.get_nombre_jugador()}")
        lbl_eliminado.setStyleSheet("color: red; font-weight: bold;")
        lbl_eliminado.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lbl_eliminado)
        
        # Botón de cierre
        btn_cerrar = QtWidgets.QPushButton("Cerrar")
        btn_cerrar.clicked.connect(self.accept)
        layout.addWidget(btn_cerrar)

