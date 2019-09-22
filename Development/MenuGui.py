import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

from BackEnd import ToolBox

tb = ToolBox.ToolBox()
mainwindow_class  = uic.loadUiType(tb.SearchUiDir("MenuUi.ui"))[0]

class MenuWidget(QWidget, mainwindow_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exitButton.clicked.connect(QCoreApplication.instance().quit)

'''
if __name__ == "__main__":

    app = QApplication(sys.argv)
    mWindow = MenuWidget()
    mWindow.show()
    app.exec_()
'''