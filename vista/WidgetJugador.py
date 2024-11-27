from PyQt6 import QtCore, QtGui, QtWidgets

class WidgetJugador(QtWidgets.QWidget):
    def __init__(self, nombre:str, avatar:str):
        super().__init__() #sacamos el parentttt
        self.__nombre = nombre
        self.__avatar = avatar
        self.__r1 = "vista/img/vacio.png"
        self.__r2 = "vista/img/vacio.png"
        self.setParent(None)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred))
        self.setMaximumSize(QtCore.QSize(60, 16777215))
        self.setup()
    
    def get_nombre_visual(self):
        return self.__nombre
    
    def get_avatar_visual(self):
        return self.__avatar
    
    def get_r1_visual(self):
        return self.__r1
    
    def get_r2_visual(self):
        return self.__r2
    
    def setup(self):
        #verticalLayout tiene como parent a wd_jugador y contendrá al layout que contiene el avatar, nombre, etc
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)

        self.layout = QtWidgets.QVBoxLayout() #"layout jugador"
        self.layout.setSpacing(0)

        #avatar
        self.lbl_avatar = QtWidgets.QLabel(parent=self)
        self.lbl_avatar.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))
        self.lbl_avatar.setMaximumSize(QtCore.QSize(40, 40))
        self.lbl_avatar.setPixmap(QtGui.QPixmap(self.__avatar))
        self.lbl_avatar.setScaledContents(True)

        #nombre
        self.wd_nombre = QtWidgets.QLabel(text=self.__nombre, parent=self)
        self.wd_nombre.setMaximumSize(QtCore.QSize(16777215, 16))
        self.wd_nombre.setObjectName("wd_nombre_jugador")
        font = QtGui.QFont()
        font.setPointSize(7)
        self.wd_nombre.setFont(font)

        #checkbox 1
        self.ly_rondas = QtWidgets.QHBoxLayout()
        self.lbl_r1 = QtWidgets.QLabel(parent=self)
        self.lbl_r1.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))
        self.lbl_r1.setMaximumSize(QtCore.QSize(17, 17))
        self.lbl_r1.setPixmap(QtGui.QPixmap(self.__r1))
        self.lbl_r1.setScaledContents(True)
        self.lbl_r1.setProperty("tipo","checkbox")
        self.ly_rondas.addWidget(self.lbl_r1)

        #checkbox 1
        self.lbl_r2 = QtWidgets.QLabel(parent=self)
        self.lbl_r2.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))
        self.lbl_r2.setMaximumSize(QtCore.QSize(17, 17))
        self.lbl_r2.setPixmap(QtGui.QPixmap(self.__r2))
        self.lbl_r2.setScaledContents(True)
        self.lbl_r2.setProperty("tipo","checkbox")
        self.ly_rondas.addWidget(self.lbl_r2)

        #agrego los elementos al layout
        self.layout.addWidget(self.lbl_avatar, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.layout.addWidget(self.wd_nombre, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.layout.addLayout(self.ly_rondas)

        self.verticalLayout.addLayout(self.layout)
        
    def actualizar_r1(self, estado: bool):
        """
        Actualiza el estado de la ronda 1.
        :param estado: True si se ha respondido correctamente, False en caso contrario.
        """
        nueva_imagen = "vista/img/correcto.png" if estado else "vista/img/incorrecto.png"
        self.__r1 = nueva_imagen
        self.lbl_r1.setPixmap(QtGui.QPixmap(self.__r1))

    def actualizar_r2(self, estado: bool):
        """
        Actualiza el estado de la ronda 2.
        :param estado: True si se ha respondido correctamente, False en caso contrario.
        """
        nueva_imagen = "vista/img/correcto.png" if estado else "vista/img/incorrecto.png"
        self.__r2 = nueva_imagen
        self.lbl_r2.setPixmap(QtGui.QPixmap(self.__r2))
        
    def reset_rondas(self):
        nueva_imagen = "vista/img/vacio.png"
        self.__r1 = nueva_imagen
        self.lbl_r1.setPixmap(QtGui.QPixmap(self.__r1))
        self.__r2 = nueva_imagen
        self.lbl_r2.setPixmap(QtGui.QPixmap(self.__r2))