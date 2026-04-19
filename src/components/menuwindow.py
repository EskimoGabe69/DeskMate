from core import constants
from PySide6 import QtCore, QtWidgets, QtGui
# NOTE: Will be used for css path that its not in main then
# import os


class MenuWindow(QtWidgets.QMainWindow):
    def __init__(self, app, css_path, parent=None) -> None:
        super(MenuWindow, self).__init__(parent)
        self.app = app
        self.css_path = css_path
        self.css_file = QtCore.QFile(self.css_path)
        self.css_file.open(QtCore.QFile.ReadOnly)
        self.style_sheet = str(self.css_file.readAll(), encoding="utf-8")
        self.css_file.close()
        self.setWindowTitle(constants.CAPTION)
        grid = QtWidgets.QGridLayout()
        self.button = QtWidgets.QPushButton("Test button", self)
        self.button.clicked.connect(self._button_clicked)
        grid.addWidget(self.button, 0, 0, QtGui.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(grid)
        self.setStyleSheet(self.style_sheet)

    def _button_clicked(self) -> None:
        print("Test button hello world")
