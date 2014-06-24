import sys
import os

sys.path.append(os.path.abspath('..'))

from Units.Tests import testUnits
from Towns.Tests import testBuildings

from Towns import Buildings

testUnits.unittest.main()
testBuildings.unittest.main()

if __name__ == '__main__':
    unittest.main()
