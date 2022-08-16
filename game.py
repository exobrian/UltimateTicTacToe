import pygame
from config import *
from gameboard import *
from player import *
from debug import *
from game import *


class game:                
    global screen, current_player

    #Initialize the game
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    current_player = 0

    def __init__(self):
        self.start()

    def initiate_game_window(self):
        icon = pygame.image.load(".\images\icon_board.png")
        pygame.display.set_caption("Ultimate Tic Tac Toe")
        pygame.display.set_icon(icon)
        screen.fill(background_color_light)  
        
        #Drawing gameboard grid
        #These are for the inner grid lines. We'll use the default initial line color here
        for line_i in [1,2,4,5,7,8]:
            pygame.draw.line(screen, line_color_light, (line_i * width / 9, 0), (line_i * width / 9, height), 7)        
            pygame.draw.line(screen, line_color_light, (0, line_i * height / 9), (width, line_i * height / 9), 7)
        #These are for the outer grid lines. We'll use a darker line color here to overlay and
        #differentiate the inner boards.
        for line_i in [3,6]:            
            pygame.draw.line(screen, line_color_dark, (line_i * width / 9, 0), (line_i * width / 9, height), 7)        
            pygame.draw.line(screen, line_color_dark, (0, line_i * height / 9), (width, line_i * height / 9), 7)

    def start(self):
        self.initiate_game_window()

        #Instantiating the two players. All assets tied to char 'x' | 'o'.
        players = (player("x"), player("o"))
        
        #Main Game Loop
        is_running = True
        while is_running:
            for event in pygame.event.get():
                #Check for ending the game
                if event.type == pygame.QUIT:
                    is_running = False    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    players[current_player].user_click(screen)
                    game.switch_player()
            pygame.display.update()

    def switch_player():
        global current_player
        if current_player == 0:
            current_player = 1
        else:
            current_player = 0 
    