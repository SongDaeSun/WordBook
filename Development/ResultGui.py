import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

from BackEnd import ToolBox

tb = ToolBox.ToolBox()

mainwindow_class  = uic.loadUiType(tb.SearchUiDir("ResultUi.ui"))[0]

class ResultWidget(QWidget, mainwindow_class):
    def __init__(self):

        super().__init__()
        self.setupUi(self)

    def ShowResult(self, quiz):
        self.resultTable.setColumnCount(4)
        self.resultTable.setRowCount(quiz.GetQuestionNumber())
        column_headers = ['문제', '정답', '답안', '채점']
        self.resultTable.setHorizontalHeaderLabels(column_headers)

        index = 0
        for result in quiz.wordQuizList:
            self.resultTable.setItem(index, 0, QTableWidgetItem(result.question))
            self.resultTable.setItem(index, 1, QTableWidgetItem(result.collectAnwser))
            self.resultTable.setItem(index, 2, QTableWidgetItem(result.userAnwser))

            if result.score == 0:
                self.resultTable.setItem(index, 3, QTableWidgetItem("틀림"))
            else:
                self.resultTable.setItem(index, 3, QTableWidgetItem("맞음"))

            index += 1

        self.resultTable.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()

        scoreText, scorePercentText = self.totalscore(quiz)

        self.scoreLabel.setText(scoreText)
        self.scorePercentLabel.setText(scorePercentText)

    def totalscore(self, quiz):
        score = 0
        totalQuestions = quiz.GetQuestionNumber()

        for result in quiz.wordQuizList:
            if result.score == 1:
                score += 1

        scoreText = "점수: " + str(score) + "/" + str(totalQuestions)
        scorePercentText = "정답률: " + str(round(score/totalQuestions*100, 0)) + "%" 

        return scoreText, scorePercentText


        