import sys
import time
import random

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QMouseEvent, QPaintEvent, QStaticText
from PyQt5.QtCore import Qt, QPoint

class Wonsz():
    def __init__(self, widthpixels, heightpixels, startpointX, startpointY, direction, WonszID):
        self.Map = [[0 for x in range(widthpixels)] for y in range(heightpixels)]
        self.heightpixels = heightpixels
        self.widthpixels = widthpixels
        self.WonszList = [[startpointY, startpointX, direction]]
        self.startpointX = startpointX
        self.startpointY = startpointY
        self.WonszID = WonszID
        self.WonszLength = 1
        self.appleid = 5
        self.score = 0
        self.alive = True
        #0 - lewo, 1 - prawo, 2 - gora, 3 - dol
    def prepareMap(self):
        for i in range(self.widthpixels):
            for j in range(self.heightpixels):
                self.Map[i][j] = 0

    def prepareMapWithApple(self):
        for i in range(self.widthpixels):
            for j in range(self.heightpixels):
                if(self.Map[i][j]!=self.appleid):
                    self.Map[i][j] = 0

    def printMap(self):
        for i in range(self.widthpixels):
            for j in range(self.heightpixels):
                print(self.Map[i][j], end='')
            print("\n")
    def putBeginWonszOnMap(self):
        self.Map[self.startpointY][self.startpointX] = self.WonszID
    def changedirection(self, x):
        self.WonszList[0][2] = x
    def addWonszLength(self):
        if(self.WonszList[0][2] == 0):
            self.WonszList.insert(0, [self.WonszList[0][0], self.WonszList[0][1]-1, 0])
        elif(self.WonszList[0][2]== 1):
            self.WonszList.insert(0, [self.WonszList[0][0], self.WonszList[0][1] + 1, 1])
        elif(self.WonszList[0][2] == 2):
            self.WonszList.insert(0, [self.WonszList[0][0]-1, self.WonszList[0][1], 2])
        elif(self.WonszList[0][2] == 3):
            self.WonszList.insert(0, [self.WonszList[0][0] + 1, self.WonszList[0][1], 3])
        self.WonszLength += 1

    def directionrewrite(self):
        for i in range(self.WonszLength-1):
            self.WonszList[i+1][2] = self.WonszList[i][2]
    def WonszMove(self):
        jablkocheck = 0
        gamecheck = 0
        if(self.WonszList[0][2] == 0):
            if(self.Map[self.WonszList[0][0]][self.WonszList[0][1]-1] == 0):
                self.prepareMapWithApple()
                self.checkMoveWidth()
                gamecheck = 1
            elif(self.Map[self.WonszList[0][0]][self.WonszList[0][1]-1] == self.appleid):
                self.addWonszLength()
                jablkocheck = 1
                self.prepareMap()
                self.checkMoveWidth()
                gamecheck = 1
        elif(self.WonszList[0][2] == 1):
            if (self.WonszList[0][1] + 1 < self.widthpixels and self.Map[self.WonszList[0][0]][self.WonszList[0][1] + 1] != self.WonszID):
                if (self.Map[self.WonszList[0][0]][self.WonszList[0][1] + 1] == self.appleid):
                    self.addWonszLength()
                    jablkocheck = 1
                    self.prepareMap()
                    self.checkMoveWidth()
                    gamecheck = 1
                else:
                    self.prepareMapWithApple()
                    self.checkMoveWidth()
                    gamecheck = 1
            elif (self.WonszList[0][1] + 1 >= self.widthpixels and self.Map[self.WonszList[0][0]][0] != self.WonszID):
                if (self.Map[0][self.WonszList[0][1]] == self.appleid):
                    self.addWonszLength()
                    jablkocheck = 1
                    self.prepareMap()
                    self.checkMoveWidth()
                    gamecheck = 1
                else:
                    self.prepareMapWithApple()
                    self.checkMoveWidth()
                    gamecheck = 1
        elif(self.WonszList[0][2] == 2):
            if (self.Map[self.WonszList[0][0]-1][self.WonszList[0][1]] == 0):
                self.prepareMapWithApple()
                self.checkMoveWidth()
                gamecheck = 1
            elif(self.Map[self.WonszList[0][0]-1][self.WonszList[0][1]] == self.appleid):
                self.addWonszLength()
                jablkocheck = 1
                self.prepareMap()
                self.checkMoveWidth()
                gamecheck = 1
        elif(self.WonszList[0][2] == 3):
            if(self.WonszList[0][0] + 1 < self.heightpixels and self.Map[self.WonszList[0][0] + 1][self.WonszList[0][1]] != self.WonszID):
                if(self.Map[self.WonszList[0][0] + 1][self.WonszList[0][1]] == self.appleid):
                    self.addWonszLength()
                    jablkocheck = 1
                    self.prepareMap()
                    self.checkMoveWidth()
                    gamecheck = 1
                else:
                    self.prepareMapWithApple()
                    self.checkMoveWidth()
                    gamecheck = 1
            elif(self.WonszList[0][0] + 1 >= self.heightpixels and self.Map[0][self.WonszList[0][1]] != self.WonszID):
                if(self.Map[0][self.WonszList[0][1]] == self.appleid):
                    self.addWonszLength()
                    jablkocheck = 1
                    self.prepareMap()
                    self.checkMoveWidth()
                    gamecheck = 1
                else:
                    self.prepareMapWithApple()
                    self.checkMoveWidth()
                    gamecheck = 1
        if(jablkocheck == 1):
            self.jablkomanager()
            self.score+=1
        if(gamecheck == 0):
            self.alive = False
        self.rewritedirection()

    def checkMoveWidth(self):
        for i in range(self.WonszLength):
            if (self.WonszList[i][2] == 0):
                if (self.WonszList[i][1] - 1 < 0):
                    self.WonszList[i][1] = self.widthpixels - 1
                else:
                    self.WonszList[i][1] -= 1
                self.Map[self.WonszList[i][0]][self.WonszList[i][1]] = self.WonszID
            elif (self.WonszList[i][2] == 1):
                if (self.WonszList[i][1] + 1 == self.widthpixels):
                    self.WonszList[i][1] = 0
                else:
                    self.WonszList[i][1] += 1
                self.Map[self.WonszList[i][0]][self.WonszList[i][1]] = self.WonszID
            elif (self.WonszList[i][2] == 2):
                if (self.WonszList[i][0] - 1 < 0):
                    self.WonszList[i][0] = self.heightpixels - 1
                else:
                    self.WonszList[i][0] -= 1
                self.Map[self.WonszList[i][0]][self.WonszList[i][1]] = self.WonszID
            elif (self.WonszList[i][2] == 3):
                if (self.WonszList[i][0] + 1 == self.heightpixels):
                    self.WonszList[i][0] = 0
                else:
                    self.WonszList[i][0] += 1
                self.Map[self.WonszList[i][0]][self.WonszList[i][1]] = self.WonszID

    def rewritedirection(self):
        Listatmp = []
        for i in range(self.WonszLength):
            Listatmp.append(self.WonszList[i][2])
        for i in range(self.WonszLength-1):
            self.WonszList[i+1][2] = Listatmp[i]
    def jablkomanager(self):
        x = random.randint(1,self.widthpixels-1)
        y = random.randint(1,self.heightpixels-1)
        while(self.Map[x][y] != 0):
            x = random.randint(1, self.widthpixels)
            y = random.randint(1, self.heightpixels)
        self.Map[x][y] = self.appleid









class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.okno()
        self.height = 400
        self.width = 500
        self.kasia = Wonsz(16, 16, 8, 8, 0, 9)
        self.kasia.prepareMap()
        self.kasia.putBeginWonszOnMap()

    def okno(self):
        self.setWindowTitle("Gra Wąż")
        self.setGeometry(100, 100, 675, 420)
        self.setMinimumSize(675, 420)
        self.setMaximumSize(675, 420)

        exit_action = QAction("Exit - wyjście", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        self.label = QStaticText()
        self.label.setTextWidth(200)
        self.statusBar()

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction(exit_action)

        action_reset = QAction("RESET", self)
        action_reset.triggered.connect(self.resetgame)
        file_menu.addAction(action_reset)

    def resetgame(self):
        self.kasia.startpointY = 8
        self.kasia.startpointX = 8
        self.kasia.score = 0
        self.kasia.alive = True
        self.kasia.WonszLength = 1
        self.kasia.WonszList.clear()
        self.kasia.WonszList.insert(0,[self.kasia.startpointY, self.kasia.startpointX, 0])
        self.kasia.prepareMap()
        window.kasia.WonszMove()
        window.kasia.jablkomanager()
        window.show()

    def keyPressEvent(self, event): #d = 68 #w = 87 #s = 83 #a=65 #uparrow = 16777235 #leftarrow = 16777234 #rightarrow = 16777236 #downarrow = 16777237
        key = event.key()
        if(key == 68 and self.kasia.WonszList[0][2] != 0):
            self.kasia.changedirection(1)
        elif(key == 87 and self.kasia.WonszList[0][2] != 3):
            self.kasia.changedirection(2)
        elif(key == 83 and self.kasia.WonszList[0][2] != 2):
            self.kasia.changedirection(3)
        elif(key == 65 and self.kasia.WonszList[0][2] != 1):
            self.kasia.changedirection(0)


    def paintEvent(self, event):
        picasso = QPainter(self)
        picasso.setBrush(Qt.darkCyan)
        sizeboxheight = (int)(self.height/self.kasia.heightpixels)
        sizeboxwidth = (int)(self.width/self.kasia.widthpixels)
        for i in range(self.kasia.heightpixels):
            for j in range(self.kasia.widthpixels):
                if(self.kasia.Map[i][j] == self.kasia.WonszID):
                    picasso.setBrush(Qt.green)
                elif(self.kasia.Map[i][j] == 5):
                    picasso.setBrush(Qt.red)
                else:
                    picasso.setBrush(Qt.darkCyan)
                picasso.drawRect(0+j*sizeboxwidth, 20+i*sizeboxheight,sizeboxwidth,sizeboxheight)
        font = picasso.font()
        font.setPointSize(font.pointSize() + 4)
        picasso.setFont(font)
        if(self.kasia.alive == True):
            self.label.setText("Score = " + str(self.kasia.score))
            picasso.drawStaticText(550, 200, self.label)
        else:
            self.label.setText("END SCORE = " + str(self.kasia.score))
            picasso.drawStaticText(520, 200, self.label)
    def rysujemybalwanka(self): ##polaczone z paintevent zeby timer dzialal poprawnie (zeby uzywal paintevent bez eventu)
        self.update()

    timer1 = QtCore.QTimer()
    timer2 = QtCore.QTimer()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.kasia.WonszMove()
    window.kasia.jablkomanager()
    window.show()
    window.timer1.timeout.connect(window.rysujemybalwanka)
    window.timer2.timeout.connect(window.kasia.WonszMove)
    window.timer1.start(250)
    window.timer2.start(500)
    sys.exit(app.exec_())



"""""
if(self.WonszList[k][2] == 0):
                if(self.Map[self.WonszList[0][0]][self.WonszList[0][1]-1] == 0):
                    self.prepareMap()
                    for i in range(self.WonszLength):
                        if(self.WonszList[i][1] - 1 < 0):
                            self.WonszList[i][1] = self.widthpixels-1
                        else:
                            self.WonszList[i][1] -= 1
                        self.Map[self.WonszList[i][0]][self.WonszList[i][1]] = self.WonszID
            elif(self.direction == 1):
                if((self.WonszList[0][1] + 1 >= self.widthpixels and self.Map[self.WonszList[0][0]][0] == 0) or (self.Map[self.WonszList[0][0]][self.WonszList[0][1] + 1] == 0)):
                    self.prepareMap()
                    for i in range(self.WonszLength):
                        if(self.WonszList[i][1] + 1 == self.widthpixels):
                            self.WonszList[i][1] = 0
                        else:
                            self.WonszList[i][1] += 1
                        self.Map[self.WonszList[i][0]][self.WonszList[i][1]] = self.WonszID
            elif(self.direction == 2):
                if (self.Map[self.WonszList[0][0]-1][self.WonszList[0][1]] == 0):
                    self.prepareMap()
                    for i in range(self.WonszLength):
                        if(self.WonszList[i][0] - 1 < 0):
                            self.WonszList[i][0] = self.heightpixels-1
                        else:
                            self.WonszList[i][0] -= 1
                        self.Map[self.WonszList[i][0]][self.WonszList[i][1]] = self.WonszID
            elif(self.direction == 3):
                if ((self.WonszList[0][0] + 1 >= self.widthpixels and self.Map[0][self.WonszList[0][1]] == 0) or (self.Map[self.WonszList[0][0] + 1][self.WonszList[0][1]] == 0)):
                    self.prepareMap()
                    for i in range(self.WonszLength):
                        if(self.WonszList[i][0] + 1 == self.heightpixels):
                            self.WonszList[i][0] = 0
                        else:
                            self.WonszList[i][0] += 1
                        self.Map[self.WonszList[i][0]][self.WonszList[i][1]] = self.WonszID
"""""