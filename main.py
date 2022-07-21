from microbit import *
#def baa(a,b):
    #display.set_pixel(a,4,9) 
    #display.set_pixel(b,4,9)
BAA = Image("00000:""00000:""00000:""00000:""09900")

while not if button_a.was_pressed() or button_b.was_pressed():
    display.scroll("BOTAN　OSHITE")
display.set_pixer(3,3,9)
display.show(BAA)
sleep(1000)

while True:
    display.show(BAA)
    if button_a.was_pressed():
        display.show(BAA.shift_left(1))
    elif button_b.was_pressed():
        display.show(BAA.shift_right(1))
    
    
    
    
    