from PySide6 import QtWidgets
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QMouseEvent, QPaintEvent, QPainter, QPen, QPixmap


class SpriteAreaPicker(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.image = None
        self.selection_start = None
        self.selection_end = None
        self.is_selecting = False
        self.setMouseTracking(True)

    def load_image(self, image_path):
        self.image = QPixmap(image_path)
        self.selection_start = None
        self.selection_end = None
        self.update()

    def paintEvent(self, event: QPaintEvent) -> None:
        super().paintEvent(event)
        if self.image is None:
            return

        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

        if self.selection_start and self.selection_end:
            rect = QRect(self.selection_start, self.selection_end).normalized()
            painter.setPen(QPen(Qt.red, 2, Qt.DashLine))
            painter.drawRect(rect)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.is_selecting = True
            self.selection_start = event.pos()
            self.selection_end = event.pos()
            self.update()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.is_selecting:
            self.selection_end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.is_selecting = False
            self.selection_end = event.pos()
            self.update()

    def on_area_selecter(self):
        if self.selection_start and self.selection_end:
            rect = QRect(self.selection_start, self.selection_end).normalized()
            print(f"Selected : {rect.x()}, {rect.y()}, {rect.width()}, {rect.height()}")
