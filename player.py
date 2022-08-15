import pygame
from config import *

class player:
    def __init__(self, type):
        self.type = type
        self.icon_location = ".\images\icon_" + self.type + ".png"    
        self.icon = pygame.image.load(self.icon_location)

    def get_icon(self):
        return self.icon

    def user_click(self, screen):
        pos_x, pos_y = pygame.mouse.get_pos()        
        #move_location = self.get_square_index(pos_x, pos_y)
        #screen.blit(self.icon, move_location)
        self.draw_move(screen, pos_x, pos_y)

        #Need to check boundaries
        #Can't go past boundaries or else icon will not show
        #Also, realise that each board is the same coordinates except adding (n-1)*240. 
        ##i.e. x axis of first square of board[1,1] is [0,80]. x axis of first square of board[2,1] is [240,320]
    
    def get_square_index(self, pos_x, pos_y):
        #int returned by dividing by scale_factor gives row/column index for inner square        
        inner_square_row = pos_x // scale_factor
        inner_square_col = pos_y // scale_factor
        return inner_square_row, inner_square_col

    def get_move_index(self, pos_x, pos_y):
        inner_move_row = ((pos_x % scale_factor) // (scale_factor / 3)) * (scale_factor / 3)
        inner_move_col = ((pos_y % scale_factor) // (scale_factor / 3)) * (scale_factor / 3)
        return inner_move_row, inner_move_col
    
    def draw_move(self, screen, pos_x, pos_y):
        inner_square_row = self.get_square_index(pos_x,pos_y)[0]*scale_factor
        inner_square_col = self.get_square_index(pos_x,pos_y)[1]*scale_factor

        inner_move_row = ((pos_x % scale_factor) // (scale_factor / 3)) * (scale_factor / 3)
        inner_move_col = ((pos_y % scale_factor) // (scale_factor / 3)) * (scale_factor / 3)

        print(inner_move_row, inner_move_col)
        screen.blit(self.icon, (inner_square_row + inner_move_row, inner_square_col + inner_move_col))