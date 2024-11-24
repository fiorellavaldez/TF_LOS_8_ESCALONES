from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_ConfigWindow(object):
    def setupUi(self, ConfigWindow):
        ConfigWindow.setObjectName("ConfigWindow")
        ConfigWindow.resize(800, 600)
        ConfigWindow.setWindowTitle("Configuración de Audio y Video")

        # Central widget
        self.centralwidget = QtWidgets.QWidget(ConfigWindow)
        self.centralwidget.setObjectName("centralwidget")
        ConfigWindow.setCentralWidget(self.centralwidget)

        # Layout principal
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(40, 40, 40, 40)
        self.main_layout.setSpacing(25)

        # Estilo general
        self.centralwidget.setStyleSheet(
            "background-color: #1e1e2f; color: #ffffff;"
        )

        # Título
        self.title_label = QtWidgets.QLabel("Configuración de Audio y Video", self.centralwidget)
        font = QtGui.QFont("Segoe UI", 28, QtGui.QFont.Weight.Bold)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("color: #00ffff;")
        self.main_layout.addWidget(self.title_label)

        # Botón para activar/desactivar música
        self.music_button = QtWidgets.QPushButton("Apagar Música", self.centralwidget)
        self.music_button.setFont(QtGui.QFont("Segoe UI", 16))
        self.music_button.setStyleSheet(
            "QPushButton {"
            "    background-color: #005f73;"
            "    border: 2px solid #00ffff;"
            "    border-radius: 10px;"
            "    padding: 10px;"
            "    color: #ffffff;"
            "}"
            "QPushButton:hover {"
            "    background-color: #00a4cc;"
            "}"
        )
        self.main_layout.addWidget(self.music_button)

        # Barra de volumen
        self.volume_layout = QtWidgets.QHBoxLayout()
        self.volume_label = QtWidgets.QLabel("Volumen de Música:", self.centralwidget)
        self.volume_label.setFont(QtGui.QFont("Segoe UI", 16))
        self.volume_label.setStyleSheet("color: #ffffff;")
        self.volume_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self.centralwidget)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        self.volume_slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.volume_slider.setTickInterval(10)
        self.volume_slider.setStyleSheet(
            "QSlider::groove:horizontal {"
            "    height: 8px;"
            "    background: #00ffff;"
            "    border-radius: 4px;"
            "}"
            "QSlider::handle:horizontal {"
            "    background: #005f73;"
            "    border: 2px solid #00ffff;"
            "    width: 20px;"
            "    height: 20px;"
            "    margin: -7px 0;"
            "    border-radius: 10px;"
            "}"
        )

        self.volume_layout.addWidget(self.volume_label)
        self.volume_layout.addWidget(self.volume_slider)
        self.main_layout.addLayout(self.volume_layout)

        # Botón para pantalla completa
        self.screen_button = QtWidgets.QPushButton("Pantalla Completa", self.centralwidget)
        self.screen_button.setFont(QtGui.QFont("Segoe UI", 16))
        self.screen_button.setStyleSheet(
            "QPushButton {"
            "    background-color: #005f73;"
            "    border: 2px solid #00ffff;"
            "    border-radius: 10px;"
            "    padding: 10px;"
            "    color: #ffffff;"
            "}"
            "QPushButton:hover {"
            "    background-color: #00a4cc;"
            "}"
        )
        self.main_layout.addWidget(self.screen_button)

        # Botón para volver atrás
        self.back_button = QtWidgets.QPushButton("Atrás", self.centralwidget)
        self.back_button.setFont(QtGui.QFont("Segoe UI", 16))
        self.back_button.setStyleSheet(
            "QPushButton {"
            "    background-color: #005f73;"
            "    border: 2px solid #00ffff;"
            "    border-radius: 10px;"
            "    padding: 10px;"
            "    color: #ffffff;"
            "}"
            "QPushButton:hover {"
            "    background-color: #00a4cc;"
            "}"
        )
        self.main_layout.addWidget(self.back_button)

    def get_music_button(self):
        return self.music_button

    def get_volume_slider(self):
        return self.volume_slider

    def get_screen_button(self):
        return self.screen_button

    def get_back_button(self):
        return self.back_button
    

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_ConfigWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())