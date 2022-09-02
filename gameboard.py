from asyncio import windows_utils
from config import *
from player import *
from game import *
import sys

class Board:
    #Class for Smaller 3x3 square tic tac toe board
    #winner variable to track winner for each small board
    
    def __init__(self):
        self.board = [[None]*3, [None]*3, [None]*3]
        self.winner = None

    def update_board(self, inner_move_row, inner_move_col, player_type):
        row = int(inner_move_row / square_width) #index for col of inner square: inner_move_row is the y coordinate of space
        col = int(inner_move_col / square_width) #index for row of inner square: inner_move_col is the x coordinate of space
        if self.board[row][col] is None:
            self.board[row][col] = player_type
            return True
        else:
            return False

    def win_check_board(self, player):

        win_type = None
        win_index = None

        #Need to make sure there's not already a winner before each loop. Otherwise there'd be redundant checks
        #index[0] = row
        #index[1] = col

        #Check rows for winner
        if (self.winner is None):
            for row in range(0,3):
                if (self.board[row][0] == self.board[row][1]== self.board[row][2]) and (self.board[row][0] is not None):
                    self.winner = player.type.upper()
                    win_type = 'horizontal'
                    win_index = row
                    break
        #Check cols for winner
        if (self.winner is None):
            for col in range(0,3):
                if (self.board[0][col] == self.board[1][col]== self.board[2][col]) and (self.board[0][col] is not None):
                    self.winner = player.type.upper()
                    win_type = 'vertical'
                    win_index = col
                    break
        #Check diagonals for winner
        if (self.winner is None):
            if self.board[1][1] is not None:
                if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                    self.winner = player.type.upper()
                    win_type = 'diagonal_topleft_to_bottomright'
                elif self.board[2][0] == self.board[1][1] == self.board[0][2]:
                    self.winner = player.type.upper()
                    win_type = 'diagonal_topright_to_bottomleft'
        #If still no winner, check for cat's game. Mark outer board as winner = NA.
        if (self.winner is None):
            count = 0
            for row in range(0,3):
                for col in range(0,3):
                    if (self.board[row][col] is None):
                        break
                    count += 1
            if count == 9:
                self.winner = "NA"
                win_type = "Cat's Game"
        return self.winner, win_type, win_index

    def print_board(self):
        for row in range(0,3):
            print(self.board[row])

    def draw_winner_board(self, screen, inner_square_index, win_type, win_index):
        match win_type:
            case 'horizontal':
                draw_x_from = inner_square_index[1]*square_width*3
                draw_x_to = inner_square_index[1]*square_width*3 + square_width*3
                draw_y_from = inner_square_index[0]*square_width*3 + win_index*square_width + square_width/2
                draw_y_to = inner_square_index[0]*square_width*3 + win_index*square_width + square_width/2
            case 'vertical':
                draw_x_from = inner_square_index[1]*square_width*3 + win_index*square_width + square_width/2
                draw_x_to = inner_square_index[1]*square_width*3 + win_index*square_width + square_width/2
                draw_y_from = inner_square_index[0]*square_width*3
                draw_y_to = inner_square_index[0]*square_width*3 + square_width*3
            case 'diagonal_topleft_to_bottomright':
                draw_y_from = inner_square_index[0]*square_width*3
                draw_y_to = inner_square_index[0]*square_width*3 + square_width*3
                draw_x_from = inner_square_index[1]*square_width*3
                draw_x_to = inner_square_index[1]*square_width*3 + square_width*3
            case 'diagonal_topright_to_bottomleft':
                draw_y_from = inner_square_index[0]*square_width*3 + square_width*3
                draw_y_to = inner_square_index[0]*square_width*3
                draw_x_from = inner_square_index[1]*square_width*3
                draw_x_to = inner_square_index[1]*square_width*3 + square_width*3
            case _:
                return
        pygame.draw.line(screen, line_color_win[Player.get_current_player()], (draw_x_from, draw_y_from), (draw_x_to, draw_y_to), width=line_width_win)
        
class GameBoard(Board):

    def __init__(self):   
        #Create nine of smaller 3x3 boards. Each inner square is indexed by its ordinal number.
        #board[column][col]
        self.outer_board = Board()
        self.gameboard = []
        self.ultimate_winner = None

        for i in range(0,9):
            temp = Board()
            self.gameboard.append(temp)

    def update_game_board(self, inner_square_ordinal, inner_move_row, inner_move_col, player_type):
        inner_board = self.get_board(inner_square_ordinal)
        return inner_board.update_board(inner_move_row, inner_move_col, player_type)

    def check_outer_board(self, inner_square_ordinal):
        row_index = int(inner_square_ordinal // 3)
        col_index = int(inner_square_ordinal % 3)
        if self.outer_board.board[row_index][col_index] is not None:
            return False
        else:
            return True

    def update_outer_board(self, inner_square_ordinal, winning_player):
        row_index = int(inner_square_ordinal // 3)
        col_index = int(inner_square_ordinal % 3)
        self.outer_board.board[row_index][col_index] = winning_player

    def get_board(self, inner_square_ordinal):
        return self.gameboard[inner_square_ordinal]
    
    def check_outer_board_open(self):
        count = 0
        for row in range(0,3):
            for col in range(0,3):
                if self.outer_board.board[row][col] is None:
                    return True
                else:
                    count += 1
        if count == 9:
            return False