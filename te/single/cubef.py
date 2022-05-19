from djitellopy import Tello


tello = Tello()
tello.connect()
   
print("Press enter to takeoff")
a=input()
tello.takeoff()
tello.move_forward(50)
tello.move_left(50)
tello.move_back(50)
tello.move_right(50)
tello.move_up(50)
tello.move_forward(50)
tello.move_left(50)
tello.move_back(50)
tello.move_right(50)
tello.move_down(50)
tello.land()
y=str(tello.query_battery())
print("你的電量是"+y)   

    

         
     
    
     
        
        
     
        