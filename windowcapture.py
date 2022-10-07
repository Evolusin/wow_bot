import numpy as np
import cv2
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
