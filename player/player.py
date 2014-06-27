import os
import sys
os.chdir('../towns')
sys.path.append(os.getcwd())
os.chdir('../hero')
sys.path.append(os.getcwd())
os.chdir('../units')
sys.path.append(os.getcwd())
os.chdir('../exceptiones')
sys.path.append(os.getcwd())

from towns import Town
from hero import Hero
from units import ALL_RACE_UNITS
from exceptiones import BuildingAtMaxLevel, NoGold
from exceptiones import HeroNotInTown, NoUnits, NoHero
from exceptiones import NoDailyUnits


class Player:
    def __init__(self, name, race):
        self.race = race
        self.town = Town(race)
        self.gold = 1000
        self.hero = None
        self.name = name

    def hire_hero(self, name):
        self.hero = Hero(name)

    def upgrade_building(self, building):
        """ Accepts the building you want to upgrade """
        if building.price > self.gold:
            raise NoGold

        if not building.upgrade_available():
            raise BuildingAtMaxLevel

        self.gold -= building.price
        building.upgrade()

    def move_army_from_town_to_hero(self, unit_type, unit_count):
        if self.hero.is_in_town == False:
            raise HeroNotInTown

        if self.hero == None:
            raise NoHero

        if self.town.army[unit_type] < unit_count:
            raise NoUnits

        self.town.decrease_army(unit_type, unit_count)
        self.hero.increase_army(unit_type, unit_count)

    def move_army_from_hero_to_town(self, unit_type, unit_count):
        if self.hero == None:
            raise NoHero

        if self.hero.is_in_town == False:
            raise HeroNotInTown

        if self.hero.army[unit_type] < unit_count:
            raise NoUnits

        self.hero.decrease_army(unit_type, unit_count)
        self.town.increase_army(unit_type, unit_count)

    def train_army(self, unit_type, unit_count):
        if self.town.castle.units_available_to_train < unit_count:
            raise NoDailyUnits

        if ALL_RACE_UNITS[self.race][self.town.barracs.\
        army[unit_type]].price * unit_count > self.gold:
            raise NoGold

        self.town.army[unit_type] += unit_count

        self.gold -= ALL_RACE_UNITS[self.race][self.town.\
            barracs.army[unit_type]].price * unit_count

