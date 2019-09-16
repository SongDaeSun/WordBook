class ToolBox():
    def IntParser(min, max, inputString):
        try:
            n = int(inputString)

            if n >= min and n <= max:
                return n

            else:
                return None
            
        except ValueError :
            return None