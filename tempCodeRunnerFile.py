from PyQt6 import QtGui,QtWidgets,QtCore    
import sys
import Menu,timkiem,Sort,thongke
from PyQt6.QtWidgets import QApplication, QMainWindow,QSplashScreen,QDialog
from PyQt6.uic import loadUi
import csv
from People import People
from nhanvien import nhanvien
from PyQt6.QtWidgets import QMessageBox

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
    ui.pushButton_6.clicked.connect(load_data_from_file)
    ui.pushButton.clicked.connect(add_data_to_table)
    MainWindow.show()


def thongkeUi():
    global ui,List
    ui=thongke.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_3.clicked.connect(homeUi)
    ui.pushButton.clicked.connect(thongke1)
    ui.pushButton_2.clicked.connect(thongke2)
    MainWindow.show()

def thongke2(self):
    global List, ui

    salary_ranges = {'<5000$': 0, '5000-10000$': 0, '10000-15000$': 0, '15000-20000$': 0, '>20000$': 0}

    total_employees = len(List.nhan_vien)
    for person in List.nhan_vien:
        salary_str = person.Salary.replace('$', '').replace(',', '')  #xoa $
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

    ui.tableWidget.clearContents()
    ui.tableWidget.setRowCount(2) 

    # Populate the tableWidget with counts and percentages within the existing columns
    for col_position, (range_label, count) in enumerate(salary_ranges.items()):
        # Set header item for the current column
        item = QtWidgets.QTableWidgetItem(range_label)
        ui.tableWidget.setHorizontalHeaderItem(col_position, item)

        # Set item for the count in the first row
        ui.tableWidget.setItem(0, col_position, QtWidgets.QTableWidgetItem(str(count)))

        # Calculate and display the percentage in the second row
        percentage = (count / total_employees) * 100
        ui.tableWidget.setItem(1, col_position, QtWidgets.QTableWidgetItem(f"{percentage:.2f}%"))