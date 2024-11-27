from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(405, 181)
        Widget.setWindowIcon(QtGui.QIcon('vista/img/icono_modificar.png'))
        self.buttonBox_Confirmar = QtWidgets.QDialogButtonBox(parent=Widget)
        self.buttonBox_Confirmar.setGeometry(QtCore.QRect(130, 140, 156, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonBox_Confirmar.setFont(font)
        self.buttonBox_Confirmar.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox_Confirmar.setCenterButtons(False)
        self.buttonBox_Confirmar.setObjectName("buttonBox_Confirmar")
        self.lineEdit_Tema = QtWidgets.QLineEdit(parent=Widget)
        self.lineEdit_Tema.setGeometry(QtCore.QRect(20, 100, 371, 22))
        self.lineEdit_Tema.setObjectName("lineEdit_Tema")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 371, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Titulo = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_Titulo.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label_Titulo.setFont(font)
        self.label_Titulo.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_Titulo.setObjectName("label_Titulo")
        self.verticalLayout.addWidget(self.label_Titulo, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_Mensaje = QtWidgets.QLabel(parent=Widget)
        self.label_Mensaje.setGeometry(QtCore.QRect(20, 80, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Mensaje.setFont(font)
        self.label_Mensaje.setObjectName("label_Mensaje")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

        self.buttonBox_Confirmar.setProperty("tipo","boton_vista_configuracion")

    def aviso_tema_modificado_vacio(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setWindowTitle("Advertencia")
        msg.setText("No se ha ingresado ningun nombre. Por favor, ingrese un nombre.")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    def aviso_tema_creado_vacio(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setWindowTitle("Advertencia")
        msg.setText("No se ha ingresado ningun nombre. Por favor, ingrese un nombre.")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    def aviso_tema_existe(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setWindowTitle("Advertencia")
        msg.setText("Este tema ya existe. Por favor, ingrese un nombre diferente.")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    def informamos_tema_creado(self,tema):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setWindowTitle("Informacion")
        msg.setText(f"Se creo correctamente el tema: {tema}")
        msg.exec()

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("VistaConfiguracionTemaABMEdit", "Configurar Tema"))
        self.label_Titulo.setText(_translate("Widget", "Tema nuevo"))
        self.label_Mensaje.setText(_translate("Widget", "Ingrese nombre del nuevo tema:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec())
