from BackEnd import Korean_Greek_Dictionary
import random

class WordQuiz():
    def __init__(self, question, collectAnwser, userAnwser, index):
        self.question = question
        self.collectAnwser = collectAnwser
        self.userAnwser = userAnwser
        self.score = 0
        self.index = index

    def scoring(self):
        if self.collectAnwser == self.userAnwser:
            self.score = 1
        else:
            self.score = 0

        return self.score

class Quiz():
    def __init__(self, KGD):
        self.dictionary = KGD
        self.wordQuizList = list()
        self.Reset(self.dictionary.GetLength())

    def SetDictionary(self, KGD):
        self.dictionary = KGD

    def Reset(self, QuestionNumber):
        self.indexList = self.GetRandomIndeces(QuestionNumber)
        self.MakeQuestion()
        self.isPerfect = False

    def MakeQuestion(self):
        self.wordQuizList = list()

        for n in range(0, len(self.indexList)):
            word = self.dictionary.dictionary[self.indexList[n]]
            user = ""
            
            self.wordQuizList.append(WordQuiz(word.korean, word.greek, user, self.indexList[n]))
        
    def SetAnwser(self, user, index):
        self.wordQuizList[index].userAnwser = user

    def ScoreQuestion(self):

        wrongIndexList = list()

        for question in self.wordQuizList:
            if question.scoring() == 0:
                wrongIndexList.append(question.index)

        self.indexList = wrongIndexList

        if not wrongIndexList:
            self.isPerfect = True
        else:
            self.isPerfect = False

    def GetRandomIndeces(self, QuestionNumber):
        QuestionIndex = list()

        n = 0

        while n < QuestionNumber:
            randNumber = random.randrange(0, self.dictionary.GetLength())
            isDuplicated = False

            for i in QuestionIndex:
                if randNumber == i:
                    isDuplicated = True
                    break

            if isDuplicated == False:
                QuestionIndex.append(randNumber)
                n += 1

        return QuestionIndex

    def GetQuestionNumber(self):
        return len(self.wordQuizList)

'''
test = Quiz()
test.AskGreek(10)

    def PrintQuizResult(self, quizList):
        strFormat = '%-30s%-30s%-30s%-30s'
        strOut = strFormat % ('질문', '정답', '답변', '채점')
        print(strOut)
        #print('질문', '정답'.ljust(30), '답변'.ljust(60), '채점'.ljust(90))

        totalScore = 0
        totalQuestions = len(quizList)

        for result in quizList:
            if result.score == 1:
                strOut = strFormat % (result.question, result.collectAnwser, result.userAnwser, '맞음')
                print(strOut)
                #print(result.question, result.collectAnwser.ljust(30), result.userAnwser.ljust(60), '맞음'.ljust(90))
                totalScore += 1
            else:
                strOut = strFormat % (result.question, result.collectAnwser, result.userAnwser, '틀림')
                print(strOut)
                #print(result.question, result.collectAnwser.ljust(30), result.userAnwser.ljust(60), '틀림'.ljust(90))

        print("점수: " + str(totalScore)+'/'+str(totalQuestions)+' 정답률: '+str(totalScore/totalQuestions*100)+'%')

    def Main(self, questionNumber):
        initialIndex = self.GetRandomIndeces(questionNumber)

        wrongIndex = self.Ask(initialIndex)

        while wrongIndex:
            inputInt = tf.IntParser(0, 1, "틀린 단어를 복습하려면 0을 그냥 넘어가려면 1을 누르세요: ")
            if inputInt == 0:
                wrongIndex = self.Ask(wrongIndex)
            elif inputInt == 1:
                break

        if not wrongIndex:
            print("축하합니다! 벌금을 낼 필요가 없습니다!")

    def Ask(self, indexList):
        wordQuizList = list()

        for n in range(0, len(indexList)):
            word = self.dictionary.dictionary[indexList[n]]
            user = input(str(n)+". " + word.korean + ": ")
            
            wordQuizList.append(WordQuiz(word.korean, word.greek, user, indexList[n]))
        
        self.PrintQuizResult(wordQuizList)

        wrongIndexList = list()
        for result in wordQuizList:
            if result.score == 0:
                wrongIndexList.append(result.index)

        return wrongIndexList
'''