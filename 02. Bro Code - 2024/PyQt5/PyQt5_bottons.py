import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QPushButton,
                             QLabel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("MD AB")
        self.setWindowIcon(QIcon("icon.png"))
        self.button = QPushButton("Click me!", self)
        self.lable = QLabel("Hello", self)
        self.init_ui()

    def init_ui(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px")
        self.button.clicked.connect(self.on_click)

        self.lable.setGeometry(150, 300, 200, 100)
        self.lable.setStyleSheet("font-size: 50px")

    def on_click(self):
        # print("Button Clicked!")
        # self.button.setText("Clicked!")
        # self.button.setDisabled(True)

        self.lable.setText("Goodbye")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()