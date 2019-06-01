from PyQt5 import QtCore, QtGui, QtWidgets
class startt(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1100, 800)
        MainWindow.setStyleSheet("background-image:url(BUPT.jpg)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stinfor = QtWidgets.QPushButton(self.centralwidget)
        self.stinfor.setGeometry(QtCore.QRect(720, 540, 301, 111))
        self.stinfor.setStyleSheet("border-image:url(start.jpg)")
        self.stinfor.setText("")
        self.stinfor.setObjectName("stinfor")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(30, 20, 231, 91))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(36)
        self.time.setFont(font)
        self.time.setText("")
        self.time.setObjectName("time")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 60, 351, 81))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(720, 240, 331, 81))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(840, 320, 231, 71))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "智能校园签到系统"))
        self.label.setText("<font color=%s>%s</font>" %('#EAFF82', "欢 迎 您 使 用"))
        self.label_2.setText("<font color=%s>%s</font>" %('#EAFF82', "智能校园"))
        self.label_3.setText("<font color=%s>%s</font>" %('#EAFF82', "签到系统"))