from windowcapture import get_screenshot, record_screen
from settings import Settings
from vision import Vision


class BaitAnalizator:
    def __init__(self):
        config = Settings()

    def get_bait_localization(self, monitor):
        """
        Tracks whole screen and looks for template match.
        If match is found then it returns it's position
        """
        points = None
        # get an updated image of the game
        screenshot = get_screenshot(monitor)

        # display the processed image
        for f in config.temp_names:
            vision_limestone = Vision(f"{config.img_dir}{f}")
            points = vision_limestone.find(screenshot, 0.6, "rectangles")
            if points:
                print(f"Detected bait at - {points}")
                return points

    def analize_bait(self, position):
        "Tracks bait changes in given screen position"
        img_bait = get_screenshot(position)
        recorded_bait = record_screen(img_bait)


config = Settings()
