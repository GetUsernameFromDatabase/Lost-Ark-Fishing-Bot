# Python Built-in import
import random
import time
from pathlib import Path
# External import
import pyautogui
from PIL.Image import Image
# Project import
import Imaging
import Input
from Counter import Counter
from Notifications import xprint


# https://stackoverflow.com/questions/46757958/how-to-create-a-return-flag-object


class __HomeFlag(object):
    """
    Indicates that fishing rod has not been cast\ 
    (It is not in the water)
    """

    def __repr__(self):
        return 'home'


class __CastFlag(object):
    """
    Indicates that fishing rod has been cast\ 
    (It is in the water)
    """

    def __repr__(self):
        return 'cast'


HOME = object.__new__(__HomeFlag)
CAST = object.__new__(__CastFlag)
STATUS = HOME

CAST_COUNTER = Counter(1)
WAIT_COUNTER = Counter(maxValue=700)

screenWidth, screenHeight = pyautogui.size()
base_path = Path(__file__).parent
CaughtFish_IconPath = str(
    (base_path / "../Resources/fishing_icon.png").resolve())
CaughtFish_Icon = Imaging.imageToFind(CaughtFish_IconPath)


def searchForCatch(huntingGrounds: Image):
    return Imaging.ImageSearch(CaughtFish_Icon, huntingGrounds)


def activateFloatFishing():
    Input.pressKeys(Input.KEYBINDINGS["fish"])


def castFishingRod():
    xprint(f"Casting fishing rod. Counter: {CAST_COUNTER.count}")

    activateFloatFishing()
    rodThrown()
    time.sleep(6)


def rodThrown():
    global STATUS
    STATUS = CAST
    CAST_COUNTER.increase()


def rodPulled():
    global STATUS
    STATUS = HOME
    WAIT_COUNTER.reset()


def pullFishingRod():
    xprint(f"Detected catch! Reeling in lure nr {CAST_COUNTER.count - 1}")

    activateFloatFishing()
    rodPulled()
    time.sleep(random.uniform(6, 7.5))
