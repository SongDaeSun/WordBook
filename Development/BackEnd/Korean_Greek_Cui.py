import Korean_Greek_Dictionary
import Korean_Greek_Quiz
import ToolFunctions

tf = ToolFunctions.ToolFunction

class CUI():
    def __init__(self):
        self.dictionary = Korean_Greek_Dictionary.Korean_Greek_Dictionary()
        self.quiz = Korean_Greek_Quiz.Quiz(self.dictionary)

    def MainCui(self):
        while True:
            print("---------헬라어 - 한글 단어장---------")
            print("1. 단어장 확인")
            print("2. 단어 추가")
            print("3. 단어 삽입")
            print("4. 단어 수정")
            print("5. 단어 삭제")
            print("6. 단어 퀴즈")
            print("0. 메인화면으로")

            inputInt = tf.IntParser(0, 6, "0에서 6사이의 값을 입력하세요: ")

            if inputInt == 1:
                self.dictionary.PrintDictionary()
            elif inputInt == 2:
                self.AddWord()
            elif inputInt == 3:
                self.InsertWord()
            elif inputInt == 4:
                self.EditWord()
            elif inputInt == 5:
                self.DelWord()
            elif inputInt == 6:
                self.QuizDictionary()
            elif inputInt == 0:
                self.dictionary.WriteMemory()
                break

    def AddWord(self):
        print("-------헬라어 - 한글 단어 추가-------")
        korean = input("한국어 단어를 입력하세요: ")
        greek = input("헬라어 단어를 입력하세요: ")

        self.dictionary.AddDictionary(korean, greek)

    def InsertWord(self):
        print("-------헬라어 - 한글 단어 삽입-------")
        self.dictionary.PrintDictionary()
        index = tf.IntParser(1, self.dictionary.GetLength(), "삽입할 인덱스를 입력하세요: ")
        korean = input("한국어 단어를 입력하세요: ")
        greek = input("헬라어 단어를 입력하세요: ")

        self.dictionary.InsertDictionary(index - 1, korean, greek)

    def EditWord(self):
        print("-------헬라어 - 한글 단어 수정-------")
        self.dictionary.PrintDictionary()
        index = tf.IntParser(1, self.dictionary.GetLength(), "수정할 단어의 인덱스를 입력하세요: ")

        korean = input("한국어 단어를 입력하세요: ")
        greek = input("헬라어 단어를 입력하세요: ")

        self.dictionary.EditDictionary(index - 1, korean, greek)
    
    def DelWord(self):
        print("-------헬라어 - 한글 단어 삭제-------")
        self.dictionary.PrintDictionary()
        index = tf.IntParser(1, self.dictionary.GetLength(), "삭제할 단어의 인덱스를 입력하세요: ")
        self.dictionary.DelDictionary(index - 1)

    def QuizDictionary(self):
        print("---------헬라어 - 한글 퀴즈---------")
        index = tf.IntParser(1, self.dictionary.GetLength(), "총 단어의 수는 "+str(self.dictionary.GetLength())+"개 입니다.\n원하는 퀴즈 문제 수를 입력하세요: ")
        self.quiz.Main(index)