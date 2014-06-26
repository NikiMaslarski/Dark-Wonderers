import os
import sys
os.chdir('../towns')
sys.path.append(os.getcwd())
os.chdir('../hero')
sys.path.append(os.getcwd())

from towns import Town
from hero import Hero

class Player:
    def __init__(self, race):
        self.race = race
        self.town = Town(race)
        self.money = 1000

    def hire_hero(self, name):
        self.hero = Hero(name)

    def upgrade_building(self, building):
        if(building.cost_to_upgrade() <= self.money):
            if(building.can_upgrade()):
                self.money -= building.cost_to_upgrade()
                building.upgrade()
                return True
            return False
