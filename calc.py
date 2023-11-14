import numpy as np
import math
from typing import Union


class Calculate:
    lastSymbolIsNumber : bool
    logErrorInExpression : str = '''Произошла ошибка при вычислении выражения, возможно, вы ввели что-то не так
    Вот вид ошибки: '''
    symbolWithOneOperand = ['!','lg','ln']

    def __init__(self):
        self.arrayNumber = []
        self.lastSymbolIsNumber = False
        self.arraySymbol = []

    def handlerError(self,error : str) -> None:
        self.logErrorInExpression += error
        print(self.logErrorInExpression)
        exit()

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
        try:
            num1 = None
            num2 = self.arrayNumber.pop()
            if not symbol in self.symbolWithOneOperand:
                num1 = self.arrayNumber.pop()

            # print(f'{symbol=} {num1=}, {num2=}')
            if symbol == '-':
                return num1 - num2
            elif symbol == '+':
                return num1 + num2
            elif symbol == '/':
                if (num2 != 0):
                    return num1 / num2
                else:
                    self.handlerError(f'''Деление на ноль: {num1}/{num2}!!! ''')
            elif symbol == '%':
                if (num2 != 0):
                    return num1 % num2
                else:
                    self.handlerError(f'''Деление на ноль: {num1}%{num2}!!! ''')
            elif symbol == '*':
                return num1 * num2
            elif symbol == '^':
                return num1 ** num2
            elif symbol == '!':
                if num2 < 0:
                    self.handlerError(f'''Пока не умеем строить гамма функции, так что не находим факториал
    отрицательного числа: !({num2})''')
                    return (math.factorial(num2))
        except:
            self.handlerError('Что-то не так с вводом символов')
        
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
                self.handlerError(f'''Неправильно введенное значение в скобках!!! ''')

        if not self.lastSymbolIsNumber and next_symbol == '-':
            self.arrayNumber.append(0)
        
        while len(self.arraySymbol) > 0:
            lastSymbol = self.arraySymbol.pop()
            if self.prioritySymbols(next_symbol) <= self.prioritySymbols(lastSymbol) and next_symbol != '(':
                result = self._doSymbol(lastSymbol)
                print(result)
                self.arrayNumber.append(result)
            else:
                self.arraySymbol.append(lastSymbol)
                if self.lastSymbolIsNumber and next_symbol == '(':
                    self.checkSymbol('*')
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
            result = self._doSymbol(self.arraySymbol.pop())
            self.arrayNumber.append(result)

    def getAnswerToExpression(self,expression : str) -> Union[int,float,str]:
        for symbol in expression:
            if symbol in ['1','2','3','4','5','6','7','8','9','0']:
                self.checkNumber(int(symbol))
            else:
                self.checkSymbol(symbol)
        self.doRemainingSymbols()
        return self.arrayNumber[0]

main = Calculate()

allInput = input()

print(f'Вот решение выражения: {main.getAnswerToExpression(allInput)}')