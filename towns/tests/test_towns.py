import unittest
import sys
import os

os.chdir('..')
sys.path.append(os.getcwd())

from buildings import Wall, Gold_mine, Castle, Barracs
from towns import Town, no_army

class TestTown(unittest.TestCase):
    def setUp(self):
        self.town = Town('elf')

    def test_town_buildings(self):
        self.assertIsInstance(self.town.wall, Wall)
        self.assertIsInstance(self.town.gold_mine, Gold_mine)
        self.assertIsInstance(self.town.castle, Castle)
        self.assertIsInstance(self.town.barracs, Barracs)

    def test_town_army(self):
        self.assertEqual(self.town.barracs.army, \
             ['archer','rogue', 'druid', 'assassin'])

    def test_increase_decrease_army(self):
        self.assertRaises(no_army, self.town.decrease_army, 1, 3)
        self.assertEqual([10, 0, 0, 0], self.town.army)
        self.town.increase_army(1, 20)
        self.assertEqual([10, 20, 0, 0], self.town.army)
        self.town.decrease_army(0, 5)
        self.assertEqual([5, 20, 0, 0], self.town.army)
        self.assertEqual([5, 20, 0, 0], self.town.army)

if __name__ == '__main__':
    unittest.main()
