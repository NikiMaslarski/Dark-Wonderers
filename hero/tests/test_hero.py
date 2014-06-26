import unittest
import os
import sys

os.chdir('..')
sys.path.append(os.getcwd())

from hero import Hero, NoUnits, NoTalentPoints

class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('San')

    def test_hero_constructor(self):
        self.assertEqual(self.hero.name, 'San')
        self.assertEqual(self.hero.level, 1)

    def test_level_up(self):
        self.hero.experience = 245
        self.hero.level_up()

        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.experience, 45)
        self.assertEqual(self.hero.experience_to_level_up, 300)

    def test_town_conditions(self):
        self.assertTrue(self.hero.is_in_town)
        self.hero.leave_town()
        self.assertFalse(self.hero.is_in_town)
        self.hero.arrive_at_town()

    def test_increase_decrease_army(self):
        self.hero.increase_army(1, 20)
        self.assertEqual(self.hero.army, [0, 20, 0, 0])
        self.hero.decrease_army(1, 10)
        self.assertEqual(self.hero.army, [0, 10, 0, 0])
        self.assertRaises(NoUnits, self.hero.decrease_army, 1, 40)
        self.hero.increase_army(3, 100)
        self.assertEqual(self.hero.army, [0, 10, 0, 100])

    def test_upgrade_bonus(self):
        self.hero.upgrade_bonus('health')
        self.assertEqual(self.hero.bonuses['health'], 1)
        self.assertEqual(self.hero.bonuses['damage'], 0)
        self.hero.talent_points = 0
        self.assertRaises(NoTalentPoints, self.hero.upgrade_bonus, 'damage')


if __name__ == '__main__':
    unittest.main()
