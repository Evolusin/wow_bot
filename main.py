import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import get_screenshot
from vision import Vision


# initialize the Vision class


# get templates
img_dir = "images/"

temp_names = []

def get_templates(img_dir,temp_names):
    for f in os.listdir(img_dir):
        temp_names.append(f)
get_templates(img_dir,temp_names)

loop_time = time()
detected_screen = {}
monitor = {"top": 100, "left": 100, "width": 1700, "height": 800}

def loop(monitor):
    while(True):

        # get an updated image of the game
        screenshot = get_screenshot(monitor)

        # display the processed image
        for f in temp_names:
            vision_limestone = Vision(f'{img_dir}{f}')
            points = vision_limestone.find(screenshot, 0.6, 'rectangles')
            if points:
                detected_screen = points
                print(detected_screen)
        # debug the loop rate
        # print('FPS {}'.format(1 / (time() - loop_time)))
        # print(points)
        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


if detected_screen:
    print("Nie pusta")
else:
    loop(monitor)