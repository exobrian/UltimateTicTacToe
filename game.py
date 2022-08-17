import pygame
from config import *
from gameboard import *
from player import *
from debug import *
from game import *
import sys


class Game:                
    global screen

    #Initialize the Game
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    def __init__(self):
        self.start()

    def initiate_game_window(self):
        icon = pygame.image.load(".\images\icon_board.png")
        pygame.display.set_caption("Ultimate Tic Tac Toe")
        pygame.display.set_icon(icon)
        screen.fill(background_color_light)  
        
        #Drawing GameBoard grid
        #These are for the inner grid lines. We'll use the default initial line color here
        for line_i in [1,2,4,5,7,8]:
            pygame.draw.line(screen, line_color_light, (line_i * width / 9, 0), (line_i * width / 9, height), line_width)        
            pygame.draw.line(screen, line_color_light, (0, line_i * height / 9), (width, line_i * height / 9), line_width)
        #These are for the outer grid lines. We'll use a darker line color here to overlay and
        #differentiate the inner boards.
        for line_i in [3,6]:            
            pygame.draw.line(screen, line_color_dark, (line_i * width / 9, 0), (line_i * width / 9, height), line_width)        
            pygame.draw.line(screen, line_color_dark, (0, line_i * height / 9), (width, line_i * height / 9), line_width)

    def start(self):
        self.initiate_game_window()

        #Instantiating the two players. All assets tied to char 'x' | 'o'.
        players = (Player("x"), Player("o"))
        game_board = GameBoard()
        
        #Main Game Loop
        is_running = True
        while is_running:
            for event in pygame.event.get():
                #Check for ending the Game
                if event.type == pygame.QUIT:
                    is_running = False
                    sys.exit(0)    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    players[Player.get_current_player()].user_click(screen, game_board)
            pygame.display.update()

    def get_screen():
        return screen