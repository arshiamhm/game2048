from random import randrange, choice
from typing import List
from tile import Tile
from enum import Enum
import copy

def trace():
  '''Set a tracepoint in PDB that works with Qt'''
  from PyQt5.QtCore import pyqtRemoveInputHook
  pyqtRemoveInputHook()

  import pdb; pdb.set_trace()

class Dir(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3

class Board:
    def __init__(self, grid_size) -> None:
        self._grid_size = grid_size
        self._board = [
            [Tile() for i in range(self._grid_size)] 
            for j in range(self._grid_size)]
        # self._board = [
        #     [Tile(), Tile(), Tile(), Tile()],
        #     [Tile(), Tile(), Tile(), Tile()],
        #     [Tile(2), Tile(), Tile(2), Tile()],
        #     [Tile(1024), Tile(1024), Tile(512), Tile(512)]
        # ]
        self.tile_collision = False
        self.collision_lastround = False
        self.points_lastround = 0
        self.board_init(self._board)

    def get_tile(self, i, j):
        return self._board[i][j]

    #pass by reference
    def board_init(self, board):
        pos = self.free_position()
        board[pos[0]][pos[1]] = Tile(2)
        pos = self.free_position()
        board[pos[0]][pos[1]] = Tile(choice([2, 4]))


    def free_position(self) -> List[int]:
        pos = []
        found = False
        i = randrange(4) 
        j = randrange(4)
        while(not found):
            if self._board[i][j].get_value() is not None:
                i = randrange(4)
                j = randrange(4)
            else:
                found = True

        pos.append(i)
        pos.append(j)

        return pos

    #for debug only
    # def board_print(self):
    #     board = self._board
    #     pboard = [[board[j][i].get_value() for i in range(self._grid_size)] for
    #               j in range(self._grid_size)]
    #     # print(pboard)
    #     s = [[str(e) for e in row] for row in pboard]
    #     lens = [max(map(len, col)) for col in zip(*s)]
    #     fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    #     table = [fmt.format(*row) for row in s]
    #     print('\n'.join(table))
    
    
    def is_diff(self, pre_board):
        # board.board_print()
        for i in range(self._grid_size):
            for j in range(self._grid_size):
                if pre_board._board[i][j].get_value() != self._board[i][j].get_value():
                    return True
        return False
 

    def move(self, direction):
        gridsize = self._grid_size
        pre_board = copy.deepcopy(self)
        self.points_lastround = 0
        self.collision_lastround = False
    
        if direction is Dir.UP:
            for i in range(gridsize):
                for j in range(gridsize):
                    self.move_vertically(i, j, direction)

        if direction is Dir.DOWN:
            for i in range(gridsize-1, -1, -1):
                for j in range(gridsize):
                    self.move_vertically(i, j, direction)

        if direction is Dir.RIGHT:
            for i in range(gridsize):
                for j in range(gridsize-1, -1, -1):
                    self.move_horizontally(i, j, direction)

        if direction is Dir.LEFT:
            for i in range(gridsize):
                for j in range(gridsize):
                    self.move_horizontally(i, j, direction)

        if(self.is_diff(pre_board)):
            pos = self.free_position()
            self._board[pos[0]][pos[1]] = Tile(2)


    def move_vertically(self, i, j, direction):
        board = self._board
        to_move = board[i][j]
        nexti = i
        if direction is Dir.UP:
            nexti -= 1;
        else:
            nexti += 1

        if to_move.get_value() != None:
            self.tile_collision = False
            while self.in_board(nexti, j) and board[nexti][j].get_value() == None:
                if direction is Dir.UP:
                    nexti -= 1;
                else:
                    nexti += 1

            if not self.in_board(nexti, j):
                if direction is Dir.UP:
                    board[0][j].set_value(to_move.get_value())
                else:
                    board[self._grid_size-1][j].set_value(to_move.get_value())
            else:
                #collision
                if to_move.get_value() == board[nexti][j].get_value():
                    self.handle_collison(nexti, j)
                    self.tile_collision = True
                else:
                    if direction is Dir.UP:
                        board[nexti+1][j].set_value(to_move.get_value())
                    else:
                        board[nexti-1][j].set_value(to_move.get_value())
            
            if ((direction is Dir.DOWN and nexti-1 != i) or 
                (direction is Dir.UP and nexti+1 != i) or
                self.tile_collision):
                    board[i][j].set_value(None)
                        
        else:
            return


    def move_horizontally(self, i, j, direction):
        board = self._board
        to_move = board[i][j]
        nextj = j
        if direction is Dir.RIGHT:
            nextj += 1
        else:
            nextj -= 1

        if to_move.get_value() != None:
            self.tile_collision = False
            while self.in_board(i, nextj) and board[i][nextj].get_value() == None:
                if direction is Dir.LEFT:
                    nextj -= 1;
                else:
                    nextj += 1

            if not self.in_board(i, nextj):
                if direction is Dir.LEFT:
                    board[i][0].set_value(to_move.get_value())
                else:
                    board[i][self._grid_size-1].set_value(to_move.get_value())
            else:
                #collision
                if board[i][j].get_value() == board[i][nextj].get_value():
                    self.handle_collison(i, nextj)
                    self.tile_collision = True
                else:
                    if direction is Dir.LEFT:
                        board[i][nextj+1].set_value(board[i][j].get_value())
                    else:
                        board[i][nextj-1].set_value(board[i][j].get_value())
                        
            if ((direction is Dir.LEFT and nextj+1 != j) or 
                (direction is Dir.RIGHT and nextj-1 != j) or
                self.tile_collision):
                    board[i][j].set_value(None)

        else:
            return

    def handle_collison(self, i, j):
        self._board[i][j].update_value()
        self.collision_lastround = True
        self.points_lastround += self._board[i][j].get_value()


    def in_board(self, i, j):
        gridsize = self._grid_size

        check_corners = (
            i >= 0 and j >= 0 and 
            j < gridsize and i < gridsize 
          )
        return check_corners 
    
        
