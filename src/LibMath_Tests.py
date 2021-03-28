###################################################################
# Project name: Gazorpazorp calculator
# File: LibMath_Tests.py
# Authors: Pavel Marek
# Description: Test for LibMath.py
# Date: 27. 3. 2020
###################################################################
# Run the tests in directory src:
# /src$ python3 LibMath_Tests.py
#

import unittest
import LibMath


class TestAdd(unittest.TestCase):

    def test_add_int_positive(self):
        self.assertEqual(LibMath.add(10, 5), 15)
        self.assertEqual(LibMath.add(5, 10), 15)
        self.assertEqual(LibMath.add(0, 5), 5)
        self.assertEqual(LibMath.add(5, 0), 5)
        self.assertEqual(LibMath.add(0, 0), 0)

    def test_add_int_negative(self):
        self.assertEqual(LibMath.add(-10, 5), -5)
        self.assertEqual(LibMath.add(10, -5), 5)
        self.assertEqual(LibMath.add(-10, -5), -15)
        self.assertEqual(LibMath.add(0, -5), -5)
        self.assertEqual(LibMath.add(-5, 0), -5)

    def test_add_float_positive(self):
        self.assertEqual(LibMath.add(0.25, 0.30), (0.55))
        self.assertEqual(LibMath.add(0, 0.30), (0.30))
        self.assertEqual(LibMath.add(15.88, 33.1259), (49.0059))

    def test_add_float_negative(self):
        self.assertEqual(LibMath.add(0.25, -0.30), (-0.05))
        self.assertEqual(LibMath.add(-0.25, 0.30), (0.05))
        self.assertEqual(LibMath.add(-15.30, -0.30), (-15.60))
        self.assertEqual(LibMath.add(15.88, -33.1259), (-17.2459))



























if __name__ == '__main__':
    unittest.main()

