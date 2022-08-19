from importlib.machinery import WindowsRegistryFinder
from config import *
from player import *
from game import *
import sys

class GameBoard:
    global winner
    winner = None

    def __init__(self):   
        #Create nine 3x3 boards. Each inner square is indexed by its ordinal number.
        #board[ordinal square][column][row]
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
    
    def update_board(self, inner_square_ordinal, inner_move_row, inner_move_col, player_type, game_board):
        #Note: Due to board being a list of lists, the row and columns have been transposed. What comes in as row is now col.
        index1 = int(inner_square_ordinal)  #index for inner square
        index2 = int(inner_move_col / icon_size[0]) #index for col of inner square: inner_move_row is the x coordinate of space
        index3 = int(inner_move_row / icon_size[0]) #index for row of inner square: inner_move_col is the y coordinate of space
        if game_board.board[index1][index2][index3] is None:
            game_board.board[index1][index2][index3] = player_type
            print(index1, index2, index3)
            Player.switch_player()
            return True
        else:
            return False

    def end_game_check_inner(self, inner_square_ordinal):
        global winner
        #Check rows for winner
        for row in range(0,3):
            if (self.board[inner_square_ordinal][row][0] == self.board[inner_square_ordinal][row][1]== self.board[inner_square_ordinal][row][2]) and (self.board[inner_square_ordinal][row][0] is not None):
                #pygame.draw.line(Game.get_screen(), line_color_win, (0,0), (720,720))
                print("PLAYER " + str(winner) + " IS THE WINNER!")
                sys.exit()
                break
        #Check cols for winner
        for col in range(0,3):
            if (self.board[inner_square_ordinal][0][col] == self.board[inner_square_ordinal][1][col]== self.board[inner_square_ordinal][2][col]) and (self.board[inner_square_ordinal][0][col] is not None):
                #pygame.draw.line(Game.get_screen(), line_color_win, (0,0), (720,720))
                print("PLAYER " + str(winner) + " IS THE WINNER!")
                sys.exit()
                break
        #Check diagonals for winner
        if ((self.board[inner_square_ordinal][0][0] == self.board[inner_square_ordinal][1][1] == self.board[inner_square_ordinal][2][2] or (self.board[inner_square_ordinal][2][0] == self.board[inner_square_ordinal][1][1] == self.board[inner_square_ordinal][0][2])) and self.board[inner_square_ordinal][1][1] is not None):
            #pygame.draw.line(Game.get_screen(), line_color_win, (0,0), (720,720))
            #print("PLAYER " + str(winner) + " IS THE WINNER!")
            sys.exit()
        if winner is None:
            print("No winner yet")

    def print_board(self):
        for square in range(0,8):
            print(self.board[square])
    
    def get_winner():
        global winner
        return winner
