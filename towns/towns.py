import sys
import os
os.chdir('../units')
sys.path.append(os.getcwd())
os.chdir('../exceptiones')
sys.path.append(os.getcwd())

from buildings import Gold_mine, Wall, Castle, Barracs
from units import ALL_RACE_UNITS
from exceptiones import NoUnits


class Town:
    def __init__(self, race):
        self.gold_mine = Gold_mine()
        self.wall = Wall()
        self.castle = Castle()
        self.barracs = Barracs( ALL_RACE_UNITS[race] )
        self.army = [10, 0, 0, 0]
        self.can_build = True

    def increase_army(self, unit_type, unit_count):
        self.army[unit_type] += unit_count

    def decrease_army(self, unit_type, unit_count):
        if self.army[unit_type] < unit_count:
            raise NoUnits
        self.army[unit_type] -= unit_count
