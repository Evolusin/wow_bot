import cv2 as cv
import numpy as np
from windowcapture import get_screenshot, convert_tuple2dict
from vision import Vision
from settings import Settings
from bait_analize import analize_bait


config = Settings()
config.get_templates()

def get_bait_localization(monitor):
    points = None
    # get an updated image of the game
    screenshot = get_screenshot(monitor)

    # display the processed image
    for f in config.temp_names:
        vision_limestone = Vision(f'{config.img_dir}{f}')
        points = vision_limestone.find(screenshot, 0.6, 'rectangles')
        if points:
            print(f"Detected bait at - {points}")
            return points

        
while True:
    if config.mode == 0:
        zone = get_bait_localization(config.monitor)
        if zone is not None:
            config.mode = 1
            cv.destroyAllWindows()

    elif config.mode == 1:
        new_dict = convert_tuple2dict(zone)
        config.mode = 2

    elif config.mode == 2:
        analize_bait(new_dict)

    if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break
