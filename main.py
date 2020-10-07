
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QLineEdit, QPushButton
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import pyqtSlot


from Game.ColorGame import ColorGame


class Main(QWidget,ColorGame):

    def __init__(self):
        super().__init__()
        self.game = ColorGame()
        self.user = 0
        self.comp = 0
        self.title = "Color Guessing Game"
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 350
        self.loadUI()

    def loadUI(self):
        self.setWindowTitle(self.title)

        self.start = QPushButton("Start",self)
        self.start.clicked.connect(self.gameStart)

        self.end = self.start = QPushButton("End",self)
        self.end.move(0,25)

        self.end.clicked.connect(self.Winner)



        self.text = QLineEdit(self)
        self.text.move(90,0)
        self.text.setValidator(QIntValidator().setRange(0,4))
        self.text.setMaxLength(1)




        self.textbox = QTextEdit(self)
        self.textbox.move(0, 120)
        self.textbox.resize(300, 200)



        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()









    @pyqtSlot()
    def gameStart(self):
            obj.textbox.setText(obj.gameWelcome())

            self.getUserInput(self.text.text())
            self.textbox.append(self.getUserInput(self.text.text()))
            self.game.computerTurn()
            self.textbox.append(self.game.computerTurn())


            usr, comp = obj.game.Score()
            self.user = usr
            self.comp = comp
            self.textbox.append("Player Score" + str(self.user))
            self.textbox.append("Computer Score " + str(self.comp))


    @pyqtSlot()
    def Winner(self):
       self.textbox.append(self.winner(self.user,self.comp))

















if __name__ == '__main__':


    app = QApplication([])
    obj = Main()
    obj.textbox.setText(obj.gameWelcome())




    app.exec()
















