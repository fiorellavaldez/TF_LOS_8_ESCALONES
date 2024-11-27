from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('vista/img/icono_ventana.png'))
        #MainWindow.resize(1080, 720)
        MainWindow.setFixedSize(1080, 720)
        #self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget = QtWidgets.QLabel(parent=MainWindow)
        self.centralwidget.setPixmap(QtGui.QPixmap("vista/img/fondo_juego.png"))
        self.centralwidget.setScaledContents(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        # self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setPixmap(QtGui.QPixmap("vista/img/titulo_juego.png"))
        self.label.setScaledContents(True)
        self.label.setMaximumSize(QtCore.QSize(700, 400))
        # font = QtGui.QFont()
        # font.setFamily("Segoe Fluent Icons")
        # font.setPointSize(70)
        # font.setBold(False)
        # self.label.setFont(font)
        # self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setIcon(QtGui.QIcon("vista/img/nueva_partida_icono.png"))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setIcon(QtGui.QIcon("vista/img/configuracion_icono.png"))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setIcon(QtGui.QIcon("vista/img/salir_icono.png"))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #los relaciono bajo la misma property para la hoja de estilos .qss
        self.pushButton.setProperty("tipo","boton_pantalla_inicial")
        self.pushButton_5.setProperty("tipo","boton_pantalla_inicial")
        self.pushButton_6.setProperty("tipo","boton_pantalla_inicial")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("VistaPantallaInicio", "Menú"))
        #self.label.setText(_translate("MainWindow", "LOS 8 ESCALONES"))
        self.pushButton.setText(_translate("MainWindow", "  Nueva partida"))
        self.pushButton_5.setText(_translate("MainWindow", "  Configuración"))
        self.pushButton_6.setText(_translate("MainWindow", "  Salir"))

    def get_button_configuracion(self):
        return self.pushButton_5 # estaría bien renombrar los 'pushButton_5' para saber de qué es el botón
    
    def get_button_nueva_partida(self):
        return self.pushButton
    
    def get_button_salir(self):
        return self.pushButton_6
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())