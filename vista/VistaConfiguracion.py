from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # Establece el tamaño inicial de la ventana
        MainWindow.resize(1080, 720)
        # Establece el tamaño mínimo de la ventana
        MainWindow.setMinimumSize(400, 400)
        self.centralwidget = QtWidgets.QLabel(parent=MainWindow)
        self.centralwidget.setPixmap(QtGui.QPixmap("vista/img/fondo_configuracion.jpg"))
        self.centralwidget.setScaledContents(True)
        
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)

        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setPixmap(QtGui.QPixmap("vista/img/configuracion_titulo.PNG"))
        self.label.setScaledContents(True)
        self.label.setMaximumSize(QtCore.QSize(700, 400))

        #self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

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

        # Botón Configuración de Audio y Video
        self.pushButton_config_audio_video = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_config_audio_video.setFont(font)
        self.pushButton_config_audio_video.setObjectName("pushButton_config_audio_video")
        self.verticalLayout_3.addWidget(self.pushButton_config_audio_video)

        # Botón Modificar o crear Preguntas de ronda
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)

        # Botón Modificar o crear Preguntas de desempate
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)

        # Botón Modificar o crear temas
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)

        # Botón Agregar o modificar jugadores
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)

        # Botón Atrás
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 660, 75, 30))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))


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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_6.setProperty("tipo","boton_vista_configuracion")
        self.pushButton_5.setProperty("tipo","boton_vista_configuracion")
        self.pushButton_4.setProperty("tipo","boton_vista_configuracion")
        self.pushButton.setProperty("tipo","boton_vista_configuracion")
        self.pushButton_2.setProperty("tipo","boton_vista_configuracion")
        self.pushButton_config_audio_video.setProperty("tipo","boton_vista_configuracion")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("VistaConfiguracion", "VistaConfiguracion"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton_config_audio_video.setText(_translate("MainWindow", "Configuración de Audio y Video"))
        self.pushButton.setText(_translate("MainWindow", "Modificar o crear Preguntas de ronda"))
        self.pushButton_2.setText(_translate("MainWindow", "Modificar o crear Preguntas de desempate"))
        self.pushButton_4.setText(_translate("MainWindow", "Modificar o crear temas"))
        self.pushButton_5.setText(_translate("MainWindow", "Agregar o modificar jugadores"))
        self.pushButton_6.setText(_translate("MainWindow", "Atrás"))

    def get_button_config_audio_video(self):
        return self.pushButton_config_audio_video

    def get_button_modificar_preguntas_ronda(self):
        return self.pushButton

    def get_button_modificar_preguntas_desempate(self):
        return self.pushButton_2

    def get_button_modificar_temas(self):
        return self.pushButton_4

    def get_button_modificar_jugadores(self):
        return self.pushButton_5

    def get_button_atras(self):
        return self.pushButton_6
