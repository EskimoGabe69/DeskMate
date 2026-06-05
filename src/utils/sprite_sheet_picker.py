from PySide6 import QtWidgets 

def sprite_sheet_picker(parent=None):
    file_name, _ = QtWidgets.QFileDialog.getOpenFileName(parent, "../assets/.", "(*.jpg, *.png)")
    return file_name[0]
    
