from PyQt6 import QtCore, QtGui, QtWidgets
import csv
from People import People
from nhanvien import nhanvien
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow,QSplashScreen,QDialog,QMessageBox, QMenu

List=nhanvien()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 290, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 340, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 390, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 440, 131, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 500, 101, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(210, 280, 541, 171))
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(270, 30, 51, 31))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 71, 31))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(270, 80, 41, 31))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 80, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 120, 131, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 30, 121, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 80, 121, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 120, 191, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 10, 711, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 470, 131, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.MainWindow = MainWindow
        
        self.tableWidget.setColumnCount(5)

        table_width = self.tableWidget.width()
        column_width = table_width / 5  
        column_width = int(column_width)  
        
        for column in range(5):
            self.tableWidget.setColumnWidth(column, column_width)

        self.tableWidget.setHorizontalHeaderLabels(["Mã nhân viên", "Họ và Tên", "Ngày sinh", "Chức vụ", "Lương"])

        self.pushButton_5.clicked.connect(self.close_application)
        self.pushButton_6.clicked.connect(self.load_data_from_file)
        self.pushButton_7.clicked.connect(self.print_data)
        self.pushButton.clicked.connect(self.add_data_to_table)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quản lý nhân viên"))
        self.pushButton.setText(_translate("MainWindow", "Thêm mới nhân viên"))
        self.pushButton_2.setText(_translate("MainWindow", "Sắp xếp"))
        self.pushButton_3.setText(_translate("MainWindow", "Tìm kiếm "))
        self.pushButton_4.setText(_translate("MainWindow", "Thống kê"))
        self.pushButton_5.setText(_translate("MainWindow", "Thoát"))
        self.groupBox.setTitle(_translate("MainWindow", "Chỗ nhập thông tin"))
        self.label_4.setText(_translate("MainWindow", "Chức vụ"))
        self.label_3.setText(_translate("MainWindow", "Ngày sinh"))
        self.label_5.setText(_translate("MainWindow", "Lương"))
        self.label_2.setText(_translate("MainWindow", "Họ và tên"))
        self.label.setText(_translate("MainWindow", "Mã nhân viên"))
        self.pushButton_6.setText(_translate("MainWindow", "Thêm dữ liệu bằng file có sẵn"))
        self.pushButton_7.setText(_translate("MainWindow", "In danh sách"))

    def close_application(self):
        QApplication.quit()

    def load_data_from_file(self):
        data = self.loadfile() 
        for row, person in enumerate(data):
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)  
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['EmCode']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['Name']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['Date']))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person['Position']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person['Salary']))
            
    def add_data_to_table(self):
        emcode = self.lineEdit.text()
        name = self.lineEdit_2.text() 
        date = self.lineEdit_3.text()
        position = self.lineEdit_4.text()
        salary = self.lineEdit_5.text()
        
        # Kiểm tra xem có đủ 5 thông tin hay không
        if emcode and name and date and position and salary:
            new_person = People(emcode, name, date, position, salary)
            List.nhan_vien.append(new_person)
            
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(emcode))
            self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(date))
            self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(position))
            self.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(salary))

            # Hiển thị thông báo khi thêm thông tin thành công
            QtWidgets.QMessageBox.information(self.MainWindow, "Thông báo", "Thêm thông tin nhân viên thành công.")
            
            # Xóa nội dung của các ô nhập liệu
            for line_edit in [self.lineEdit, self.lineEdit_2,self.lineEdit_3, self.lineEdit_4, self.lineEdit_5]:
                line_edit.clear()

        else:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập đủ 5 thông tin.")

    def loadfile(self):
        data=[]
        filename='nhanvien.csv'
        with open(filename,mode='r',newline='',encoding='utf8') as file:    
            reader=csv.DictReader(file)
            for row in reader:
                data.append(row)
                Newone=People(row['EmCode'],row['Name'],row['Date'],row['Position'],row['Salary'])
                List.nhan_vien.append(Newone)
                
        return data
    def print_data(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        for row, person in enumerate(List.nhan_vien):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person.EmCode))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person.Name))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person.Date))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person.Position))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person.Salary))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
