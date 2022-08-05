from msilib.schema import Error
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime
import pickle
import requests


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.filecreator()
        self.ReadPricesAndDate()
        self.crypto_tracker()
        self.WritePricesAndDate()

        MainWindow.setObjectName("CryptoPriceChecker")
        MainWindow.resize(808, 657)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: black")

        self.Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.Refresh.setGeometry(QtCore.QRect(0, 510, 811, 101))
        self.Refresh.setObjectName("Refresh")
        self.Refresh.setStyleSheet("background-color: gray")
        self.Refresh.clicked.connect(self.refresh)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(75, 170, 201, 161))
        self.label_5.setText(f'$ {self.price_dic["BTC"]}')
        self.label_5.setStyleSheet(
            "border: 1px solid black;")
        self.label_5.setFont(QFont('Arial', 20))
        self.label_5.move(15, 220)
        self.label_5.adjustSize()

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(275, 170, 201, 161))
        self.label_6.setText(f'$ {self.price_dic["BAT"]}')
        self.label_6.setStyleSheet("border: 1px solid black;")
        self.label_6.setFont(QFont('Arial', 20))
        self.label_6.move(215, 220)
        self.label_6.adjustSize()

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(475, 170, 201, 161))
        self.label_7.setText(f'$ {self.price_dic["ETH"]}')
        self.label_7.setStyleSheet("border: 1px solid black;")
        self.label_7.setFont(QFont('Arial', 20))
        self.label_7.move(415, 220)
        self.label_7.adjustSize()

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(675, 170, 211, 161))
        self.label_8.setText(f'$ {self.price_dic["XMR"]}')
        self.label_8.setStyleSheet("border: 1px solid black;")
        self.label_8.setFont(QFont('Arial', 20))
        self.label_8.move(615, 220)
        self.label_8.adjustSize()

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 330, 201, 161))
        self.label_9.setObjectName("label_9")
        self.label_9.setText("Last Checked:")
        self.label_9.setStyleSheet("border: 1px solid black;")
        self.label_9.setFont(QFont('Arial', 20))
        self.label_9.setStyleSheet("background-color: white")
        self.label_9.adjustSize()

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(410, 330, 201, 161))
        self.label_10.setObjectName("label_10")
        self.label_10.setText(self.date)
        self.label_10.setStyleSheet("border: 1px solid black;")
        self.label_10.setFont(QFont('Arial', 20))
        self.label_10.setStyleSheet("background-color: white")
        self.label_10.adjustSize()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(4, 5, 201, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("src/Bitcoin-BTC-icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 0, 191, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(
            "src/Basic-Attention-Token-icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(404, 0, 201, 171))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("src/Ethereum-ETH-icon.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(604, 0, 211, 161))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("src/Monero-icon.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.PriceColour()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "CryptoPriceChecker"))
        MainWindow.setWindowIcon(QtGui.QIcon("src/generic-crypto.ico"))
        self.Refresh.setText(_translate("MainWindow", "Refresh"))

    def crypto_tracker(self):

        # API urls
        bat_api_url = 'https://min-api.cryptocompare.com/data/price?fsym=BAT&tsyms=USD,JPY,EUR'
        btc_api_url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR'
        eth_api_url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,JPY,EUR'
        xmr_api_url = 'https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,JPY,EUR'

        # sends a get request and recives the info of respective crpyto encoded in json and decodes and stores it.
        btc_info = requests.get(btc_api_url).json()
        bat_info = requests.get(bat_api_url).json()
        eth_info = requests.get(eth_api_url).json()
        xmr_info = requests.get(xmr_api_url).json()

        # gets the USD price from the dictionary
        btc_price = str(btc_info['USD'])
        bat_price = str(bat_info['USD'])
        eth_price = str(eth_info['USD'])
        xmr_price = str(xmr_info['USD'])

        self.price_dic = {'BTC': btc_price, 'BAT': bat_price, 'ETH': eth_price, 'XMR': xmr_price
                          }

    def refresh(self):
        self.crypto_tracker()
        self.ReadPricesAndDate()
        self.WritePricesAndDate()
        self.PriceColour()

        self.label_5.setText(f'$ {self.price_dic["BTC"]}')
        self.label_5.adjustSize()

        self.label_6.setText(f'$ {self.price_dic["BAT"]}')
        self.label_6.adjustSize()

        self.label_7.setText(f'$ {self.price_dic["ETH"]}')
        self.label_7.adjustSize()

        self.label_8.setText(f'$ {self.price_dic["XMR"]}')
        self.label_8.adjustSize()

        self.label_10.setText(self.date)
        self.label_10.adjustSize()

    def filecreator(self):  # Creates all the necessary files at launch.
        try:
            file1r = open("src/prices.dat", "rb")
            file2r = open("src/date.dat", "rb")
            file2r.close()
            file1r.close()
        except FileNotFoundError:
            f1 = open("src/prices.dat", "w")
            f2 = open("src/date.dat", "w")
            f2.close()
            f1.close()

    def WritePricesAndDate(self):
        try:
            f1 = open("src/prices.dat", "wb")
            f2 = open("src/date.dat", "wb")
            pickle.dump(self.price_dic, f1)
            pickle.dump(datetime.now().strftime('%D %H:%M:%S'), f2)
            f2.close()
            f1.close()
        except:
            f2.close()
            f1.close()

    def ReadPricesAndDate(self):
        try:
            f1 = open("src/prices.dat", "rb")
            f2 = open("src/date.dat", "rb")
            self.prices1 = pickle.load(f1)
            self.date = pickle.load(f2)
            f2.close()
            f1.close()
        except:
            f2.close()
            f1.close()

    def PriceColour(self):
        if self.price_dic['BTC'] >= self.prices1['BTC']:
            self.label_5.setStyleSheet(
                "border: 1px solid black; background-color: green;")
        else:
            self.label_5.setStyleSheet(
                "border: 1px solid black; background-color: red;")
        if self.price_dic['BAT'] >= self.prices1['BAT']:
            self.label_6.setStyleSheet(
                "border: 1px solid black; background-color: green;")
        else:
            self.label_6.setStyleSheet(
                "border: 1px solid black; background-color: red;")
        if self.price_dic['ETH'] >= self.prices1['ETH']:
            self.label_7.setStyleSheet(
                "border: 1px solid black; background-color: green;")
        else:
            self.label_7.setStyleSheet(
                "border: 1px solid black; background-color: red;")
        if self.price_dic['XMR'] >= self.prices1['XMR']:
            self.label_8.setStyleSheet(
                "border: 1px solid black; background-color: green;")
        else:
            self.label_8.setStyleSheet(
                "border: 1px solid black; background-color: red;")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
