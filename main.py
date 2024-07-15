from PySide6.QtWidgets import QApplication
import sys
from re import compile

from main_window import MainWindow

from changer import add_break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle(' ')
    window.show()

    sys.exit(app.exec())