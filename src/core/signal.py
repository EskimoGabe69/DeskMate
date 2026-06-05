from PySide6 import QtCore
from components.sprite_area_picker import SpriteAreaPicker
from utils.sprite_sheet_picker import sprite_sheet_picker



class SpriteSignal(QtCore.QObject):
    sprite_selected = QtCore.Signal(str)
   
    def __init__(self) -> None:
        super(SpriteSignal, self).__init__()

    def sprite_btn_return(self):
        area_picker = SpriteAreaPicker()
        file_path = sprite_sheet_picker()
        if file_path:
            loaded_image = area_picker.load_image(file_path)
            self.sprite_selected.emit(loaded_image)
