# Python Built-in import
from typing import Union
# External import
import pyautogui
# Project import
from CustomTypes import Coord

KEYBINDINGS = {"fish": "q",
               "petMenu": ["alt", "p"],
               }
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()


def pressKeys(keys: Union[list, str]):
    if type(keys) == str:
        pyautogui.keyDown(keys)
        pyautogui.keyUp(keys)
        return

    for key in keys:
        pyautogui.keyDown(key)
    for key in reversed(keys):
        pyautogui.keyUp(key)


def clickOnScreen(coord: Coord):
    # Moves there over 2 seconds
    pyautogui.moveTo(coord["x"], coord["y"], 1)
    pyautogui.leftClick()


def clickRelativeToScreen(offset: Coord):
    coord = {"x": round(SCREEN_WIDTH * offset["x"]),
             "y": round(SCREEN_HEIGHT * offset["y"])}
    clickOnScreen(coord)


def escape():
    pressKeys("esc")

# ----- TESTING -----


def __keyPress_TEST():
    pressKeys(["shift", "a"])
    pressKeys("b")


if __name__ == "__main__":
    __keyPress_TEST()
