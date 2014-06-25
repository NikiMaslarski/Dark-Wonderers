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

    def hire_hero(self, name):
        self.hero = Hero(name)

