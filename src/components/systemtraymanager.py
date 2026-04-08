import sys
from components.mainwindow import MainWindow
from core import constants
from PySide6 import QtGui, QtWidgets



def systemtraymanager(all_sprites, icon_path):
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
    show_action = QtGui.QAction("Show window", app)
    show_action.triggered.connect(window.show)
    exit_action = QtGui.QAction("Quit", app)
    exit_action.triggered.connect(app.quit)
    menu.addAction(show_action)
    menu.addAction(exit_action)
    tray.setContextMenu(menu)
    print("Setup complete")
    window.show()
    sys.exit(app.exec())
