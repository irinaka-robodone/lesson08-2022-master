from microbit import *


def display_bar(bar_pos):
    for pos in bar_pos:
        display.set_pixel(pos, 4, 9)
    # display.clear()


def display_ball(ball_pos):
    display.set_pixel(ball_pos[0], ball_pos[1], 9)


dt = 1000
bar_pos = [2, 3]
ball_pos = [3, 0]
speed = [0, 1]
IsGameOver = False
score = 0

while not button_a.was_pressed() and not button_b.was_pressed():
    display.scroll('Press any button', wait=False)
    pass

for i in range(3):
    display.show(str(3-i))
    sleep(1000)

start = running_time()
while not IsGameOver:
    time = running_time() - start

    if time > 0 and time % 10000 == 0:
        dt -= 10

    if dt < 100:
        dt = 100

    if time % dt == 0:
        ball_pos[0] += speed[0]
        ball_pos[1] += speed[1]

        if ball_pos[0] == bar_pos[0] and speed[0] == 0 and ball_pos[1] == 3:
            speed[0] = -1
            speed[1] = -1

        elif ball_pos[0] == bar_pos[1] and speed[0] == 0 and ball_pos[1] == 3:
            speed[0] = 1
            speed[1] = -1

        elif ball_pos[0] == bar_pos[0] and speed[0] > 0 and ball_pos[1] == 3:
            speed[0] = 0
            speed[1] = -1

        elif ball_pos[0] == bar_pos[0] and speed[0] < 0 and ball_pos[1] == 3:
            speed[0] *= -1
            speed[1] = -1

        elif ball_pos[0] == bar_pos[1] and speed[0] > 0 and ball_pos[1] == 3:
            speed[0] *= -1
            speed[1] = -1

        elif ball_pos[0] == bar_pos[1] and speed[0] < 0 and ball_pos[1] == 3:
            speed[0] = 0
            speed[1] = -1

        if ball_pos[0] == 4 and speed[0] > 0:
            speed[0] = -1
        elif ball_pos[0] == 0 and speed[0] < 0:
            speed[0] = 1

        if ball_pos[1] == 0 and speed[1] < 0:
            speed[1] = 1

    display_bar(bar_pos)
    display_ball(ball_pos)

    sleep(10)
    display.clear()

    if button_a.was_pressed():
        bar_pos[0] -= 1
        bar_pos[1] -= 1
    elif button_b.was_pressed():
        bar_pos[0] += 1
        bar_pos[1] += 1

    if bar_pos[0] < 0:
        bar_pos[0] = 0
        bar_pos[1] = 1
    elif bar_pos[1] > 4:
        bar_pos[0] = 3
        bar_pos[1] = 4

    # if running_time() % dt == 0:
    #   ball_pos[0] += speed[0]
    #   ball_pos[1] += speed[1]

    if ball_pos[1] == 4:
        IsGameOver = True

display.scroll('Game Over')
