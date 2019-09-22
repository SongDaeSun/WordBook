import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

from BackEnd import ToolBox

tb = ToolBox.ToolBox()

mainwindow_class  = uic.loadUiType(tb.SearchUiDir("AskUi.ui"))[0]

class AskWidget(QWidget, mainwindow_class):
    def __init__(self, quiz):

        super().__init__()
        self.setupUi(self)

        self.quiz = quiz
        self.index = 0
        self.isPerfect = False

    def GetQuiz(self):
        return self.quiz

    def SetQuestion(self):
        nameLabel = "문제 " + str(self.index + 1) + "/" + str(self.quiz.GetQuestionNumber())
        self.indexLabel.setText(nameLabel)

        self.questionLabel.setText(self.quiz.wordQuizList[self.index].question)

        self.userLine.setText("")


    def GetAwnser(self):
        self.quiz.SetAnwser(self.userLine.text(), self.index)

    def AddIndex(self):
        self.index += 1

    def Reset(self, QuestionNumber):
        self.index = 0
        self.isPerfect = False
        self.quiz.Reset(QuestionNumber)
        self.SetQuestion()

    def Retry(self):
        self.index = 0
        self.isPerfect = False
        self.quiz.MakeQuestion()
        self.SetQuestion()

    def NextQuestion(self):
        self.GetAwnser()
        self.AddIndex()

        isEnd = False

        if self.index < self.quiz.GetQuestionNumber():
            self.SetQuestion()
            isEnd = False

        else:
            self.quiz.ScoreQuestion()
            isEnd = True
            self.isPerfect = self.quiz.isPerfect
            
        return isEnd
        



        

