import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from calculateSmart import CalculateSmart

def application():


    app = QApplication(sys.argv) # объект отвечающий за создание приложения в целом
                                # Создается он всего 1 раз
                                # Параметр - настройки нашего устроиства
    window = QMainWindow() # создаем окно
    window.setWindowTitle("Calculate")
    window.setGeometry(300,250,350,200)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Это что-то")
    main_text.move(100,100)
    main_text.adjustSize()


    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()