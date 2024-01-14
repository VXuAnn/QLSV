from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
import sys
from People import People
from nhanvien import nhanvien
List=nhanvien()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 20, 621, 231))
        self.tableWidget.setObjectName("tableWidget")   
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 280, 181, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 330, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 280, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 340, 181, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 410, 181, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(530, 280, 191, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(530, 340, 191, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 480, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 380, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 430, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.pushButton.clicked.connect(self.search_and_display)
        self.pushButton_2.clicked.connect(self.binary_search_and_display)

        self.MainWindow = MainWindow
        
        self.tableWidget.setColumnCount(5)

        table_width = self.tableWidget.width()
        column_width = table_width / 5 
        column_width = int(column_width)  
        for column in range(5):
            self.tableWidget.setColumnWidth(column, column_width)
        self.tableWidget.setHorizontalHeaderLabels(["Mã nhân viên", "Họ và Tên", "Ngày sinh", "Chức vụ", "Lương"])

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tìm kiếm"))
        self.pushButton.setText(_translate("MainWindow", "Tìm kiếm tuần tự"))
        self.pushButton_2.setText(_translate("MainWindow", "Tìm kiếm nhị phân"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Nhập mã cần tìm"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Nhập tên cần tìm"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Nhập ngày sinh cần tìm"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Nhập chức vụ cần tìm"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Nhập lương cần tìm"))
        self.pushButton_3.setText(_translate("MainWindow", "Thoát"))
        self.pushButton_4.setText(_translate("MainWindow", "Xóa"))
        self.pushButton_5.setText(_translate("MainWindow", "Cập nhật"))

    def search_and_display(self):
        search_value_1 = self.lineEdit.text()
        search_value_2 = self.lineEdit_2.text()
        search_value_3 = self.lineEdit_3.text()
        search_value_4 = self.lineEdit_4.text()
        search_value_5 = self.lineEdit_5.text()

        
        found_people = []

       
        for person in List.nhan_vien:
            is_found = False 
            if search_value_1 and person.EmCode == search_value_1:
                is_found = True
            elif search_value_2 and person.Name == search_value_2:
                is_found = True
            elif search_value_3 and person.Date == search_value_3:
                is_found = True
            elif search_value_4 and person.Position == search_value_4:
                is_found = True
            elif search_value_5 and person.Salary == search_value_5:
                is_found = True

            if is_found:
                found_people.append(person)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        for person in found_people:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(person.EmCode))
            self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(person.Name))
            self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(person.Date))
            self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(person.Position))
            self.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(person.Salary))

        for line_edit in [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5]:
            line_edit.clear()

    def binary_search(sorted_list, search_value):
        left = 0
        right = len(sorted_list) - 1

        while left <= right:
            mid = (left + right) // 2 

            if sorted_list[mid].EmCode == search_value:
                return sorted_list[mid] 

            elif sorted_list[mid].EmCode < search_value:
                left = mid + 1  
            else:
                right = mid - 1  
        return None  

    def binary_search_and_display(self):
        search_value_1 = self.lineEdit.text()
        search_value_2 = self.lineEdit_2.text()
        search_value_3 = self.lineEdit_3.text()
        search_value_4 = self.lineEdit_4.text()
        search_value_5 = self.lineEdit_5.text()

        if not any([search_value_1, search_value_2, search_value_3, search_value_4, search_value_5]):
            QtWidgets.QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập ít nhất một thông tin để tìm kiếm.")
            return
        List.nhan_vien.sort(key=lambda x: x.EmCode) 
        found_people = []
        for person in List.nhan_vien:
            is_found = (
                (not search_value_1 or person.EmCode == search_value_1) and
                (not search_value_2 or person.Name == search_value_2) and
                (not search_value_3 or person.Date == search_value_3) and
                (not search_value_4 or person.Position == search_value_4) and
                (not search_value_5 or person.Salary == search_value_5)
            )
            if is_found:
                found_people.append(person)

        if found_people:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            for person in found_people:
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(person.EmCode))
                self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(person.Name))
                self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(person.Date))
                self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(person.Position))
                self.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(person.Salary))
        else:
            QtWidgets.QMessageBox.critical(self.MainWindow, "Không tìm thấy", "Không tìm thấy nhân viên thỏa mãn điều kiện tìm kiếm.")

        for line_edit in [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4,self.lineEdit_5]:
                line_edit.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
