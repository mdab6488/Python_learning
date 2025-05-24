import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MD AB")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("icon.png"))

        lable = QLabel("Hello", self)
        lable.setFont(QFont("Arial", 30))
        lable.setGeometry(0, 0, 500, 100)
        lable.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;")

        # lable.setAlignment(Qt.AlignTop) # VERTICALLY TOP
        # lable.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
        # lable.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER

        # lable.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        # lable.setAlignment(Qt.AlignHCenter) # HORIZONTALLY CENTER
        # lable.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT

        # lable.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        # lable.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        # lable.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER & CENTER

        lable.setAlignment(Qt.AlignCenter) # CENTER & CENTER


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ =="__main__":
    main()