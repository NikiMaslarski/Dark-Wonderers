import unittest
import os
import sys

os.chdir('..')
sys.path.append(os.getcwd())

import hero

class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = hero.Hero('San')

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

    def test_increace_decreace_army(self):
        self.hero.increace_army(1, 20)
        self.assertEqual(self.hero.army, [0, 20, 0, 0])
        self.assertTrue(self.hero.decreace_army(1, 10))
        self.assertEqual(self.hero.army, [0, 10, 0, 0])
        self.assertFalse(self.hero.decreace_army(1, 40))
        self.hero.increace_army(3, 100)
        self.assertEqual(self.hero.army, [0, 10, 0, 100])

    def test_upgrade_bonus(self):
        self.hero.upgrade_bonus('health')
        self.assertEqual(self.hero.bonuses, [0, 0, 1])


if __name__ == '__main__':
    unittest.main()
