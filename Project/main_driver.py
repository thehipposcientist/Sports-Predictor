from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys
from Sports_Data import NFL, NCAA_Football, NBA, PL, Champions, MLB

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('app.ui', self)
        self.setWindowTitle("Who's Winning")
        self.setFixedWidth(1100)
        self.setFixedHeight(900)
        self.actionSChedule.triggered.connect(self.NFL)
        self.actionNBA.triggered.connect(self.NBA)
        self.actionMLB.triggered.connect(self.MLB)

    def NFL(self):
        self.header.setText("This Weeks Games in the NFL")
        curr_sched = NFL.get_curr_sched()
        self.create_widget(0, 0)

    def NBA(self):
        self.header.setText("This Weeks Games in the NBA")

    def MLB(self):
        self.header.setText("This Weeks Games in the MLB")

    def create_widget(self, row, col):
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(1000, 150))
        self.frame.setMaximumSize(QtCore.QSize(1000, 150))
        self.frame.setStyleSheet('background-color: black;')
        # self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setStyleSheet('background-color: black;')
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, row, col, 1, 1)
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)   

        
stylesheet = """
    .QWidget {
        background-color: #272E33;
    }

    #header {
        color: white;
        font-size: 30px;
        font-weight: bold;
        font-family: Tahoma, Verdana, sans-serif;
    }

    .QMenuBar, .QMenu {
        background-color: #6B7C89;
        color: white;
        font-weight: bold;
    }

    .Qmenu{
        font-size: 10px;
    }

    .actionNFL:hover {
        background-color: #4F3E3E;
    }

"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    window = Ui()
    window.show()
    app.exec_()   