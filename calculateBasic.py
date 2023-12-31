import math
import decimal

import numpy

from typing import Union

class CalculateBasic:
    logErrorInExpression : str = '''Error: '''
    def handlerError(self,error : str) -> None:
        self.logErrorInExpression += error
        exit()

    def getLog(self) -> str:
        return self.logErrorInExpression

    def __plus(self,num1 : Union[int,float], num2 : Union[int,float]) -> Union[int,float]:
        return num1 + num2
    
    def __minus(self,num1 : Union[int,float], num2 : Union[int,float]) -> Union[int,float]:
        return num1 - num2
    
    def __degree(self,num1 : Union[int,float], num2 : Union[int,float]) -> float:
        num1 = decimal.Decimal(str(num1))
        num2 = decimal.Decimal(str(num2))
        return float(num1 ** num2)
    
    def __division(self,num1 : Union[int,float], num2 : Union[int,float]) -> float:
        if (num2 != 0):
            num1 = decimal.Decimal(str(num1))
            num2 = decimal.Decimal(str(num2))
            return float(num1 / num2)
        else:
            self.handlerError(f'Деление на ноль: {num1}/{num2}!!!')
    
    def __remainderOfDivision(self,num1 : Union[int,float], num2 : Union[int,float]) -> int:
        if (num2 != 0):
            return num1 % num2
        else:
            self.handlerError(f'Деление на ноль: {num1}%{num2}!!!')

    def __multiplication(self,num1 : Union[int,float], num2 : Union[int,float]) -> float:
        num1 = decimal.Decimal(str(num1))
        num2 = decimal.Decimal(str(num2))
        return float(num1 * num2)
    
    def __factorial(self,num : int,_ : None = None) -> int:
        if num < 0:
            self.handlerError(f'''Пока не умеем строить гамма функции, так что не находим факториал
отрицательного числа: ({num})!''')
        elif not isinstance(num, int):
            self.handlerError(f'''Факториал нужно брать от целого числа: ({num})!''')
        else:    
            return (math.factorial(num))
        
    def __subfactorial(self,num : int, _ : None = None) -> int:
        if num == 0:
            return 1
        elif num == 1:
            return 0
        else:
            return (num - 1) * (self.__subfactorial(num - 1) + self.__subfactorial(num - 2))
    
    def __init__(self):
        self.doSymbols = {
            '-' : self.__minus,
            '+' : self.__plus,
            '^' : self.__degree,
            '*' : self.__multiplication,
            '!' : self.__factorial,
            '/' : self.__division,
            '%' : self.__remainderOfDivision
        }

    def getSampleAnswer(self,
                        symbol : str,num1 : Union[int,float],
                        num2 : Union[int,float,None] = None) -> Union[int,float]:
        return self.doSymbols[symbol](num1,num2)
    

if __name__ == '__main__':
    calc = CalculateBasic()
    print(calc.getSampleAnswer('*', 5, 7))