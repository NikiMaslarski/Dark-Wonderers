import sys
sys.path.append('/home/niki/DarkWonderers/Dark-Wonderers/Units')

from Buildings import Gold_mine, Wall, Castle, Barracs
from Units import ALL_RACE_UNITS

class Town:
    def __init__(self, race):
        self.gold_mine = Gold_mine()
        self.wall = Wall()
        self.castle = Castle()
        self.barracs = Barracs( ALL_RACE_UNITS[race] )
