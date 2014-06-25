import unittest
import os
import sys

os.chdir('..')
sys.path.append(os.getcwd())

from hero import *

class TestHeroe(unittest.TestCase):
    def setUp(self):
        self.hero = hero





if __name__ == '__main__':
    unittest.main()
