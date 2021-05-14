from cal import Ui_Form
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5 import QtGui,QtWidgets
from PyQt5.QtCore import Qt

class Cacular(QWidget, Ui_Form):
    """docstring for Cacular"""
    def __init__(self):
        super(Cacular, self).__init__()
        self.setupUi(self)
        self.connecter()
        self.show()

    def ps_CE(self):
        text = self.textedit.toPlainText()
        if text:
            self.textedit.setPlainText(text[:-1])

    def ps_b_1(self):
        global a
        if a == 1:
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText('1')

    def ps_b_0(self):
        global a
        if a == 1:
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText('0')

    def ps_b_2(self):
        global a
        if a == 1:
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText('2')

    def ps_b_3(self):
        global a
        if a == 1:
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText('3')

    def ps_b_4(self):
        global a
        if a == 1:
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText('4')

    def ps_b_5(self):
        global a
        if a == 1:
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText('5')

    def ps_b_6(self):
        global a
        if a == 1:
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText('6')

    def ps_b_7(self):
        global a
        if a == 1:
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText('7')

    def ps_b_8(self):
        global a
        if a == 1:
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText('8')

    def ps_b_9(self):
        global a
        if a == 1:
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText('9')

    def ps_plus(self):
        global a
        text = ""
        if a == 1:
            text = self.textedit.toPlainText()
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText(text+'+')

    def ps_minus(self):
        global a
        text = ""
        if a == 1:
            text = self.textedit.toPlainText()
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText(text + '-')

    def ps_multi(self):
        global a
        text = ""
        if a == 1:
            text = self.textedit.toPlainText()
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText(text + '*')

    def ps_devide(self):
        global a
        text = ""
        if a == 1:
            text = self.textedit.toPlainText()
            self.textedit.clear()
            a = 0
        self.textedit.insertPlainText(text + '/')

    def connecter(self):
        self.b_0.clicked.connect(self.ps_b_0)
        self.b_1.clicked.connect(self.ps_b_1)
        self.b_2.clicked.connect(self.ps_b_2)
        self.b_3.clicked.connect(self.ps_b_3)
        self.b_4.clicked.connect(self.ps_b_4)
        self.b_5.clicked.connect(self.ps_b_5)
        self.b_6.clicked.connect(self.ps_b_6)
        self.b_7.clicked.connect(self.ps_b_7)
        self.b_8.clicked.connect(self.ps_b_8)
        self.b_9.clicked.connect(self.ps_b_9)
        self.b_add.clicked.connect(self.ps_plus)
        self.b_sub.clicked.connect(self.ps_minus)
        self.b_mul.clicked.connect(self.ps_multi)
        self.b_div.clicked.connect(self.ps_devide)
        self.b_eql.clicked.connect(self.calcu)
        self.b_del.clicked.connect(self.ps_CE)


    def calcu(self):
        text = self.textedit.toPlainText()
        try:
            result = eval(text)
            self.textedit.setPlainText((str(eval(text))))
        except:
            self.textedit.setPlainText('invalid syntax, check your input!')
        global a
        a = 1

if __name__ == '__main__':
    a = 0
    app = QApplication(sys.argv)
    Ca = Cacular()
    sys.exit(app.exec_())
