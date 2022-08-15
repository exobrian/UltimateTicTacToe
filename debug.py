class debug:
    def hello():
        print("Hello!")

    #Draw a player onto the screen at a given location
    def draw(screen, player, pos_x, pos_y):
        screen.blit(player.get_icon(), (pos_x, pos_y))