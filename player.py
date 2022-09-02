import pygame
import sys
from config import *
from gameboard import *
from game import *

class Player:
    def __init__(self, type):
        self.type = type
        self.icon_location = ".\images\icon_" + self.type + ".png"    
        self.icon_prior_location = ".\images\icon_" + self.type + "_prior.png" 
        self.icon = pygame.image.load(self.icon_location)
        self.icon = pygame.transform.scale(self.icon, icon_size)
        self.icon_prior = pygame.image.load(self.icon_prior_location)
        self.icon_prior = pygame.transform.scale(self.icon_prior, icon_size)
        
        self.prior_location = None

    def get_icon(self):
        return self.icon

    def user_click(self, screen, game_board):
        pos_x, pos_y = pygame.mouse.get_pos()
        self.draw_move(screen, pos_x, pos_y, game_board)
        #Also, realise that each board is the same coordinates except adding (n-1)*240. 
        ##i.e. x axis of first square of board[1,1] is [0,80]. x axis of first square of board[2,1] is [240,320]
    
    def get_square_index(self, pos_x, pos_y):
        #int returned by dividing by scale_factor gives row/column index for inner square        
        inner_square_row = pos_y // scale_factor
        inner_square_col = pos_x // scale_factor
        inner_square_ordinal = inner_square_row * 3 + inner_square_col
        return int(inner_square_row), int(inner_square_col), int(inner_square_ordinal)

    def get_move_index(self, pos_x, pos_y):
        #get coordinates for whatever square player clicks inside of
        #mod to get remainder after dividing by width of inner square
        #int divide to get index for square. Multiply again by square width to convert to pixel coordinate of top left most pixel.
        inner_move_row = ((pos_y % scale_factor) // (square_width)) * (square_width)
        inner_move_col = ((pos_x % scale_factor) // (square_width)) * (square_width)
        return int(inner_move_row), int(inner_move_col)
    
    def is_valid_move(self, pos_x, pos_y, game_board):
        inner_square_index = self.get_square_index(pos_x, pos_y)
        inner_move_index = self.get_move_index(pos_x, pos_y)
        return game_board.update_game_board(inner_square_index[2], inner_move_index[0], inner_move_index[1], self.type)

    def draw_move(self, screen, pos_x, pos_y, game_board):
        global current_board, prior_board, is_running

        #This calculates the index for which inner square the user clicked in by int dividing how many pixels wide each square is
        inner_square_index = self.get_square_index(pos_x, pos_y)    #row, col, ordinal

        #This calculates the index for which square in the inner square the user clicked in by modding the inner square out, then finding
        #which smallest square the remainder falls in. 
        inner_move_index = self.get_move_index(pos_x, pos_y)
        current_board = inner_square_index[2]
        #first move can be anywhere; check if prior move is null first and set equal to pass next logical check
        if prior_board is None:
            prior_board = current_board

        if (current_board == prior_board and game_board.update_game_board(inner_square_index[2], inner_move_index[0], inner_move_index[1], self.type)): 
            #First call update to check if smaller board at inner_square_index[2] space index[0],index[1] is empty. If not, place player type in it.           
            #Then draw the icon on the board by first find the beginning location of the square then offsetting by the inner square location
            
            #change prior move back to black 
            if self.prior_location is not None:
                screen.blit(self.icon, self.prior_location) 
             
            pos_y_new = inner_square_index[0] * scale_factor + inner_move_index[0]
            pos_x_new = inner_square_index[1] * scale_factor + inner_move_index[1]
            self.prior_location = pos_x_new, pos_y_new
            screen.blit(self.icon_prior, (pos_x_new, pos_y_new))    #change new move to highlighted color        
            prior_board = Player.get_inner_square_ordinal(inner_move_index[0], inner_move_index[1])
            if game_board.check_outer_board(inner_square_index[2]):
                inner_board_win_check = game_board.get_board(inner_square_index[2]).win_check_board(self)
                if (inner_board_win_check[0] is not None and inner_board_win_check[1] is not None):
                    game_board.update_outer_board(inner_square_index[2], inner_board_win_check[0])
                    game_board.get_board(inner_square_index[2]).draw_winner_board(screen, inner_square_index, inner_board_win_check[1], inner_board_win_check[2])
            if game_board.outer_board.win_check_board(self)[1] is not None and game_board.outer_board.win_check_board(self)[1] != "Cat's Game":
                print("Player " + str(self.type) + " wins!!")
                self.declare_winner(screen)
                #pygame.quit()
                #sys.exit()
            Player.switch_player()

    @staticmethod
    def get_inner_square_ordinal(row_index, col_index):
        return int(row_index * 3/square_width + col_index/square_width)

    @staticmethod
    def switch_player():
        global current_player
        if current_player == 0:
            current_player = 1
        else:
            current_player = 0

    @staticmethod
    def get_current_player():
        return current_player

    def declare_winner(self, screen):
        game_over_screen_location = ".\images\game_over_screen.png" 
        game_over_screen = pygame.image.load(game_over_screen_location)
        game_over_screen = pygame.transform.scale(game_over_screen, (scale_factor, scale_factor))
        screen.blit(game_over_screen, (width/3, height/3))
        pygame.display.update()