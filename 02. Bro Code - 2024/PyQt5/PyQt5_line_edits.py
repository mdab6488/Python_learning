import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QLineEdit,
                             QPushButton)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("MD AB")
        self.setWindowIcon(QIcon("icon.png"))
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.init_ui()

    def init_ui(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.line_edit.setStyleSheet("font-size: 30px;"
                                     "font-family: Arial")

        self.button.setGeometry(210, 10, 100, 40)
        self.button.setStyleSheet("font-size: 20px;"
                                     "font-family: Arial")

        self.line_edit.setPlaceholderText("Enter your name")

        self.button.clicked.connect(self.submit)

    def submit(self):
        # print("You clicked the button!")
        text = self.line_edit.text()
        print(f"Hello, {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()