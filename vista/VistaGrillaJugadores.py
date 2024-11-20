from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(231, -1, 231, -1)
        self.frame_16 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_16)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_25.addItem(spacerItem2)
        self.nombre_jugador4 = QtWidgets.QLabel(parent=self.frame_16) #Jugador 4
        self.nombre_jugador4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre_jugador4.sizePolicy().hasHeightForWidth())
        self.nombre_jugador4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nombre_jugador4.setFont(font)
        self.nombre_jugador4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_25.addWidget(self.nombre_jugador4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_25.addItem(spacerItem3)
        self.bt_seleccionar_jugador4 = QtWidgets.QPushButton(parent=self.frame_16)
        self.verticalLayout_25.addWidget(self.bt_seleccionar_jugador4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_25.addItem(spacerItem4)
        #self.bt_jugador_nuevo4 = QtWidgets.QPushButton(parent=self.frame_16)
        #self.bt_jugador_nuevo4.setObjectName("bt_jugador_nuevo4")
        #.verticalLayout_25.addWidget(self.bt_jugador_nuevo4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_25.addItem(spacerItem5)
        self.gridLayout.addWidget(self.frame_16, 1, 0, 1, 1)
        self.frame_15 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(spacerItem6)
        self.nombre_jugador8 = QtWidgets.QLabel(parent=self.frame_15) #Jugador 8
        self.nombre_jugador8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre_jugador8.sizePolicy().hasHeightForWidth())
        self.nombre_jugador8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nombre_jugador8.setFont(font)
        self.nombre_jugador8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombre_jugador8.setObjectName("nombre_jugador8")
        self.verticalLayout_9.addWidget(self.nombre_jugador8)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(spacerItem7)
        self.bt_seleccionar_jugador8 = QtWidgets.QPushButton(parent=self.frame_15)
        self.bt_seleccionar_jugador8.setObjectName("bt_seleccionar_jugador8")
        self.verticalLayout_9.addWidget(self.bt_seleccionar_jugador8)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(spacerItem8)
        #self.#t_jugador_nuevo8 = QtWidgets.QPushButton(parent=self.frame_15)
        #self.bt_jugador_nuevo8.setObjectName("bt_jugador_nuevo8")
        #self.verticalLayout_9.addWidget(self.bt_jugador_nuevo8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(spacerItem9)
        self.gridLayout.addWidget(self.frame_15, 2, 1, 1, 1)
        self.frame_12 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.nombre_jugador2 = QtWidgets.QLabel(parent=self.frame_12) #Jugador 2
        self.nombre_jugador2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre_jugador2.sizePolicy().hasHeightForWidth())
        self.nombre_jugador2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nombre_jugador2.setFont(font)
        self.nombre_jugador2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombre_jugador2.setObjectName("nombre_jugador2")
        self.verticalLayout_4.addWidget(self.nombre_jugador2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.bt_seleccionar_jugador2 = QtWidgets.QPushButton(parent=self.frame_12)
        self.bt_seleccionar_jugador2.setObjectName("bt_seleccionar_jugador2")
        self.verticalLayout_4.addWidget(self.bt_seleccionar_jugador2)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        # self.bt_jugador_nuevo2 = QtWidgets.QPushButton(parent=self.frame_12)
        # self.bt_jugador_nuevo2.setObjectName("bt_jugador_nuevo2")
        # self.verticalLayout_4.addWidget(self.bt_jugador_nuevo2)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.gridLayout.addWidget(self.frame_12, 0, 1, 1, 1)
        self.frame_14 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem14)
        self.nombre_jugador5 = QtWidgets.QLabel(parent=self.frame_14) #Jugador 5
        self.nombre_jugador5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre_jugador5.sizePolicy().hasHeightForWidth())
        self.nombre_jugador5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nombre_jugador5.setFont(font)
        self.nombre_jugador5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombre_jugador5.setObjectName("nombre_jugador5")
        self.verticalLayout_8.addWidget(self.nombre_jugador5)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem15)
        self.bt_seleccionar_jugador5 = QtWidgets.QPushButton(parent=self.frame_14)
        self.bt_seleccionar_jugador5.setObjectName("bt_seleccionar_jugador5")
        self.verticalLayout_8.addWidget(self.bt_seleccionar_jugador5)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem16)
        # self.bt_jugador_nuevo5 = QtWidgets.QPushButton(parent=self.frame_14)
        # self.bt_jugador_nuevo5.setObjectName("bt_jugador_nuevo5")
        # self.verticalLayout_8.addWidget(self.bt_jugador_nuevo5)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem17)
        self.gridLayout.addWidget(self.frame_14, 1, 1, 1, 1)
        self.frame_17 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_26.addItem(spacerItem18)
        self.nombre_jugador6 = QtWidgets.QLabel(parent=self.frame_17) #Jugador 6
        self.nombre_jugador6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre_jugador6.sizePolicy().hasHeightForWidth())
        self.nombre_jugador6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nombre_jugador6.setFont(font)
        self.nombre_jugador6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombre_jugador6.setObjectName("nombre_jugador6")
        self.verticalLayout_26.addWidget(self.nombre_jugador6)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_26.addItem(spacerItem19)
        self.bt_seleccionar_jugador6 = QtWidgets.QPushButton(parent=self.frame_17)
        self.bt_seleccionar_jugador6.setObjectName("bt_seleccionar_jugador6")
        self.verticalLayout_26.addWidget(self.bt_seleccionar_jugador6)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_26.addItem(spacerItem20)
        # self.bt_jugador_nuevo6 = QtWidgets.QPushButton(parent=self.frame_17)
        # self.bt_jugador_nuevo6.setObjectName("bt_jugador_nuevo6")
        # self.verticalLayout_26.addWidget(self.bt_jugador_nuevo6)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_26.addItem(spacerItem21)
        self.gridLayout.addWidget(self.frame_17, 1, 2, 1, 1)
        self.frame_18 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_18.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_29.addItem(spacerItem22)
        self.nombre_jugador7 = QtWidgets.QLabel(parent=self.frame_18) #Jugador 7
        self.nombre_jugador7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre_jugador7.sizePolicy().hasHeightForWidth())
        self.nombre_jugador7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nombre_jugador7.setFont(font)
        self.nombre_jugador7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombre_jugador7.setObjectName("nombre_jugador7")
        self.verticalLayout_29.addWidget(self.nombre_jugador7)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_29.addItem(spacerItem23)
        self.bt_seleccionar_jugador7 = QtWidgets.QPushButton(parent=self.frame_18)
        self.bt_seleccionar_jugador7.setObjectName("bt_seleccionar_jugador7")
        self.verticalLayout_29.addWidget(self.bt_seleccionar_jugador7)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_29.addItem(spacerItem24)
        # self.bt_jugador_nuevo7 = QtWidgets.QPushButton(parent=self.frame_18)
        # self.bt_jugador_nuevo7.setObjectName("bt_jugador_nuevo7")
        # self.verticalLayout_29.addWidget(self.bt_jugador_nuevo7)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_29.addItem(spacerItem25)
        self.gridLayout.addWidget(self.frame_18, 2, 0, 1, 1)
        self.frame_19 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_19.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_30.addItem(spacerItem26)
        self.nombre_jugador9 = QtWidgets.QLabel(parent=self.frame_19) #Jugador 9
        self.nombre_jugador9.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre_jugador9.sizePolicy().hasHeightForWidth())
        self.nombre_jugador9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nombre_jugador9.setFont(font)
        self.nombre_jugador9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombre_jugador9.setObjectName("nombre_jugador9")
        self.verticalLayout_30.addWidget(self.nombre_jugador9)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_30.addItem(spacerItem27)
        self.bt_seleccionar_jugador9 = QtWidgets.QPushButton(parent=self.frame_19)
        self.bt_seleccionar_jugador9.setObjectName("bt_seleccionar_jugador9")
        self.verticalLayout_30.addWidget(self.bt_seleccionar_jugador9)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_30.addItem(spacerItem28)
        # self.bt_jugador_nuevo9 = QtWidgets.QPushButton(parent=self.frame_19)
        # self.bt_jugador_nuevo9.setObjectName("bt_jugador_nuevo9")
        # self.verticalLayout_30.addWidget(self.bt_jugador_nuevo9)
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_30.addItem(spacerItem29)
        self.gridLayout.addWidget(self.frame_19, 2, 2, 1, 1)
        self.frame_11 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem30)
        self.nombre_jugador1 = QtWidgets.QLabel(parent=self.frame_11) #Jugador 1
        self.nombre_jugador1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre_jugador1.sizePolicy().hasHeightForWidth())
        self.nombre_jugador1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nombre_jugador1.setFont(font)
        self.nombre_jugador1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombre_jugador1.setObjectName("nombre_jugador1")
        self.verticalLayout_3.addWidget(self.nombre_jugador1)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem31)
        self.bt_seleccionar_jugador1 = QtWidgets.QPushButton(parent=self.frame_11)
        self.bt_seleccionar_jugador1.setObjectName("bt_seleccionar_jugador1")
        self.verticalLayout_3.addWidget(self.bt_seleccionar_jugador1)
        spacerItem32 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem32)
        self.bt_jugador_nuevo = QtWidgets.QPushButton(parent=self.frame_11)
        self.bt_jugador_nuevo.setObjectName("bt_jugador_nuevo")
        self.verticalLayout_3.addWidget(self.bt_jugador_nuevo)
        spacerItem33 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem33)
        self.gridLayout.addWidget(self.frame_11, 0, 0, 1, 1)
        self.frame_13 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem34 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem34)
        self.nombre_jugador3 = QtWidgets.QLabel(parent=self.frame_13) #Jugador 3
        self.nombre_jugador3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre_jugador3.sizePolicy().hasHeightForWidth())
        self.nombre_jugador3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nombre_jugador3.setFont(font)
        self.nombre_jugador3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombre_jugador3.setObjectName("nombre_jugador3")
        self.verticalLayout_7.addWidget(self.nombre_jugador3)
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem35)
        self.bt_seleccionar_jugador3 = QtWidgets.QPushButton(parent=self.frame_13)
        self.bt_seleccionar_jugador3.setObjectName("bt_seleccionar_jugador3")
        self.verticalLayout_7.addWidget(self.bt_seleccionar_jugador3)
        spacerItem36 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem36)
        # self.bt_jugador_nuevo3 = QtWidgets.QPushButton(parent=self.frame_13)
        # self.bt_jugador_nuevo3.setObjectName("bt_jugador_nuevo3")
        # self.verticalLayout_7.addWidget(self.bt_jugador_nuevo3)
        spacerItem37 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem37)
        self.gridLayout.addWidget(self.frame_13, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_atras = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_atras.setObjectName("bt_atras")
        self.horizontalLayout.addWidget(self.bt_atras)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem38)
        self.bt_iniciar_partida = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_iniciar_partida.setEnabled(True) #False
        self.horizontalLayout.addWidget(self.bt_iniciar_partida)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("VistaGrillaJugadores", "VistaGrillaJugadores"))
        self.label.setText(_translate("MainWindow", "Jugadores"))
        #Jugador 1
        self.nombre_jugador1.setText(_translate("MainWindow", "Jugador 1"))
        self.bt_seleccionar_jugador1.setText(_translate("MainWindow", "Seleccionar Jugador"))
        self.bt_jugador_nuevo.setText(_translate("MainWindow", "Jugador Nuevo")) ############
        #Jugador 2
        self.nombre_jugador2.setText(_translate("MainWindow", "Jugador 2"))
        self.bt_seleccionar_jugador2.setText(_translate("MainWindow", "Seleccionar Jugador"))
        ##self.bt_jugador_nuevo2.setText(_translate("MainWindow", "Jugador Nuevo"))
        #Jugador 3
        self.nombre_jugador3.setText(_translate("MainWindow", "Jugador 3"))
        self.bt_seleccionar_jugador3.setText(_translate("MainWindow", "Seleccionar Jugador"))
        ##self.bt_jugador_nuevo3.setText(_translate("MainWindow", "Jugador Nuevo"))
        #Jugador 4
        self.nombre_jugador4.setText(_translate("MainWindow", "Jugador 4"))
        self.bt_seleccionar_jugador4.setText(_translate("MainWindow", "Seleccionar Jugador"))
        ##self.bt_jugador_nuevo4.setText(_translate("MainWindow", "Jugador Nuevo"))
        #Jugador 5
        self.nombre_jugador5.setText(_translate("MainWindow", "Jugador 5"))
        self.bt_seleccionar_jugador5.setText(_translate("MainWindow", "Seleccionar Jugador"))
        ##self.bt_jugador_nuevo5.setText(_translate("MainWindow", "Jugador Nuevo"))
        #Juagdor 6
        self.nombre_jugador6.setText(_translate("MainWindow", "Jugador 6"))
        self.bt_seleccionar_jugador6.setText(_translate("MainWindow", "Seleccionar Jugador"))
        ##self.bt_jugador_nuevo6.setText(_translate("MainWindow", "Jugador Nuevo"))
        #Jugador 7
        self.nombre_jugador7.setText(_translate("MainWindow", "Jugador 7"))
        self.bt_seleccionar_jugador7.setText(_translate("MainWindow", "Seleccionar Jugador"))
        ##self.bt_jugador_nuevo7.setText(_translate("MainWindow", "Jugador Nuevo"))
        #Jugador 8
        self.nombre_jugador8.setText(_translate("MainWindow", "Jugador 8"))
        self.bt_seleccionar_jugador8.setText(_translate("MainWindow", "Seleccionar Jugador"))
        ##self.bt_jugador_nuevo8.setText(_translate("MainWindow", "Jugador Nuevo"))
        #Jugador 9
        self.nombre_jugador9.setText(_translate("MainWindow", "Jugador 9"))
        self.bt_seleccionar_jugador9.setText(_translate("MainWindow", "Seleccionar Jugador"))
        ##self.bt_jugador_nuevo9.setText(_translate("MainWindow", "Jugador Nuevo"))

        #Botones
        self.bt_atras.setText(_translate("MainWindow", "Atrás"))
        self.bt_iniciar_partida.setText(_translate("MainWindow", "Iniciar Partida"))


# MÉTODOS JUGADORES

    #Métodos Jugador 1
    def get_nombre_jugador1 (self):
        return self.nombre_jugador1

    def get_button_seleccionar_jugador1(self):
        return self.bt_seleccionar_jugador1

    #Métodos Jugador 2
    def get_nombre_jugador2 (self):
        return self.nombre_jugador2
    
    def get_button_seleccionar_jugador2(self):
        return self.bt_seleccionar_jugador2

    #Métodos Jugador 3
    def get_nombre_jugador3 (self):
        return self.nombre_jugador3

    def get_button_seleccionar_jugador3(self):
        return self.bt_seleccionar_jugador3

    #Métodos Jugador 4
    def get_nombre_jugador4 (self):
        return self.nombre_jugador4

    def get_button_seleccionar_jugador4(self):
        return self.bt_seleccionar_jugador4
    
    
    #Métodos Jugador 5
    def get_nombre_jugador5 (self):
        return self.nombre_jugador5
    
    def get_button_seleccionar_jugador5(self):
        return self.bt_seleccionar_jugador5
    

    #Métodos Jugador 6
    def get_nombre_jugador6 (self):
        return self.nombre_jugador6

    def get_button_seleccionar_jugador6(self):
        return self.bt_seleccionar_jugador6

    #Métodos Jugador 7
    def get_nombre_jugador7 (self):
        return self.nombre_jugador7

    def get_button_seleccionar_jugador7(self):
        return self.bt_seleccionar_jugador7

    #Métodos Jugador 8
    def get_nombre_jugador8 (self):
        return self.nombre_jugador8

    def get_button_seleccionar_jugador8(self):
        return self.bt_seleccionar_jugador8
    
    #Métodos Jugador 9
    def get_nombre_jugador9 (self):
        return self.nombre_jugador9
    
    def get_button_seleccionar_jugador9(self):
        return self.bt_seleccionar_jugador9

#MÉTODOS OTROS BOTONES

    def get_button_atras(self):
        return self.bt_atras
    
    def get_button_iniciar_partida(self):
        return self.bt_iniciar_partida

    def get_button_jugador_nuevo(self):
        return self.bt_jugador_nuevo
    
    def aviso_iniciar_partida(self):
        msg=QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setWindowTitle("Advertencia")
        msg.setText("Debes seleccionar a todos los jugadores")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()
        
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())