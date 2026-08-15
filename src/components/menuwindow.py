import shlex
from components.sprite_area_picker import SpriteAreaPicker
from core import constants
from PySide6 import QtCore, QtWidgets, QtGui
from core.signal import SpriteSignal
from utils.application_updater import ApplicationUpdater

class MenuWindow(QtWidgets.QMainWindow):
    """
    Class component which shows the menu of the application

    Usecase:
        menuwindow = MenuWindow(app)
        menuwindow.show()

    Attributes:
        app: object of QApplication from QtWidgets
    """

    def __init__(self, app, parent=None) -> None:
        super().__init__(parent)
        self.app = app
        self.process = None
        self.text_area = QtWidgets.QPlainTextEdit()
        self.text_area.setReadOnly(True)
        self.setWindowFlags(QtCore.Qt.Window)
        self.css_file = QtCore.QFile(constants.CSS_PATH)
        self.css_file.open(QtCore.QFile.OpenModeFlag.ReadOnly)
        self.style_sheet = str(self.css_file.readAll(), encoding="utf-8")
        self.css_file.close()
        self.setWindowTitle(constants.CAPTION)
        grid = QtWidgets.QGridLayout()
        self.updater_button = QtWidgets.QPushButton("Update button", self)
        self.sprite_button = QtWidgets.QPushButton("Insert new sprite", self)
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(grid)
        self.setCentralWidget(central_widget)
        self.updater_button.clicked.connect(self.update_button)
        self.updater_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sprite_signal = SpriteSignal()
        # NOTE: Might move it to config_ask_window(the SpriteAreaPicker)
        self.area_picker = SpriteAreaPicker()
        grid.addWidget(self.area_picker)
        self.sprite_button.clicked.connect(self.sprite_signal.sprite_btn_return)
        self.sprite_signal.sprite_selected.connect(self.load_image)
        self.sprite_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        grid.addWidget(self.updater_button, 0, 0, QtGui.Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.sprite_button, 500, 0, QtGui.Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.text_area)
        self.setStyleSheet(self.style_sheet)   
        self.text = QtWidgets.QLabel(ApplicationUpdater.update_message())
        self.text.adjustSize()
        grid.addWidget(self.text, 1920, 0, QtGui.Qt.AlignmentFlag.AlignLeft)

    def load_image(self, file_path):
        self.area_picker.load_image(file_path)

    def update_button(self) -> None:
        if self.process is not None:
            return

        self.text_area.clear()
        self.updater_button.setEnabled(False)

        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_error)
        self.process.finished.connect(self.process_finished)
        self.split_command: list = shlex.split("pull origin dev-branch")
        self.process.start("git", self.split_command)

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        text = bytes(data).decode("utf-8")
        self.text_area.appendPlainText(text.rstrip())

    def handle_error(self):
        data = self.process.readAllStandardError()
        text = bytes(data).decode("utf-8")
        self.text_area.appendPlainText(text.rstrip())

    def process_finished(self):
        self.text_area.appendPlainText("Update finished!")
        self.process = None
        self.updater_button.setEnabled(True)
