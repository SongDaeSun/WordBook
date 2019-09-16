class ToolFunction():
    def IntParser(min, max, InfoString):
        while True:
            raw_string = input('\n' + InfoString)

            try:
                n = int(raw_string)

                if n >= min and n <= max:
                    return n

                else:
                    return None
            
            except ValueError :
                return None

    