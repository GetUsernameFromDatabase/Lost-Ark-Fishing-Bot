# Python Built-in import
import time
import random
from pathlib import Path
# External import
import pyautogui
# Project import
import Input
import Imaging
import Notifications as Notifs
from Notifications import xprint
from Configuration import Keybindings

WIDTH, HEIGHT = Input.SCREEN_WIDTH, Input.SCREEN_HEIGHT
MENU_DEPTH = 0

OriginalMouseLocation = pyautogui.position()
base_path = Path(__file__).parent
repairTool_IconPath = str(
    (base_path / "../Resources/repairTools_icon.png").resolve())


def surface(level: int = 0):
    """_summary_
    Reduces menu depth till it reaches desired level

    Args:
        level (int, optional): Menu Depth to surface to. Defaults to 0.
    """
    global MENU_DEPTH
    while True:
        if MENU_DEPTH <= level:
            return
        Input.escape()
        time.sleep(random.uniform(0.25, 1.25))
        MENU_DEPTH -= 1


def getToPetMenu():
    global MENU_DEPTH
    steps = MENU_DEPTH - 1
    if steps == 0:
        return

    Notifs.PetMenu.navigatingToPetMenu()
    if steps < 0:  # It shouldn't be possible for it to be below -1
        MENU_DEPTH += 1
        Input.pressKeys(Keybindings.PetMenu)
    else:
        surface(1)
    time.sleep(random.uniform(1.0, 2.5))


def returnMouse():
    pyautogui.moveTo(OriginalMouseLocation.x,
                     OriginalMouseLocation.y,
                     random.uniform(0.2, 0.75))


class PetSubMenu:
    def _preparingToOpenSubmenu(self, submenuName):
        global OriginalMouseLocation
        OriginalMouseLocation = pyautogui.position()

        Notifs.PetMenu.openingSubmenu(submenuName)
        # To reduce possible interference from tooltips
        pyautogui.moveTo(WIDTH/2, 0, 0.3)
        time.sleep(0.5)

    def _subMenuOpened(self):
        global MENU_DEPTH
        MENU_DEPTH += 1
        time.sleep(random.uniform(0.5, 1.5))

    def _subMenuClosed(self):
        global MENU_DEPTH
        MENU_DEPTH -= 1
        returnMouse()

    def closeSubMenu(self):
        Input.escape()
        self._subMenuClosed()


class __ToolRepair(PetSubMenu):
    name = "remote repair"

    def __init__(self, ratio=16/9):
        super().__init__()

        self.Icon = Imaging.imageToFind(repairTool_IconPath)
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
        """_summary_
        Tries to open the remote repair submenu

        Returns:
            string: description of failure
        """
        self._preparingToOpenSubmenu(self.name)
        getToPetMenu()

        screenshot = Imaging.screenshot()
        imgSearch = Imaging.ImageSearch(self.Icon, screenshot)
        coord = imgSearch.getCoordOfFirstPositiveMatch()
        if coord == False:
            Notifs.PetMenu.failedToOpenSubmenu(self.name)
            self.closeSubMenu()
            return "Didn't find remote repair"

        Input.clickOnScreen({"x": coord["x"] + self.IconSize["width"] / 2,
                             "y": coord["y"] + self.IconSize["height"] / 2})
        self._subMenuOpened()

    def __repairAll_ButtonPress(self):
        Notifs.PetMenu.Repairs.clickingRepairAll()
        Input.clickRelativeToScreen(self.Offsets["repairAll"])

    def __confirmRepair_ButtonPress(self):
        # Repair OK offset
        Notifs.PetMenu.Repairs.clickingOK()
        Input.clickRelativeToScreen(self.Offsets["confirm"])

    def repair(self):
        if MENU_DEPTH != 1:
            outcome = self.openSubmenu()
            if outcome != None:
                return
        self.__repairAll_ButtonPress()
        self.__confirmRepair_ButtonPress()
        self.closeSubMenu()


def repairTools():
    # Development: get current mouse position
    pyautogui.position()

    toolRepair = __ToolRepair()
    toolRepair.repair()

    # Exiting from Pet Menu
    time.sleep(random.uniform(0.25, 3))
    surface()


def __repairTools_TEST():
    toolRepair = __ToolRepair()
    toolRepair.repair()
    surface()


if __name__ == "__main__":
    waitTime = 3
    xprint(f"Starting the pet menu test in {waitTime} seconds\n")
    time.sleep(waitTime)
    __repairTools_TEST()
