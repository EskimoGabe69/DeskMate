import pygame
from components.mate import Mate
import core.constants as constants
from PySide6 import QtGui, QtWidgets
from components.mainwindow import MainWindow
import sys
import os


pygame.init()
game_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(game_directory, ".."))
asset_directory = os.path.join(parent_directory, "assets")


def app(icon_path):
    pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    image_file = pygame.image.load(
        os.path.join(asset_directory, "Doggo.png")
    ).convert_alpha()
    mate = Mate(image_file)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(mate)
    constants.SCREEN.fill(constants.TRANSPARENT)
    all_sprites.draw(constants.SCREEN)
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = MainWindow(all_sprites, constants.SCREEN)
    pixmap = QtGui.QPixmap(icon_path)
    scaled_pixmap = pixmap.scaled(32, 32)
    icon = QtGui.QIcon(scaled_pixmap)
    window.setWindowIcon(icon)
    tray = QtWidgets.QSystemTrayIcon(icon, app)
    tray.setToolTip(constants.CAPTION)
    tray.show()
    menu = QtWidgets.QMenu()
    exit_action = QtGui.QAction("Quit", app)
    exit_action.triggered.connect(app.quit)
    menu.addAction(exit_action)
    tray.setContextMenu(menu)
    print("Setup complete")
    window.show()
    sys.exit(app.exec())
