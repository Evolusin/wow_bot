import numpy as np
import cv2
import mss
import time
from time import perf_counter as T

left  = 0
right = 2
top   = 0
btm   = 2 

def get_screenshot(monitor):
    with mss.mss() as sct:
        # Part of the screen to capture
        

        while "Screen capturing":
            last_time = time.time()

            # Get raw pixels from the screen, save it to a Numpy array
            img = np.array(sct.grab(monitor))

            # # Display the picture
            # cv2.imshow("OpenCV/Numpy normal", img)

            # Display the picture in grayscale
            # cv2.imshow('OpenCV/Numpy grayscale',
            #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

            return img
