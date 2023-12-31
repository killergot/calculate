from calculateBasic import *


class CalculateSmart(CalculateBasic):
    lastSymbolIsNumber : bool
    symbolWithOneOperand = ['!','lg','ln']
    arrayNumber = []
    lastSymbolIsNumber = False
    arraySymbol = []
    
    def __reset(self) -> None:
        
        self.logErrorInExpression = '''Error: '''
        self.arrayNumber = []
        self.lastSymbolIsNumber = False
        self.arraySymbol = []

    def prioritySymbols(self,symbol : str) -> int:
        if symbol in ['(']:
            return 0
        elif symbol in ['-', '+']:
            return 1
        elif symbol in ['*', '/','%']:
            return 2
        elif symbol in ['^']:
            return 3
        elif symbol in ['!','log','ln','lg']:
            return 4
        else:
            self.handlerError(f'Неизвеcтный символ: {symbol}')

    def _doSymbol(self,symbol : str) -> Union[int,float]:
        if symbol in self.symbolWithOneOperand:
            num1 = self.arrayNumber.pop()
            return self.getSampleAnswer(symbol,num1)
        else:
            num2 = self.arrayNumber.pop()
            num1 = self.arrayNumber.pop()
            return self.getSampleAnswer(symbol,num1,num2)
        
    def closeBracket(self) -> None:
        currentSymbol = self.arraySymbol.pop()
        while currentSymbol != '(':
            result = self._doSymbol(currentSymbol)
            self.arrayNumber.append(result)
            currentSymbol = self.arraySymbol.pop()
        self.lastSymbolIsNumber = True

    def checkSymbol(self, next_symbol : str) -> None:
        if next_symbol == ')':
            if self.lastSymbolIsNumber: 
                self.closeBracket()
                return
            else:
                self.handlerError(f'''Что-то не так в скобках!!! ''')

        if not self.lastSymbolIsNumber and next_symbol == '-':
            self.arrayNumber.append(0)

        if not self.lastSymbolIsNumber and next_symbol == '!':
            self.handlerError(f'''Пока не умеем считать субфакториал''')
        
        while len(self.arraySymbol) > 0:
            lastSymbol = self.arraySymbol.pop()
            if self.prioritySymbols(next_symbol) <= self.prioritySymbols(lastSymbol) and next_symbol != '(':
                result = self._doSymbol(lastSymbol)
                self.arrayNumber.append(result)
            else:
                self.arraySymbol.append(lastSymbol)
                if self.lastSymbolIsNumber and next_symbol == '(':
                    self.checkSymbol('*')
                break
        
        self.arraySymbol.append(next_symbol)
        if not next_symbol in self.symbolWithOneOperand:
            self.lastSymbolIsNumber = False
    
    def checkNumber(self,nextNumber : int):
        if self.lastSymbolIsNumber:
            self.arrayNumber[-1] = self.arrayNumber[-1] * 10 + nextNumber
        else:
            self.arrayNumber.append(nextNumber)
            self.lastSymbolIsNumber = True

    def doRemainingSymbols(self):
        while len(self.arraySymbol) > 0:
            result = self._doSymbol(self.arraySymbol.pop())
            self.arrayNumber.append(result)

    def getAnswerToExpression(self,expression : str) -> Union[int,float,str]:
        '''Принимает на вход математическое выражение в виде строки.\n
        На выходе выдает ответ или ошибку, при неверном вводе'''
        try:
            for symbol in expression:
                if symbol in ['1','2','3','4','5','6','7','8','9','0','.',',']:
                    self.checkNumber(int(symbol))
                else:
                    self.checkSymbol(symbol)
            self.doRemainingSymbols()
            result = self.arrayNumber[0]
            self.__reset()
            return result
        except:
            self.__reset()
            return self.getLog()


if __name__ == '__main__':
    main = CalculateSmart()

    while True:
        inputExpression = input()
        

        print(f'Вот решение выражения: {main.getAnswerToExpression(inputExpression)}')