import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

from BackEnd import ToolBox

tb = ToolBox.ToolBox()

mainwindow_class  = uic.loadUiType(tb.SearchUiDir("QuizUi.ui"))[0]

class QuizWidget(QWidget, mainwindow_class):
    def __init__(self, quiz):
        super().__init__()
        self.stLayout = QStackedLayout()
        self.quiz = quiz

        self.setupUi(self)
        
        self.maxLabel.setText(str(self.quiz.dictionary.GetLength()))

        

        #self.setGUI()

        #def setGUI(self):
        #  self.stLayout.addWidget(self.menuWidget)

    def CheckVaildInput(self):
        inputstring = tb.IntParser(1,self.quiz.dictionary.GetLength(),self.questionNumberLine.text())

        if not inputstring:
            QMessageBox.warning(self, "경고", "1과 "+str(self.quiz.dictionary.GetLength())+"사이에 있는 숫자를 입력하세요.", QMessageBox.Ok)

        else:
            self.questionNumberLine.setText("")

        return inputstring




