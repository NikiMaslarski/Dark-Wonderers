import unittest
import sys
import os

os.chdir('..')
sys.path.append(os.getcwd())

from combat_simulator import *

class test_fight_modul(unittest.TestCase):
    def test_fight(self):
        self.assertEqual(fight(400, 400, 300, 300), (1, 100))


class test_get_hero_damage(unittest.TestCase):
    def setUp(self):
        self.player = Player('Player1', 'elf')
        self.player.hire_hero('San')
        self.player.hero.army[0] += 100

    def test_get_damage(self):
        self.assertEqual(get_total_damage\
                        (self.player.hero.army,'elf'), 30000)


class test_hero_combat(unittest.TestCase):
    def setUp(self):
        self.player1 = Player('Player1', 'human')
        self.player2 = Player('Player2', 'human')
        self.player1.hire_hero('Drizzt')
        self.player2.hire_hero('Entreri')
        self.player1.hero.army[1] += 30
        self.player2.hero.army[1] += 20

    def test_combat(self):
        self.assertEqual(hero_combat(self.player1, self.player2),\
                         self.player1.name)
        self.assertEqual(self.player2.hero, None)
        self.assertEqual(self.player1.hero.experience, 10)


if __name__ == '__main__':
    unittest.main()
