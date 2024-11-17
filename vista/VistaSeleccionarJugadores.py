from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHeaderView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, lista_jugadores):
        MainWindow.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel(text= "Elegir jugador",parent=self.centralwidget)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.label_2 = QtWidgets.QLabel(text= "Buscar:",parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
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

        for row, (id, nombre, avatar_path) in enumerate(self.lista):
            # Columna nombres
            item_nombre = QtWidgets.QTableWidgetItem(nombre)
            item_nombre.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
            item_nombre.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.tableWidget.setItem(row, 0, item_nombre)
            # Columna avatares
            label_avatar = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap(avatar_path)
            label_avatar.setPixmap(pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            label_avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget.setCellWidget(row, 1, label_avatar)

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

        #self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_button_cancelar(self):
        return self.bt_cancelar
    
    def get_button_aceptar(self):
        return self.bt_aceptar
    
    # def muestra_jugadores_en_tabla(self):

    def get_tableWidget(self):
        return self.tableWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())