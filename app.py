import sys
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

import ui_FortaManager
from mainpage import MainPage


class AppWindow(QMainWindow, ui_FortaManager.Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setupUi(self)

        self.stackedWidget.addWidget(MainPage())

        self.stackedWidget.addWidget(QWidget())

        self.last_navigate_button = self.pushButton_main

        self.pushButton_main.clicked.connect(
            lambda: self.navigate_button_clicked(self.pushButton_main, 0))

        self.pushButton_database.clicked.connect(
            lambda: self.navigate_button_clicked(self.pushButton_database, 1))

    def navigate_button_clicked(self, btn, index):
        self.stackedWidget.setCurrentIndex(index)


def main():
    app = QApplication()

    win = AppWindow()

    win.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
