import pyautogui
from PIL.Image import Image
import cv2
import numpy as np
from numpy import ndarray
from CustomTypes import Coord


def imageToFind(location: str):
    return cv2.imread(location, 0)


def screenshot(start: Coord = None, size: Coord = {"x": 64, "y": 64}):
    if start is None:
        return pyautogui.screenshot()

    return pyautogui.screenshot(
        region=(start["x"], start["y"], size["x"], size["y"]))


class ImageSearch:
    def __init__(self, what: ndarray, where: Image):
        self.ConfidenceTreshold = 0.8
        self.PositiveMatches = None

        pixelsNumpy = np.array(where)
        grayscaleImage = cv2.cvtColor(pixelsNumpy, cv2.COLOR_BGR2GRAY)

        self.Matches = cv2.matchTemplate(
            grayscaleImage, what, cv2.TM_CCOEFF_NORMED)

    def changeConfidenceTreshold(self, newTreshold: float):
        self.ConfidenceTreshold = newTreshold
        self.getPositiveMatches(self)

    def getPositiveMatches(self):
        matchLocations = np.where(self.Matches >= self.ConfidenceTreshold)
        self.PositiveMatches = matchLocations

    def isThereAMatch(self):
        if self.PositiveMatches is None:
            self.getPositiveMatches()

        return len(self.PositiveMatches[0]) > 0

    def getCoordOfFirstPositiveMatch(self):
        if self.PositiveMatches is None:
            self.getPositiveMatches()

        if not self.isThereAMatch():
            return False

        return {"y": self.PositiveMatches[0][0],
                "x": self.PositiveMatches[1][0]}


def __Test_ImageMatch():
    pass


if __name__ == "__main__":
    __Test_ImageMatch()
