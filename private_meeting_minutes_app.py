# -*- coding: utf-8 -*-

import os
import threading
# Form implementation generated from reading ui file '나만의 회의록 작성 프로그램.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication
from my_clova_speech_client import ClovaSpeechClient


class Ui_MainWindow(object):
    temp_file_name = [""]  # 음성 파일 열기, 해당 파일 열기 눌렀을 때 변경될 파일 이름.

    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 78, 150, 17))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 100, 401, 17))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 76, 151, 21))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 120, 371, 21))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 150, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 40, 731, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 202, 401, 17))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(40, 320, 731, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 180, 150, 17))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 290, 151, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 262, 401, 17))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 240, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 340, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(170, 360, 401, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 370, 151, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 520, 151, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.open_file)
        self.pushButton_2.clicked.connect(MainWindow.convertToString)
        self.pushButton_3.clicked.connect(MainWindow.openFolder)
        self.pushButton_4.clicked.connect(MainWindow.clearStateTxt)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def open_file(self): # 클릭하면 폴더를 오픈해주고 선택한 파일의 경로를 저장해줌.
        self.temp_file_name = list(QFileDialog.getOpenFileName(self))
        self.lineEdit.setText(self.temp_file_name[0])
        self.temp_file_name[0] = self.temp_file_name[0].replace('/', '\\') # window 경로는 이렇게 표시한다.
        # -> 굳이 왜? 그리고 굳이 왜 temp_file_name[0]인걸까? -> 여러 개중 경로만 담겨진 부분만 가져오기 위해.


    def createClovaSpeechClient(self, clovaSpeechClient): # txt파일 변환하기 버튼을 클릭하면 setInvoke_url이 입력한 매개변수에 불린다.
        # converToString에서 사용되는 부분.
        clovaSpeechClient.setInvoke_url(self.lineEdit_3.text())
        clovaSpeechClient.setSecret(self.lineEdit_2.text())


    def convertToString(self):
        # 응답없음 방지하기 위한 멀티쓰레드 프로그래밍
        self.pushButton_2.setEnabled(False)
        thread = threading.Thread(target=self.convertToString2)
        thread.start()


    def convertToString2(self):
        # 상태창에 기록을 해주는 부분
        QApplication.processEvents()
        fileName = self.temp_file_name[0].split("\\") # 윈도우라서
        self.textBrowser.append(fileName[-1] + " 파일 -> " + fileName[-1].split('.')[0] + ".txt 파일로 변환중") # ~.mp3에서 앞부분 .txt
        QApplication.processEvents()

        # 이 부분이 createClovaSpeechClient와 연결
        clovaSpeechClient = ClovaSpeechClient() # 클래스에서 인스턴스를 생성하는 부분
        self.createClovaSpeechClient(clovaSpeechClient)

        try:
            response = clovaSpeechClient.req_upload(file=self.temp_file_name[0], completion='sync')  # 로컬 파일을 업로드해서 요청. request보내는 부분은 항상 예외처리를 해야한다.
            self.saveTxtFile(response, fileName)
            self.textBrowser.append("변환 완료")
            print(response.text)
        except Exception as e: # 예외 처리 기록
            print('예외가 발생했습니다.', e)
            self.textBrowser.append(str(e) + ' 예외가 발생했습니다.')
            try:
                response_json = response.json() # json으로 바꿔줘야, key = message
                self.textBrowser.append(response_json["message"])
            except:
                pass
        pass


    def saveTxtFile(self, response, fileName): # txt 파일을 만들어주는 함수
        new_filename = fileName[-1].split('.')[0] + ".txt"  # To keep the same name except ext
        response_json = response.json()
        with open(new_filename, mode='w') as fw:
            fw.write(response_json["text"])

    def openFolder(self): # 파이썬의 os 모듈을 사용
        # os.path.realpath 하면 파일의 상대 경로를 출력해 줌.
        # .은 현재폴더, ..은 이전폴더
        path = os.path.realpath('.')
        # 해당 path의 파일(디렉토리를 열어줌)
        os.startfile(path)


    def clearStateTxt(self):
        self.textBrowser.clear()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "나만의 회의록 작성 프로그램"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#55aa7f;\">나만의 회의록 작성 프로그램</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "파일명"))
        self.pushButton.setText(_translate("MainWindow", "1. 음성파일 열기"))
        self.label_3.setText(_translate("MainWindow", "* 음성 데이터의 파일 형식은 mp3, aac, ac3, ogg, flac, wav를 지원."))
        self.label_6.setText(_translate("MainWindow", "Secret Key 입력"))
        self.pushButton_2.setText(_translate("MainWindow", "2. txt 파일로 변환하기"))
        self.label_4.setText(_translate("MainWindow", "CLOVA Speech Invoke URL"))
        self.label_5.setText(_translate("MainWindow", "상태창"))
        self.pushButton_3.setText(_translate("MainWindow", "3. 해당 폴더 열기"))
        self.pushButton_4.setText(_translate("MainWindow", "상태창 지우기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

