import cv2 as cv
import numpy as np
import os
import time

class Settings():
    def __init__(self):
        # get templates
        self.img_dir = "images/"
        self.temp_names = []
        self.monitor = {"top": 0, "left": 0, "width": 2560, "height": 1440}
        self.mode = 0
        self.new_monitor = {}
        
    def get_templates(self):
        for f in os.listdir(self.img_dir):
            self.temp_names.append(f)