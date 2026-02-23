import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Di(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Marjo")
        self.tl = QLabel(self)
        self.ti = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 110)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tl)
        self.setLayout(vbox)

        self.tl.setAlignment(Qt.AlignCenter)
        self.tl.setStyleSheet("font-size: 150px;"
                              "color: hsl(111,100%,50%);")
        self.setStyleSheet("background-color: black;")

        fo = QFontDatabase.addApplicationFont("DS-DIGI.TTF")
        ff = QFontDatabase.applicationFontFamilies(fo)[0]
        mf = QFont(ff,150)
        self.tl.setFont(mf)

        self.ti.timeout.connect(self.up)
        self.ti.start(1000)
        self.up()

    def up(self):
        cr = QTime.currentTime().toString("hh:mm:ss AP")
        self.tl.setText(cr)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Di()
    ex.show()
    sys.exit(app.exec_())