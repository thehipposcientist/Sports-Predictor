from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys
from datetime import date, datetime
import PyQt5
from Sports_Data import NFL, NCAA_Football, NBA, PL, Champions, MLB
import stylesheet as st
import time
from PyQt5.QtGui import QMovie
import mysql.connector 

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('app.ui', self)
        self.setWindowTitle("Who's Winning")
        self.setFixedWidth(1100)
        self.setFixedHeight(900)
        self.actionSChedule.triggered.connect(self.NFL)
        self.actionNBASchedule.triggered.connect(self.NBA)
        self.mlbSchedule.triggered.connect(self.MLB)
        self.header.setText("Welcome")
        self.games_view.hide()

    def NFL(self):
        self.clear_widgets()
        self.header.setText("This Weeks Games in the NFL")
        self.games_view.show()
        away, home, away_score, home_score, winner, game_date = NFL.get_curr_sched()
        for i in range(len(away)):
            self.create_widget(i, away[i], home[i], home_score[i], away_score[i], game_date[i])

    def NBA(self):
        self.clear_widgets()
        self.header.setText("Todays Game(s) in the NBA")
        self.games_view.show()
        away, home, away_score, home_score, winner, game_date = NBA.get_curr_schedule()
        for i in range(len(away)):
            self.create_widget(i, away[i], home[i], home_score[i], away_score[i], game_date[i])

    def MLB(self):
        self.clear_widgets()
        self.header.setText("Todays Game(s) in the MLB")
        self.games_view.show()
        away, home, away_score, home_score, winner, game_date = MLB.get_curr_schedule()
        for i in range(len(away)):
            self.create_widget(i, away[i], home[i], home_score[i], away_score[i], game_date[i])

    def create_widget(self, row, away, home, home_score, away_score, game_date):
        self.game_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.game_frame.setMinimumSize(QtCore.QSize(675, 175))
        self.game_frame.setMaximumSize(QtCore.QSize(675, 175))
        self.game_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.game_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.game_frame.setObjectName("frame")
        self.home_team = QtWidgets.QLabel(self.game_frame)
        self.home_team.setGeometry(QtCore.QRect(50, 50, 200, 31))
        self.home_team.setAlignment(QtCore.Qt.AlignCenter)
        self.home_team.setObjectName("home_team")
        self.away_team = QtWidgets.QLabel(self.game_frame)
        self.away_team.setGeometry(QtCore.QRect(300, 50, 200, 31))
        self.away_team.setAlignment(QtCore.Qt.AlignCenter)
        self.away_team.setObjectName("away_team")
        self.home_score = QtWidgets.QLabel(self.game_frame)
        self.home_score.setGeometry(QtCore.QRect(92, 100, 111, 71))
        self.home_score.setAlignment(QtCore.Qt.AlignCenter)
        self.home_score.setObjectName("home_score")
        self.away_score = QtWidgets.QLabel(self.game_frame)
        self.away_score.setGeometry(QtCore.QRect(342, 100, 111, 71))
        self.away_score.setAlignment(QtCore.Qt.AlignCenter)
        self.away_score.setObjectName("away_score")
        self.graphicsView = QtWidgets.QGraphicsView(self.game_frame)
        self.graphicsView.setGeometry(QtCore.QRect(510, 20, 161, 121))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.game_frame)
        self.pushButton.setGeometry(QtCore.QRect(560, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.datetime = QtWidgets.QLabel(self.game_frame)
        self.datetime.setGeometry(QtCore.QRect(210, 10, 151, 31))
        self.datetime.setAlignment(QtCore.Qt.AlignCenter)
        self.datetime.setObjectName("datetime")
        self.home_team.setText(away)
        self.away_team.setText(home)
        if str(home_score) == 'None': home_score = 0;
        if str(away_score) == 'None': away_score = 0;
        self.home_score.setText(str(away_score))
        self.away_score.setText(str(home_score))
        self.pushButton.setText('History')
        self.datetime.setText(str(game_date))
        self.verticalLayout.addWidget(self.game_frame, row, QtCore.Qt.AlignHCenter)
        
    def clear_widgets(self):
        for i in reversed(range(self.verticalLayout.count())): 
            widgetToRemove = self.verticalLayout.itemAt(i).widget()
            # remove it from the layout list
            self.verticalLayout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

stylesheet = st.stylesheet

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    window = Ui()
    window.show()
    app.exec_()   