import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QLabel,
                             QPushButton,
                             QVBoxLayout,
                             QHBoxLayout)
from PyQt5.QtCore import (QTime,
                          QTimer,
                          Qt)


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stopwatch")
        self.setWindowIcon(QIcon("icon.png"))
        self.time = QTime(0, 0, 0, 0)
        self.time_lable = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_lable)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)

        self.setLayout(vbox)

        self.time_lable.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
            QPushButton{
                font-size: 50px;
            }
            QLabel{
                font-size: 100px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 10px;
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)


    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_lable.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10

        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_lable.setText(self.format_time(self.time))

def main():
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()