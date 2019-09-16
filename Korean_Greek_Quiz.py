import Korean_Greek_Dictionary
import ToolFunctions
import random

tf = ToolFunctions.ToolFunction

class WordQuiz():
    def __init__(self, question, collectAnwser, userAnwser, index):
        self.question = question
        self.collectAnwser = collectAnwser
        self.userAnwser = userAnwser
        self.score = 0
        self.index = index

        if self.collectAnwser == self.userAnwser:
            self.score = 1
        else:
            self.score = 0

class Quiz():
    def __init__(self, KGD):
        self.dictionary = KGD

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

'''
test = Quiz()
test.AskGreek(10)
'''