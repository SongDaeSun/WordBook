import Korean_Greek_Cui
import ToolFunctions
import sys

class Main():
    def main(self):
        tf = ToolFunctions.ToolFunction
        self.KGC = Korean_Greek_Cui.CUI()

        while True:
            print("----------------단어장--------------")
            print("1. 헬라어 - 한글 단어장")
            print("0. 프로그램 종료")

            inputInt = tf.IntParser(0, 1, "0에서 1사이의 값을 입력하세요: ")

            if inputInt == 1:
                self.KGC.MainCui()
            else:
                sys.exit()
        0
m = Main()
m.main()