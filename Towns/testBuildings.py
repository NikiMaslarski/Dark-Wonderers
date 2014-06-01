import unittest

from Buildings import *


class TestBuilding(unittest.TestCase):
    def test_upgrade_is_available_1(self):
        temp = Building(100, 8)
        self.assertTrue(temp.upgrade_is_available())

    def test_upgrade(self):
        temp = Building(100, 8)
        temp.upgrade()
        self.assertFalse(temp.upgrade_is_available())
        self.assertEqual(2, temp.level)

    def test_upgrade_is_available_2(self):
        temp = Building(100, 8)
        temp.level = 10
        self.assertFalse(temp.upgrade_is_available())

        temp.builded_this_turn = False
        self.assertFalse(temp.upgrade_is_available())


    @unittest.skip('No money modul')
    def test_upgrade_is_available_3(self):
        temp = Building(1000, 10)
        self.assertFalse(temp.upgrade_is_available())


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


class TestWall(unittest.TestCase):
    def setUp(self):
        self.wall = Wall()

    def test_wall(self):
        self.assertEqual(1, self.wall.get_bonus_defence())
        self.assertEqual(0.5, self.wall.get_bonus_range_attack())

    def test_wall_upgrade(self):
        self.wall.upgrade()
        self.assertEqual(2, self.wall.get_bonus_defence())
        self.assertNotEqual(1, self.wall.get_bonus_defence())
        self.assertEqual(1, self.wall.get_bonus_range_attack())


if __name__ == '__main__':
    unittest.main()
