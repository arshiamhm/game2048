from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class QTile(QtWidgets.QLabel):
    def __init__(self, parent=None, tile=None):
        super().__init__(parent)
        self.tile = tile
        self.setAlignment(Qt.AlignCenter) 
        self.draw_tile(tile)


    def draw_tile(self, tile):
        value = tile.get_value()
        if value is None:
            self.setText("")
            self.setStyleSheet("QTile { background: rgb(204, 192, 179); border-radius: 3px}")
        else:
            self.setText(str(value))
            if value == 2:
                self.setStyleSheet("QTile { background: rgb(238,228,218); color: rgb(119,110,101); font: bold; border-radius: 3px; font: 36pt; }")
            elif value == 4:
                self.setStyleSheet("QTile { background: rgb(237,224,200); color:\
                                rgb(119,110,101); font: bold; border-radius:\
                                3px; font: 36pt;}")
            elif value == 8:
                self.setStyleSheet("QTile { background: rgb(242,177,121); color:\
                                rgb(255,255,255); font: bold; border-radius:\
                                3px; font: 36pt; }")
            elif value == 16:
                self.setStyleSheet("QTile { background: rgb(245,150,100); color: rgb(255,255,255); font: bold; border-radius: 3px; font: 36pt; }")
            elif value == 32:
                self.setStyleSheet("QTile { background: rgb(245,125,95); color: rgb(255,255,255); font: bold; border-radius: 3px; font: 36pt; }")
            elif value == 64:
                self.setStyleSheet("QTile { background: rgb(245,95,60); color: rgb(255,255,255); font: bold; border-radius: 3px; font: 36pt; }")
            elif value == 128:
                self.setStyleSheet("QTile { background: rgb(237,207,114); color: rgb(255,255,255); font: bold; border-radius: 3px; font: 25pt; }")
            elif value == 256:
                self.setStyleSheet("QTile { background: rgb( 236, 204, 97); color: rgb(255,255,255); font: bold; border-radius: 3px; font: 25pt; }")
            elif value == 512:
                self.setStyleSheet("QTile { background: rgb( 237, 200, 79); color: rgb(255,255,255); font: bold; border-radius: 3px; font: 25pt; }")
            elif value == 1024:
                self.setStyleSheet("QTile { background: rgb( 237, 197, 62); color: rgb(255,255,255); font: bold; border-radius: 3px; font: 20pt; }")
            elif value == 2048:
                self.setStyleSheet("QTile { background: rgb( 236, 193, 45); color: rgb(255,255,255); font: bold; border-radius: 3px; font: 20pt; }")




            