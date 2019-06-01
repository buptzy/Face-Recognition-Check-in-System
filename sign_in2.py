from sql import *
import sys
class Example(QWidget):
     data=[]
     def initUI(self):
              titles = ['序号', '姓名', '学号', '班级', ' 签到时间']
              self.setWindowTitle('签到日志')
              self.table = QTableWidget()
              self.table.setRowCount(9)                                   #行下标最大值
              self.table.setColumnCount(5)                                #列
              self.table.setHorizontalHeaderLabels(titles)                #标题列


              #表格或者窗体背景图片
              palette =  QtGui.QPalette()
              icon =  QtGui.QPixmap('C:/Users/DELL/PycharmProjects/aiprogram/face/renxiang.jpg')
              palette.setBrush(self.table.backgroundRole(),  QtGui.QBrush(icon))  # 添加背景图片
              self.setWindowOpacity(0.8)
              self.setPalette(palette)
              #表格行
              self.table.horizontalHeader().setStyleSheet("background-color: gray");
              self.table.setEditTriggers(QTableWidget.NoEditTriggers)#单元格不可编辑
              self.table.setSelectionBehavior(QTableWidget.SelectRows)  #选中列还是行，这里设置选中行
              # self.table.setSelectionMode(QTableWidget.SingleSelection) #只能选中一行或者一列
              self.table.horizontalHeader().setStretchLastSection(True)  #列宽度占满表格(最后一个列拉伸处理沾满表格)
              self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch);#所有列自适应表格宽度
              self.table.verticalHeader().hide()
              #1、设置每一个标题单元格样式
              for i in range(self.table.columnCount()):
                     headItem = self.table.horizontalHeaderItem(i)
                     headItem.setFont(QFont("song", 14, QFont.Bold))
                     headItem.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)


              #2、设置整个表格列标题样式
              font = self.table.horizontalHeader().font()
              font.setBold(True)
              self.table.horizontalHeader().setFont(font)
              #self.table.setFrameShape(QFrame.NoFrame)                   #设置表格外层无边框
              #self.table.setShowGrid(False)                              #是否显示单元格网格线False 则不显示
              #self.table.horizontalHeader().setHighlightSections(False)  #设置表格列头不塌陷
              #self.table.horizontalHeader().setFixedHeight(35)           #设置表列头高度
              #self.table.horizontalHeader().setFixedWidth(820)           #设置列标题头所在行，宽度（没啥用）


              #设置表格的滚动调样式：self.table.horizontalScrollBar().setStyleSheet.... ,窗体的也可以设置：self.horizontalScrollBar().setStyleSheet...
              self.table.horizontalScrollBar().setStyleSheet("QScrollBar{background:transparent; height:10px;}"
                                                  "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
                                                  "QScrollBar::handle:hover{background:gray;}"
                                                  "QScrollBar::sub-line{background:transparent;}"
                                                  "QScrollBar::add-line{background:transparent;}");
              self.table.verticalScrollBar().setStyleSheet("QScrollBar{background:transparent; width: 10px;}"
                                                  "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
                                                  "QScrollBar::handle:hover{background:gray;}"
                                                  "QScrollBar::sub-line{background:transparent;}"
                                                  "QScrollBar::add-line{background:transparent;}");
               #遍历数据，并形成行索引，列索引；
              self.upd()

     def upd(self):
              cnxn = con_sql()
              result = record(cnxn)
              if result!=None:
               for i in range(len(result)):
                  self.table.setItem(i, 0, QTableWidgetItem("                    "+str(i+1)))
                  self.table.setItem(i,4,  QTableWidgetItem(result[i][6]))
                  for j in range(3):
                     self.table.setItem(i, j+1, QTableWidgetItem("           "+result[i][j]))
              row_count = self.table.rowCount()
              self.table.insertRow(row_count)
              mainLayout = QHBoxLayout()
              mainLayout.addWidget(self.table)
              self.setLayout(mainLayout)
              self.setGeometry(200,300,900,400)
     def reset(self):
         reset_info()
         for i in range(9):
             for j in range(5):
                 self.table.setItem(i, j , QTableWidgetItem(""))
