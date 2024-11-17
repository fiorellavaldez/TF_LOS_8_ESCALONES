from PyQt6 import QtCore, QtGui, QtWidgets


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
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        
        # Spacer para empujar los botones hacia la derecha
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        
        # Botón "Modificar pregunta"
        self.pushButton_modificar = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_modificar.setFont(font)
        self.pushButton_modificar.setObjectName("pushButton_modificar")
        self.pushButton_modificar.setText("Modificar pregunta")  # El texto del nuevo botón
        self.horizontalLayout_3.addWidget(self.pushButton_modificar)
        
        # Botón "Eliminar pregunta"
        self.pushButton_eliminar = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_eliminar.setFont(font)
        self.pushButton_eliminar.setObjectName("pushButton_eliminar")
        self.pushButton_eliminar.setText("Eliminar pregunta")  # El texto del nuevo botón
        self.horizontalLayout_3.addWidget(self.pushButton_eliminar)
        
        # Botón "Agregar nueva pregunta"
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_3.addWidget(self.pushButton_12)

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.tableWidget.setColumnWidth(0,877)
        self.tableWidget.setColumnWidth(2,40)
        self.tableWidget.setColumnWidth(3,40)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Preguntas de desempate: Historia</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Buscar:  "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pregunta"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Respuesta"))
        self.pushButton_2.setText(_translate("MainWindow", "Atrás"))
        self.pushButton_12.setText(_translate("MainWindow", "Agregar nueva pregunta"))
        self.pushButton_modificar.setText(_translate("MainWindow", "Modificar pregunta"))
        self.pushButton_eliminar.setText(_translate("MainWindow", "Eliminar pregunta"))

    def get_button_atras(self):
        return self.pushButton_2

    def get_button_agregar_pregunta(self):
        return self.pushButton_12

    def get_button_modificar_pregunta(self):
        return self.pushButton_modificar

    def get_button_eliminar_pregunta(self):
        return self.pushButton_eliminar




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
#         self.tableWidget.setColumnCount(4)
#         self.tableWidget.setRowCount(0)
#         item = QtWidgets.QTableWidgetItem()
#         item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
#         self.tableWidget.setHorizontalHeaderItem(0, item)
#         item = QtWidgets.QTableWidgetItem()
#         self.tableWidget.setHorizontalHeaderItem(1, item)
#         item = QtWidgets.QTableWidgetItem()
#         self.tableWidget.setHorizontalHeaderItem(2, item)
#         item = QtWidgets.QTableWidgetItem()
#         self.tableWidget.setHorizontalHeaderItem(3, item)
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
#         self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.pushButton_12.setFont(font)
#         self.pushButton_12.setObjectName("pushButton_12")
#         self.horizontalLayout.addWidget(self.pushButton_12)
#         self.horizontalLayout_3.addLayout(self.horizontalLayout)
#         self.verticalLayout.addLayout(self.horizontalLayout_3)
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#         self.tableWidget.setColumnWidth(0,877)
#         self.tableWidget.setColumnWidth(2,40)
#         self.tableWidget.setColumnWidth(3,40)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Preguntas de desempate: Historia</span></p></body></html>"))
#         self.label_2.setText(_translate("MainWindow", "Buscar:  "))
#         item = self.tableWidget.horizontalHeaderItem(0)
#         item.setText(_translate("MainWindow", "Pregunta"))
#         item = self.tableWidget.horizontalHeaderItem(1)
#         item.setText(_translate("MainWindow", "Respuesta"))
#         self.pushButton_2.setText(_translate("MainWindow", "Atrás"))
#         self.pushButton_12.setText(_translate("MainWindow", "Agregar nueva pregunta"))

#     def get_button_atras(self):
#         return self.pushButton_2

#     def get_button_agregar_pregunta(self):
#         return self.pushButton_12