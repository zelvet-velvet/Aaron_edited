from djitellopy import Tello


tello = Tello()
tello.connect()
   
print("Press enter to takeoff")
a=input()
tello.takeoff()
tello.move_forward(50)
tello.move_back(50)
tello.move_left(50)
tello.move_right(50)
tello.move_left(50)
tello.rotate_clockwise(360)
tello.rotate_counter_clockwise(360)
tello.move_down(50)
tello.move_up(50)
tello.curve_xyz_speed(0, -20, 0, 100, -50, 0, 15)
tello.curve_xyz_speed(0, 50, 0, -100, 20, 0, 15 )
tello.flip_forward()
tello.flip_back()
tello.land()
y=str(tello.query_battery())
print("你的電量是"+y)   

    

         
     
    
     
        
        
     
        