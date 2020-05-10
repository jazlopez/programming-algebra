import unittest
from src.tokenize import tokenize

class TestTokenizeCase(unittest.TestCase):

    """
    """

    def test_tokenize(self):
        self.assertEqual(tokenize("121+1+30*45"), ["121", "+", "1", "+", "30", "*", "45"])


if __name__ == '__main__':
    unittest.main()

