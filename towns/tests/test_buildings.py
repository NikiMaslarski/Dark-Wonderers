import unittest
import os
import sys
os.chdir('..')
sys.path.append(os.getcwd())
os.chdir('../units')
sys.path.append(os.getcwd())

from buildings import *
from units import ALL_RACE_UNITS


class TestBuilding(unittest.TestCase):
    def setUp(self):
        self.building1 = Building(100, 8)
        self.building2 = Building(50, 2)

    def test_upgrade(self):
        self.building1.upgrade()
        self.assertEqual(2, self.building1.level)

        self.assertTrue(self.building2.upgrade())
        self.assertFalse(self.building2.upgrade())
        self.assertEqual(2, self.building2.level)
        self.assertEqual(80, self.building2.price)
        self.assertEqual(80, self.building2.cost_to_upgrade())

    def test_can_upgrade(self):
        self.assertTrue(self.building1.can_upgrade())
        self.building2.upgrade()
        self.assertFalse(self.building2.can_upgrade())


class TestGoldMine(unittest.TestCase):
    def setUp(self):
        self.gold_mine = Gold_mine()

    def test_get_income(self):
        self.assertEqual(500, self.gold_mine.get_income())

    def test_upgrade_mine(self):
        self.gold_mine.upgrade()
        self.assertEqual(1000, self.gold_mine.get_income())
        self.assertEqual(2, self.gold_mine.level)
        self.assertNotEqual(500, self.gold_mine.get_income())
        self.assertEqual(980, self.gold_mine.price)


class TestWall(unittest.TestCase):
    def setUp(self):
        self.wall = Wall()

    def test_wall(self):
        self.assertEqual(1, self.wall.give_bonus_defence())
        self.assertEqual(0.5, self.wall.give_bonus_range_attack())

    def test_upgrade_wall(self):
        self.wall.upgrade()
        self.assertEqual(2, self.wall.give_bonus_defence())
        self.assertNotEqual(1, self.wall.give_bonus_defence())
        self.assertEqual(1, self.wall.give_bonus_range_attack())


class TestBarracs(unittest.TestCase):
    def setUp(self):
        self.barracks = Barracs(ALL_RACE_UNITS['elf'])

    def test_army(self):
        self.assertEqual(self.barracks.army, ['archer', 'rogue', 'druid', 'assassin'])


class TestCastle(unittest.TestCase):
    def setUp(self):
        self.castle = Castle()
    def test_upgrade(self):
        self.assertEqual(1, self.castle.level)
        self.castle.upgrade()
        self.assertEqual(2, self.castle.level)
        self.assertEqual(1980, self.castle.price)

    def test_get_units_for_training(self):
        self.assertEqual(self.castle.units_available_to_train, 100)
        self.castle.get_daily_units_for_training()
        self.assertEqual(self.castle.units_available_to_train, 200)


if __name__ == '__main__':
    unittest.main()
