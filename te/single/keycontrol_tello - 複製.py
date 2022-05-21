
import asyncio
from djitellopy import Tello
import cv2, math, time
import keyboard
from threading import Thread



tello = Tello()
tello.connect()
  #send_rc_control(self, left_right_velocity: int, forward_backward_velocity: int, up_down_velocity: int,yaw_velocity: int):

def takeoff():
    tello.takeoff()
def land():
    tello.land() 
def move_forward():
    tello.send_rc_control(0,20,0,0)
def move_back():
    tello.send_rc_control(0,-20,0,0)
def move_left():
    tello.send_rc_control(20,0,0,0)
def move_right():
    tello.send_rc_control(-20,0,0,0)
def rotate_clockwise():
    tello.send_rc_control(0,0,0,1)
def rotate_counter_clockwise():
    tello.send_rc_control(0,0,0,-1)
def move_up():
    tello.send_rc_control(0,0,20,0)
def move_down():
    tello.send_rc_control(0,0,-20,0)


print("Press enter to start")
a=input()

while True:
    try:
        key = cv2.waitKey(1) & 0xff
        if key == ord('x'):
            #self.capture.release()
            Thread(target=land, args=()).start()
            cv2.destroyAllWindows()
            exit(1)
        elif key == ord('w'):
            Thread(target=move_forward, args=()).start()
        elif key == ord('s'):
            move_back(30)
            Thread(target=move_back, args=()).start()
        elif key == ord('a'):
            move_left(30)
            Thread(target=move_left, args=()).start()
        elif key == ord('d'):
            move_right(30)
            Thread(target=move_right, args=()).start()
        elif key == ord('q'):
            Thread(target=rotate_clockwise, args=()).start()
        elif key == ord('e'):
            Thread(target=rotate_counter_clockwise, args=()).start()
        elif key == ord('r'):
            Thread(target=move_up, args=()).start()
        elif key == ord('f'):
            Thread(target=move_down, args=()).start()
        elif key == ord('t'):
            Thread(target=takeoff, args=()).start()
        elif key == ord('l'):
            Thread(target=land, args=()).start()
    except AttributeError:
        pass
     
        
        
     
        