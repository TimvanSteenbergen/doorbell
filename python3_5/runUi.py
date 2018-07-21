import sys
sys.path.append('/usr/lib/python3/dist-packages') #That's where PyQt5 is
import PyQt5

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit
from PyQt5.QtWidgets import QTextEdit, QWidget, QDialog, QApplication
import qtScreendesign.uibuttons as ui


class MainWindow(QDialog, ui):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':  #If this is the main program, then ...
    app = QApplication(sys.argv) #... Define 'app' as an QApplication, accepting arguments
    form = MainWindow()          #... Instantiate 'form' as a MainWindow 
    form.show()                  #... Show the form
    sys.exit(app.exec_())        #... Run 'app' until it is stopped

