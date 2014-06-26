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
        self.hero = None

    def hire_hero(self, name):
        self.hero = Hero(name)

    def upgrade_building(self, building):
        if building.cost_to_upgrade() <= self.money:
            if building.can_upgrade():
                self.money -= building.cost_to_upgrade()
                building.upgrade()
                return True
        return False

    def move_army_from_town_to_hero(self, unit_type, unit_count):
        if self.hero.is_in_town == False:
            raise Exception('Hero need to be in town')

        if self.hero == None:
            raise Exception('No hero in town')

        if self.town.army[unit_type] < unit_count:
            raise Exception('Not enough army')


        self.town.decrease_army(unit_type, unit_count)
        self.hero.increase_army(unit_type, unit_count)


    def move_army_from_hero_to_town(self, unit_type, unit_count):
        if self.hero == None:
            raise Exception('No hero')

        if self.hero.is_in_town == False:
            raise Exception('Hero not in town')

        if self.hero.army[unit_type] < unit_count:
            raise Exception('Not enough army')

        self.hero.decrease_army(unit_type, unit_count)
        self.town.increase_army(unit_type, unit_count)
