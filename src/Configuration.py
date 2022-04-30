import argparse

if __name__ == "__main__":
    raise RuntimeError("This is not meant to be run as standalone")

Parser = argparse.ArgumentParser()
Parser.add_argument("-r", "--repair", type=int, default=10, metavar="", dest="REPAIR",
                    help="Defines after how many fishing rod casts repairs happen."
                    "\nSet as 0 to disable")
Parser.add_argument("-tts", "--timeTillStart", type=int, default=4, metavar="", dest="TTS",
                    help="How long to wait (in seconds) till the bot starts")
Parser.add_argument("-ak", "--actionKey", type=str, default="q", metavar="", dest="FISH",
                    help="The action key for fishing")

_Arguments = Parser.parse_args()
TIME_TILL_START = _Arguments.TTS
REPAIR_DIVIDER = _Arguments.REPAIR


class Keybindings:
    Fish = _Arguments.FISH
    PetMenu = ["alt", "p"]
