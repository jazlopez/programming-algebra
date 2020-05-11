from src.resolve_linear_equation import find_equation_identity_name
import unittest


class TestFindEquationVariableName(unittest.TestCase):

    def test_exec1_x_is_variable_name_in_4x(self):
        self.assertEqual(find_equation_identity_name("4x+1=25"), "x")

    def test_exec2_c_is_variable_name_in_3c(self):
        self.assertEqual(find_equation_identity_name("1-3c=25"), "c")

if __name__ == "__main__":
    unittest.main()
