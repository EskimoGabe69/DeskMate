from PySide6 import QtWidgets, QtCore

# TODO: Might add CSS here too


class ConfigAskWindow(QtWidgets.QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.app = app
        self.text_area = QtWidgets.QPlainTextEdit()
        self.text_area.setReadOnly(True)
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
        grid.addWidget(self.text_area)
        grid.addWidget(self.new_config_button)
        grid.addWidget(self.existing_config_button)

    def close_button_func(self) -> None:
        print("Close button")


    def existing_config_button_func(self) -> None:
        print("existing config")

    def new_config_button_func(self) -> None:
        print("new config")

