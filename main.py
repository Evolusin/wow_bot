import cv2 as cv
import numpy as np
import os
from time import time
# from windowcapture import WindowCapture
from windowcapture import get_screenshot
from vision import Vision

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
# wincap = WindowCapture()
# initialize the Vision class
vision_limestone = Vision('wow_bait.png')


loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = get_screenshot()

    # display the processed image
    points = vision_limestone.find(screenshot, 0.5, 'rectangles')
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

    # debug the loop rate
    # print('FPS {}'.format(1 / (time() - loop_time)))

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

# screenshot = get_screenshot()
# cv.imshow('t',screenshot)
# cv.waitKey()
# points = vision_limestone.find(screenshot, 0.5, debug_mode='rectangles')
# cv.imshow('t',points)
