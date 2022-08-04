from microbit import *

"""
while True:
    """"""

"""

ball_pos = [2, 0]
bar_pos = [2, 3]    # 
isGameOver = False

while not isGameOver:
    
    # ループ処理の最初に描画してもよい
    
    # set_pixel(x座標, y座標, 明るさ)
    display.clear()
    display.set_pixel(bar_pos[0], 4, 9)
    display.set_pixel(bar_pos[1], 4, 9)
    
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