from PyQt4 import QtCore
from PyQt4 import QtGui # Import the PyQt4 module we'll need
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys # We need sys so that we can pass argv to QApplication

import design # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer
import os
import webbrowser
import subprocess
import new as script
import threading

import datetime 
from datetime import datetime
import time





class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()
	self.stop = False

    def run(self):
	while not self.stop:
            script.main()


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
       
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        self.t1 = None
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        # When the button is pressed
        self.btnAddContact.clicked.connect(self.openWebToAddContact)                                                    # Execute browse_folder function
        self.btnHistory.clicked.connect(self.openHistory)
        self.btnStart.clicked.connect(self.runScriptStart)
        self.btnStop.clicked.connect(self.btn_stop)
        self.btnContactList.clicked.connect(self.open_contact)
        #update date and current time from os.
        time = QTime()
        date = QDate()
        
        current_t = time.currentTime()
        current_d = date.currentDate()

        self.timeEdit.setTime(current_t)
        self.dateEdit.setDate(current_d)

      
    def openWebToAddContact(self):
        webbrowser.open('https://www.twilio.com/console/phone-numbers/verified')

    def openHistory(self):
        os.system('xdg-open /home/pi/Desktop/history.csv')

        
    def runScriptStart(self):
        self.t1 = StoppableThread()
        self.t1.start()
        
        
    def btn_stop(self):
        self.t1.stop = True

    def open_contact(self):
        script.open_contact()
        os.system('xdg-open /home/pi/Desktop/contact.txt')
        
     
def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app
    


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
