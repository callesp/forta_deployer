from PySide6.QtWidgets import QWidget
import ui_MainPage


class MainPage(QWidget, ui_MainPage.Ui_Main):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setupUi(self)
