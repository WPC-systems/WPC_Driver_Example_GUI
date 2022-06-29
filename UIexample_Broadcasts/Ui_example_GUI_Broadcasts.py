# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Chunglee_WPC\Python_Driver_GUI_Example\UIexample_Broadcasts\example_GUI_Broadcasts.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 582)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_declare = QtWidgets.QLabel(self.centralwidget)
        self.lb_declare.setGeometry(QtCore.QRect(20, 110, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.lb_declare.setFont(font)
        self.lb_declare.setObjectName("lb_declare")
        self.btn_broadcast = QtWidgets.QPushButton(self.centralwidget)
        self.btn_broadcast.setGeometry(QtCore.QRect(480, 170, 131, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.btn_broadcast.setFont(font)
        self.btn_broadcast.setStyleSheet("QPushButton {\n"
"    background-color: rgb(61, 79, 99);\n"
"    border-radius : 5px;\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 137, 235);\n"
"}")
        self.btn_broadcast.setObjectName("btn_broadcast")
        self.tableWidget_brst = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_brst.setGeometry(QtCore.QRect(20, 250, 590, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_brst.setFont(font)
        self.tableWidget_brst.setObjectName("tableWidget_brst")
        self.tableWidget_brst.setColumnCount(5)
        self.tableWidget_brst.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_brst.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_brst.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_brst.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_brst.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(195, 195, 195))
        self.tableWidget_brst.setHorizontalHeaderItem(4, item)
        self.lb_trademark = QtWidgets.QLabel(self.centralwidget)
        self.lb_trademark.setGeometry(QtCore.QRect(10, 10, 81, 81))
        self.lb_trademark.setText("")
        self.lb_trademark.setPixmap(QtGui.QPixmap("d:\\Chunglee_WPC\\Python_Driver_GUI_Example\\UIexample_Broadcasts\\../Material/WPC_trademark.jpg"))
        self.lb_trademark.setScaledContents(True)
        self.lb_trademark.setObjectName("lb_trademark")
        self.lb_rights = QtWidgets.QLabel(self.centralwidget)
        self.lb_rights.setGeometry(QtCore.QRect(90, 10, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lb_rights.setFont(font)
        self.lb_rights.setObjectName("lb_rights")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Example - Finding all devices"))
        self.lb_declare.setText(_translate("MainWindow", "This is example for finding all available device from WPC DAQ Device."))
        self.btn_broadcast.setText(_translate("MainWindow", "Find all devices"))
        item = self.tableWidget_brst.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IP address"))
        item = self.tableWidget_brst.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Subnet mask"))
        item = self.tableWidget_brst.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "MAC address"))
        item = self.tableWidget_brst.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Model"))
        item = self.tableWidget_brst.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Firmware ver."))
        self.lb_rights.setText(_translate("MainWindow", " Ⓒ2022 WPC Systems Ltd. All right reserved"))
