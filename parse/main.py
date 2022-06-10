
# -*- coding: utf-8 -*-
import time
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QApplication, QGridLayout
from bs4 import BeautifulSoup

url = 'https://myfin.by/converter'
# url = 'https://www.instagram.com/gazetakm/?hl=ru'
# url = 'https://www.instagram.com/gazetakm/?hl=ru'
headers = {'User-agent': 'your bot 0.1'}
response = requests.get(url=url, headers=headers)
print(response.status_code)

dictionary = []
dictionary_end = []


def content():
    while True:
        index = 0
        if response.status_code == 200:
            content = response.content
            with open(file='new.html', mode="wb") as file:
                file.write(content)
            content = BeautifulSoup(response.text, 'lxml')
            text = content.find_all('div', class_="converter-container converter-container-in-grid")
            for i in text:
                text = i.find_all('div', class_="converter-container__content")
                for ii in text:
                    text = ii.find_all('div', class_="tab-pane fade in active")
                    for iii in text:
                        text = iii.find_all('div', class_="converter-container__inputs")
                        for iiii in text:
                            for iiiii in text:
                                text = iii.find_all('div', class_="converter-container__item")
                                for label_in_text in text:
                                    label_text = label_in_text.find_all('span',
                                                                        class_="converter-container__item-currency-abbr")
                                    for lb in label_text:
                                        label_text = lb.text
                                        dictionary.append(label_text)
                                for input_in_text in text:
                                    input_text = input_in_text.find_all('input',
                                                                        class_="input_calc form-control form-input-sum bestmb")
                                    for inp in input_text:
                                        input_text = inp.get('value')
                                        dic_index = dictionary[index]
                                        dic_new_el = []
                                        dic_new_el.append(dic_index)
                                        dic_new_el.append(input_text)
                                        dictionary_end.append(dic_new_el)
                                        # print("ddd"+ dic_index)
                                        index += 1

        tm = 1
        time.sleep(tm)
        tm += 2
        if tm > 9:
            tm = 1
        print("Обновился")
print("dic" + str(dictionary_end))

print(response.status_code)


Thread(target=content).start()
time.sleep(2)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setStyleSheet("QLineEdit{max-width:500;margin:5;} *{font-size:20px;padding:5;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 701, 363))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 6, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 4, 2, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 5, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setStyleSheet("")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lineEdit.textChanged.connect(self.line_edit_text_changed)
        self.lineEdit_2.textChanged.connect(self.line_edit_text_changed_2)
        self.lineEdit_3.textChanged.connect(self.line_edit_text_changed_3)
        self.lineEdit_4.textChanged.connect(self.line_edit_text_changed_4)
        self.lineEdit_5.textChanged.connect(self.line_edit_text_changed_5)
        self.lineEdit_6.textChanged.connect(self.line_edit_text_changed_6)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", str(dictionary_end[0][0])))
        self.label_2.setText(_translate("MainWindow", str(dictionary_end[1][0])))
        self.label_5.setText(_translate("MainWindow", str(dictionary_end[2][0])))
        self.label_7.setText(_translate("MainWindow", str(dictionary_end[3][0])))
        self.label_8.setText(_translate("MainWindow", str(dictionary_end[4][0])))
        self.label_10.setText(_translate("MainWindow", str(dictionary_end[5][0])))
        self.label_13.setText(_translate("MainWindow", "По лучшему курсу в Москве"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", ""))
        self.label_9.setText(_translate("MainWindow", ""))
        self.label_11.setText(_translate("MainWindow", ""))
        self.label_12.setText(_translate("MainWindow", ""))

    def line_edit_text_changed(self, text):
        try:
            if text == "":
                self.label_3.setText("")
                self.label_4.setText("")
                self.label_6.setText("")
                self.label_9.setText("")
                self.label_11.setText("")
                self.label_12.setText("")
            # print("Work")
            # print(float(text)*float(dictionary_end[1][1]))
            # text1 = float(text)*float(dictionary_end[0][1])
            text2 = float(text) * float(dictionary_end[1][1])
            text3 = float(text) * float(dictionary_end[2][1])
            text4 = float(text) * float(dictionary_end[3][1])
            text5 = float(text) * float(dictionary_end[4][1])
            text6 = float(text) * float(dictionary_end[5][1])

            # print(text2)text2
            self.label_3.setText(text)
            self.label_4.setText(f'{float(text2)}')
            self.label_6.setText(f'{float(text3)}')
            self.label_9.setText(f'{float(text4)}')
            self.label_11.setText(f'{float(text5)}')
            self.label_12.setText(f'{float(text6)}')

            # lineEdit_2

            print(text)
        except Exception as error:
            pass

    def line_edit_text_changed_2(self, text):
        try:
            if text == "":
                self.label_3.setText("")
                self.label_4.setText("")
                self.label_6.setText("")
                self.label_9.setText("")
                self.label_11.setText("")
                self.label_12.setText("")
            # print("Work")
            # print(float(text)/float(dictionary_end[1][1]))
            text1 = float(text) / float(dictionary_end[1][1])
            # text2 = float(text)/float(dictionary_end[1][1])
            text3 = float(text) / float(dictionary_end[1][1]) * float(dictionary_end[2][1])
            text4 = float(text) / float(dictionary_end[1][1]) * float(dictionary_end[3][1])
            text5 = float(text) / float(dictionary_end[1][1]) * float(dictionary_end[4][1])
            text6 = float(text) / float(dictionary_end[1][1]) * float(dictionary_end[5][1])

            # print(text2)text2
            self.label_3.setText(f'{float(text1)}')
            self.label_4.setText(text)
            self.label_6.setText(f'{float(text3)}')
            self.label_9.setText(f'{float(text4)}')
            self.label_11.setText(f'{float(text5)}')
            self.label_12.setText(f'{float(text6)}')

            # lineEdit_2

            print(text)
        except Exception as error:
            pass

    def line_edit_text_changed_3(self, text):
        try:
            if text == "":
                self.label_3.setText("")
                self.label_4.setText("")
                self.label_6.setText("")
                self.label_9.setText("")
                self.label_11.setText("")
                self.label_12.setText("")
            # print("Work")
            # print(float(text)*float(dictionary_end[1][1]))
            text1 = float(text) / float(dictionary_end[2][1])
            text2 = float(text) / float(dictionary_end[2][1]) * float(dictionary_end[1][1])
            # text3 = float(text)/float(dictionary_end[2][1])*float(dictionary_end[2][1])
            text4 = float(text) / float(dictionary_end[2][1]) * float(dictionary_end[3][1])
            text5 = float(text) / float(dictionary_end[2][1]) * float(dictionary_end[4][1])
            text6 = float(text) / float(dictionary_end[2][1]) * float(dictionary_end[5][1])

            # print(text2)text2
            self.label_3.setText(f'{float(text1)}')
            self.label_4.setText(f'{float(text2)}')
            self.label_6.setText(text)
            self.label_9.setText(f'{float(text4)}')
            self.label_11.setText(f'{float(text5)}')
            self.label_12.setText(f'{float(text6)}')

            # lineEdit_2

            print(text)
        except Exception as error:
            pass

    def line_edit_text_changed_4(self, text):
        try:
            if text == "":
                self.label_3.setText("")
                self.label_4.setText("")
                self.label_6.setText("")
                self.label_9.setText("")
                self.label_11.setText("")
                self.label_12.setText("")
            # print("Work")
            text1 = float(text) / float(dictionary_end[3][1])
            text2 = float(text) / float(dictionary_end[3][1]) * float(dictionary_end[1][1])
            text3 = float(text) / float(dictionary_end[3][1]) * float(dictionary_end[2][1])
            # text4 = float(text) / float(dictionary_end[2][1]) * float(dictionary_end[3][1])
            text5 = float(text) / float(dictionary_end[3][1]) * float(dictionary_end[4][1])
            text6 = float(text) / float(dictionary_end[3][1]) * float(dictionary_end[5][1])
            # print(text2)text2
            self.label_3.setText(f'{float(text1)}')
            self.label_4.setText(f'{float(text2)}')
            self.label_6.setText(f'{float(text3)}')
            self.label_9.setText(text)
            self.label_11.setText(f'{float(text5)}')
            self.label_12.setText(f'{float(text6)}')

            # lineEdit_2

            print(text)
        except Exception as error:
            pass

    def line_edit_text_changed_5(self, text):
        try:
            if text == "":
                self.label_3.setText("")
                self.label_4.setText("")
                self.label_6.setText("")
                self.label_9.setText("")
                self.label_11.setText("")
                self.label_12.setText("")
            # print("Work")
            text1 = float(text) / float(dictionary_end[4][1])
            text2 = float(text) / float(dictionary_end[4][1]) * float(dictionary_end[1][1])
            text3 = float(text) / float(dictionary_end[4][1]) * float(dictionary_end[2][1])
            text4 = float(text) / float(dictionary_end[4][1]) * float(dictionary_end[3][1])
            # text5 = float(text) / float(dictionary_end[3][1]) * float(dictionary_end[4][1])
            text6 = float(text) / float(dictionary_end[4][1]) * float(dictionary_end[5][1])

            self.label_3.setText(f'{float(text1)}')
            self.label_4.setText(f'{float(text2)}')
            self.label_6.setText(f'{float(text3)}')
            self.label_9.setText(f'{float(text4)}')
            self.label_11.setText(text)
            self.label_12.setText(f'{float(text6)}')

            # lineEdit_2

            print(text)
        except Exception as error:
            pass

    def line_edit_text_changed_6(self, text):
        try:
            if text == "":
                self.label_3.setText("")
                self.label_4.setText("")
                self.label_6.setText("")
                self.label_9.setText("")
                self.label_11.setText("")
                self.label_12.setText("")
            # print("Work")
            text1 = float(text) / float(dictionary_end[5][1])
            text2 = float(text) / float(dictionary_end[5][1]) * float(dictionary_end[1][1])
            text3 = float(text) / float(dictionary_end[5][1]) * float(dictionary_end[2][1])
            text4 = float(text) / float(dictionary_end[5][1]) * float(dictionary_end[3][1])
            text5 = float(text) / float(dictionary_end[5][1]) * float(dictionary_end[4][1])
            # text6 = float(text) / float(dictionary_end[4][1]) * float(dictionary_end[5][1])
            # print(text2)text2
            self.label_3.setText(f'{float(text1)}')
            self.label_4.setText(f'{float(text2)}')
            self.label_6.setText(f'{float(text3)}')
            self.label_9.setText(f'{float(text4)}')
            self.label_11.setText(f'{float(text5)}')
            self.label_12.setText(text)

            # lineEdit_2

            print(text)
        except Exception as error:
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
