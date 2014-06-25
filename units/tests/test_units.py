import unittest
import sys
import os
os.chdir('..')
sys.path.append(os.getcwd())

from units import *


class testUnit(unittest.TestCase):
    def test_unit_stats(self):
        unit = Unit_status(10, 100, 1, 200, 4, 200, 3)
        self.assertEqual('heavy', unit.armor_type)
        self.assertEqual('swift', unit.damage_type)


if __name__ == '__main__':
    unittest.main()
