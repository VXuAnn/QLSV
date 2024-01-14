

from PyQt6 import QtCore, QtGui, QtWidgets
from People import People
from nhanvien import nhanvien
List=nhanvien()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 400, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 400, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 510, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 220, 641, 171))
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(70, 10, 641, 201))
        self.tableWidget_2.setRowCount(3)
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.pushButton.clicked.connect(self.thongke1)
        self.pushButton_2.clicked.connect(self.thongke2)

        table_width = self.tableWidget.width()
        column_width = table_width / 5  
        column_width = int(column_width)  
        for column in range(5):
            self.tableWidget.setColumnWidth(column, column_width)
            
        table_width = self.tableWidget_2.width()
        column_width = table_width / 5 
        column_width = int(column_width)  
        for column in range(5):
            self.tableWidget_2.setColumnWidth(column, column_width)
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Thống kê số lượng nhân viên theo chức vụ"))
        self.pushButton_2.setText(_translate("MainWindow", "Thống kê tiền lương"))
        self.pushButton_3.setText(_translate("MainWindow", "Thoát"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "<=5000$"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "5000$-10000$"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "10000$-15000$"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "15000$-20000$"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", ">20000$"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "GĐ"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PGĐ"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "QL"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "HC"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "KT"))

    def thongke2(self):
        if not List.nhan_vien: 
            QtWidgets.QMessageBox.warning(None, "Thông báo", "Không có dữ liệu để thống kê!")
            return
        salary_ranges = {'<5000$': 0, '5000-10000$': 0, '10000-15000$': 0, '15000-20000$': 0, '>20000$': 0}
        total_employees = len(List.nhan_vien)
        for person in List.nhan_vien:
            salary_str = person.Salary.replace('$', '').replace(',', '')
            try:
                salary = int(salary_str)
            except ValueError:
                salary = 0 

            if salary < 5000:
                salary_ranges['<5000$'] += 1
            elif 5000 <= salary < 10000:
                salary_ranges['5000-10000$'] += 1
            elif 10000 <= salary < 15000:
                salary_ranges['10000-15000$'] += 1
            elif 15000 <= salary < 20000:
                salary_ranges['15000-20000$'] += 1
            else:
                salary_ranges['>20000$'] += 1

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(2) 

        for col_position, (range_label, count) in enumerate(salary_ranges.items()):
            item = QtWidgets.QTableWidgetItem(range_label)
            self.tableWidget.setHorizontalHeaderItem(col_position, item)

            self.tableWidget.setItem(0, col_position, QtWidgets.QTableWidgetItem(str(count)))

            percentage = (count / total_employees) * 100
            self.tableWidget.setItem(1, col_position, QtWidgets.QTableWidgetItem(f"{percentage:.2f}%"))

    def thongke1(self):
        if not List.nhan_vien:  
            QtWidgets.QMessageBox.warning(None, "Thông báo", "Không có dữ liệu để thống kê!")
            return
        position_counts = {'GĐ': 0, 'PGĐ': 0, 'QL': 0, 'HC': 0, 'KT': 0}

        for person in List.nhan_vien:
            position_counts[person.Position] += 1

       
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(1)  

        for col_position, (position, count) in enumerate(position_counts.items()):
            item = QtWidgets.QTableWidgetItem(position)
            self.tableWidget_2.setHorizontalHeaderItem(col_position, item)
            
            self.tableWidget_2.setItem(0, col_position, QtWidgets.QTableWidgetItem(str(count)))

