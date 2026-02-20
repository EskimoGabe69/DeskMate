import pygame
from components.mate import Mate
import core.constants as constants
from PySide6 import QtGui, QtWidgets
from components.mainwindow import MainWindow
import sys


def app(icon_path):
    pygame.init()

    mate = Mate()

    mate = Mate()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(mate)
    constants.SCREEN.fill((constants.TRANSPARENT))
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
