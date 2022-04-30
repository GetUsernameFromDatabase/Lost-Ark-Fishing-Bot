# Python Built-in import
from time import strftime
# Project import
from Configuration import Keybindings


def xprint(*args, **kwargs):
    """
    Wrapped print -- shows time at which print was used
    """
    modifiedArgs = (strftime("%H:%M:%S"),) + args
    print(*modifiedArgs, **kwargs)


def _toPrintOrNotToPrint(notification: str, print: bool):
    if print:
        return xprint(notification)
    return notification


def showFlag(flag: str, print: bool = False):
    notif = f"flag: {flag}"
    return _toPrintOrNotToPrint(notif, print)


def startingIn(ttsInSeconds: int, print: bool = False):
    notif = f"Starting the bot in {ttsInSeconds} seconds!"
    return _toPrintOrNotToPrint(notif, print)


def initializingBot(timeTillStart: int, repairAfterX: int, print: bool = True):
    """
    Prints when bot will start and when automatic repairs occur if they happen
    """
    x1 = startingIn(timeTillStart)
    x2 = PetMenu.Repairs.autoRepairStatus(repairAfterX)
    notif = f"{x1} {x2}"
    return _toPrintOrNotToPrint(notif, print)


def botInitialized(print: bool = True):
    notif = "I'mma be fishing. Feel free to take a nap orsm"
    return _toPrintOrNotToPrint(notif, print)


class PetMenu:
    def navigatingToPetMenu(print: bool = True):
        keys_humanReadable = " + ".join(Keybindings.PetMenu).upper()
        notif = f"Going to the pet inventory menu ({keys_humanReadable})."
        return _toPrintOrNotToPrint(notif, print)

    def closingPetMenu(print: bool = True):
        notif = "Closing the Pet Window."
        return _toPrintOrNotToPrint(notif, print)

    def openingSubmenu(name: str, print: bool = True):
        notif = f"Clicking on Pet Function: {name}."
        return _toPrintOrNotToPrint(notif, print)

    def failedToOpenSubmenu(name: str, print: bool = True):
        notif = f"Failed to open {name}. Exiting from pet menu"
        return _toPrintOrNotToPrint(notif, print)

    class Repairs:
        def clickingRepairAll(print: bool = True):
            notif = "Clicking on Repair All button."
            return _toPrintOrNotToPrint(notif, print)

        def clickingOK(print: bool = True):
            notif = "Clicking on OK button."
            return _toPrintOrNotToPrint(notif, print)

        def autoRepairStatus(repairModulus: int = 0, print: bool = False):
            """
            Notification: Are automatic repairs on or not
            if they are also notifies after how many casts repairs occur.\ 
            If {repairModulus} is 0 or not given -- 
            notification for automatic repairs will be returned
            """
            if repairModulus < 0:
                raise ValueError(
                    "Repairs cannot be made after negative amount of repairs")

            if repairModulus > 0:
                notif = f"Automatic repair every {repairModulus} casts."
            else:
                notif = "Automatic repairs are disabled."

            return _toPrintOrNotToPrint(notif, print)

        def repairsStarted(counter: int, print: bool = False):
            notif = f"Counter: {counter}. Repairing now."
            return _toPrintOrNotToPrint(notif, print)


class Fishing:
    def maxIdleReached(max_value: int, print: bool = True):
        notif = f"Idle timer reached {max_value}. Recasting now."
        return _toPrintOrNotToPrint(notif, print)

    def waiting(print: bool = False):
        notif = "Waiting for a fish."
        return _toPrintOrNotToPrint(notif, print)

    def idleStatus(idle_timer: int, max_value: int, print: bool = False):
        """
        Notification: Current idle timer and the max value
        """
        notif = f"Idle timer: {idle_timer}. Recast at {max_value}."
        return _toPrintOrNotToPrint(notif, print)
