import urllib
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys
import ssl
import json
import shutil
import cv2
from ai import oshi_distance,face_feature,get_time,update_time,rec_face
from htjc import  htjc
from sql import *
import dlib
import numpy as np
import pyodbc
import os,time
from manually_enter import *
from startui import  startt
from sign_in3 import Ui_MainWindow
from sign_in2 import *
from sign_in import  *
from PyQt5 import  QtWidgets,QtGui,QtCore
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np

#继承主页面
class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.actionconfidence.triggered.connect(self.hj)
    #关闭提示
    def closeEvent(self,QCloseEvent):
        reply=QMessageBox.question(self,
                                   '提示',
                                   "是否退出应用程序？",
                                   QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.stop=1
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
    def rec(self):
            try:
                atime = get_time()
                detector = dlib.get_frontal_face_detector()
                image = cv2.imread("C:/Users/DELL/PycharmProjects/aiprogram/image/0.jpg")
                face = detector(image, 1)
                if (len(face) > 0):
                    atime = get_time()
                    face1_feature = face_feature(image)
                    result = rec_face(face1_feature)
                    if result == 0:
                        pixmap = QPixmap('C:/Users/DELL/PycharmProjects/aiprogram/face/sb.jpg')
                        self.sign_in_result_9.setPixmap(pixmap)
                        self.sign_in_result_9.setScaledContents(True)
                    else:
                        update_time(result[1], atime)
                        ttime = get_time()
                        self.name_9.setText((result[0]))
                        self.xuehao_9.setText((result[1]))
                        self.class_10.setText((result[2]))
                        pixmap = QPixmap(result[3])
                        self.label_2.setPixmap(pixmap)
                        self.label_2.setScaledContents(True)
                        cnxn=con_sql()
                        r=record(cnxn)
                        g=get_feature(cnxn)
                        self.sign_1_num_9.setText(str(len(r))+"/"+str(len(g)))
                        self.sign_0_num_9.setText(str(len(g)-len(r))+"/"+str(len(g)))
                        pixmap = QPixmap('C:/Users/DELL/PycharmProjects/aiprogram/face/cg.jpg')
                        self.sign_in_result_9.setPixmap(pixmap)
                        self.sign_in_result_9.setScaledContents(True)
            except:
                print("请再试一下！！")

    def catch(self):
            gtime=get_time()
            a=float(gtime[-5:-3] + gtime[-2:])
            self.timer = QTimer()
            self.timer.start()  # 实时刷新，不然视频不动态
            self.timer.setInterval(100)
            self.cap = cv2.VideoCapture(0)
            classfier = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
            color = (0, 255, 0)
            num = 0
            face3 = 0
            face2 = 0
            face1 = 0
            face = 0
            while self.cap.isOpened():
                ctime=get_time()
                sta.time.setText("<font color=%s>%s</font>" % ('#EAFF82', gtime[-8:-3]))
                b = float(ctime[-5:-3] + ctime[-2:])
                k=int((b-a)/100)
                self.time_8.setText("<font color=%s>%s</font>" %('#D5FF30',str(10-k)))
                if k==10:
                    break
                ok, frame = self.cap.read()  # 读取一帧数据
                if not ok:
                    break
                img_name = "C:/Users/DELL/PycharmProjects/aiprogram/image/1.jpg"
                cv2.imwrite(img_name, frame, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                # 变换彩色空间顺序
                sframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 转为QImage对象
                self.image = QImage(sframe.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.label.setPixmap(
                    QPixmap.fromImage(self.image).scaled(self.label.width(), self.label.height()))
                mywin.label_3.setPixmap(
                    QPixmap.fromImage(self.image).scaled(mywin.label_3.width(), mywin.label_3.height()))
                grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将当前桢图像转换成灰度图像
                faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
                face3 = face2
                face2 = face1
                face1 = face
                face = len(faceRects)
                if (face > 0):
                    for faceRect in faceRects:
                        x, y, w, h = faceRect
                        cv2.rectangle(frame, (x, y), (x + w + 10, y + h + 10), color, 2)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.putText(frame, "detecting", (x, y - 20), font, 1, (255, 0, 255), 4)
                        height, width, bytesPerComponent = frame.shape
                        bytesPerLine = bytesPerComponent * width
                        # 变换彩色空间顺序
                        sframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        # 转为QImage对象
                        self.image = QImage(sframe.data, width, height, bytesPerLine, QImage.Format_RGB888)
                        self.label.setPixmap(
                            QPixmap.fromImage(self.image).scaled(self.label.width(), self.label.height()))
                        mywin.label_3.setPixmap(
                            QPixmap.fromImage(self.image).scaled(mywin.label_3.width(), mywin.label_3.height()))
                        if (face == 1):
                            if (face1 == 1) & (face2 == 1) & (face3 == 0):
                                img_name = "C:/Users/DELL/PycharmProjects/aiprogram/image/0.jpg"
                                cv2.imwrite(img_name, frame, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
                        else:
                            cv2.putText(frame, "please one person !", (0, 44), font, 2, (0, 255, 255), 4)
                if cv2.waitKey(1) & 0xFF ==  32:
                    break
                if self.stop==1 :
                    break

            self.cap.release()
            cv2.destroyAllWindows()
    def hj(self):
        try:
           result=htjc()
           if result<0.7:
               QMessageBox.warning(self,
                                   "警告",
                                   "             未通过活体检测！",
                                   QMessageBox.Yes)
           else: QMessageBox.warning(self,
                                   "提示",
                                   "             检测成功！",
                                   QMessageBox.Yes)
        except:
               print("d")


class recordWindow(Example):
    def __init__(self):
        super().__init__()
        self.initUI()
class signin(Sign):
    def __init__(self):
        super(signin,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def word_get(self):
        login_user = self.lineEdit.text()
        login_password = self.lineEdit_2.text()
        if login_user == 'admin' and login_password == 'zouyan1999':
            mywin.show()
            MainWindow.close()
        else:
            QMessageBox.warning(self,
                    "警告",
                    "             用户名或密码错误！",
                    QMessageBox.Yes)
            self.lineEdit.setFocus()
class mydialog(QDialog,Ui_Dialog):
    def __init__(self):
        super(mydialog,self).__init__()
        self.setupUi(self)
    def text(self):
        try:
           Sname = self.name_in.text()
           Sno = self.xuehao_in.text()
           Sphoto='C:/Users/DELL/PycharmProjects/aiprogram/face/'+Sno+'.jpg'
           Sclass=self.class_in.text()
           Srec=0
           img = cv2.imread("C:/Users/DELL/PycharmProjects/aiprogram/image/1.jpg")
           cropped = img[90:400, 220:460]
           cv2.imwrite(Sphoto, cropped)
           image = cv2.imread(Sphoto)
           feat = face_feature(image)
           Sfeature = str(feat[0])[1:-1]
           cnxn = con_sql()
           insert_info(cnxn, Sname, Sno, Sclass, Sfeature, Sphoto, Srec)
           result=get_sno(cnxn)
           for i in range(len(result)):
              if Sno==result[i][0]:
                  QMessageBox.warning(self,
                                   "提示",
                                   "          录入成功！",
                                   QMessageBox.Yes)
        except: QMessageBox.warning(self,
                                   "警告",
                                   "          录入失败！",
                                   QMessageBox.Yes)

class start(QtWidgets.QMainWindow,startt):
    def __init__(self):
        super(start, self).__init__()
        self.setupUi(self)
        self.stinfor.clicked.connect(self.do)
    def do(self):
        myWin.show()
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = mywindow()                                           #例化主页面
    child = recordWindow()                                       #例化签到日志
    sign = signin()                                              #例化登陆页面
    mywin = mydialog()                                           #例化注册页面
    sta=start()
    sta.show()

    MainWindow = QtWidgets.QMainWindow()
    sign.setupUi(MainWindow)
    Maindialog = QDialog()

    #连接信号和槽函数
    myWin.pushButton.clicked.connect(myWin.rec)
    myWin.action_Y.triggered.connect(child.show)
    myWin.action_Y.triggered.connect(child.upd)
    myWin.actionaddress_name.triggered.connect(child.reset)
    myWin.actioninformations.triggered.connect(MainWindow.show)
    sign.pushButton_2.clicked.connect(MainWindow.close)
    sign.pushButton.clicked.connect(sign.word_get)
    mywin.pushButton_3.clicked.connect(mywin.text)

    myWin.catch()
    sys.exit(app.exec_())

