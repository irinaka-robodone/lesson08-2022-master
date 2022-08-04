from microbit import *

# 配列から線を描画
def display_bar(bar_pos):
    for pos in bar_pos:
        display.set_pixel(pos, 4, 9)
    # display.clear()

# 配列から点を描画
def display_ball(ball_pos):
    display.set_pixel(ball_pos[0], ball_pos[1], 9)

# ボール、バーの初期位置、ボールの速度、スコアなどを初期化した
dt = 1000
bar_pos = [2, 3]
ball_pos = [3, 0]
speed = [0, 1]
IsGameOver = False  # ゲームオーバー判定用のフラグ
score = 0

# どれかのボタンを押すまでゲームを実行しないようにした
while not button_a.was_pressed() and not button_b.was_pressed():
    display.scroll('Press any button', wait=True)
    pass

# ゲーム開始カウントダウンを表示させた
for i in range(3):
    display.show(str(3-i))
    sleep(1000)

start = running_time()
start2 = running_time()
while not IsGameOver:

    time = running_time() - start
    time2 = running_time() - start2

    if time2 > 0 and 9995 < time2 < 10005:
        # およそ10秒間隔でボールの位置の変わる速さを大きくした (再描画の間隔 dt を短くする)
        dt -= 100
        start2 = running_time()

    if dt < 50:
        # 短すぎるとプレイできないので、小さくても間隔は 50 になるようにした
        dt = 50

    if time > 0 and (time % dt < 5 or dt - 5 < time % dt):
        start = running_time()
        
        # ボールとバーが接触したときの跳ね返り処理
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
            speed[0] = -1
            speed[1] = -1

        elif ball_pos[0] == bar_pos[1] and speed[0] > 0 and ball_pos[1] == 3:
            speed[0] = 1
            speed[1] = -1

        elif ball_pos[0] == bar_pos[1] and speed[0] < 0 and ball_pos[1] == 3:
            speed[0] = 0
            speed[1] = -1
            
        # ボールと壁が接触したときの跳ね返り処理
        if ball_pos[0] == 4 and speed[0] > 0:
            speed[0] = -1
        elif ball_pos[0] == 0 and speed[0] < 0:
            speed[0] = 1

        if ball_pos[1] == 0 and speed[1] < 0:
            speed[1] = 1
            
        ball_pos[0] += speed[0]
        ball_pos[1] += speed[1]
        
    # ボールとバーの位置配列をもとにボールとバーを描画
    display_bar(bar_pos)
    display_ball(ball_pos)

    sleep(10)
    display.clear()
    
    # ボタンが押されたらバーが動く処理
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
        
    # ボールが最下段に到達でゲームオーバーフラグを True にしてループを終了した
    if ball_pos[1] == 4:
        IsGameOver = True

display.scroll('Game Over')
