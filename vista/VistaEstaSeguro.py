from PyQt6 import QtCore, QtGui, QtWidgets

class VistaEstaSeguro(object):
    def setupUi(self, dialog, label_text):
        dialog.setObjectName("Dialog")
        dialog.resize(500, 150)
        self.centralwidget = QtWidgets.QWidget(parent=dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_3.addWidget(self.pushButton_13)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_3.addWidget(self.pushButton_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        dialog.setLayout(self.verticalLayout)
        self.retranslateUi(dialog, label_text)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog, label_text):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Confirmación"))
        self.label.setText(label_text)
        self.pushButton_13.setText(_translate("Dialog", "Cancelar"))
        self.pushButton_12.setText(_translate("Dialog", "Aceptar"))
    
    def get_button_cancelar(self):
        return self.pushButton_13

    def get_button_aceptar(self):
        return self.pushButton_12
