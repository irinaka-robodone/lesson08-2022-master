from microbit import *

while not button_a.was_pressed():
    pass
display.scroll('Are You Ready?')

while not button_a.was_pressed():
    pass
display.scroll('Game Start!')

def display_bar(bar_pos):
    for pos in bar_pos:
        display.set_pixel(pos, 4, 9)
    # display.clear()

def display_ball(ball_pos):
    display.set_pixel(ball_pos[0], ball_pos[1], 9)

dt = 10
bar_pos = [2, 3]
ball_pos = [3, 0]
IsGameOver = False

while not IsGameOver:
    
    display_bar(bar_pos)
    display_ball(ball_pos)
    
    sleep(10)
    display.clear()