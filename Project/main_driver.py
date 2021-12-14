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
        self.actionNFL.triggered.connect(self.NFL)
        self.actionNBA.triggered.connect(self.NBA)
        self.actionMLB.triggered.connect(self.MLB)

    def NFL(self):
        self.header.setText("This Weeks Games in the NFL")
        NFL.run_nfl()

    def NBA(self):
        self.header.setText("This Weeks Games in the NBA")

    def MLB(self):
        self.header.setText("This Weeks Games in the MLB")
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
        font-size: 20px;
        font-weight: bold;
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