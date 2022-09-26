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
for f in os.listdir(img_dir):
    temp_names.append(f)
    # templates.append(cv.imread(f"{img_dir}/{f}".format(f),0))

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = get_screenshot()

    # display the processed image
    for f in temp_names:
        vision_limestone = Vision(f'{img_dir}{f}')
        points = vision_limestone.find(screenshot, 0.7, 'rectangles')
    # debug the loop rate
    # print('FPS {}'.format(1 / (time() - loop_time)))

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

