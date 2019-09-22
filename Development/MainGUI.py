import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

from MenuGui import MenuWidget
from MainQuizGui import MainQuizWidget

from BackEnd import Korean_Greek_Dictionary, Korean_Greek_Quiz

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stk_l = QStackedLayout()
        self.menuWidget = MenuWidget()

        self.dictionary = Korean_Greek_Dictionary.Korean_Greek_Dictionary()
        self.quiz = Korean_Greek_Quiz.Quiz(self.dictionary)

        self.quizWidget = MainQuizWidget(self.quiz)

        self.setGUI()

    def setGUI(self):
        self.stk_l.addWidget(self.menuWidget)
        self.stk_l.addWidget(self.quizWidget)

        self.menuWidget.quizButton.clicked.connect(self.GoQuizMenu)
        self.quizWidget.quizWidget.menuButton.clicked.connect(self.GoMenu)

        self.setLayout(self.stk_l)
        self.setGeometry(0, 30, 1200, 675)
    
        
    def GoQuizMenu(self):
        self.stk_l.setCurrentIndex(1)
    
    def GoMenu(self):
        self.stk_l.setCurrentIndex(0)
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    mWindow = MainWindow()
    mWindow.show()
    app.exec_()