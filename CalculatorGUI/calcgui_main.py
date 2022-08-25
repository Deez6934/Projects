from calcgui import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class CalcWindow(qtw.QMainWindow, Ui_MainWindow):

    def __init__(self):

        super().__init__()

        self.setupUi(self)

        self.label.setText("0")
        self.numlist = ['']

        self.pushButton_7.clicked.connect(self.num_1)
        self.pushButton_5.clicked.connect(self.num_2)
        self.pushButton_8.clicked.connect(self.num_3)
        self.pushButton_11.clicked.connect(self.num_4)
        self.pushButton_9.clicked.connect(self.num_5)
        self.pushButton_12.clicked.connect(self.num_6)
        self.pushButton_15.clicked.connect(self.num_7)
        self.pushButton_13.clicked.connect(self.num_8)
        self.pushButton_16.clicked.connect(self.num_9)
        self.pushButton_10.clicked.connect(self.num_0)
        self.pushButton.clicked.connect(self.div)
        self.pushButton_2.clicked.connect(self.multi)
        self.pushButton_3.clicked.connect(self.add)
        self.pushButton_4.clicked.connect(self.sub)
        self.pushButton_6.clicked.connect(self.decimal)
        self.pushButton_14.clicked.connect(self.enter)
        self.pushButton_17.clicked.connect(self.clear)

    def number_box(self):
        self.label.setText(self.numlist[0])

    def num_1(self):
        self.numlist[0] += '1'
        self.number_box()

    def num_2(self):
        self.numlist[0] += '2'
        self.number_box()

    def num_3(self):
        self.numlist[0] += '3'
        self.number_box()

    def num_4(self):
        self.numlist[0] += '4'
        self.number_box()

    def num_5(self):
        self.numlist[0] += '5'
        self.number_box()

    def num_6(self):
        self.numlist[0] += '6'
        self.number_box()

    def num_7(self):
        self.numlist[0] += '7'
        self.number_box()

    def num_8(self):
        self.numlist[0] += '8'
        self.number_box()

    def num_9(self):
        self.numlist[0] += '9'
        self.number_box()

    def num_0(self):
        self.numlist[0] += '0'
        self.number_box()

    def div(self):
        self.numlist[0] += '/'
        self.number_box()

    def multi(self):
        self.numlist[0] += '*'
        self.number_box()

    def add(self):
        self.numlist[0] += '+'
        self.number_box()

    def sub(self):
        self.numlist[0] += '-'
        self.number_box()

    def decimal(self):
        self.numlist[0] += '.'
        self.number_box()

    def enter(self):
        try:
            result = eval(self.numlist[0])
            self.label.setText(str(result))
            self.numlist = [f'{result}']
        except:
            self.label.setText("Error")
            self.numlist = ['']

    def clear(self):
        self.label.setText('0')
        self.numlist = ['']


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = CalcWindow()
    widget.show()

    app.exec_()
