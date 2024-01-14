from PyQt6 import QtGui,QtWidgets,QtCore    
import sys
import Menu,timkiem,Sort,thongke
from PyQt6.QtWidgets import QApplication, QMainWindow,QSplashScreen,QDialog
from PyQt6.uic import loadUi
from People import People
from nhanvien import nhanvien

ui=''
app=QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
List=nhanvien()

def homeUi():
    global ui
    ui=Menu.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_3.clicked.connect(timkiemUi)
    ui.pushButton_2.clicked.connect(sortUi)
    ui.pushButton_4.clicked.connect(thongkeUi)
    MainWindow.show()

def thongkeUi():
    global ui
    ui=thongke.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_3.clicked.connect(homeUi)
    MainWindow.show()

def timkiemUi():
    global ui
    ui=timkiem.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_3.clicked.connect(homeUi)
    ui.pushButton_4.clicked.connect(deleteEmployee)
    ui.pushButton_5.clicked.connect(updateEmployee)
    MainWindow.show()


def sortUi():
    global ui, List
    ui = Sort.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.thoat.clicked.connect(homeUi)
    
    ui.m1.clicked.connect(Type1)
    ui.h1.clicked.connect(Type2)
    ui.n1.clicked.connect(Type3)
    ui.c1.clicked.connect(Type4)
    ui.l1.clicked.connect(Type5)
    
    ui.m2.clicked.connect(Type6)
    ui.h2.clicked.connect(Type7)
    ui.n2.clicked.connect(Type8)
    ui.c2.clicked.connect(Type9)
    ui.l2.clicked.connect(Type10)
    
    ui.m3.clicked.connect(Type11)
    ui.h3.clicked.connect(Type12)
    ui.n3.clicked.connect(Type13)
    ui.c3.clicked.connect(Type14)
    ui.l3.clicked.connect(Type15)
    
    ui.m4.clicked.connect(Type16)
    ui.h4.clicked.connect(Type17)
    ui.n4.clicked.connect(Type18)
    ui.c4.clicked.connect(Type19)
    ui.l4.clicked.connect(Type20)
    ui.List = List
    MainWindow.show()

def Type1():
    List.selection_sort('EmCode')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type2():
    List.selection_sort('Name')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type3():
    List.selection_sort('Date')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type4():
    List.selection_sort('Position')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type5():
    List.selection_sort('Salary')
    updateTableWidgetWithSortedData(List, List.nhan_vien)

def Type6():
    List.insertion_sort('EmCode')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type7():
    List.insertion_sort('Name')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type8():
    List.insertion_sort('Date')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type9():
    List.insertion_sort('Position')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type10():
    List.insertion_sort('Salary')
    updateTableWidgetWithSortedData(List, List.nhan_vien)

def Type11():
    global List
    List.nhan_vien=List.quick_sort(List.nhan_vien,'EmCode')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type12():
    global List
    List.nhan_vien=List.quick_sort(List.nhan_vien,'Name')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type13():
    global List
    List.nhan_vien=List.quick_sort(List.nhan_vien,'Date')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type14():
    global List
    List.nhan_vien=List.quick_sort(List.nhan_vien,'Position')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type15():
    global List
    List.nhan_vien=List.quick_sort(List.nhan_vien,'Salary')
    updateTableWidgetWithSortedData(List, List.nhan_vien)

def Type16():
    global List
    List.nhan_vien=List.merge_sort(List.nhan_vien,'EmCode')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type17():
    global List
    List.nhan_vien=List.merge_sort(List.nhan_vien,'Name')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type18():
    global List
    List.nhan_vien=List.merge_sort(List.nhan_vien,'Date')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type19():
    global List
    List.nhan_vien=List.merge_sort(List.nhan_vien,'Position')
    updateTableWidgetWithSortedData(List, List.nhan_vien)
def Type20():
    global List
    List.nhan_vien=List.merge_sort(List.nhan_vien,'Salary')
    updateTableWidgetWithSortedData(List, List.nhan_vien)

def updateTableWidgetWithSortedData(List,sorted_data):
    ui.tableWidget.clearContents()
    ui.tableWidget.setRowCount(0)

    for row, person in enumerate(sorted_data):
        row_position = ui.tableWidget.rowCount()
        ui.tableWidget.insertRow(row_position)
        ui.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(person.EmCode))
        ui.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(person.Name))
        ui.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(person.Date))
        ui.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(person.Position))
        ui.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(person.Salary))

def deleteEmployee():
    global List, ui
    search_id = ui.lineEdit.text()

    found_employee = None
    for employee in List.nhan_vien:
        if employee.EmCode == search_id: 
            found_employee = employee
            break

    if found_employee:
        List.nhan_vien.remove(found_employee)
        updateTableWidgetWithSortedData(List, List.nhan_vien)
        QtWidgets.QMessageBox.information(MainWindow, "Xóa", "Nhân viên đã được xóa thành công!")
    else:
        QtWidgets.QMessageBox.warning(MainWindow, "Xóa", "Không tìm thấy nhân viên!")

def updateEmployee():
    global List, ui
    search_id = ui.lineEdit.text()  
    new_salary = ui.lineEdit_5.text() 
    new_name=ui.lineEdit_2.text()
    new_date=ui.lineEdit_3.text()
    new_pos=ui.lineEdit_4.text()

    found_employee = None
    for employee in List.nhan_vien:  
        if employee.EmCode == search_id:  
            found_employee = employee
            break

    if found_employee:
        if new_salary:
            found_employee.Salary = new_salary

        if new_name:
            found_employee.Name = new_name

        if new_pos:
            found_employee.Position = new_pos
        
        if new_date:
            found_employee.Date = new_date

        updateTableWidgetWithSortedData(List, List.nhan_vien)
        QtWidgets.QMessageBox.information(MainWindow, "Cập nhật", "Thông tin nhân viên đã được cập nhật thành công!")
    else:
        QtWidgets.QMessageBox.warning(MainWindow, "Cập nhật", "Không tìm thấy nhân viên!")

List.ShowInfo()
homeUi()
sys.exit(app.exec())

