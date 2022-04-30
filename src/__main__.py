# Python Built-in import
from time import sleep
# Project import
import Input
import Imaging
import PetMenu
import Fishing
import Notifications as Notifs
from Notifications import xprint
from Configuration import TIME_TILL_START, REPAIR_DIVIDER


if __name__ != "__main__":
    raise RuntimeError("This is not meant to be imported")

scrWidth, scrHeight = Input.SCREEN_WIDTH, Input.SCREEN_HEIGHT

Notifs.initializingBot(TIME_TILL_START, REPAIR_DIVIDER)
sleep(TIME_TILL_START)
Notifs.botInitialized()

idles = Fishing.WAIT_COUNTER
casts = Fishing.CAST_COUNTER
maxIdleReached = False
while True:
    if Fishing.STATUS == Fishing.HOME:
        # +1 so it would be after the Xth cast not before
        if (REPAIR_DIVIDER != 0) and ((casts.count + 1) % REPAIR_DIVIDER == 0):
            xprint(Notifs.PetMenu.Repairs.repairsStarted(casts.count),
                   Notifs.showFlag(Fishing.STATUS))
            PetMenu.repairTools()
        Fishing.castFishingRod()
        continue
    elif maxIdleReached:
        # By this time rod should be automatically pulled
        Notifs.Fishing.maxIdleReached(idles.maxValue)
        Fishing.rodPulled()
    else:
        xprint(Notifs.Fishing.waiting(),
               Notifs.Fishing.idleStatus(idles.count, idles.maxValue),
               Notifs.showFlag(Fishing.STATUS))

    # Taking a screenshot
    screenshotOfCenter = Imaging.screenshot(
        {"x": scrWidth/2 - 32, "y": scrHeight/2 - 100},
        {"x": 64, "y": 128})

    # Deciding wether to pull or not
    imgSearch = Fishing.searchForCatch(screenshotOfCenter)
    if imgSearch.isThereAMatch():
        Fishing.pullFishingRod()

    maxIdleReached = idles.increase()
