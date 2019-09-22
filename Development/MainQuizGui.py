import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

from QuizGui import QuizWidget
from AskGui import AskWidget
from ResultGui import ResultWidget

class MainQuizWidget(QWidget):
    def __init__(self, quiz):
        super().__init__()
        self.stLayout = QStackedLayout()

        self.quiz = quiz
        self.quizWidget = QuizWidget(self.quiz)
        self.askWidget = AskWidget(self.quiz)
        self.resultWidget = ResultWidget()

        self.setGUI()

    def setGUI(self):
        self.stLayout.addWidget(self.quizWidget)
        self.stLayout.addWidget(self.askWidget)
        self.stLayout.addWidget(self.resultWidget)

        self.quizWidget.startButton.clicked.connect(self.GoAsk)
        self.askWidget.enterButton.clicked.connect(self.Anwser)
        self.askWidget.userLine.returnPressed.connect(self.Anwser)
        self.resultWidget.QuizMenuButton.clicked.connect(self.GoQuizMenu)
        self.resultWidget.RetryButton.clicked.connect(self.Retry)

        self.setLayout(self.stLayout)
    
    def GoAsk(self):
        inputNumber = self.quizWidget.CheckVaildInput()
        if inputNumber:
            self.askWidget.Reset(inputNumber)
            self.stLayout.setCurrentIndex(1)

    def Anwser(self):
        if self.askWidget.NextQuestion():
            self.resultWidget.ShowResult(self.askWidget.GetQuiz())
            self.stLayout.setCurrentIndex(2)
    
    def GoQuizMenu(self):
        self.stLayout.setCurrentIndex(0)
    
    def Retry(self):
        if len(self.askWidget.quiz.indexList) == 0:
            QMessageBox.warning(self, "경고", "틀린 것이 없음으로 재시험을 볼 것도 없습니다! 축하해요!", QMessageBox.Ok)
        
        else:
            self.askWidget.Retry()
            self.stLayout.setCurrentIndex(1)

