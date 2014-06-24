import unittest
import sys
import os

os.chdir('..')
sys.path.append(os.getcwd())
os.chdir('../towns')
sys.path.append(os.getcwd())

from player import *
import towns

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player('troll')

    def test_player(self):
        self.assertIsInstance(self.player.town, Town)
        self.assertEqual(self.player.race, 'troll')
        self.assertEqual(self.player.level, 1)

    def test_level_up(self):
        self.player.experience = 245
        self.player.level_up()

        self.assertEqual(self.player.level, 2)
        self.assertEqual(self.player.experience, 45)
        self.assertEqual(self.player.experience_to_level_up, 400)



if __name__ == '__main__':
    unittest.main()
