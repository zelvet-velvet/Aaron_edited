from djitellopy import Tello


tello = Tello()
tello.connect()
   
print("Press enter to takeoff")
a=input()
tello.takeoff()
tello.flip_forward()
tello.flip_forward()
tello.flip_back()
tello.flip_back()
tello.land() 