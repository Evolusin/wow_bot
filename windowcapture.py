import numpy as np
import cv2 as cv
import mss
import time
import pyautogui


def get_screenshot(monitor):
    with mss.mss() as sct:
        # Part of the screen to capture
        while "Screen capturing":
            # Get raw pixels from the screen, save it to a Numpy array
            img = np.array(sct.grab(monitor))
            return img


def convert_tuple2dict(tuple):
    left = int(tuple[0])
    top = int(tuple[1])
    width = int(tuple[2])
    height = int(tuple[3])
    created_dict = {"top": top, "left": left, "width": width, "height": height}
    return created_dict

def convert_tuple2dict_position(tuple):
    x = int(tuple[0]) 
    y = int(tuple[1])
    width = int(tuple[2])
    height = int(tuple[3])
    x = x + (width/2)
    y = y + (height/2)
    return x,y


def record_screen(image):
    image = cv.cvtColor(np.array(image),cv.COLOR_BGRA2GRAY)
    cv.imshow("Matches", image)
    return image

def reset_mode():
    print("Reseting in 3 seconds")
    time.sleep(1)
    print("Reseting in 2 seconds")
    time.sleep(1)
    print("Reseting in 1 seconds")
    time.sleep(1.5)
    cv.destroyAllWindows()
    mode = 0
    pyautogui.press('1')
    print("Throwing fishing pole")
    return mode

