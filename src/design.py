# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Wed Jun  7 18:51:43 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(589, 381)     
        #MainWindow.setStyleSheet('background-color:rgb(202, 255, 251)')
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(ba.png);")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        myFont=QtGui.QFont()
        myFont.setBold(True)
        self.btnLocation = QtGui.QPushButton(self.centralwidget)
        self.btnLocation.setGeometry(QtCore.QRect(370, 140, 101, 31))      
        self.btnLocation.setObjectName(_fromUtf8("btnLocation"))
        self.btnLocation.setFont(myFont)
        self.btnLocation.setStyleSheet('background-color:rgb(0, 255, 0)')
        self.btnHistory = QtGui.QPushButton(self.centralwidget)
        self.btnHistory.setGeometry(QtCore.QRect(80, 200, 101, 31))
        self.btnHistory.setObjectName(_fromUtf8("btnHistory"))
        self.btnHistory.setFont(myFont)
        self.btnHistory.setStyleSheet('background-color:rgb(219, 147, 255)')    
        self.btnStop = QtGui.QPushButton(self.centralwidget)
        self.btnStop.setGeometry(QtCore.QRect(20, 130, 101, 31))
        self.btnStop.setObjectName(_fromUtf8("btnStop"))
        self.btnStop.setFont(myFont)
        self.btnStop.setStyleSheet('background-color:rgb(255, 125, 125)') 
        self.btnStart = QtGui.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(20, 90, 101, 31))
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.btnStart.setFont(myFont)
        self.btnStart.setStyleSheet('background-color:rgb(0, 255, 0)')
        self.btnContactList = QtGui.QPushButton(self.centralwidget)
        self.btnContactList.setGeometry(QtCore.QRect(150, 30, 101, 31))
        self.btnContactList.setObjectName(_fromUtf8("btnContactList"))
        self.btnContactList.setFont(myFont)
        self.btnContactList.setStyleSheet('background-color:rgb(255, 255, 76)')
        #self.btnStatus = QtGui.QPushButton(self.centralwidget)
        #self.btnStatus.setGeometry(QtCore.QRect(10, 70, 101, 31))
        #self.btnStatus.setObjectName(_fromUtf8("btnStatus"))
        self.btnAddContact = QtGui.QPushButton(self.centralwidget)
        self.btnAddContact.setGeometry(QtCore.QRect(270, 30, 101, 31))
        self.btnAddContact.setObjectName(_fromUtf8("btnAddContact"))
        self.btnAddContact.setFont(myFont)
        self.btnAddContact.setStyleSheet('background-color:rgb(117, 142, 255)')
        self.timeEdit = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(230, 160, 118, 33))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(230, 200, 110, 33))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuExit = QtGui.QMenu(self.menubar)
        self.menuExit.setObjectName(_fromUtf8("menuExit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 300, 100, 14))  
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setFont(myFont)
        self.label.setStyleSheet('color:red')
        self.label.hide()
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Baby System Care", None))
        self.btnLocation.setText(_translate("MainWindow", "Location map", None))
        self.btnHistory.setText(_translate("MainWindow", "history", None))
        self.btnStop.setText(_translate("MainWindow", "stop", None))
        self.btnStart.setText(_translate("MainWindow", "start", None))
        self.btnContactList.setText(_translate("MainWindow", "contact list", None))
        #self.btnStatus.setText(_translate("MainWindow", "status report", None))
        self.btnAddContact.setText(_translate("MainWindow", "add contact ", None))
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.menuHelp.setTitle(_translate("MainWindow", "help", None))
        self.menuExit.setTitle(_translate("MainWindow", "exit", None))
        self.actionOpen.setText(_translate("MainWindow", "open", None))
        self.actionSave.setText(_translate("MainWindow", "save", None))
        self.label.setText(_translate("MainWindow", "Exeption !!!", None))


