import unittest
from IR import IR

class IR_tests(unittest.TestCase):
    def test_salary_under_1000(self):
        assert IR(500) == 0

    def test_salary_greater_than_1000_less_than_2000(self):
        assert IR(1500) == 75

    def test_salary_greater_than_2000_less_than_3000(self):
        assert IR(2500) == 250

    def test_salary_greater_than_3000(self):
        assert IR(3500) == 475