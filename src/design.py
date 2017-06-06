# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Tue Jun  6 12:14:22 2017
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
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnLocation = QtGui.QPushButton(self.centralwidget)
        self.btnLocation.setGeometry(QtCore.QRect(10, 20, 101, 31))
        self.btnLocation.setObjectName(_fromUtf8("btnLocation"))
        self.btnHistory = QtGui.QPushButton(self.centralwidget)
        self.btnHistory.setGeometry(QtCore.QRect(190, 10, 101, 31))
        self.btnHistory.setObjectName(_fromUtf8("btnHistory"))
        self.btnStop = QtGui.QPushButton(self.centralwidget)
        self.btnStop.setGeometry(QtCore.QRect(20, 200, 101, 31))
        self.btnStop.setObjectName(_fromUtf8("btnStop"))
        self.btnStart = QtGui.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(10, 160, 101, 31))
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.btnContactList = QtGui.QPushButton(self.centralwidget)
        self.btnContactList.setGeometry(QtCore.QRect(20, 120, 101, 31))
        self.btnContactList.setObjectName(_fromUtf8("btnContactList"))
        self.btnStatus = QtGui.QPushButton(self.centralwidget)
        self.btnStatus.setGeometry(QtCore.QRect(10, 70, 101, 31))
        self.btnStatus.setObjectName(_fromUtf8("btnStatus"))
        self.btnAddContact = QtGui.QPushButton(self.centralwidget)
        self.btnAddContact.setGeometry(QtCore.QRect(190, 90, 101, 31))
        self.btnAddContact.setObjectName(_fromUtf8("btnAddContact"))
        self.QDateTime = QtGui.QDateTimeEdit(self.centralwidget)
        self.QDateTime.setGeometry(QtCore.QRect(140, 200, 194, 33))
        self.QDateTime.setObjectName(_fromUtf8("QDateTime"))
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnLocation.setText(_translate("MainWindow", "Location map", None))
        self.btnHistory.setText(_translate("MainWindow", "history", None))
        self.btnStop.setText(_translate("MainWindow", "stop", None))
        self.btnStart.setText(_translate("MainWindow", "start", None))
        self.btnContactList.setText(_translate("MainWindow", "contact list", None))
        self.btnStatus.setText(_translate("MainWindow", "status report", None))
        self.btnAddContact.setText(_translate("MainWindow", "add contact ", None))
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.menuHelp.setTitle(_translate("MainWindow", "help", None))
        self.menuExit.setTitle(_translate("MainWindow", "exit", None))
        self.actionOpen.setText(_translate("MainWindow", "open", None))
        self.actionSave.setText(_translate("MainWindow", "save", None))

