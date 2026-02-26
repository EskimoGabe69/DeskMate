from components.imagewidget import ImageWidget
import core.constants as constants
from PySide6 import QtWidgets, QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, all_sprites, surface, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        self.setCentralWidget(ImageWidget(surface))
        self.setWindowTitle(constants.CAPTION)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint
        )
        self.showMaximized()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.game_step)
        self.timer.start(1000 // 30)
        self.all_sprites = all_sprites

    def game_step(self): 
        constants.SCREEN.fill(constants.TRANSPARENT)
        self.all_sprites.update()
        self.all_sprites.draw(constants.SCREEN)
        self.centralWidget().update()
