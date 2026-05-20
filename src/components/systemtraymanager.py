import sys
from components.mainwindow import MainWindow
from components.menuwindow import MenuWindow
from core import constants
from PySide6 import QtGui, QtWidgets
from core.signal import SpriteSignal


def systemtraymanager(all_sprites, icon_path):
    app = QtWidgets.QApplication(sys.argv)

    app.setQuitOnLastWindowClosed(False)
    menu_window = MenuWindow(app)
    menu_window.show()
    window = MainWindow(all_sprites, constants.SCREEN)
    signal = SpriteSignal()
    signal.sprite_selected.connect(window.add_sprite)
    pixmap = QtGui.QPixmap(icon_path)
    scaled_pixmap = pixmap.scaled(32, 32)
    icon = QtGui.QIcon(scaled_pixmap)
    window.setWindowIcon(icon)
    tray = QtWidgets.QSystemTrayIcon(icon, app)
    tray.setToolTip(constants.CAPTION)
    tray.show()
    menu = QtWidgets.QMenu()
    show_action = QtGui.QAction("Show window", app)
    show_action.triggered.connect(window.show)
    menu_open_action = QtGui.QAction("Open menu", app)
    menu_open_action.triggered.connect(menu_window.show)
    exit_action = QtGui.QAction("Quit application", app)
    exit_action.triggered.connect(app.quit)
    menu.addAction(show_action)
    menu.addAction(menu_open_action)
    menu.addAction(exit_action)
    tray.setContextMenu(menu)
    print("Setup complete")
    window.show()
    sys.exit(app.exec())
