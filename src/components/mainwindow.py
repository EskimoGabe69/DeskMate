import imagewidget
import core.constants as constants
from PySide6 import QtWidgets, QtCore


# NOTE: gotta fix dependencies
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, surface, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        self.setCentralWidget(imagewidget.ImageWidget(surface))
        self.setWindowTitle("Deskmate by EskimoGabe")
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint
        )
        self.showMaximized()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.game_step)
        self.timer.start(1000 // 30)

    def game_step(self):
        constants.SCREEN.fill(constants.TRANSPARENT)
        all_sprites.update()
        all_sprites.draw(constants.SCREEN)
        self.centralWidget().update()
