from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 570)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(9, 9, 411, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)

        # Etiqueta "Enunciado"
        self.label_enunciado = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_enunciado.setGeometry(QtCore.QRect(10, 120, 70, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_enunciado.setFont(font)
        self.label_enunciado.setObjectName("label_enunciado")

        # Caja de texto para "Enunciado"
        self.textEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 120, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")

        # Cajas de texto reemplazando label_3 a label_6
        self.textEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(50, 180, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")

        self.textEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(50, 240, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")

        self.textEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(50, 300, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")

        self.textEdit_6 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(50, 360, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setObjectName("textEdit_6")

        # Labels para opciones a), b), c), d)
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 180, 30, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 240, 30, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 300, 30, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 360, 30, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 430, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(340, 430, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(290, 490, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 490, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Agregar pregunta</span></p></body></html>"))
        self.label_enunciado.setText(_translate("MainWindow", "Enunciado:"))
        self.label_8.setText(_translate("MainWindow", "a)"))
        self.label_9.setText(_translate("MainWindow", "b)"))
        self.label_10.setText(_translate("MainWindow", "c)"))
        self.label_11.setText(_translate("MainWindow", "d)"))
        self.label_7.setText(_translate("MainWindow", "Respuesta correcta:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "a)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "b)"))
        self.comboBox.setItemText(2, _translate("MainWindow", "c)"))
        self.comboBox.setItemText(3, _translate("MainWindow", "d)"))
        self.pushButton_12.setText(_translate("MainWindow", "Aceptar"))
        self.pushButton_13.setText(_translate("MainWindow", "Cancelar"))
        
    def get_button_atras(self):
        return self.pushButton_13

    def get_button_aceptar(self):
        return self.pushButton_12
