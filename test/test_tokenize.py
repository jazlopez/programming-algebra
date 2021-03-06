import unittest
from src.tokenize import tokenize

class TestTokenizeCase(unittest.TestCase):

    """
    """

    def test_tokenize(self):
        self.assertEqual(tokenize("121+1+30*45"), ["121", "+", "1", "+", "30", "*", "45"])
        self.assertEqual(tokenize("2+6.00"), ["2", "+", "6.00"])
        self.assertEqual(tokenize("2x+3+2"), ["2x", "+", "3", "+", "2"])


if __name__ == '__main__':
    unittest.main()

