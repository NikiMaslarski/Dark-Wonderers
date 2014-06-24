import unittest
import os
import sys
os.chdir('..')
sys.path.append(os.getcwd())

from Buildings import *


class TestBuilding(unittest.TestCase):

    def test_upgrade(self):
        building1 = Building(100, 8)
        building2 = Building(50, 2)

        building1.upgrade()
        self.assertEqual(2, building1.level)

        building2.upgrade()
        self.assertEqual(2, building2.level)
        self.assertEqual(100, building2.price)


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
        self.assertEqual(1000, self.gold_mine.price)


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

@unittest.skip('I am not sure how it should work')
class TestBarracs(unittest.TestCase):
    pass


class TestCastle(unittest.TestCase):
    def test_upgrade(self):
        castle = Castle()
        castle.upgrade()
        self.assertEqual(2, castle.level)
        self.assertEqual(2000, castle.price)


if __name__ == '__main__':
    unittest.main()
