from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.Qt import Qt
from qtile import QTile
from board import Board, Dir
import sys


class QBoard(QMainWindow):
    def __init__(self, parent=None):
        super(QBoard, self).__init__()
        uic.loadUi("untitled.ui", self)
        self.board = Board(4)
        self.score = 0
        
        self.display_board()


    def display_board(self):
        grid_size = self.board._grid_size
        for i in range(grid_size):
            for j in range(grid_size):
                tile = self.board.get_tile(i, j)
                self.gridLayout.addWidget(QTile(self, tile), i, j)


    def qmove(self, direction):
        self.board.move(direction)

        if self.board.collision_lastround:
            self.score += self.board.points_lastround
            self.score_counter.setText(str(self.score))

        
        self.display_board()

                

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.qmove(Dir.LEFT)
        elif event.key() == Qt.Key_Right:
            self.qmove(Dir.RIGHT)
        elif event.key() == Qt.Key_Up:
            self.qmove(Dir.UP)
        elif event.key() == Qt.Key_Down:
            self.qmove(Dir.DOWN)

        
        
            

            

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QBoard()
    window.show()

    sys.exit(app.exec())
