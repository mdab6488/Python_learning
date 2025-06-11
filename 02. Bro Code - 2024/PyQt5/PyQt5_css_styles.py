import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QWidget,
                             QPushButton,
                             QHBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MD AB")
        self.setWindowIcon(QIcon("icon.png"))
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.init_ui()

    def init_ui(self):
        center_widget = QWidget()
        self.setCentralWidget(center_widget)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        center_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 10px;
            }
            QPushButton#button1{
                background-color: hsl(0, 100%, 64%);
            }
            QPushButton#button2{
                background-color: hsl(122, 100%, 64%);
            }
            QPushButton#button3{
                background-color: hsl(204, 100%, 64%);
            }
            QPushButton#button1:hover{
                background-color: hsl(0, 100%, 84%);
            }
            QPushButton#button2:hover{
                background-color: hsl(122, 100%, 84%);
            }
            QPushButton#button3:hover{
                background-color: hsl(204, 100%, 84%);
            }
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()