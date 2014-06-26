import unittest
import sys
import os

os.chdir('..')
sys.path.append(os.getcwd())
os.chdir('../towns')
sys.path.append(os.getcwd())

from player import *
from buildings import *
import towns


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player('troll')

    def test_player(self):
        self.assertIsInstance(self.player.town, Town)
        self.assertEqual(self.player.race, 'troll')

    def test_hire_hero(self):
        self.player.hire_hero('San')

    def test_upgrade_building(self):
        self.assertTrue(self.player.upgrade_building(self.player.town.wall))
        self.assertEqual(self.player.money, 800)
        self.player.money = 100
        self.assertFalse(self.player.upgrade_building(self.player.town.wall))
        self.assertEqual(self.player.money, 100)

    def test_move_army_to_hero(self):
        self.player.hire_hero('Drizzt')
        self.player.hero.arrive_at_town()
        self.player.move_army_from_town_to_hero(0,10)
        self.assertEqual(self.player.hero.army, [10, 0, 0, 0])
        self.assertEqual(self.player.town.army, [0, 0, 0, 0])

    def test_move_army_to_town(self):
        self.player.hire_hero('San')
        self.player.move_army_from_town_to_hero(0,10)
        self.player.move_army_from_hero_to_town(0,10)
        self.assertEqual(self.player.town.army, [10, 0, 0, 0])
        self.assertEqual(self.player.hero.army, [0, 0, 0, 0])


@unittest.skip('Will fix later')
class test_exceptions(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
