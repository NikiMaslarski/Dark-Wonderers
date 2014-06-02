import os
import sys
os.chdir('../Towns')
sys.path.append(os.getcwd())

from Towns import Town

class Player:
    def __init__(self, race):
        self.race = race
        self.town = Town(race)
        self.level = 1
        self.experience = 0
        self.experience_to_level_up = 200*self.level


    def level_up(self):
        if self.experience_to_level_up < self.experience:
            self.level += 1
            self.experience -= self.experience_to_level_up
            self.experience_to_level_up *= 2

