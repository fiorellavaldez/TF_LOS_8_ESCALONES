from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHeaderView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        # self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget) ####
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        # self.tableWidget.setSizePolicy(sizePolicy)
        # self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        # self.tableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        # self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.tableWidget.setFont(font)
        # self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(3)
        # self.tableWidget.setRowCount(1)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditSelectAll")
        # item.setIcon(icon)
        # self.tableWidget.setItem(0, 2, item)
        jugadores = [
        ("Jugador 1", "vista/img/al.jpg"),
        ("Jugador 2", "vista/img/ta.png"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),
        ("Jugador 3", "vista/img/da.jpg"),]
        self.tableWidget = QtWidgets.QTableWidget(len(jugadores), 2)
        self.tableWidget.setHorizontalHeaderLabels(["Nombre", "Avatar"])

        for row, (nombre, avatar_path) in enumerate(jugadores):
            # Columna de nombres
            item_nombre = QtWidgets.QTableWidgetItem(nombre)
            item_nombre.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.tableWidget.setItem(row, 0, item_nombre)
            # Columna de imágenes
            label_avatar = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap(avatar_path)
            label_avatar.setPixmap(pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            label_avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget.setCellWidget(row, 1, label_avatar)


        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    #     self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Elegir Jugador</span></p></body></html>"))
    #     self.label_2.setText(_translate("MainWindow", "Buscar:  "))
    #     item = self.tableWidget.verticalHeaderItem(0)
    #     item.setText(_translate("MainWindow", "Nombre"))
    #     item = self.tableWidget.horizontalHeaderItem(0)
    #     item.setText(_translate("MainWindow", "Jugador"))
    #     item = self.tableWidget.horizontalHeaderItem(1)
    #     item.setText(_translate("MainWindow", "Avatar"))
    #     item = self.tableWidget.horizontalHeaderItem(2)
    #     item.setText(_translate("MainWindow", ""))
    #     __sortingEnabled = self.tableWidget.isSortingEnabled()
    #     self.tableWidget.setSortingEnabled(False)
    #     item = self.tableWidget.item(0, 0)
    #     item.setText(_translate("MainWindow", "<nombre>"))
    #     item = self.tableWidget.item(0, 1)
    #     item.setText(_translate("MainWindow", "<foto>"))
    #     self.tableWidget.setSortingEnabled(__sortingEnabled)
    #     self.pushButton_2.setText(_translate("MainWindow", "Atrás"))
    #     self.pushButton.setText(_translate("MainWindow", "Aceptar"))

    def get_button_atras(self):
        return self.pushButton_2
    
    def get_button_aceptar(self):
        return self.pushButton

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())