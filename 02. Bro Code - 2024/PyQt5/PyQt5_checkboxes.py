import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QCheckBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("MD AB")
        self.setWindowIcon(QIcon("icon.png"))
        self.checkbox = QCheckBox("Don you like food?", self)
        self.init_ui()

    def init_ui(self):
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial")
        self.checkbox.setChecked(False)

        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        # print(state)
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You do not like food")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()