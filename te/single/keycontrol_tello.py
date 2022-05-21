
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
global t,l
t=0
l=0
while True:
    try:
        #key = keyboard.waitKey(1) & 0xff
        #keyboard.is_pressed('q')
        if keyboard.is_pressed('x') & 0xff:
            cv2.waitKey(1)
            #self.capture.release()
            Thread(target=land, args=()).start()
            cv2.destroyAllWindows()
            exit(1)
        elif keyboard.is_pressed('w') & 0xff:
            Thread(target=move_forward, args=()).start()
            time.sleep(1)
        elif keyboard.is_pressed('s') & 0xff:
            Thread(target=move_forward, args=()).start()
            time.sleep(1)
        elif keyboard.is_pressed('a') & 0xff:
            Thread(target=move_forward, args=()).start()
            time.sleep(1)
        elif keyboard.is_pressed('d') & 0xff:
            Thread(target=move_forward, args=()).start()
            time.sleep(1)
        elif keyboard.is_pressed('q') & 0xff:
            Thread(target=rotate_clockwise, args=()).start()
            time.sleep(1)
        elif keyboard.is_pressed('e') & 0xff:
            Thread(target=rotate_counter_clockwise, args=()).start()
            time.sleep(1)
        elif keyboard.is_pressed('r') & 0xff:
            Thread(target=move_up, args=()).start()
            time.sleep(1)
        elif keyboard.is_pressed('f') & 0xff:
            Thread(target=move_down, args=()).start()
            time.sleep(1)
        elif keyboard.is_pressed('t') & 0xff:
            if t==0:
                Thread(target=takeoff, args=()).start()
                t=1
                time.sleep(1)
            else:
                time.sleep(1)
                pass
        elif keyboard.is_pressed('l') & 0xff:
            if l==0:
                print("wtf")
                Thread(target=land, args=()).start()
                l=1
                t=0
                time.sleep(1)
            else:
                time.sleep(1)
                pass
    except AttributeError:
        pass
     
        
        
     
        