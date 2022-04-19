import time
from time import gmtime, strftime
import random
import pyautogui
from pathlib import Path

import Imaging
import Input
import PetMenu

# Configuration
TIME_TILL_START = 4  # Seconds
REPAIR_COUNTER = 10  # Repair after __ throws
REPAIRS = True
KEYBINDINGS = {"fish": "q",
               "petMenu": ["alt", "p"]}
# - - - - - - - - - - - - -

FLAG = "pulled"
COUNTER = 1
IDLETIMER = 0
MAXIDLE = 666

screenWidth, screenHeight = pyautogui.size()
base_path = Path(__file__).parent
CaughtFish_IconPath = str(
    (base_path / "../Resources/fishing_icon.png").resolve())
CaughtFish_Icon = Imaging.imageToFind(CaughtFish_IconPath)


def ActivateFloatFishing():
    key = KEYBINDINGS["fish"]
    Input.pressKeys(key)


def castFishingRod():
    print(strftime("%H:%M:%S", gmtime()),
          f"Casting fishing rod. Counter: {COUNTER}")

    ActivateFloatFishing()
    rodThrown()
    time.sleep(random.uniform(4.5, 6.5))


def rodThrown():
    global FLAG, COUNTER
    COUNTER += 1
    FLAG = "thrown"


def rodPulled():
    global FLAG, IDLETIMER
    IDLETIMER = 0
    FLAG = "pulled"


def pullFishingRod():
    print(strftime("%H:%M:%S", gmtime()),
          f"Detected catch! Reeling in lure nr {COUNTER - 1}")

    ActivateFloatFishing()
    rodPulled()
    time.sleep(random.uniform(6, 7.5))


repairNotification = f"Automatic repair every {REPAIR_COUNTER} casts" if REPAIRS else "Automatic repairs are disabled"
launchMessage = f"Starting the bot in {TIME_TILL_START} seconds! {repairNotification}."
print(strftime("%H:%M:%S", gmtime()), launchMessage)

time.sleep(TIME_TILL_START)
print(strftime("%H:%M:%S", gmtime()), "Started!")

while True:
    if IDLETIMER == MAXIDLE:
        # By this time rod should be automatically pulled
        print(f"Idle timer reached 500. Recasting now.")
        rodPulled()

    if FLAG == "pulled":
        if REPAIRS and (COUNTER % REPAIR_COUNTER == 0):
            print(strftime("%H:%M:%S", gmtime()),
                  f"Counter: {COUNTER}. Repairing now. flag: {FLAG}")
            PetMenu.repairTools(KEYBINDINGS["petMenu"])
        castFishingRod()
    else:
        print(strftime("%H:%M:%S", gmtime()),
              f"Waiting for a fish. Idle timer: {IDLETIMER}. Recast at {MAXIDLE}. flag: {FLAG}")

    # Taking a screenshot
    screenshotOfCenter = Imaging.screenshot(
        {"x": screenWidth/2 - 32, "y": screenHeight/2 - 100}, {"x": 64, "y": 128})

    # Deciding wether to pull or not
    imgSearch = Imaging.ImageSearch(CaughtFish_Icon, screenshotOfCenter)
    if imgSearch.isThereAMatch():
        pullFishingRod()

    IDLETIMER += 1
