from microbit import *

"""
while True:
    """"""

"""

ball_pos = [2, 0]
bar_pos = [2, 3]    # 
isGameOver = False
speed = [0, 1]
dt = 1000       #1000ミリ秒[ms] = 1秒

start = running_time()
while not isGameOver:
    
    time = running_time() - start   # ループが始まってからの時間
    # ループ処理の最初に描画してもよい
    
    # set_pixel(x座標, y座標, 明るさ)
    display.clear()
    display.set_pixel(bar_pos[0], 4, 9)
    display.set_pixel(bar_pos[1], 4, 9)
    display.set_pixel(ball_pos[0], ball_pos[1], 9)
    
    
    #if time % dt == 0:
    if time % dt < 2 or time % dt > dt - 2:
        """
        ball_pos の計算処理
        """
        ball_pos[0] += speed[0]
        ball_pos[1] += speed[1]
        
        # ボールの跳ね返りを計算する
        
        """まずはバーとボールの跳ね返り処理"""
        """ ダメなやつ
        if ball_pos[1] == 3 and ball_pos[0] == 3 and bar_pos[1] == 3:
        """
        if ball_pos[1] == 3 and ball_pos[0] == bar_pos[0]:
            speed[1] *= -1
        elif ball_pos[1] == 3 and ball_pos[0] == bar_pos[1]:
            speed[1] *= -1
        elif ball_pos[1] == 0:
            speed[1] *= -1
    
    # ボタンを押すとバーが動く処理を書くよ
    if button_a.was_pressed():
        bar_pos[0] -= 1
        bar_pos[1] -= 1
        # display.set_pixel(bar_pos[0], 4, 9)
        
    elif button_b.was_pressed():
        bar_pos[0] += 1
        bar_pos[1] += 1
    
    # バーが壁にぶつかってもエラーに
    # ならなくさせる処理
    if bar_pos[0] < 0:
        bar_pos[0] = 0
        bar_pos[1] = 1
        
    elif bar_pos[1] > 4:
        bar_pos[0] = 3
        bar_pos[1] = 4
    
    # 全部の計算が終わったあとに描画しても良い
    
display.scroll("Game Over!")