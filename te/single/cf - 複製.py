import asyncio
from djitellopy import Tello
import cv2, math, time
import keyboard




tello = Tello()
tello.connect()
  #send_rc_control(self, left_right_velocity: int, forward_backward_velocity: int, up_down_velocity: int,yaw_velocity: int):
async def move_forward():
    await tello.send_rc_control(0,20,0,0)
async def move_back():
    await tello.send_rc_control(0,-20,0,0)
async def move_left():
    await tello.send_rc_control(20,0,0,0)
async def move_right():
    await tello.send_rc_control(-20,0,0,0)
async def rotate_clockwise():
    await tello.send_rc_control(0,0,0,1)
async def rotate_counter_clockwise():
    await tello.send_rc_control(0,0,0,-1)
async def move_up():
    await tello.send_rc_control(0,0,20,0)
async def move_down():
    await tello.send_rc_control(0,0,-20,0)
def takeoff():
    tello.takeoff()
def land():
    tello.land() 

print("Press enter to start")
a=input()
while True:

    try:
        print("ahoy")
        key = keyboard.waitKey(1) & 0xff
        if key == ord('x'):
            cv2.waitKey(1)
            #self.capture.release()
            Thread(target=land, args=()).start()
            cv2.destroyAllWindows()
            exit(1)
        elif key == ord('w'):
            Thread(target=move_forward, args=()).start()
        elif key == ord('s'):
            move_back(30)
            Thread(target=move_forward, args=()).start()
        elif key == ord('a'):
            move_left(30)
            Thread(target=move_forward, args=()).start()
        elif key == ord('d'):
            move_right(30)
            Thread(target=move_forward, args=()).start()
        elif key == ord('q'):
            Thread(target=rotate_clockwise, args=()).start()
        elif key == ord('e'):
            Thread(target=rotate_counter_clockwise, args=()).start()
        elif key == ord('r'):
            Thread(target=move_up, args=()).start()
        elif key == ord('f'):
            Thread(target=move_down, args=()).start()
        elif key == ord('t'):
            print("wtf")
            Thread(target=takeoff, args=()).start()
        elif key == ord('l'):
            Thread(target=land, args=()).start()
    except AttributeError:
        pass
     
        
        
     
        