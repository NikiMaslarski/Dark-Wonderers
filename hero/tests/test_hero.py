import unittest
import os
import sys

os.chdir('..')
sys.path.append(os.getcwd())

from hero import *

class TestHeroe(unittest.TestCase):
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
        self.assertEqual(self.hero.experience_to_level_up, 400)





if __name__ == '__main__':
    unittest.main()
