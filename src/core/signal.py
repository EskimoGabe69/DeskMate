from PySide6 import QtCore
from utils.sprite_sheet_picker import sprite_sheet_picker


class SpriteSignal(QtCore.QObject):
    """
    Component class which is used to throw the sprite around the project where its needed.

    Still isnt really properly used to give usecase.
    """

    sprite_selected = QtCore.Signal(str)

    def __init__(self) -> None:
        super(SpriteSignal, self).__init__()

    def sprite_btn_return(self):
        file_path = sprite_sheet_picker()
        if file_path:
            self.sprite_selected.emit(file_path)
