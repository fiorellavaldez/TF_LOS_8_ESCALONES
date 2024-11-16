from PyQt6 import QtCore, QtGui, QtWidgets

class WidgetJugador(QtWidgets.QWidget):
    def __init__(self, parent, nombre:str, avatar:str, img_r1:str, img_r2:str):
        super().__init__(parent)
        self.nombre = nombre
        self.avatar = avatar
        self.r1 = img_r1
        self.r2 = img_r2
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred))
        self.setMaximumSize(QtCore.QSize(60, 16777215))
        self.setup()

    def setup(self):
        #verticalLayout tiene como parent a wd_jugador y contendrá al layout que contiene el avatar, nombre, etc
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)

        self.layout = QtWidgets.QVBoxLayout() #"layout jugador"
        self.layout.setSpacing(0)

        #avatar
        self.lbl_avatar = QtWidgets.QLabel(parent=self)
        self.lbl_avatar.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))
        self.lbl_avatar.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_avatar.setPixmap(QtGui.QPixmap(self.avatar))
        self.lbl_avatar.setScaledContents(True)

        #nombre
        self.wd_nombre = QtWidgets.QLabel(text=self.nombre, parent=self)
        self.wd_nombre.setMaximumSize(QtCore.QSize(16777215, 14))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.wd_nombre.setFont(font)

        #checkbox 1
        self.ly_rondas = QtWidgets.QHBoxLayout()
        self.lbl_r1 = QtWidgets.QLabel(parent=self)
        self.lbl_r1.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))
        self.lbl_r1.setMaximumSize(QtCore.QSize(15, 15))
        self.lbl_r1.setPixmap(QtGui.QPixmap(self.r1))
        self.lbl_r1.setScaledContents(True)
        self.ly_rondas.addWidget(self.lbl_r1)

        #checkbox 1
        self.lbl_r2 = QtWidgets.QLabel(parent=self)
        self.lbl_r2.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))
        self.lbl_r2.setMaximumSize(QtCore.QSize(15, 15))
        self.lbl_r2.setPixmap(QtGui.QPixmap(self.r2))
        self.lbl_r2.setScaledContents(True)
        self.ly_rondas.addWidget(self.lbl_r2)

        #agrego los elementos al layout
        self.layout.addWidget(self.lbl_avatar, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.layout.addWidget(self.wd_nombre, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.layout.addLayout(self.ly_rondas)

        self.verticalLayout.addLayout(self.layout)