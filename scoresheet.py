from enum import Enum, auto
import sys

from typing import List, Optional


class DieColor(Enum):
    YELLOW = 1
    BLUE = 2
    GREEN = 3
    ORANGE = 4
    PURPLE = 5
    WHITE = 6


# Workaround for PyCharm issue with auto():
#  https://youtrack.jetbrains.com/issue/PY-53388/PyCharm-thinks-enumauto-needs-an-argument
def _auto_enumerate():
    # noinspection PyArgumentList
    return auto()


class BonusType(Enum):
    REROLL = _auto_enumerate()
    PLUS_ONE = _auto_enumerate()
    BLUE_X = _auto_enumerate()
    YELLOW_X = _auto_enumerate()
    GREEN_X = _auto_enumerate()
    ORANGE_FOUR = _auto_enumerate()
    ORANGE_FIVE = _auto_enumerate()
    ORANGE_SIX = _auto_enumerate()
    PURPLE_SIX = _auto_enumerate()
    ANY_SIX = _auto_enumerate()
    ANY_X = _auto_enumerate()
    FOX = _auto_enumerate()


class RolledDie:
    def __init__(self, value: int, color: DieColor):
        self.value = value
        self.color = color


class ScoreSheetArea:
    def __init__(self, color: DieColor):
        if color == DieColor.WHITE:
            sys.exit("ERROR: cannot create WHITE score sheet area.")
        self.color = color
        self.slots = []

    def can_place_die(self, die: RolledDie, other_die: Optional[RolledDie]) -> bool:
        """To be overridden by subclasses"""
        sys.exit("ERROR: called base can_place_die().")

    def place_die(self, die: RolledDie, other_die: Optional[RolledDie] = None) -> Optional[List[BonusType]]:
        if die.color != self.color and die.color != DieColor.WHITE:
            print(f"ERROR: tried to place {die.color} die in {self.color} score sheet area.")
            return None

        if not self.can_place_die(die, other_die):
            return None

        if other_die is None:
            self.slots.append(die)
        else:
            self.slots.append( (die, other_die) )

        return self.assess_bonus()

    def assess_bonus(self) -> Optional[List[BonusType]]:
        """To be overridden by subclasses."""
        sys.exit("ERROR: called base assess_bonus().")

    def get_score(self) -> int:
        """To be overridden by subclasses."""
        sys.exit("ERROR: called base get_score().")


class YellowScoreSheetArea(ScoreSheetArea):
    def __init__(self):
        super().__init__(DieColor.YELLOW)

    def can_place_die(self, die: RolledDie, other_die: Optional[RolledDie]) -> bool:
        # TODO: issues is that need also to specify target location,
        #  as each die value can potentially occupy different spots.
        return True

    def assess_bonus(self) -> Optional[List[BonusType]]:
        # TODO
        return None


class BlueScoreSheetArea(ScoreSheetArea):
    def __init__(self):
        super().__init__(DieColor.BLUE)
        self.points = [
            1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56]

    def can_place_die(self, die: RolledDie, other_die: Optional[RolledDie]) -> bool:
        if other_die is None:
            print(f"BlueScoreSheetArea: Need both dice, but only one provided.")
            return False
        colors = (die.color, other_die.color)
        if colors not in [ (DieColor.BLUE, DieColor.WHITE), (DieColor.WHITE, DieColor.BLUE) ]:
            print(f"Incompatible dice colors in BlueScoreSheetArea: {colors}.")
            return False
        sum = die.value + other_die.value
        for i in range(len(self.slots)):
            if self.slots[i][0].value + self.slots[i][1].value == sum:
                print(f"Already have blue sheet die placed for sum {sum}: {self.slots[i]}")
                return False
        return True

    def assess_bonus(self) -> Optional[List[BonusType]]:
        # TODO
        return None

    def get_score(self) -> int:
        return self.points[len(self.slots) - 1]


class GreenScoreSheetArea(ScoreSheetArea):
    def __init__(self):
        super().__init__(DieColor.GREEN)
        # Number represents the die value that must be met or exceeded (i.e., >=)
        self.slot_constraints = [
            1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]
        self.max_slots = len(self.slot_constraints)
        self.points = [
            1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]

    def can_place_die(self, die: RolledDie, other_die: Optional[RolledDie]) -> bool:
        slot_index = len(self.slots)
        if slot_index >= self.max_slots:
            print("Cannot add any more dice to GREEN area.")
            return False
        if die.value < self.slot_constraints[slot_index]:
            print(f"GREEN slot constraint not met ({die.value} < {self.slot_constraints[slot_index]})")
            return False
        return True

    def assess_bonus(self) -> Optional[List[BonusType]]:
        # TODO
        return None

    def get_score(self) -> int:
        return self.points[len(self.slots)-1]


class OrangeScoreSheetArea(ScoreSheetArea):
    def __init__(self):
        super().__init__(DieColor.ORANGE)
        self.multipliers = [
            1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 3]
        self.max_slots = len(self.multipliers)

    def can_place_die(self, die: RolledDie, other_die: Optional[RolledDie]) -> bool:
        slot_index = len(self.slots)
        if slot_index >= self.max_slots:
            print("Cannot add any more dice to ORANGE area.")
            return False
        return True

    def assess_bonus(self) -> Optional[List[BonusType]]:
        # TODO
        return None

    def get_score(self) -> int:
        sum = 0
        for i in range(len(self.slots)):
            sum += self.slots[i].value * self.multipliers[i]
        return sum


class PurpleScoreSheetArea(ScoreSheetArea):
    def __init__(self):
        super().__init__(DieColor.PURPLE)
        self.max_slots = 11

    def can_place_die(self, die: RolledDie, other_die: Optional[RolledDie]) -> bool:
        slot_index = len(self.slots)
        if slot_index == 0:
            return True
        prev_value = self.slots[slot_index - 1].value
        if prev_value == 6:
            return True
        if die.value > prev_value:
            return True
        print(f"Cannot add die because not greater than {die.value} <= {prev_value}.")
        return False

    def assess_bonus(self) -> Optional[List[BonusType]]:
        # TODO
        return None

    def get_score(self) -> int:
        sum = 0
        for i in range(len(self.slots)):
            sum += self.slots[i].value
        return sum
