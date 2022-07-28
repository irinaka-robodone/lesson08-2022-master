from microbit import *
a = 0
b = 1
"""
# ここにレッスン８「ピンポンゲーム」のコードを実装していこう！
# 以下のコードは先生が少し書いた例です
"""
while not button_a.was_pressed():
  pass
display.scroll('Game Start!')
display.show(Image.HAPPY)
IsGameOver = False # ゲームオーバー判定用の真偽値
display.set_pixel(0,4,9 )
display.set_pixel(1, 4, 9)
display.set_pixel(2, 0, 9)
while not IsGameOver: # IsGameOver が True になると while False になってループ終了する
  display.set_pixel(a,4,0 )
  display.set_pixel(b,4,9 )
  sleep(10) # 10ms ごとに画面の描画を更新する
  display.clear() #画面の描画をリセットする
  if button_a.get_presses():
    a+=1
    b += 1
