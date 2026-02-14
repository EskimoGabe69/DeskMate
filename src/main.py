from PySide6 import QtCore, QtGui, QtWidgets
import pygame
import sys
import core.constants as constants
import components.imagewidget as imagewidget


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


pygame.init()


class Mate(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((constants.RED))
        self.rect = self.image.get_rect()
        self.rect.center = (constants.WIDTH // 2, constants.HEIGHT // 2)
        self.vx = 2

    def update(self) -> None:
        self.rect.x += self.vx
        if self.rect.right > constants.WIDTH or self.rect.left < 0:
            self.vx *= -1


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
