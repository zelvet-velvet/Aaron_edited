from djitellopy import Tello
import keyboard
tello = Tello()
tello.connect()
while True:
    if keyboard.read_key() == "w":
        tello.move_forward(30)
        break

while True:
    if keyboard.is_pressed("enter"):
        tello.takeoff()
        break
    
while True:
    if keyboard.is_pressed("esc"):
        tello.land()
        break        
