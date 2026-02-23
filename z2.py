import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class StopW(QWidget):

    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.tl = QLabel("00:00:00",self)
        self.bt = QPushButton("Start",self)
        self.bt1 = QPushButton("Stop",self)
        self.bt2 = QPushButton("Reset",self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        vb = QVBoxLayout()
        vb.addWidget(self.tl)
        vb.addWidget(self.bt)
        vb.addWidget(self.bt1)
        vb.addWidget(self.bt2)

        self.setLayout(vb)

        self.tl.setAlignment(Qt.AlignCenter)

        hb = QHBoxLayout()
        hb.addWidget(self.bt)
        hb.addWidget(self.bt1)
        hb.addWidget(self.bt2)

        vb.addLayout(hb)

        self.setStyleSheet("""
            QPushButton, QLabel{
            padding: 20px;
            font-weight: Arial;
            }
            QPushButton {
            font-size: 50px;
            }
            QLabel {
            font-size: 120px;
            background-color: hsl(200, 100%,92%);
            border-radius: 20px;
            }
        """)

        self.bt.clicked.connect(self.st)
        self.bt1.clicked.connect(self.stp)
        self.bt2.clicked.connect(self.re)
        self.timer.timeout.connect(self.up)

    def st(self):
        self.timer.start(10)

    def stp(self):
        self.timer.stop()

    def re(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.tl.setText(self.fr(self.time))

    def fr(self,time):
        h = time.hour()
        m = time.minute()
        s = time.second()
        mi = time.msec() // 10
        return f"{h:02}:{m:02}:{s:02}.{mi:02}"

    def up(self):
        self.time = self.time.addMSecs(10)
        self.tl.setText(self.fr(self.time))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    W = StopW()
    W.show()
    sys.exit(app.exec_())