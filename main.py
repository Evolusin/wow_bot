import cv2 as cv
from windowcapture import convert_tuple2dict
from settings import Settings
from bait_analize import BaitAnalizator
import time


config = Settings()
analizator = BaitAnalizator()

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
        analizator.analize_bait(new_dict)
        if elapsed > 15:
            print("Reseting in 3 seconds")
            time.sleep(3)
            config.mode = 0
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
