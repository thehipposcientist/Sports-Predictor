# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1092, 846)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(120, 30, 861, 51))
        self.header.setTextFormat(QtCore.Qt.PlainText)
        self.header.setScaledContents(False)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.games_view = QtWidgets.QScrollArea(self.centralwidget)
        self.games_view.setGeometry(QtCore.QRect(110, 90, 901, 661))
        self.games_view.setWidgetResizable(True)
        self.games_view.setObjectName("games_view")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 899, 659))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(675, 175))
        self.frame.setMaximumSize(QtCore.QSize(675, 175))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.home_team = QtWidgets.QLabel(self.frame)
        self.home_team.setGeometry(QtCore.QRect(50, 50, 200, 31))
        self.home_team.setAlignment(QtCore.Qt.AlignCenter)
        self.home_team.setObjectName("home_team")
        self.away_team = QtWidgets.QLabel(self.frame)
        self.away_team.setGeometry(QtCore.QRect(300, 50, 200, 31))
        self.away_team.setAlignment(QtCore.Qt.AlignCenter)
        self.away_team.setObjectName("away_team")
        self.home_score = QtWidgets.QLabel(self.frame)
        self.home_score.setGeometry(QtCore.QRect(92, 100, 111, 71))
        self.home_score.setAlignment(QtCore.Qt.AlignCenter)
        self.home_score.setObjectName("home_score")
        self.away_score = QtWidgets.QLabel(self.frame)
        self.away_score.setGeometry(QtCore.QRect(342, 100, 111, 71))
        self.away_score.setAlignment(QtCore.Qt.AlignCenter)
        self.away_score.setObjectName("away_score")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(510, 20, 161, 121))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(560, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.datetime = QtWidgets.QLabel(self.frame)
        self.datetime.setGeometry(QtCore.QRect(210, 10, 151, 31))
        self.datetime.setAlignment(QtCore.Qt.AlignCenter)
        self.datetime.setObjectName("datetime")
        self.divider = QtWidgets.QFrame(self.frame)
        self.divider.setGeometry(QtCore.QRect(30, 150, 521, 16))
        self.divider.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.divider.setLineWidth(2)
        self.divider.setFrameShape(QtWidgets.QFrame.HLine)
        self.divider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.divider.setObjectName("divider")
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.games_view.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 21))
        self.menubar.setObjectName("menubar")
        self.menuNFL = QtWidgets.QMenu(self.menubar)
        self.menuNFL.setObjectName("menuNFL")
        self.menuMLB = QtWidgets.QMenu(self.menubar)
        self.menuMLB.setObjectName("menuMLB")
        self.menuNCAAF = QtWidgets.QMenu(self.menubar)
        self.menuNCAAF.setObjectName("menuNCAAF")
        self.menuNBA = QtWidgets.QMenu(self.menubar)
        self.menuNBA.setObjectName("menuNBA")
        self.menuPremiere_League = QtWidgets.QMenu(self.menubar)
        self.menuPremiere_League.setObjectName("menuPremiere_League")
        MainWindow.setMenuBar(self.menubar)
        self.actionNFL = QtWidgets.QAction(MainWindow)
        self.actionNFL.setObjectName("actionNFL")
        self.actionNBA = QtWidgets.QAction(MainWindow)
        self.actionNBA.setObjectName("actionNBA")
        self.actionNCAA_Football = QtWidgets.QAction(MainWindow)
        self.actionNCAA_Football.setObjectName("actionNCAA_Football")
        self.actionPremiere_League = QtWidgets.QAction(MainWindow)
        self.actionPremiere_League.setObjectName("actionPremiere_League")
        self.actionMLB = QtWidgets.QAction(MainWindow)
        self.actionMLB.setObjectName("actionMLB")
        self.actionChampions_League = QtWidgets.QAction(MainWindow)
        self.actionChampions_League.setObjectName("actionChampions_League")
        self.actionSChedule = QtWidgets.QAction(MainWindow)
        self.actionSChedule.setObjectName("actionSChedule")
        self.actionHistory = QtWidgets.QAction(MainWindow)
        self.actionHistory.setObjectName("actionHistory")
        self.actionData = QtWidgets.QAction(MainWindow)
        self.actionData.setObjectName("actionData")
        self.mlbSchedule = QtWidgets.QAction(MainWindow)
        self.mlbSchedule.setObjectName("mlbSchedule")
        self.actionNBASchedule = QtWidgets.QAction(MainWindow)
        self.actionNBASchedule.setObjectName("actionNBASchedule")
        self.menuNFL.addAction(self.actionSChedule)
        self.menuNFL.addSeparator()
        self.menuNFL.addAction(self.actionHistory)
        self.menuNFL.addSeparator()
        self.menuNFL.addAction(self.actionData)
        self.menuMLB.addAction(self.mlbSchedule)
        self.menuNBA.addAction(self.actionNBASchedule)
        self.menubar.addAction(self.menuNFL.menuAction())
        self.menubar.addAction(self.menuMLB.menuAction())
        self.menubar.addAction(self.menuNCAAF.menuAction())
        self.menubar.addAction(self.menuNBA.menuAction())
        self.menubar.addAction(self.menuPremiere_League.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "This Weeks Games"))
        self.home_team.setText(_translate("MainWindow", "TextLabel"))
        self.away_team.setText(_translate("MainWindow", "TextLabel"))
        self.home_score.setText(_translate("MainWindow", "TextLabel"))
        self.away_score.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.datetime.setText(_translate("MainWindow", "TextLabel"))
        self.menuNFL.setTitle(_translate("MainWindow", "NFL"))
        self.menuMLB.setTitle(_translate("MainWindow", "MLB"))
        self.menuNCAAF.setTitle(_translate("MainWindow", "NCAAF"))
        self.menuNBA.setTitle(_translate("MainWindow", "NBA"))
        self.menuPremiere_League.setTitle(_translate("MainWindow", "Premiere League"))
        self.actionNFL.setText(_translate("MainWindow", "NFL"))
        self.actionNBA.setText(_translate("MainWindow", "NBA"))
        self.actionNCAA_Football.setText(_translate("MainWindow", "NCAA Football"))
        self.actionPremiere_League.setText(_translate("MainWindow", "Premiere League"))
        self.actionMLB.setText(_translate("MainWindow", "MLB"))
        self.actionChampions_League.setText(_translate("MainWindow", "Champions League"))
        self.actionSChedule.setText(_translate("MainWindow", "Schedule"))
        self.actionHistory.setText(_translate("MainWindow", "History"))
        self.actionData.setText(_translate("MainWindow", "Data"))
        self.mlbSchedule.setText(_translate("MainWindow", "Schedule"))
        self.actionNBASchedule.setText(_translate("MainWindow", "Schedule"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
