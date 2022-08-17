from config import *
from player import *

class GameBoard:
    def __init__(self):   
        #Create nine 3x3 boards. Each inner square is indexed by its ordinal number.
        #board[ordinal square][row][column]
        self.board = [
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3],
            [[None]*3, [None]*3, [None]*3]
        ]
    
    def update_board(self, inner_square_ordinal, inner_move_row, inner_move_col, player_icon, game_board):
        index1 = int(inner_square_ordinal)
        index2 = int(inner_move_row / icon_size[0])
        index3 = int(inner_move_col / icon_size[0])
        if game_board.board[index1][index2][index3] is None:
            game_board.board[index1][index2][index3] = player_icon
            Player.switch_player()
            return True
        else:
            return False