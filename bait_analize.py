import pyautogui
from windowcapture import get_screenshot, record_screen
from settings import Settings
from vision import Vision
import time


class BaitAnalizator:
    def __init__(self):
        config = Settings()
    
    def counter_increase(self):
        config.counter = config.counter + 1
        return None

    def get_bait_localization(self, monitor):
        """
        Tracks whole screen and looks for template match.
        If match is found then it returns it's position
        """
        points = None
        # get an updated image of the game
        screenshot = get_screenshot(monitor)

        # display the processed images
        for f in config.temp_names:
            vision_limestone = Vision(f"{config.img_dir}{f}")
            points = vision_limestone.find(screenshot, 0.7, "rectangles")
            if points:
                print(f"Detected bait at - {points}")
                return points

    def analize_bait(self, position):
        "Tracks bait changes in given screen position"
        img_bait = get_screenshot(position)
        recorded_bait = record_screen(img_bait)
        splashed = self.check_spalsh(recorded_bait)
        if splashed:
            return True
        else:
            return False
    
    def check_spalsh(self, image):
        splashed = False
        white_pixels = (image >= 220).sum()
        if white_pixels > 3:
            print(f"Got splash!")
            splashed = True
            return splashed
        else:
            return splashed

    def click_point(self, x,y):
        pyautogui.moveTo(x,y)
        time.sleep(0.5)
        pyautogui.click(x,y,button='right')
        time.sleep(2)
        pyautogui.moveTo(100,100)
    

config = Settings()
