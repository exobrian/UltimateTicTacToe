from config import *
from player import *
from game import *
import sys

class Board:
    #Class for Smaller 3x3 square tic tac toe board
    global winner
    winner = None

    def __init__(self):
        self.board = [[None]*3, [None]*3, [None]*3]

    def update_board(self, inner_move_row, inner_move_col, player_type):
        #Note: Due to board being a list of lists, the row and columns have been transposed. What comes in as row is now col.
        index1 = int(inner_move_col / icon_size[0]) #index for col of inner square: inner_move_row is the x coordinate of space
        index2 = int(inner_move_row / icon_size[0]) #index for row of inner square: inner_move_col is the y coordinate of space
        if self.board[index1][index2] is None:
            self.board[index1][index2] = player_type
            return True
        else:
            return False

    def win_check_board(self, player, screen, inner_square_index):
        #Pygame drawing: first coordinate to second.
        global winner
        #Check rows for winner
        for row in range(0,3):
            if (self.board[row][0] == self.board[row][1]== self.board[row][2]) and (self.board[row][0] is not None):
                draw_x_from = inner_square_index[0]*square_width*3
                draw_x_to = square_width*3 + inner_square_index[0]*square_width*3
                draw_y_from = inner_square_index[1]*square_width*3 + row*square_width + square_width/2
                draw_y_to = inner_square_index[1]*square_width*3 + row*square_width + square_width/2
                print(str(draw_x_from) + ", " + str(draw_y_from) + " to " + str(draw_x_to) + ", " + str(draw_y_to))

                pygame.draw.line(screen, line_color_win, (draw_x_from, draw_y_from), (draw_x_to, draw_y_to), width=line_width_win)
                winner = player.type.upper()
                print("PLAYER " + winner + " IS THE WINNER!")
                #sys.exit()
                break
        #Check cols for winner
        for col in range(0,3):
            if (self.board[0][col] == self.board[1][col]== self.board[2][col]) and (self.board[0][col] is not None):
                draw_x_from = inner_square_index[0]*square_width*3 + col*square_width + square_width/2
                draw_x_to = inner_square_index[0]*square_width*3 + col*square_width + square_width/2
                draw_y_from = inner_square_index[1]*square_width*3
                draw_y_to = inner_square_index[1]*square_width*3 + square_width*3
                print(str(draw_x_from) + ", " + str(draw_y_from) + " to " + str(draw_x_to) + ", " + str(draw_y_to))

                pygame.draw.line(screen, line_color_win, (draw_x_from, draw_y_from), (draw_x_to, draw_y_to), width=line_width_win)
                winner = player.type.upper()
                print("PLAYER " + winner + " IS THE WINNER!")
                #sys.exit()
                break
        #Check diagonals for winner
        if (((self.board[0][0] == self.board[1][1] == self.board[2][2]) or (self.board[2][0] == self.board[1][1] == self.board[0][2])) and self.board[1][1] is not None):
            winner = player.type.upper()
            print("PLAYER " + winner + " IS THE WINNER!")
            sys.exit()
        if winner is None:
            print("No winner yet")

class GameBoard(Board):
    def __init__(self):   
        #Create nine of smaller 3x3 boards. Each inner square is indexed by its ordinal number.
        #board[column][col]
        self.gameboard = []
        for i in range(0,9):
            temp = Board()
            self.gameboard.append(temp)
    
    def update_game_board(self, inner_square_ordinal, inner_move_row, inner_move_col, player_type):
        inner_board = self.get_board(int(inner_square_ordinal))
        return inner_board.update_board(inner_move_row, inner_move_col, player_type)

    def print_board(self):
        for square in range(0,8):
            print(self.board[square])

    def get_board(self, inner_square_ordinal):
        return self.gameboard[inner_square_ordinal]