#This program is a template for using a ui designed in QtDesign5
import sys
sys.path.append('/usr/lib/python3/dist-packages') #That's where PyQt5 is
from Ringer import FamilyOrFriend, Salesman, Deliverer, HansOrGrietje

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class DoorbellButton(QDialog):
    def __init__(self):
        super(DoorbellButton, self).__init__()
        loadUi('DoorbellUi.ui', self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        ringer = FamilyOrFriend()
        ringer.respond()
        
        
app=QApplication(sys.argv)
widget=DoorbellButton()
widget.showFullScreen()
sys.exit(app.exec_())        