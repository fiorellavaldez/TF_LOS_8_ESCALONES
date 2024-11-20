from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Encabezado
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        # Espaciador entre encabezado y contenido
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)

        # Buscar tema
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

        # Tabla
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)  # Solo una columna
        self.tableWidget.setRowCount(0)

        # Cabecera de tabla
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)

        # Configuración de la tabla
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionsMovable(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.verticalLayout.addWidget(self.tableWidget)

        # Botones
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Botón "Atrás" a la izquierda
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)

        # Espaciador para separar botones
        spacerItem_buttons = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem_buttons)

        # Botón "Eliminar Tema"
        self.pushButton_eliminar = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_eliminar.setFont(font)
        self.pushButton_eliminar.setObjectName("pushButton_eliminar")
        self.horizontalLayout_3.addWidget(self.pushButton_eliminar)

        # Botón "Cambiar Nombre"
        self.pushButton_cambiar = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_cambiar.setFont(font)
        self.pushButton_cambiar.setObjectName("pushButton_cambiar")
        self.horizontalLayout_3.addWidget(self.pushButton_cambiar)

        # Nuevo botón "Agregar Tema Nuevo" a la derecha
        self.pushButton_agregar = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_agregar.setFont(font)
        self.pushButton_agregar.setObjectName("pushButton_agregar")
        self.horizontalLayout_3.addWidget(self.pushButton_agregar)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # Configuración final
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("VistaConfiguracionModificarTema", "VistaConfiguracionModificarTema Temas"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Modificar Temas</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Buscar:  "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Descripción Tema"))
        self.pushButton_2.setText(_translate("MainWindow", "Atrás"))
        self.pushButton_eliminar.setText(_translate("MainWindow", "Eliminar Tema"))
        self.pushButton_cambiar.setText(_translate("MainWindow", "Cambiar Nombre"))
        self.pushButton_agregar.setText(_translate("MainWindow", "Agregar Tema Nuevo"))

    def get_button_atras(self):
        return self.pushButton_2

    def get_button_eliminar(self):
        return self.pushButton_eliminar

    def get_button_cambiar(self):
        return self.pushButton_cambiar

    def get_button_agregar(self):
        return self.pushButton_agregar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())



# from PyQt6 import QtCore, QtGui, QtWidgets


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1080, 720)
#         self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.verticalLayout_3 = QtWidgets.QVBoxLayout()
#         self.verticalLayout_3.setObjectName("verticalLayout_3")
#         self.label = QtWidgets.QLabel(parent=self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(9)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         self.verticalLayout_3.addWidget(self.label)
#         self.verticalLayout.addLayout(self.verticalLayout_3)
#         spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
#         self.verticalLayout.addItem(spacerItem)
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.label_2.setFont(font)
#         self.label_2.setObjectName("label_2")
#         self.horizontalLayout_2.addWidget(self.label_2)
#         self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.lineEdit.setFont(font)
#         self.lineEdit.setObjectName("lineEdit")
#         self.horizontalLayout_2.addWidget(self.lineEdit)
#         self.verticalLayout.addLayout(self.horizontalLayout_2)
#         self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.tableWidget.setFont(font)
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setColumnCount(3)
#         self.tableWidget.setRowCount(0)
#         item = QtWidgets.QTableWidgetItem()
#         item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
#         self.tableWidget.setHorizontalHeaderItem(0, item)
#         item = QtWidgets.QTableWidgetItem()
#         self.tableWidget.setHorizontalHeaderItem(1, item)
#         item = QtWidgets.QTableWidgetItem()
#         self.tableWidget.setHorizontalHeaderItem(2, item)
#         self.verticalLayout.addWidget(self.tableWidget)
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")
#         self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.pushButton_2.setFont(font)
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.horizontalLayout_3.addWidget(self.pushButton_2)
#         spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
#         self.horizontalLayout_3.addItem(spacerItem1)
#         self.horizontalLayout = QtWidgets.QHBoxLayout()
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.horizontalLayout_3.addLayout(self.horizontalLayout)
#         self.verticalLayout.addLayout(self.horizontalLayout_3)
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#         self.tableWidget.setColumnWidth(0,977)
#         self.tableWidget.setColumnWidth(1,40)
#         self.tableWidget.setColumnWidth(2,40)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Modificar Temas</span></p></body></html>"))
#         self.label_2.setText(_translate("MainWindow", "Buscar:  "))
#         item = self.tableWidget.horizontalHeaderItem(0)
#         item.setText(_translate("MainWindow", "Tema"))
#         self.pushButton_2.setText(_translate("MainWindow", "Atrás"))

#     def get_button_atras(self):
#         return self.pushButton_2