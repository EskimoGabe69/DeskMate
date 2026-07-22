from PySide6 import QtGui, QtWidgets
from components.config_ask_window import ConfigAskWindow
from components.mainwindow import MainWindow
from components.menuwindow import MenuWindow
from core.constants import CAPTION, SCREEN
from core.signal import SpriteSignal
import sys


class AppManager:
    """
    A helper which allows to bundle some of the windows, icontray and actions into one place.

    Attributes:
        all_sprites: which is a pygame sprite group container, which contains a bunch of game sprites
        icon_path (str): string containing info regarding where the icon for the icon tray is located.

    Usecase:
        appmanager = AppManager(all_sprites)
        appmanager.run() # which runs the application including the initializer and the main window

    """

    def __init__(self, all_sprites, icon_path) -> None:
        self.all_sprites = all_sprites
        self.icon_path = icon_path
        self.app = QtWidgets.QApplication(sys.argv)
        self.signal = SpriteSignal()

    def initialize_app(self):
        self.app.setQuitOnLastWindowClosed(False)

    def setup_window(self):
        self.mate_window = MainWindow(self.all_sprites, SCREEN)
        self.signal.sprite_selected.connect(self.mate_window.add_sprite)
        self.config_window = ConfigAskWindow(self.app)
        self.menu_window = MenuWindow(self.app)

    def setup_tray_icon(self):
        self.pixmap = QtGui.QPixmap(self.icon_path)
        self.scaled_pixmap = self.pixmap.scaled(32, 32)
        self.icon = QtGui.QIcon(self.scaled_pixmap)
        self.tray = QtWidgets.QSystemTrayIcon(self.icon, self.app)
        self.tray.setToolTip(CAPTION)
        self.tray.show()
        self.menu = QtWidgets.QMenu()
        # mate window action
        self.mate_action = QtGui.QAction("Open Mate Window", self.app)
        self.mate_action.triggered.connect(self.mate_window.show)
        self.menu.addAction(self.mate_action)
        # config window action
        self.config_action = QtGui.QAction("Open Config Window", self.app)
        self.config_action.triggered.connect(self.config_window.show)
        self.menu.addAction(self.config_action)
        # menu window action
        self.menu_action = QtGui.QAction("Open Menu Window", self.app)
        self.menu_action.triggered.connect(self.menu_window.show)
        self.menu.addAction(self.menu_action)
        # exit program action
        self.exit_action = QtGui.QAction("Exit Deskmate", self.app)
        self.exit_action.triggered.connect(self.app.quit)
        self.menu.addAction(self.exit_action)
        self.tray.setContextMenu(self.menu)

    def run(self):
        self.initialize_app()
        self.setup_window()
        self.setup_tray_icon()
        self.mate_window.show()
        print("Setup complete")
        sys.exit(self.app.exec())
