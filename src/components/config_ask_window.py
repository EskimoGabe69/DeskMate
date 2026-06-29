from PySide6 import QtWidgets, QtCore
import os

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")


class ConfigAskWindow(QtWidgets.QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.app = app
        self.text_area = QtWidgets.QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setHtml("<h1>Test h1</h1><h2>Test h2</h2><p>Test p</p>")
        self.css_file = QtCore.QFile(css_path)
        self.css_file.open(QtCore.QFile.OpenModeFlag.ReadOnly)
        self.style_sheet = str(self.css_file.readAll(), encoding="utf-8")
        self.css_file.close()
        grid = QtWidgets.QGridLayout()
        self.close_button = QtWidgets.QPushButton("Close window.", self)
        self.existing_config_button = QtWidgets.QPushButton(
            "Use exsiting configuration", self
        )
        self.new_config_button = QtWidgets.QPushButton("Make new configuration", self)
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(grid)
        self.setCentralWidget(central_widget)
        self.close_button.clicked.connect(self.close_button_func)
        self.close_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.existing_config_button.clicked.connect(self.existing_config_button_func)
        self.existing_config_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.new_config_button.clicked.connect(self.new_config_button_func)
        self.new_config_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.setStyleSheet(self.style_sheet)
        grid.addWidget(self.text_area)
        grid.addWidget(self.new_config_button)
        grid.addWidget(self.existing_config_button)

    def close_button_func(self) -> None:
        print("Close button")

    def existing_config_button_func(self) -> None:
        print("existing config")

    def new_config_button_func(self) -> None:
        print("new config")
