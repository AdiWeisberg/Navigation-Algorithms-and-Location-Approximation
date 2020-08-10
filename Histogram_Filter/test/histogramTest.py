##
# Tests for histogram.py
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##

from src.histogram import *
import unittest


class histogramTest(unittest.TestCase):

    # test with a list sorted in ascending order
    def test_1(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurements = ['R']
        motions = [[0, 0]]
        sensor_right = 0.8
        p_move = 1.0
        p = histogram_localization(colors, measurements, motions, sensor_right, p_move)
        self.assertAlmostEqual(p[0][1], 0.06667, places=3)


if __name__ == '__main__':
    unittest.main()
