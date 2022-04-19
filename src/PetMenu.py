from typing import Union
import pyautogui
import time
import random
from time import gmtime, strftime

import Input
import Imaging

ESCAPE_KEY = "esc"
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
MENU_DEPTH = 0

OriginalMouseLocation = pyautogui.position()


def openPetMenu(keys: Union[list, str]):
    global MENU_DEPTH
    keyBinds_HumanReadable = " + ".join(keys).upper()
    notification = f"Opening pet inventory ({keyBinds_HumanReadable})."
    print(strftime("%H:%M:%S", gmtime()), notification)

    MENU_DEPTH += 1
    Input.pressKeys(keys)
    time.sleep(random.uniform(1.0, 2.5))


def exitFromPetMenu():
    global MENU_DEPTH

    while True:
        if MENU_DEPTH < 1:
            return
        Input.pressKeys(ESCAPE_KEY)
        time.sleep(random.uniform(0.5, 1.5))
        MENU_DEPTH -= 1


def returnMouse():
    pyautogui.moveTo(OriginalMouseLocation.x,
                     OriginalMouseLocation.y,
                     random.uniform(1.0, 2.0))


class PetSubMenu:
    def preparingToOpenSubmenu(self, submenuName):
        global OriginalMouseLocation
        OriginalMouseLocation = pyautogui.position()

        print(strftime("%H:%M:%S", gmtime()),
              f"Clicking on Pet Function: {submenuName}.")
        # To reduce possible interference from tooltips
        pyautogui.moveTo(SCREEN_WIDTH/2, 0, 0.3)
        time.sleep(0.5)

    def subMenuOpened(self):
        global MENU_DEPTH
        MENU_DEPTH += 1
        time.sleep(random.uniform(0.5, 1.5))

    def subMenuClosed(self):
        global MENU_DEPTH
        MENU_DEPTH -= 1
        returnMouse()

    def closeSubMenu(self):
        Input.pressKeys(ESCAPE_KEY)
        self.subMenuClosed()


class __ToolRepair(PetSubMenu):
    def __init__(self, ratio=16/9):
        super().__init__()

        self.Icon = Imaging.imageToFind('Resources/repairTools_icon.png')
        self.IconSize = {"width": len(self.Icon[0]),
                         "height": len(self.Icon)}

        availableRatios = [16/9]
        if ratio not in availableRatios:
            raise ValueError("Sorry, your ratio is unavailable")

        RepairAll_Offsets = {16/9: {"x": 0.384, "y": 0.688}}
        ConfirmRepair_Offsets = {16/9: {"x": 0.457, "y": 0.578}}

        self.Offsets = {
            "repairAll": RepairAll_Offsets[ratio],
            "confirm": ConfirmRepair_Offsets[ratio]
        }

    def openSubmenu(self):
        self.preparingToOpenSubmenu("remote repair")

        screenshot = Imaging.screenshot()
        imgSearch = Imaging.ImageSearch(self.Icon, screenshot)
        coord = imgSearch.getCoordOfFirstPositiveMatch()
        if coord == False:
            print(strftime("%H:%M:%S", gmtime()),
                  "Failed to open tool repair. Exiting from pet menu")
            exitFromPetMenu()
            return

        Input.clickOnScreen({"x": coord["x"] + self.IconSize["width"] / 2,
                             "y": coord["y"] + self.IconSize["height"] / 2})
        self.subMenuOpened()

    def repairAll_ButtonPress(self):
        print(strftime("%H:%M:%S", gmtime()), "Clicking on Repair All button.")
        Input.clickRelativeToScreen(self.Offsets["repairAll"])

    def confirmRepair_ButtonPress(self):
        # Repair OK offset
        print(strftime("%H:%M:%S", gmtime()), "Clicking on OK button.")
        Input.clickRelativeToScreen(self.Offsets["confirm"])

    def repair(self):
        self.repairAll_ButtonPress()
        self.confirmRepair_ButtonPress()
        self.closeSubMenu()


def repairTools(openPetMenu_Keybinding: Union[list, str]):
    # Development: get current mouse position
    pyautogui.position()

    openPetMenu(openPetMenu_Keybinding)
    toolRepair = __ToolRepair()
    toolRepair.openSubmenu()
    toolRepair.repair()

    # Exiting from Pet Menu
    time.sleep(random.uniform(0.25, 3))
    print(strftime("%H:%M:%S", gmtime()), "Closing the Pet Window.")
    exitFromPetMenu()


def __repairTools_TEST():
    openPetMenu(["alt", "p"])
    toolRepair = __ToolRepair()
    toolRepair.openSubmenu()
    toolRepair.repair()


if __name__ == "__main__":
    print("This is not meant to be run Standalone")
    time.sleep(3)
    __repairTools_TEST()
