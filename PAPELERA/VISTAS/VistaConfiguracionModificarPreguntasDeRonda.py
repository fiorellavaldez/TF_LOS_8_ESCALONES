from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1080, 720)
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
        
        # Reemplazo de QTableWidget por QListView
        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listView.setFont(font)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        # Botón Atrás
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        
        # Spacer para empujar los botones hacia la derecha
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        
        # Nuevo botón "Modificar pregunta" a la derecha
        self.pushButton_modificar = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_modificar.setFont(font)
        self.pushButton_modificar.setObjectName("pushButton_modificar")
        self.pushButton_modificar.setText("Modificar pregunta")  # El texto del nuevo botón
        self.horizontalLayout_3.addWidget(self.pushButton_modificar)  # Añadir el nuevo botón
        
        # Botón "Eliminar pregunta" a la derecha
        self.pushButton_eliminar = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_eliminar.setFont(font)
        self.pushButton_eliminar.setObjectName("pushButton_eliminar")
        self.pushButton_eliminar.setText("Eliminar pregunta")  # El texto del nuevo botón
        self.horizontalLayout_3.addWidget(self.pushButton_eliminar)  # Añadir el nuevo botón
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # Botón Agregar nueva pregunta
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout.addWidget(self.pushButton_12)
        
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("VistaConfiguracionModificarPreguntasDeRonda", "VistaConfiguracionModificarPreguntasDeRonda"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Preguntas de ronda: Historia</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Buscar:  "))
        self.pushButton_2.setText(_translate("MainWindow", "Atrás"))
        self.pushButton_12.setText(_translate("MainWindow", "Agregar nueva pregunta"))
        self.pushButton_eliminar.setText(_translate("MainWindow", "Eliminar pregunta"))
        self.pushButton_modificar.setText(_translate("MainWindow", "Modificar pregunta"))

    def get_button_atras(self):
        return self.pushButton_2

    def get_button_agregar_pregunta(self):
        return self.pushButton_12
    
    def get_button_eliminar_pregunta(self):
        return self.pushButton_eliminar

    def get_button_modificar_pregunta(self):
        return self.pushButton_modificar