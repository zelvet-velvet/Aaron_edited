
from djitellopy import Tello
import keyboard

tello = Tello()
tello.connect()
  
while 6==6:    
     if keyboard.is_pressed("w"):
         tello.move_forward(30)
     elif keyboard.is_pressed('s'):
         tello.move_back(30)
     elif keyboard.is_pressed('a'):
         tello.move_left(30)
     elif keyboard.is_pressed('d'):
         tello.move_right(30)
     elif keyboard.is_pressed('e'):
         tello.rotate_clockwise(30)
     elif keyboard.is_pressed('q'):
         tello.rotate_counter_clockwise(30)
     elif keyboard.is_pressed('r'):
         tello.move_up(30)
     elif keyboard.is_pressed('f'):
         tello.move_down(30)
     elif keyboard.is_pressed('c'):
         tello.land()   
     elif keyboard.is_pressed('enter'):
         tello.takeoff()
     elif keyboard.is_pressed('k'):
         tello.emergency()
     elif keyboard.is_pressed('b'):
         y=str(tello.query_battery())
         print("你的電量是"+y)
     
        
        
     
        