from djitellopy import Tello


tello = Tello()
tello.connect()
 
y=str(tello.query_battery())
print("你的電量是"+y)  
print("Press enter to takeoff")
a=input()
tello.takeoff()
tello.flip_forward()
tello.flip_forward()
tello.flip_back()
tello.flip_back()
tello.land() 
y=str(tello.query_battery())
print("你的電量是"+y)