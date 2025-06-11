import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QLabel,
                             QVBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MD AB")
        self.setWindowIcon(QIcon("icon.png"))
        self.time_lable = QLabel(self)
        self.timer = QTimer(self)
        self.init_ul()

    def init_ul(self):
        self.setGeometry(600,400,300,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_lable)
        self.setLayout(vbox)

        self.time_lable.setAlignment(Qt.AlignCenter)

        self.time_lable.setStyleSheet("font-size: 150px;"
                                      "color: hsl(111, 100%, 50%);")

        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_lable.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_lable.setText(current_time)

def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()