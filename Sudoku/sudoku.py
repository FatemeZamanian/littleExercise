import random
from PySide6 import QtCore
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader=QUiLoader()
        self.ui=loader.load('sudoku.ui')
        self.game=[[None for i in range(9)]for j in range(9)]
        self.ui.btn_new.clicked.connect(self.new_game)
        self.ui.btn_check.clicked.connect(self.check)
        self.ui.btn_dark.clicked.connect(self.change_mode)
        self.mode='light'

        for i in range(9):
            for j in range(9):
                tb=QLineEdit()
                tb.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
                # tb.setStyleSheet("Text-align:center")
                tb.setAlignment(QtCore.Qt.AlignCenter)
                tb.setStyleSheet('font-size : 25px; border-color:gray;border-style:solid;border-width:2;')
                self.game[i][j]=tb
                
                self.ui.gridLayout.addWidget(tb,i,j)

        r=random.randint(1,6)
        try:
            file_path=f'data/s{r}.txt'
            f=open(file_path,'r')
            big_txt=f.read()
            rows=big_txt.split('\n')
            for i in range(9):
                numbers=rows[i].split(' ')
                for j in range(9):
                    if numbers[j] != '0':
                        self.game[i][j].setStyleSheet('font-size : 25px; color:green;border-color:gray;border-style:solid;border-width:2;')
                        self.game[i][j].setText(numbers[j])
                        self.game[i][j].setEnabled(False)
                    self.game[i][j].textChanged.connect(self.check)
        except:
            msgbox=QMessageBox()
            msgbox.setText('data not found :)')
            msgbox.exec()

        self.ui.show()

    def new_game(self):
        for i in range(9):
            for j in range(9):
                self.game[i][j].setText('')
                self.game[i][j].setEnabled(True)

        r=random.randint(1,6)
        try:
            file_path=f'data/s{r}.txt'
            f=open(file_path,'r')
            big_txt=f.read()
            rows=big_txt.split('\n')
            for i in range(9):
                numbers=rows[i].split(' ')
                for j in range(9):
                    if numbers[j] != '0':
                        self.game[i][j].setStyleSheet('font-size : 25px; color:green;border-color:gray;border-style:solid;border-width:2;')
                        self.game[i][j].setText(numbers[j])
                        self.game[i][j].setEnabled(False)
                    self.game[i][j].textChanged.connect(self.check)
        except:
            msgbox=QMessageBox()
            msgbox.setText('data not found :)')
            msgbox.exec()


    def check(self):
        flagwin=True
        for row in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text()==self.game[row][j].text() and i!=j and self.game[row][i].text()!='':
                        self.game[row][j].setStyleSheet('font-size: 25px; background-color: pink;font-size : 25px; border-color:gray;border-style:solid;border-width:2;color:black')
                        flagwin=False

                    else:
                        self.game[row][i].setStyleSheet('font-size : 25px; color:green;border-color:gray;border-style:solid;border-width:2;')


        for col in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text()==self.game[j][col].text() and i !=j and self.game[i][col].text() != '' :
                        self.game[i][col].setStyleSheet('font-size : 25px; background-color: pink;font-size : 25px; border-color:gray;border-style:solid;border-width:2;color:black')
                        flagwin=False
                    
                    # else:
                    #     self.game[i][col].setStyleSheet('font-size : 25px; color:green;border-color:gray;border-style:solid;border-width:2;')

                
        

        for r in range(9,-1,-3):
            for c in range(9,-1,-3):
                for ro in range(r-3,r):
                    for co in range(c-3,c):
                        for i in range(r-3,r):
                            for j in range(c-3,c):
                                if self.game[ro][co].text()==self.game[i][j].text() and (i !=ro or j !=co )and self.game[ro][co].text() != '' :
                                    self.game[ro][co].setStyleSheet('font-size : 25px; background-color: pink;font-size : 25px; border-color:gray;border-style:solid;border-width:2;color:black')
                                    flagwin=False
                                if (len(self.game[i][j].text())>1 or not(self.game[i][j].text().isdigit())) and (i !=ro or j !=co )and self.game[i][j].text() != '':
                                    self.game[i][j].setStyleSheet('font-size : 25px; background-color: pink;font-size : 25px; border-color:gray;border-style:solid;border-width:2;color:black')
                                    flagwin=False

        #                         # else:
        #                         #     self.game[row][i].setStyleSheet('font-size : 25px; color:green;border-color:gray;border-style:solid;border-width:2;')



        if flagwin:
            for i in range(9):
                for j in range(9):
                    if self.game[i][j].text() =='':
                        flagwin=False
            if flagwin:
                    self.new_game()
                    msgbox=QMessageBox()
                    msgbox.setText('you win :)')
                    msgbox.exec()

    def change_mode(self):
        if self.mode=='light':
            self.mode='dark'
            self.ui.setStyleSheet('background-color:black; color: white ;')
            for row in range(9):
                for col in range(9):
                    self.game[row][col].setStyleSheet('background-color:black;border-color:gray;border-style:solid;border-width:2; font-size : 25px; color:green')
        else:
            self.mode='light'
            self.ui.setStyleSheet('background-color:white; color: black ;')
            for row in range(9):
                for col in range(9):
                    self.game[row][col].setStyleSheet('background-color:white;border-color:gray;border-style:solid;border-width:2; font-size : 25px; color:green')




app=QApplication([])
window=MainWindow()
app.exec()
