from turtle import pos
import cv2 as cv
import numpy as np
import os
import time
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

monitor_number = 2
detected_screen = {}
monitor = {"top": 0, "left": 0, "width": 2560, "height": 1440, "mon": monitor_number}
# monitor = {"top": 311, 'left': 692, 'width': 2560, 'height': 1440, "mon": monitor_number}
mode = 0
new_monitor = {}

def record_screen(image):
        cv.imshow('Matches', image)
        return None

def get_bait_localization(monitor):
    points = None
    # get an updated image of the game
    screenshot = get_screenshot(monitor)

    # display the processed image
    for f in temp_names:
        vision_limestone = Vision(f'{img_dir}{f}')
        points = vision_limestone.find(screenshot, 0.6, 'rectangles')
        if points:
            detected_screen = points
            # print(type)
            print(f"Detected bait at - {detected_screen}")
            return detected_screen
    # debug the loop rate
    # print('FPS {}'.format(1 / (time() - loop_time)))ł
    # print(points)
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
       

def analize_bait(position):
    img_bait = get_screenshot(position)
    recorded_bait = record_screen(img_bait)

def convert_tuple2dict(tuple):
    left = int(tuple[0])
    top = int(tuple[1])
    width = int(tuple[2])
    height = int(tuple[3])
    created_dict = {"top": top, "left": left, "width": width, "height": height, "mon":monitor_number}
    print(created_dict)
    return created_dict
        
while True:
    if mode == 0:
        zone = get_bait_localization(monitor)
        if zone is not None:
            mode = 1
            cv.destroyAllWindows()

    elif mode == 1:
        new_dict = convert_tuple2dict(zone)
        mode = 2
        # break
        
    elif mode == 2:
        analize_bait(new_dict)
    # if zone:
    #     new_monitor = convert_tuple2dict(zone)
    #     print(new_monitor)
    #     analize_bait(new_monitor)
    if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break
