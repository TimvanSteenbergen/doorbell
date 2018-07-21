# This program is a template for using a ui designed in QtDesign5
# Credits to Hanif's tutorial see https://youtu.be/7SrD4l2o-uk

import sys
sys.path.append('/usr/lib/python3/dist-packages') #That's where PyQt5 is

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class Life2Coding(QDialog):
    def __init__(self):
        super(Life2Coding, self).__init__()
        loadUi('TemplateQtUi.ui', self)
        self.setWindowTitle('Life2Coding PyQt5 Gui')
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.label1.setText('Hoi ' + self.lineEdit.text())
        
app=QApplication(sys.argv)
widget=Life2Coding()
widget.show()
sys.exit(app.exec_())        