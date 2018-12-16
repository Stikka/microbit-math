from microbit import *
import math

while True:
    x = accelerometer.get_x()
    
    if button_a.is_pressed():
        theta = math.degrees(math.acos(x/1024))
        display.scroll(str(round(theta,1)))
