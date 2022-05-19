from djitellopy import Tello


tello = Tello()
tello.connect()
 
y=str(tello.query_battery())
print("你的電量是"+y)  
print("Press enter to takeoff")
a=input()
tello.takeoff()
tello.move_up(30)
tello.flip_forward()
tello.flip_left()
tello.flip_back()
tello.flip_right()
tello.land()
y=str(tello.query_battery())
print("你的電量是"+y) 