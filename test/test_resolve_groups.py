import unittest
from src.resolve_groups import resolve_groups


class TestResolveGroups(unittest.TestCase):

    def setUp(self):
        pass

    def test_resolve_groups(self):

        self.assertEqual(resolve_groups("2+3*2"), 8.00)



if __name__ == '__main__':
    unittest.main()

