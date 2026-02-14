from PySide6 import QtWidgets, QtGui


class ImageWidget(QtWidgets.QWidget):
    def __init__(self, surface, parent=None) -> None:
        super().__init__(parent)
        self.surface = surface
        self._update_qimage()

    def _update_qimage(self):
        width = self.surface.get_width()
        height = self.surface.get_height()
        self.data = self.surface.get_buffer().raw
        self.image = QtGui.QImage(
            self.data, width, height, QtGui.QImage.Format.Format_ARGB32
        )

    def paintEvent(self, event):
        self._update_qimage()
        qp = QtGui.QPainter(self)
        qp.drawImage(0, 0, self.image)
        qp.end()
