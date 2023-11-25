import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from calculateSmart import CalculateSmart

class Window(QMainWindow):
    counter : int = 0

    def __init__(self):
        super(Window,self).__init__() # Дополняем конструктор QMainWindow

        self.setWindowTitle("Calculate") # Меняем название окна
        self.setGeometry(300,  # Отклонение по x от окна монитора
                        250,  # Отклонение по y от окна монитора
                        350,  # Ширина
                        200)  # Высота
        
        
        self.main_text = QtWidgets.QLabel(self) # Создает текстовую надпись
        self.main_text.setText(f"Это что-то: {self.counter}") # меняет текст
        self.main_text.move(100,100) # положение текста от угла окна приложения
        self.main_text.adjustSize() # Увеличивает ширину объекта, которая ему нужна

        

        button = QtWidgets.QPushButton(self)
        button.move(70,150)
        button.setText("Нажми на меня")
        button.setFixedWidth(200)
        button.clicked.connect(self.addLabel)
    
    def addLabel(self):
        self.counter += 1
        self.main_text.setText(f"Это что-то: {self.counter}") # меняет текст
        self.main_text.adjustSize() # Увеличивает ширину объекта, которая ему нужна
 
def application():


    app = QApplication(sys.argv) # объект отвечающий за создание приложения в целом
                                # Создается он всего 1 раз
                                # Параметр - настройки нашего устроиства
    mainWindow = Window()

    mainWindow.show() # Показывает окно
    # Пока окно открыто, программа не идет дальшеы
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()