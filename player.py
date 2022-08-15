import pygame

class player:
    def __init__(self, type):
        self.type = type
        self.icon_location = ".\images\icon_" + self.type + ".png"    
        self.icon = pygame.image.load(self.icon_location)

    def get_icon(self):
        return self.icon

    def user_click(self, screen):
        pos_x, pos_y = pygame.mouse.get_pos()
        screen.blit(self.icon, (pos_x, pos_y))
        print(pos_x, pos_y)
        pygame.display.update()


        #Need to check boundaries
        #Can't go past boundaries or else icon will not show
        #Also, realise that each board is the same coordinates except adding (n-1)*240. 
        ##i.e. x axis of first square of board[1,1] is [0,80]. x axis of first square of board[2,1] is [240,320]
