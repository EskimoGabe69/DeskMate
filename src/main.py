from PySide6 import QtCore, QtGui, QtWidgets
import pygame
import sys
import core.constants as constants
from components.imagewidget import ImageWidget
from components.mate import Mate


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, surface, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        self.setCentralWidget(ImageWidget(surface))
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


pygame.init()




mate = Mate()
all_sprites = pygame.sprite.Group()
all_sprites.add(mate)
constants.SCREEN.fill((constants.TRANSPARENT))
all_sprites.draw(constants.SCREEN)

app = QtWidgets.QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)
window = MainWindow(constants.SCREEN)
pixmap = QtGui.QPixmap("./assets/first_logo.png")
scaled_pixmap = pixmap.scaled(32, 32)
icon = QtGui.QIcon(scaled_pixmap)
window.setWindowIcon(icon)
tray = QtWidgets.QSystemTrayIcon(icon, app)
tray.setToolTip("Deskmate by EskimoGabe")
tray.show()

menu = QtWidgets.QMenu()
exit_action = QtGui.QAction("Quit", app)
exit_action.triggered.connect(app.quit)
menu.addAction(exit_action)
tray.setContextMenu(menu)

if __name__ == "__main__":
    app.exec()
