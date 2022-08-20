#global variables to be shared
is_running = True
current_player = 0

#default icon size
icon_size = (64,64)

#Screen Resolution: main Game will be square, but add more lines for stats/score etc.
height = icon_size[0] * 9
width = icon_size[1] * 9    

#use this to get index of inner square later. Note: assumes width = height.
#divide by 3 because we have a 3x3 grid of smaller tic tac toe squares
scale_factor = width / 3    

#Display set up
background_color_light = (125,125,125)

#Initial line_color
line_color_light = (200,200,200)
line_color_dark = (50,50,50)
line_width = 7

#Game win color
line_color_win = (100,0,0)