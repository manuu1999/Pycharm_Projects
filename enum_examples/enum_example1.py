from enum import Enum, auto

# Enum nummeriert einfach auf
def laufe():
    if Gefahr.niedrig:
        print("you can walk through here")
    elif Gefahr.mittel:
        print("It's getting dangerous")
    else:
        print("Turn back or you will die")

class Gefahr:
    niedrig, mittel, hoch = range(3)


laufe()