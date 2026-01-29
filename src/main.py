from PySide6 import QtGui, QtWidgets
import pygame
import sys

# NOTE: constants, will put them into their own file
# NOTE: for width and height I will use a library to get the screen width and height
WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# NOTE: I think its better to put the QT6 thing here, before initialising pygame, lets see
class ImageWidget(QtWidgets.QWidget):
    def __init__(self, surface, parent=None) -> None:
        super(ImageWidget, self).__init__(parent)
        width = surface.get_width()
        height = surface.get_height()
        self.data = surface.get_buffer().raw
        self.image =QtGui.QImage(self.data, width, height, QtGui.QImage.Format.Format_RGB32) 

    def paintEvent(self, event) -> None:
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(0,0,self.image)
        qp.end()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, surface, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        self.setCentralWidget(ImageWidget(surface))

pygame.init()


class Mate(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.vx = 2

    def update(self) -> None:
        self.rect.x += self.vx
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.vx *= -1


all_sprites = pygame.sprite.Group()
mate = Mate()
all_sprites.add(mate)
app = QtWidgets.QApplication(sys.argv)
window = pygame.display.set_mode((WIDTH, HEIGHT))
using_surface = MainWindow(window)
pygame.display.set_caption("Deskmate made by EskimoGabe")
clock = pygame.time.Clock()

if __name__ == "__main__":
    while True:
        all_sprites.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.fill(BLACK)
        all_sprites.draw(window) 
        using_surface.show()
        app.exec()
