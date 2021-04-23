import unittest
from triangle import Triangle, TriangleType, InvalidTriangle

class TestTriangleMethods(unittest.TestCase):

    def test_invalid_triangle_negative_side(self):
        with self.assertRaises(InvalidTriangle):
            t = Triangle(-1,-1,-1)

    def test_invalid_triangle_existence_condition(self):
        with self.assertRaises(InvalidTriangle):
            t = Triangle(11,5,5)

    def test_classify_equilateral_triangle(self):
        t = Triangle(5,5,5)
        self.assertEqual(t.classify(), TriangleType.EQUILATERAL)

    def test_classify_isosceles_triangle(self):
        t = Triangle(3,3,4)
        self.assertEqual(t.classify(), TriangleType.ISOSCELES)

    def test_scalene_triangle(self):
        t = Triangle(3,4,5)
        self.assertEqual(t.classify(), TriangleType.SCALENE)
