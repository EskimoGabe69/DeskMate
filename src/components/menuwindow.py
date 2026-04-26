from core import constants
from PySide6 import QtCore, QtWidgets, QtGui
import os

from utils.updater import updater


css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")


class MenuWindow(QtWidgets.QMainWindow):
    def __init__(self, app, parent=None) -> None:
        super(MenuWindow, self).__init__(parent)
        self.app = app
        self.setWindowFlags(
            self.windowFlags() | QtGui.Qt.WindowType.WindowStaysOnTopHint
        )
        self.css_file = QtCore.QFile(css_path)
        self.css_file.open(QtCore.QFile.ReadOnly)
        self.style_sheet = str(self.css_file.readAll(), encoding="utf-8")
        self.css_file.close()
        self.setWindowTitle(constants.CAPTION)
        grid = QtWidgets.QGridLayout()
        self.button = QtWidgets.QPushButton("Update button", self)
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(grid)
        self.setCentralWidget(central_widget)
        self.button.clicked.connect(self.update_button)
        grid.addWidget(self.button, 0, 0, QtGui.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(grid)
        self.setStyleSheet(self.style_sheet)

    def update_button(self) -> None:
        updater()
