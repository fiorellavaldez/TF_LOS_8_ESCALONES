from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        # Inicializamos los atributos para almacenar los valores
        self.enunciado = ""
        self.respuesta = ""

    def setupUi(self, MainWindow, enunciado="", respuesta=""):
        # Guardamos los valores en los atributos de instancia
        self.enunciado = enunciado
        self.respuesta = respuesta

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 400)
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
        self.listView_2 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(10, 120, 411, 91))
        self.listView_2.setObjectName("listView_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 401, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(290, 310, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.listView_7 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_7.setGeometry(QtCore.QRect(10, 230, 211, 31))
        self.listView_7.setObjectName("listView_7")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 230, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 310, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(260, 229, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Editar Pregunta"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Editar pregunta</span></p></body></html>"))
        
        # Usamos los valores de los atributos para configurar los textos
        self.label_2.setText(_translate("MainWindow", self.enunciado))
        self.pushButton_12.setText(_translate("MainWindow", "Aceptar"))
        self.label_7.setText(_translate("MainWindow", " Respuesta correcta:"))
        self.textEdit.setHtml(_translate("MainWindow", self.respuesta))
        self.pushButton_13.setText(_translate("MainWindow", "Cancelar"))

    def get_button_atras(self):
        return self.pushButton_13

    def get_button_aceptar(self):
        return self.pushButton_12
