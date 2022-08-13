# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import Tuple

from scoresheet import *


def sheet_status(ss: ScoreSheetArea):
    print(f"{ss.color} ScoreSheet status:")
    for i in range(len(ss.slots)):
        if isinstance(ss.slots[i], RolledDie):
            print(f"  slot #{i+1}: {ss.slots[i].value} {ss.slots[i].color}")
        elif isinstance(ss.slots[i], Tuple):
            t = ss.slots[i]
            print(f"  slot #{i+1}: ({t[0].value} {t[0].color}, {t[1].value} {t[1].color})")

    print(f"Score so far: {ss.get_score()}")

def horizontal_rule():
    print('=' * 80)

def test():
    horizontal_rule()
    ss = GreenScoreSheetArea()
    print(f"Color is {ss.color}.")

    ss.place_die(RolledDie(6, DieColor.BLUE))
    ss.place_die(RolledDie(6, DieColor.GREEN))
    sheet_status(ss)

    ss.place_die(RolledDie(2, DieColor.WHITE))
    sheet_status(ss)

    ss.place_die(RolledDie(1, DieColor.GREEN))
    sheet_status(ss)

    horizontal_rule()
    ss = OrangeScoreSheetArea()
    print(f"Color is {ss.color}.")

    ss.place_die(RolledDie(6, DieColor.ORANGE))
    sheet_status(ss)

    ss.place_die(RolledDie(5, DieColor.BLUE))
    sheet_status(ss)

    ss.place_die(RolledDie(4, DieColor.WHITE))
    sheet_status(ss)

    ss.place_die(RolledDie(3, DieColor.ORANGE))
    sheet_status(ss)

    ss.place_die(RolledDie(5, DieColor.ORANGE))
    sheet_status(ss)

    horizontal_rule()
    ss = PurpleScoreSheetArea()
    print(f"Color is {ss.color}.")

    ss.place_die(RolledDie(1, DieColor.PURPLE))
    sheet_status(ss)

    ss.place_die(RolledDie(5, DieColor.BLUE))
    sheet_status(ss)

    ss.place_die(RolledDie(2, DieColor.WHITE))
    sheet_status(ss)

    ss.place_die(RolledDie(1, DieColor.PURPLE))
    sheet_status(ss)

    ss.place_die(RolledDie(5, DieColor.PURPLE))
    sheet_status(ss)

    ss.place_die(RolledDie(6, DieColor.WHITE))
    sheet_status(ss)

    ss.place_die(RolledDie(1, DieColor.PURPLE))
    sheet_status(ss)

    horizontal_rule()
    ss = BlueScoreSheetArea()
    print(f"Color is {ss.color}.")

    ss.place_die(RolledDie(1, DieColor.GREEN))
    ss.place_die(RolledDie(1, DieColor.BLUE))
    ss.place_die(RolledDie(1, DieColor.BLUE), RolledDie(2, DieColor.WHITE))
    sheet_status(ss)

    ss.place_die(RolledDie(1, DieColor.BLUE), RolledDie(2, DieColor.WHITE))
    ss.place_die(RolledDie(1, DieColor.BLUE), RolledDie(1, DieColor.WHITE))
    sheet_status(ss)

    ss.place_die(RolledDie(3, DieColor.BLUE), RolledDie(4, DieColor.WHITE))
    ss.place_die(RolledDie(3, DieColor.GREEN), RolledDie(5, DieColor.WHITE))
    ss.place_die(RolledDie(3, DieColor.WHITE), RolledDie(4, DieColor.WHITE))
    sheet_status(ss)

    ss.place_die(RolledDie(6, DieColor.BLUE), RolledDie(2, DieColor.WHITE))
    sheet_status(ss)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
