from PySide6 import QtWidgets

# TODO: Under construction
class SpriteAreaPicker(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super.__init__(parent)
        self.image = None
        self.selection_start = None

