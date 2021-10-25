import random
from PySide6 import QtCore
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader=QUiLoader()
        self.ui=loader.load('convertor.ui')
        self.ui.combo_kind.currentTextChanged.connect(self.change_kind)
        self.ui.btn_clc.clicked.connect(self.convert)
        self.change_kind()
        self.ui.show()
        
    def change_kind(self):
        self.ui.combo_to.clear()
        self.ui.combo_from.clear()
        if self.ui.combo_kind.currentText()=='Weight':
            self.ui.combo_from.addItems(['grams','kilograms','Ton','Pond'])
            self.ui.combo_to.addItems(['grams','kilograms','Ton','Pond'])
        elif self.ui.combo_kind.currentText()=='Lenght':
            self.ui.combo_from.addItems(['millimeters','centimeters','meters','kilometers','inches'])
            self.ui.combo_to.addItems(['millimeters','centimeters','meters','kilometers','inches'])
        elif self.ui.combo_kind.currentText()=='Temperature':
            self.ui.combo_from.addItems(['Celsius','Fahrenheit','Kelvin'])
            self.ui.combo_to.addItems(['Celsius','Fahrenheit','Kelvin'])
        else:
            self.ui.combo_from.addItems(['bits','bytes','kilobytes','megabytes','gigabytes','terabytes'])
            self.ui.combo_to.addItems(['bits','bytes','kilobytes','megabytes','gigabytes','terabytes'])


    def convert(self):
        inp=float(self.ui.txt_inp.text())
        res=0
        if self.ui.combo_from.currentText()=='grams' and self.ui.combo_to.currentText()=='kilograms':
            res=inp/1000
        elif self.ui.combo_from.currentText()=='grams' and self.ui.combo_to.currentText()=='Ton':
            res=inp/10000000
        elif self.ui.combo_from.currentText()=='grams' and self.ui.combo_to.currentText()=='Pond':
            res=inp*2.2046000
        elif self.ui.combo_from.currentText()=='grams' and self.ui.combo_to.currentText()=='grams':
            res=inp
        elif self.ui.combo_from.currentText()=='kilograms' and self.ui.combo_to.currentText()=='grams':
            res=inp*1000
        elif self.ui.combo_from.currentText()=='kilograms' and self.ui.combo_to.currentText()=='Ton':
            res=inp*10000000
        elif self.ui.combo_from.currentText()=='kilograms' and self.ui.combo_to.currentText()=='Pond':
            res=inp*2.2046
        elif self.ui.combo_from.currentText()=='kilograms' and self.ui.combo_to.currentText()=='kilograms':
            res=inp
        elif self.ui.combo_from.currentText()=='Ton' and self.ui.combo_to.currentText()=='grams':
            res=inp*10000000
        elif self.ui.combo_from.currentText()=='Ton' and self.ui.combo_to.currentText()=='kilograms':
            res=inp/100000
        elif self.ui.combo_from.currentText()=='Ton' and self.ui.combo_to.currentText()=='Pond':
            res=inp*2204.62262185
        elif self.ui.combo_from.currentText()=='Ton' and self.ui.combo_to.currentText()=='Ton':
            res=inp
        elif self.ui.combo_from.currentText()=='Pond' and self.ui.combo_to.currentText()=='grams':
            res=inp/2.2046000
        elif self.ui.combo_from.currentText()=='Pond' and self.ui.combo_to.currentText()=='kilograms':
            res=inp/2.2046
        elif self.ui.combo_from.currentText()=='Pond' and self.ui.combo_to.currentText()=='Ton':
            res=inp/2204.62262185
        elif self.ui.combo_from.currentText()=='Pond' and self.ui.combo_to.currentText()=='Pond':
            res=inp
        elif self.ui.combo_from.currentText()=='millimeters' and self.ui.combo_to.currentText()=='centimeters':
            res=inp*10
        elif self.ui.combo_from.currentText()=='millimeters' and self.ui.combo_to.currentText()=='meters':
            res=inp*100
        elif self.ui.combo_from.currentText()=='millimeters' and self.ui.combo_to.currentText()=='kilometers':
            res=inp/1000000
        elif self.ui.combo_from.currentText()=='millimeters' and self.ui.combo_to.currentText()=='inches':
            res=inp*25.4
        elif self.ui.combo_from.currentText()=='millimeters' and self.ui.combo_to.currentText()=='millimeters':
            res=inp
        elif self.ui.combo_from.currentText()=='centimeters' and self.ui.combo_to.currentText()=='millimeters':
            res=inp/10
        elif self.ui.combo_from.currentText()=='centimeters' and self.ui.combo_to.currentText()=='meters':
            res=inp/100
        elif self.ui.combo_from.currentText()=='centimeters' and self.ui.combo_to.currentText()=='kilometers':
            res=inp/100000
        elif self.ui.combo_from.currentText()=='centimeters' and self.ui.combo_to.currentText()=='inches':
            res=inp*2.54
        
        elif self.ui.combo_from.currentText()=='centimeters' and self.ui.combo_to.currentText()=='centimeters':
            res=inp

        elif self.ui.combo_from.currentText()=='meters' and self.ui.combo_to.currentText()=='millimeters':
            res=inp/1000
        elif self.ui.combo_from.currentText()=='meters' and self.ui.combo_to.currentText()=='centimeters':
            res=inp*100
        elif self.ui.combo_from.currentText()=='meters' and self.ui.combo_to.currentText()=='kilometers':
            res=inp*1000
        elif self.ui.combo_from.currentText()=='meters' and self.ui.combo_to.currentText()=='inches':
            res=inp*0.0254
        elif self.ui.combo_from.currentText()=='meters' and self.ui.combo_to.currentText()=='meters':
            res=inp

        elif self.ui.combo_from.currentText()=='kilometers' and self.ui.combo_to.currentText()=='millimeters':
            res=inp*1000000
        elif self.ui.combo_from.currentText()=='kilometers' and self.ui.combo_to.currentText()=='centimeters':
            res=inp*100000
        elif self.ui.combo_from.currentText()=='kilometers' and self.ui.combo_to.currentText()=='meters':
            res=inp*1000
        elif self.ui.combo_from.currentText()=='kilometers' and self.ui.combo_to.currentText()=='inches':
            res=inp*0.0000254
        elif self.ui.combo_from.currentText()=='kilometers' and self.ui.combo_to.currentText()=='kilometers':
            res=inp


        elif self.ui.combo_from.currentText()=='inches' and self.ui.combo_to.currentText()=='millimeters':
            res=inp/25.4
        elif self.ui.combo_from.currentText()=='inches' and self.ui.combo_to.currentText()=='centimeters':
            res=inp/2.54
        elif self.ui.combo_from.currentText()=='inches' and self.ui.combo_to.currentText()=='meters':
            res=inp/0.0254
        elif self.ui.combo_from.currentText()=='inches' and self.ui.combo_to.currentText()=='kilometers':
            res=inp/0.0000254
        elif self.ui.combo_from.currentText()=='inches' and self.ui.combo_to.currentText()=='inches':
            res=inp

        elif self.ui.combo_from.currentText()=='Celsius' and self.ui.combo_to.currentText()=='Fahrenheit':
            res=inp*(9/5)+32
        elif self.ui.combo_from.currentText()=='Celsius' and self.ui.combo_to.currentText()=='Kelvin':
            res=inp+273.15
        elif self.ui.combo_from.currentText()=='Celsius' and self.ui.combo_to.currentText()=='Celsius':
            res=inp
        elif self.ui.combo_from.currentText()=='Fahrenheit' and self.ui.combo_to.currentText()=='Celsius':
            res=(inp-32)*5/9
        elif self.ui.combo_from.currentText()=='Fahrenheit' and self.ui.combo_to.currentText()=='Kelvin':
            res=(inp+459.67)*5/9
        elif self.ui.combo_from.currentText()=='Fahrenheit' and self.ui.combo_to.currentText()=='Fahrenheit':
            res=inp
        elif self.ui.combo_from.currentText()=='Kelvin' and self.ui.combo_to.currentText()=='Celsius':
            res=inp-273.15
        elif self.ui.combo_from.currentText()=='Kelvin' and self.ui.combo_to.currentText()=='Fahrenheit':
            res=inp*(9/5)-459.67
        elif self.ui.combo_from.currentText()=='Kelvin' and self.ui.combo_to.currentText()=='Kelvin':
            res=inp
        
        elif self.ui.combo_from.currentText()=='bits' and self.ui.combo_to.currentText()=='bytes':
            res=inp/8
        elif self.ui.combo_from.currentText()=='bits' and self.ui.combo_to.currentText()=='kilobytes':
            res=inp/8*10**-3
        elif self.ui.combo_from.currentText()=='bits' and self.ui.combo_to.currentText()=='megabytes':
            res=inp/8*10**-6
        elif self.ui.combo_from.currentText()=='bits' and self.ui.combo_to.currentText()=='gigabytes':
            res=inp/8*10**-9
        elif self.ui.combo_from.currentText()=='bits' and self.ui.combo_to.currentText()=='terabytes':
            res=inp/8*10**-12
        elif self.ui.combo_from.currentText()=='bits' and self.ui.combo_to.currentText()=='bits':
            res=inp


        elif self.ui.combo_from.currentText()=='bytes' and self.ui.combo_to.currentText()=='bits':
            res=inp*8
        elif self.ui.combo_from.currentText()=='bytes' and self.ui.combo_to.currentText()=='kilobytes':
            res=inp*10**-3
        elif self.ui.combo_from.currentText()=='bytes' and self.ui.combo_to.currentText()=='megabytes':
            res=inp*10**-6
        elif self.ui.combo_from.currentText()=='bytes' and self.ui.combo_to.currentText()=='gigabytes':
            res=inp*10**-9
        elif self.ui.combo_from.currentText()=='bytes' and self.ui.combo_to.currentText()=='terabytes':
            res=inp*10**-12
        elif self.ui.combo_from.currentText()=='bytes' and self.ui.combo_to.currentText()=='bytes':
            res=inp


        elif self.ui.combo_from.currentText()=='kilobytes' and self.ui.combo_to.currentText()=='bits':
            res=inp*8*10**3
        elif self.ui.combo_from.currentText()=='kilobytes' and self.ui.combo_to.currentText()=='bytes':
            res=inp*10**3
        elif self.ui.combo_from.currentText()=='kilobytes' and self.ui.combo_to.currentText()=='megabytes':
            res=inp*10**-3
        elif self.ui.combo_from.currentText()=='kilobytes' and self.ui.combo_to.currentText()=='gigabytes':
            res=inp*10**-6
        elif self.ui.combo_from.currentText()=='kilobytes' and self.ui.combo_to.currentText()=='terabytes':
            res=inp*10**-9
        elif self.ui.combo_from.currentText()=='kilobytes' and self.ui.combo_to.currentText()=='kilobytes':
            res=inp
        
        elif self.ui.combo_from.currentText()=='megabytes' and self.ui.combo_to.currentText()=='bits':
            res=inp*8*10**6
        elif self.ui.combo_from.currentText()=='megabytes' and self.ui.combo_to.currentText()=='bytes':
            res=inp*10**6
        elif self.ui.combo_from.currentText()=='megabytes' and self.ui.combo_to.currentText()=='kilobytes':
            res=inp*10**3
        elif self.ui.combo_from.currentText()=='megabytes' and self.ui.combo_to.currentText()=='gigabytes':
            res=inp*10**-3
        elif self.ui.combo_from.currentText()=='megabytes' and self.ui.combo_to.currentText()=='terabytes':
            res=inp*10**-6
        elif self.ui.combo_from.currentText()=='megabytes' and self.ui.combo_to.currentText()=='megabytes':
            res=inp
        
        elif self.ui.combo_from.currentText()=='gigabytes' and self.ui.combo_to.currentText()=='bits':
            res=inp*8*10**9
        elif self.ui.combo_from.currentText()=='gigabytes' and self.ui.combo_to.currentText()=='bytes':
            res=inp*10**9
        elif self.ui.combo_from.currentText()=='gigabytes' and self.ui.combo_to.currentText()=='kilobytes':
            res=inp*10**6
        elif self.ui.combo_from.currentText()=='gigabytes' and self.ui.combo_to.currentText()=='megabytes':
            res=inp*10**3
        elif self.ui.combo_from.currentText()=='gigabytes' and self.ui.combo_to.currentText()=='terabytes':
            res=inp*10**-3
        elif self.ui.combo_from.currentText()=='gigabytes' and self.ui.combo_to.currentText()=='gigabytes':
            res=inp
        
        elif self.ui.combo_from.currentText()=='terabytes' and self.ui.combo_to.currentText()=='bits':
            res=inp*8*10**12
        elif self.ui.combo_from.currentText()=='terabytes' and self.ui.combo_to.currentText()=='bytes':
            res=inp*10**12
        elif self.ui.combo_from.currentText()=='terabytes' and self.ui.combo_to.currentText()=='kilobytes':
            res=inp*10**9
        elif self.ui.combo_from.currentText()=='terabytes' and self.ui.combo_to.currentText()=='megabytes':
            res=inp*10**6
        elif self.ui.combo_from.currentText()=='terabytes' and self.ui.combo_to.currentText()=='gigabytes':
            res=inp*10**3
        elif self.ui.combo_from.currentText()=='terabytes' and self.ui.combo_to.currentText()=='terabytes':
            res=inp

        try:
            self.ui.lbl_res.setText(str(res))
        except:
            msgbox=QMessageBox()
            msgbox.setText('Enter number...')
            msgbox.exec()

app=QApplication([])
window=MainWindow()
app.exec()
