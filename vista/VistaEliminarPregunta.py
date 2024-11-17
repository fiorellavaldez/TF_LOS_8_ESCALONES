from PyQt6.QtWidgets import ( QMainWindow, QWidget, QVBoxLayout, QLabel,
    QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QStatusBar
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configuración principal de la ventana
        self.setWindowTitle("MainWindow")
        self.setGeometry(0, 0, 365, 165)

        # Widget central
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # Layout principal (vertical)
        self.verticalLayout = QVBoxLayout(self.centralwidget)

        # Etiqueta con texto
        self.label = QLabel(self.centralwidget)
        font_label = QFont()
        font_label.setPointSize(35)
        self.label.setFont(font_label)
        self.label.setText(
            "<html><head/><body>"
            "<p><span style='font-size:11pt;'>¿Está seguro de que desea borrar la pregunta?</span></p>"
            "<p><span style='font-size:11pt;'>Esta acción no se puede deshacer.</span></p>"
            "</body></html>"
        )
        self.verticalLayout.addWidget(self.label)

        # Layout horizontal para los botones
        self.horizontalLayout = QHBoxLayout()

        # Botón "Cancelar"
        self.pushButton_2 = QPushButton("Cancelar", self.centralwidget)
        font_button = QFont()
        font_button.setPointSize(13)
        self.pushButton_2.setFont(font_button)
        self.horizontalLayout.addWidget(self.pushButton_2)

        # Espaciador
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        # Botón "Aceptar"
        self.pushButton_3 = QPushButton("Aceptar", self.centralwidget)
        self.pushButton_3.setFont(font_button)
        self.horizontalLayout.addWidget(self.pushButton_3)

        # Agregar el layout horizontal al layout principal
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Barra de estado
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)


#if __name__ == "__main__":
#    import sys
#    app = QApplication(sys.argv)
#    mainWindow = MainWindow()
#    mainWindow.show()
#    sys.exit(app.exec())
