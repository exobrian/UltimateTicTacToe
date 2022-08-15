import pygame
from gameboard import *
from player import *
from debug import *
from game import *


class game:
    def __init__(self):
        self.start()

    def start(self):
        #initialize the game
        pygame.init()

        #Screen Resolution: main game will be square, but add more lines for stats/score etc.
        screen = pygame.display.set_mode((720, 720))
        icon = pygame.image.load(".\images\icon_board.png")

        pygame.display.set_caption("Ultimate Tic Tac Toe")
        pygame.display.set_icon(icon)

        #Instantiating the two players. All assets tied to char 'x' | 'o'.
        player_x = player("x")
        player_o = player("o")


        #Main Game Loop
        is_running = True
        while is_running:
            #Display set up
            screen.fill((125,125,125))    

            for event in pygame.event.get():
                #Check for ending the game
                if event.type == pygame.QUIT:
                    isRunning = False    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    player_o.user_click(screen)            
            #pygame.display.update()