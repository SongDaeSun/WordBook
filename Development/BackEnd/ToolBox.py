import os

class ToolBox():
    def IntParser(self, min, max, inputString):
        try:
            n = int(inputString)

            if n >= min and n <= max:
                return n

            else:
                return None
            
        except ValueError :
            return None

    def SearchUiDir(self, fileName):
        dirSting = os.getcwd() + "\\UIs\\" + fileName
        return (dirSting)

    def SearchBackEndiDir(self, fileName):
        dirSting = os.getcwd() + "\\BackEnd\\" + fileName
        return (dirSting)

test = ToolBox()

print(test.SearchUiDir("AskUi.ui"))
