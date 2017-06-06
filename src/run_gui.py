
from PyQt4 import QtGui # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication

import design # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer
import os
import webbrowser
import subprocess
import new as script
import threading
import datetime
import time

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
       
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        #self.btnBrowse.clicked.connect(self.browse_folder)  # When the button is pressed
        self.btnAddContact.clicked.connect(self.openWebToAddContact)                                                    # Execute browse_folder function
        self.btnHistory.clicked.connect(self.openHistory)
        self.btnStart.clicked.connect(self.runScriptStart)
        self.btnStop.clicked.connect(self.stop)
        
       # self.QDateTime.connect(self.defaultTime)
      #  self.dateTimeEdit.clicked.connect(self.disp_time)
        #now = QDateTime
        #now.setTime_t(time.time())
        #self.time.setDateTime(now)
      
  #  def browse_folder(self):
     #   self.listWidget.clear() # In case there are any existing elements in the list
      #  directory = QtGui.QFileDialog.getExistingDirectory(self,"Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory

      #  if directory: # if user didn't pick a directory don't continue
       #     for file_name in os.listdir(directory): # for all files, if any, in the directory
        #        self.listWidget.addItem(file_name)  # add file to the listWidget


   # def defaultTime(self):
        # now = QDateTime()
        # now.setTime_t(time.time())
        # self.time.setDateTime(now)
        
    def openWebToAddContact(self):
        webbrowser.open('https://www.twilio.com/console/phone-numbers/verified')

    def openHistory(self):
        os.system('xdg-open /home/pi/Desktop/history.csv')

        
    def runScriptStart(self):
        t1 = threading.Thread(target= script.main())
        t1.start()
        #t1.join()

    def stop(self):
        t2 = threading.Thread(target= script.stop())
        #t2.exit()
       # t2= threading.Thread(target= script.stop())
      #  t2.start()
     #   t2.join()
        

        
def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app
    


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
