import unittest
from silly_pascal import isValid

class TestSillyPascal(unittest.TestCase):

    def test_valid_string(self):
        assert isValid('a1ab2') == True

    def test_identifier_beggining_with_number(self):
        assert isValid('1asd') == False

    def test_identifier_with_invalid_characters(self):
        assert isValid('a&23') == False

    def test_too_long_identifier(self):
        assert isValid('a12dbgcght') == False

    def test_empty_identifier(self):
        assert isValid('') == False

if __name__ == '__main__':
    unittest.main()