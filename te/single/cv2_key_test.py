import asyncio
from djitellopy import Tello
import cv2, math, time
import keyboard
from threading import Thread
import numpy as np


# Load an color image in grayscale
img = cv2.imread('030..jpg')
WINDOW_NAME = 'Image de Lena'
cv2.imshow(WINDOW_NAME,img)

while True:
    try:
        key = cv2.waitKey(100)&0xff
        
        print(key)
        if key == ord('x'):
            print("x")
            break
        elif key == ord('w'):
            print("w")
            break
        elif key == ord('s'):
            print("s")
            break
        elif key == ord('a'):
            print("a")
            break
        elif key == ord('d'):
            print("d")
            break
        elif key == ord('q'):
            print("q")
            break
        elif key == ord('e'):
            print("e")
            break
        elif key == ord('r'):
            print("r")
            break
        elif key == ord('f'):
            print("f")
            break
        elif key == ord('t'):
            print("t")
            break
        elif key == ord('l'):
            cv2.destroyAllWindows()
            exit(1)
            break
    except AttributeError:
        pass
     








