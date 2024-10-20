from PySide6.QtWidgets import QApplication
import sys

from main_window import MainWindow

# Запуск пользовательского интерфейса
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Gap Slover')
    window.show()

    sys.exit(app.exec())