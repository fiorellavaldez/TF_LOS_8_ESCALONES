from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHeaderView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, lista_jugadores):
        MainWindow.resize(1080, 720)
        MainWindow.setWindowTitle("Seleccionar jugadores")
        MainWindow.setWindowIcon(QtGui.QIcon('vista/img/icono_ventana.png'))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("fondo_seleccion_jugadores")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setPixmap(QtGui.QPixmap("vista/img/elegir_jugador_titulo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setMaximumSize(QtCore.QSize(400, 70))
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.label_2 = QtWidgets.QLabel(text= "Buscar:",parent=self.centralwidget)
        self.label_2.setObjectName("texto_buscar")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        #lista_jugadores
        self.lista = lista_jugadores #debería estar en privado

        
        self.tableWidget = QtWidgets.QTableWidget(len(self.lista), 2)
        self.tableWidget.setHorizontalHeaderLabels(["Nombre", "Avatar"])

    
        # self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_cancelar = QtWidgets.QPushButton(text= "Cancelar",parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_cancelar.setFont(font)
        self.horizontalLayout_3.addWidget(self.bt_cancelar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.bt_aceptar = QtWidgets.QPushButton(text= "Aceptar", parent=self.centralwidget)
        self.horizontalLayout_3.addWidget(self.bt_aceptar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.bt_aceptar.setProperty("tipo","boton_vista_seleccion")
        self.bt_cancelar.setProperty("tipo","boton_vista_seleccion")

        #self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_table(self, lista_jugadores):
        """Actualiza la tabla con los datos proporcionados."""
        self.tableWidget.setRowCount(len(lista_jugadores))  # Ajusta la cantidad de filas
        for i, jugador in enumerate(lista_jugadores):
            # Columna 0: Nombre
            nombre_item = QtWidgets.QTableWidgetItem(jugador.get_nombre_jugador())
            nombre_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            # Cambiar el tamaño de la fuente para los nombres
            font = QtGui.QFont()
            font.setPointSize(14)  # Cambia el tamaño de la fuente (ajústalo a tu gusto)
            nombre_item.setFont(font)

            self.tableWidget.setItem(i, 0, nombre_item)
            self.tableWidget.setRowHeight(i, 40)  # Doble altura de la fila para los nombres

            # Columna 1: Avatar
            avatar_label = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap(jugador.get_avatar())
            if pixmap.isNull():
                pixmap = QtGui.QPixmap("vista/img/default_avatar.png")
            avatar_label.setPixmap(pixmap)
            avatar_label.setScaledContents(True)
            avatar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            avatar_label.setMaximumSize(QtCore.QSize(50, 50))
            self.tableWidget.setCellWidget(i, 1, avatar_label)
    
    def get_button_cancelar(self):
        return self.bt_cancelar
    
    def get_button_aceptar(self):
        return self.bt_aceptar
    
    def aviso_repeticion_jugador(self,nombre):
        msg=QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setWindowTitle("Jugador Ya Seleccionado")
        msg.setText(f'Jugador {nombre} ya ha sido seleccionado ')
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()
    
    def aviso_seleccionar_jugador(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setWindowTitle("Advertencia")
        msg.setText("Debe seleccionar un jugador primero.")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())