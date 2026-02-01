from PySide6 import QtCore, QtGui, QtWidgets
import pygame
import sys

# NOTE: constants, will put them into their own file
# NOTE: for width and height I will use a library to get the screen width and height
WIDTH = 1336
HEIGHT = 768
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SCREEN = pygame.surface.Surface((WIDTH, HEIGHT))

# NOTE: I think its better to put the QT6 thing here, before initialising pygame, lets see
# this is the one that works


class ImageWidget(QtWidgets.QWidget):
    def __init__(self, surface, parent=None) -> None:
        super().__init__(parent)
        self.surface = surface
        self._update_qimage()

    def _update_qimage(self):
        width = self.surface.get_width()
        height = self.surface.get_height()
        self.data = self.surface.get_buffer().raw
        self.image = QtGui.QImage(self.data, width, height, QtGui.QImage.Format.Format_RGB32)

    def paintEvent(self, event):
        self._update_qimage()
        qp = QtGui.QPainter(self)    
        qp.drawImage(0, 0, self.image)
        


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, surface, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        self.setCentralWidget(ImageWidget(surface))
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.game_step)
        self.timer.start(1000 // 30)

    def game_step(self):
        SCREEN.fill(BLACK)
        all_sprites.update()
        all_sprites.draw(SCREEN)
        self.centralWidget().update()


pygame.init()


class Mate(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((RED))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.vx = 2

    def update(self) -> None:
        self.rect.x += self.vx
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.vx *= -1


mate = Mate()
all_sprites = pygame.sprite.Group()
all_sprites.add(mate)
SCREEN.fill((BLACK))
all_sprites.draw(SCREEN)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow(SCREEN)
window.show()
if __name__ == "__main__":
    app.exec()
