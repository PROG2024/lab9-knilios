"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
from math import pi
import unittest

class TestCircle(unittest.TestCase):
    """ Test the class 'Circle'"""
    def setUp(self) -> None:
        """Set up the circle so it can be tested"""
        self.circle = Circle(3)
    
    def test_legal_add_area(self):
        add_circle = Circle(4)
        new_circle = self.circle.add_area(add_circle)
        self.assertEqual(25*pi, new_circle.get_area())
        self.assertEqual(5, new_circle.get_radius())
    
    def test_edge_case_add_area(self):
        add_circle = Circle(0)
        new_circle = self.circle.add_area(add_circle)
        self.assertEqual(9*pi, new_circle.get_area())
        self.assertEqual(3, new_circle.get_radius())
    
    def test_circle_constructor_with_illegal_case(self):
        with self.assertRaises(Exception):
            new_illegal_circle = Circle(-69)
        with self.assertRaises(Exception):
            newer_illegal_circle = Circle(-0.001)
            
            
if __name__ == "__main__":
    unittest.main()



