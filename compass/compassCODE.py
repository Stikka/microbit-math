from microbit import *

compass.calibrate() #calibrate magnometer

while True:
    bearing = compass.heading() #gets bearing reading
    
    #following if statements determine whether to show north, south, east or west depending on the bearing reading
    
    if bearing < 45:
        display.show("N")
        
    elif bearing < 135:
        display.show("E")
        
    elif bearing < 225:
        display.show("S")
        
    elif bearing < 315:
        display.show("W")
        
    else:
        display.show("N")
