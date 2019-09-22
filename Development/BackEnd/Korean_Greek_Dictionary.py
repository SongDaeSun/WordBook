class Korean_Greek():
    def __init__(self, korean ,greek):
        self.korean = korean
        self.greek = greek


class Korean_Greek_Dictionary():
    def __init__(self):
        self.dictionary = list()
        self.ReadMemory()

    def AddDictionary(self,korean, greek):

        for word in self.dictionary:
            if word.korean == korean and word.greek == greek:
                print("중복되는 단어입니다.")
                return

        self.dictionary.append(Korean_Greek(korean, greek))
        self.WriteMemory()

    def InsertDictionary(self, index, korean, greek):
        for word in self.dictionary:
            if word.korean == korean and word.greek == greek:
                print("중복되는 단어입니다.")
                return

        self.dictionary.insert(index, Korean_Greek(korean, greek))
        self.WriteMemory()

    def EditDictionary(self, index, korean, greek):
        self.dictionary[index] = Korean_Greek(korean, greek)
        self.WriteMemory()

    def DelDictionary(self, index):
        self.dictionary.remove(self.dictionary[index])
        self.WriteMemory()

    def PrintDictionary(self):
        index = 1
        for word in self.dictionary:
            string = str(index)+'. '+word.greek + " : " + word.korean
            print(string)
            index += 1

    def FindKoreanByGreek(self, greek):
        for word in self.dictionary:
            if word.greek == greek:
                return word.korean
        return None

    def FindGreekByKorean(self, korean):
        for word in self.dictionary:
            if word.korean == korean:
                return word.greek
        return None

    def GetLength(self):
        return len(self.dictionary)
    
    def ReadMemory(self):
        f = open('BackEnd\\Korean_Greek_Memory.txt', 'r', -1, "utf-8")
        self.dictionary = list()
        
        while True:
            line = f.readline()
            if not line: break
            raw = line.split(':')
            raw[1] = raw[1][:len(raw[1])-1]
            self.dictionary.append(Korean_Greek(raw[1], raw[0]))
        
        f.close()

    def WriteMemory(self):

        f = open('Korean_Greek_Memory.txt', 'w', -1, "utf-8")

        for word in self.dictionary:
            f.write(word.greek + ":"  + word.korean + '\n')

        f.close()

'''
example = Korean_Greak_Dictionary()
example.AddDictionary("야만적인", 'βαρβαρος')
example.AddDictionary('용, 악마', 'δρακων')
example.WriteMemory()
example.ReadMemory()
example.PrintDictionary()
'''