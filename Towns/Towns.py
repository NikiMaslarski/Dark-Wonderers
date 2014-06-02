import sys
import os
os.chdir('../Units')
sys.path.append(os.getcwd())

from Buildings import Gold_mine, Wall, Castle, Barracs
from Units import ALL_RACE_UNITS

class Town:
    def __init__(self, race):
        self.gold_mine = Gold_mine()
        self.wall = Wall()
        self.castle = Castle()
        self.barracs = Barracs( ALL_RACE_UNITS[race] )
        self.army = [10, 0, 0, 0]

    def increace_army(self, unit_type, unit_count):
        self.army[unit_type] += unit_count

