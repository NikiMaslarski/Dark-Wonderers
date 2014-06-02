import unittest
import sys
import os

os.chdir('..')
sys.path.append(os.getcwd())

from Buildings import Wall, Gold_mine, Castle, Barracs
from Towns import Town

class TestTown(unittest.TestCase):
    def setUp(self):
        self.town = Town('elf')

    def test_town_buildings(self):
        self.assertIsInstance(self.town.wall, Wall)
        self.assertIsInstance(self.town.gold_mine, Gold_mine)
        self.assertIsInstance(self.town.castle, Castle)
        self.assertIsInstance(self.town.barracs, Barracs)

    def test_town_army(self):
        for minion in ['archer','rogue','druid','assasin']:
            self.assertTrue(minion in self.town.barracs.army.keys())

if __name__ == '__main__':
    unittest.main()
