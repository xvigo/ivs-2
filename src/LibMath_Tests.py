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

# Tests of function add
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

# Tests of function sub
class TestSub(unittest.TestCase):

    def test_sub_int_positive(self):
        self.assertEqual(LibMath.sub(10, 5), 5)
        self.assertEqual(LibMath.sub(0, 5), -5)
        self.assertEqual(LibMath.sub(150, 150), 0)
        self.assertEqual(LibMath.sub(10, 50), -40)

    def test_sub_int_negative(self):
        self.assertEqual(LibMath.sub(10, -5), 15)
        self.assertEqual(LibMath.sub(-10, -5), -5)
        self.assertEqual(LibMath.sub(-10, 5), -15)

    def test_sub_float_positive(self):
        self.assertEqual(LibMath.sub(10.5, 0.5), 10)
        self.assertEqual(LibMath.sub(0, 1.5), -1.5)
        self.assertEqual(LibMath.sub(150.33, 150.33), 0)
        self.assertEqual(LibMath.sub(10.01, 50), -39.99)
























if __name__ == '__main__':
    unittest.main()

