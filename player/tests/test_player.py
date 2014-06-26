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





if __name__ == '__main__':
    unittest.main()
