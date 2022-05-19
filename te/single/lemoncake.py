from djitellopy import Tello


tello = Tello()
tello.connect()
   
print("Press enter to takeoff")
a=input()
tello.takeoff()
tello.curve_xyz_speed(0, -20, 0, 100, -50, 0, 15)
tello.curve_xyz_speed(0, 50, 0, -100, 20, 0, 15 )
tello.land() 
y=str(tello.query_battery())
print("你的電量是"+y)  