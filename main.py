import cv2 as cv
from windowcapture import convert_tuple2dict, convert_tuple2dict_position, reset_mode
from settings import Settings
from bait_analize import BaitAnalizator
import time
import pyautogui

def counter_increase():
        config.counter = config.counter + 1


config = Settings()
analizator = BaitAnalizator()
timer = 600
bait_time = time.perf_counter()
time.sleep(2)
bait_second = time.perf_counter()

print("Bot launched")
while True:
    if config.mode == 0:
        zone = analizator.get_bait_localization(config.monitor)
        if zone is not None:
            config.mode = 1
            cv.destroyAllWindows()

    elif config.mode == 1:
        new_dict = convert_tuple2dict(zone)
        tic = time.perf_counter()
        config.mode = 2

    elif config.mode == 2:
        toc = time.perf_counter()
        elapsed = toc - tic
        analize = analizator.analize_bait(new_dict)

        if elapsed > 15 and analize == False:
            elapsed = 0
            config.mode = reset_mode()
        elif analize == True:
            x, y = convert_tuple2dict_position(zone)
            analizator.click_point(x,y)
            print("Got fish!")
            counter_increase()
            print(f"Number of gathered fishes - {config.counter}")
            elapsed = 0
            elapsed_bait = int(bait_second - bait_time)
            left_time = timer - elapsed_bait
            if elapsed_bait > timer:
                print("Aplying lure")
                bait_time = time.perf_counter()
                pyautogui.press("2")
                time.sleep(5)
                bait_second = time.perf_counter()
                print("Done")
            else:
                bait_second = time.perf_counter()
                print(f"Time left to lure - {left_time}")
            config.mode = reset_mode()

            
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        print(f"Number of fish gatherd - {config.counter}")
        break
