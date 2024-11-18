from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 391)
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
        self.question_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.question_input.setGeometry(QtCore.QRect(10, 120, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.question_input.setFont(font)
        self.question_input.setObjectName("question_input")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(290, 310, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.correct_answer_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.correct_answer_input.setGeometry(QtCore.QRect(10, 230, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.correct_answer_input.setFont(font)
        self.correct_answer_input.setObjectName("correct_answer_input")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 310, 131, 51))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Editar pregunta</span></p></body></html>"))
        self.question_input.setPlaceholderText(_translate("MainWindow", "Ingrese la pregunta aquí"))
        self.pushButton_12.setText(_translate("MainWindow", "Aceptar"))
        self.correct_answer_input.setPlaceholderText(_translate("MainWindow", "Ingrese la respuesta correcta aquí"))
        self.pushButton_13.setText(_translate("MainWindow", "Cancelar"))

    def get_button_atras(self):
        return self.pushButton_13

    def get_button_aceptar(self):
        return self.pushButton_12
