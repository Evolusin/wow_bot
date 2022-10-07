import numpy as np
import cv2 as cv
import mss
import time
from time import perf_counter as T



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

def record_screen(image):
        cv.imshow('Matches', image)
        return None