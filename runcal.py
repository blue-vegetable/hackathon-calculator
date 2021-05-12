from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from game import Ui_Form
import numpy as np
import sys

class mywindow(Ui_Form,QWidget):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.num = np.random.randint(10)
        self.setWindowTitle("猜数字")
        print(self.num)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '确认', '确认退出吗？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def guess(self):
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = mywindow()
    win.show()
    sys.exit(app.exec_())