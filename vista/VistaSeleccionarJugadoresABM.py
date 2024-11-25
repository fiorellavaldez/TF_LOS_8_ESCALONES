from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHeaderView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1080, 720)
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
        self.label_2 = QtWidgets.QLabel(text="Buscar:", parent=self.centralwidget)
        self.label_2.setObjectName("texto_buscar")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # Configuración inicial de la tabla
        self.tableWidget = QtWidgets.QTableWidget(0, 2)  # 0 filas iniciales
        self.tableWidget.setHorizontalHeaderLabels(["Nombre", "Avatar"])
        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.bt_cancelar = QtWidgets.QPushButton(text="Atrás", parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_cancelar.setFont(font)
        self.horizontalLayout_3.addWidget(self.bt_cancelar)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)

        # Botones adicionales
        self.bt_nuevo = QtWidgets.QPushButton(text="Nuevo jugador", parent=self.centralwidget)
        self.bt_nuevo.setFont(font)
        self.horizontalLayout_3.addWidget(self.bt_nuevo)

        self.bt_modificar = QtWidgets.QPushButton(text="Modificar jugador", parent=self.centralwidget)
        self.bt_modificar.setFont(font)
        self.horizontalLayout_3.addWidget(self.bt_modificar)

        self.bt_eliminar = QtWidgets.QPushButton(text="Eliminar jugador", parent=self.centralwidget)
        self.bt_eliminar.setFont(font)
        self.horizontalLayout_3.addWidget(self.bt_eliminar)

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        MainWindow.setStatusBar(self.statusbar)

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

        # Ajustar columnas
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
    
    def aviso_seleccionar_jugador(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setWindowTitle("Advertencia")
        msg.setText("Debe seleccionar un jugador primero.")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()


    # Métodos para exponer botones al Controlador
    def get_button_cancelar(self):
        return self.bt_cancelar

    def get_button_nuevo(self):
        return self.bt_nuevo

    def get_button_modificar(self):
        return self.bt_modificar

    def get_button_eliminar(self):
        return self.bt_eliminar
