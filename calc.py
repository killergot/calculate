from typing import Union


class Calculate:
    lastSymbolIsNumber : bool
    priorityBracket : int
    logErrorInExpression : str = '''Произошла ошибка при вычислении выражения, возможно, вы ввели что-то не так
    Вот вид ошибки: '''

    def __init__(self):
        self.arrayNumber = []
        self.lastSymbolIsNumber = False
        self.arraySymbol = []
        self.priorityBracket = 5

    def handlerError(self,error) -> None:
        pass

    def _prioritySymbols(self,next_symbol : str) -> int:
        if next_symbol in ['-', '+']:
            return 1
        elif next_symbol in ['*', '/','%']:
            return 2
        elif next_symbol in ['^']:
            return 3
        elif next_symbol in ['(']:
            self.priorityBracket += 1
            return self.priorityBracket
    
    

    def _doSymbol(self,symbol : str,num2 : int,num1 : int) -> Union[int,float,str]:
        if symbol == '-':
            return num1 - num2
        if symbol == '+':
            return num1 + num2
        if symbol == '/':
            if (num2 != 0):
                return num1 / num2
            else:
                self.logErrorInExpression += f'''Деление на 0: {num1}/{num2}!!! '''
                print(self.logErrorInExpression)
                exit()
        if symbol == '%':
            if (num2 != 0):
                return num1 % num2
            else:
                self.logErrorInExpression += f'''Деление на ноль: {num1}%{num2}!!! '''
                print(self.logErrorInExpression)
                exit()
        elif symbol == '*':
            return num1 * num2
        elif symbol == '^':
            return num1 ** num2
        
    def closeBracket(self) -> None:
        currentSymbol = self.arraySymbol.pop()
        while currentSymbol != '(':
            result = self._doSymbol(currentSymbol,
                                    self.arrayNumber.pop(),
                                    self.arrayNumber.pop())
            self.arrayNumber.append(result)
            currentSymbol = self.arraySymbol.pop()

    def checkSymbol(self, next_symbol : str) -> None:
        if next_symbol == ')':
            self.closeBracket()
            return
        if not self.lastSymbolIsNumber and next_symbol == '-':
            self.arrayNumber.append(0)
        while len(self.arraySymbol) > 0:
            lastSymbol = self.arraySymbol.pop()
            if self._prioritySymbols(next_symbol) <= self._prioritySymbols(lastSymbol) and lastSymbol != '(':
                result = self._doSymbol(lastSymbol,self.arrayNumber.pop(),self.arrayNumber.pop())
                self.arrayNumber.append(result)
            else:
                self.arraySymbol.append(lastSymbol)
                break
        self.arraySymbol.append(next_symbol)
        self.lastSymbolIsNumber = False
        
    
    def checkNumber(self,nextNumber : int):
        if self.lastSymbolIsNumber:
            self.arrayNumber[-1] = self.arrayNumber[-1] * 10 + nextNumber
        else:
            self.arrayNumber.append(nextNumber)
            self.lastSymbolIsNumber = True

    def doRemainingSymbols(self):
        while len(self.arraySymbol) > 0:
            result = self._doSymbol(self.arraySymbol.pop(),self.arrayNumber.pop(),self.arrayNumber.pop())
            self.arrayNumber.append(result)

    def getAnswerToExpression(self,expression : str) -> Union[int,float,str]:
        for symbol in allInput:
            if symbol in ['1','2','3','4','5','6','7','8','9','0']:
                self.checkNumber(int(symbol))
            else:
                self.checkSymbol(symbol)
        self.doRemainingSymbols()
        return self.arrayNumber[0]

main = Calculate()

# allInput = input()
allInput = '(((1+2)-3)-4)'

print(f'Вот решение выражения: {main.getAnswerToExpression(allInput)}')
print(main.arraySymbol,main.arrayNumber)