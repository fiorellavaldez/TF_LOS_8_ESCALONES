from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self, lista_temas):
        self.__lista_temas = lista_temas
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("VistaConfiguracionPregunta")
        # Establece el tamaño inicial de la ventana
        MainWindow.resize(1080, 720)
        # Establece el tamaño mínimo de la ventana
        MainWindow.setMinimumSize(400, 400)
        MainWindow.setWindowIcon(QtGui.QIcon('vista/img/configuracion_icono.png'))
        self.centralwidget = QtWidgets.QLabel(parent=MainWindow)
        self.centralwidget.setPixmap(QtGui.QPixmap("vista/img/fondo_escalones.png"))
        self.centralwidget.setScaledContents(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(66, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setStyleSheet("color: #ffffff; font-weight: bold;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(66, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(161, 75, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setStyleSheet("color: #ffffff; font-weight: bold;")
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(1060)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        #
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_3.addWidget(self.pushButton_14)
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_3.addWidget(self.pushButton_13)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout.addWidget(self.pushButton_12)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_14.setIcon(QtGui.QIcon("vista/img/icono_eliminar.png"))
        self.pushButton_13.setIcon(QtGui.QIcon("vista/img/icono_modificar.png"))
        self.pushButton_12.setIcon(QtGui.QIcon("vista/img/icono_agregar.png"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.setProperty("tipo","boton_vista_configuracion")
        self.pushButton_14.setProperty("tipo","boton_vista_configuracion_eliminar")
        self.pushButton_12.setProperty("tipo","boton_vista_configuracion_agregar")
        self.pushButton_13.setProperty("tipo","boton_vista_configuracion")
    
    def aviso_seleccionar_pregunta(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setWindowTitle("Advertencia")
        msg.setText("Debe seleccionar una pregunta primero.")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("VistaConfiguracionPregunta", "Configuración de Preguntas"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Seleccione el tema:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "Buscar:  "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Enunciado"))
        self.pushButton_2.setText(_translate("MainWindow", "Atrás"))
        self.pushButton_14.setText(_translate("MainWindow", "Eliminar pregunta"))
        self.pushButton_13.setText(_translate("MainWindow", "Modificar pregunta"))
        self.pushButton_12.setText(_translate("MainWindow", "Nueva pregunta"))

    
    def mostrar_lista_en_combobox(self):
        self.comboBox.clear()  # Limpiar todos los ítems
        self.comboBox.addItems([str(tema) for tema in self.__lista_temas])

    
    def get_button_atras(self):
        return self.pushButton_2
    def get_button_eliminar(self):
        return self.pushButton_14
    def get_button_modificar(self):
        return self.pushButton_13
    def get_button_nueva(self):
        return self.pushButton_12
    def get_line_edit_busqueda(self):
        return self.lineEdit
    def get_comboBox(self):
        return self.comboBox

lista_temas = [25,8645,65,65,31,32]
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(lista_temas)
    ui.setupUi(MainWindow)  # Configura la UI primero
    ui.mostrar_lista_en_combobox()  # Luego llena el ComboBox
    MainWindow.show()
    sys.exit(app.exec())
