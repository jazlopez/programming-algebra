from src.resolve_linear_equation import resolve_linear_equation
import unittest


class TestResolveLinearEquations(unittest.TestCase):

    def test_exec1_3y_plus_1_equals_25(self):
        self.assertEqual(resolve_linear_equation("3y+1=25"), 8.00)

    def test_exec2_2z_plus_2_equals_16(self):
        self.assertEqual(resolve_linear_equation("2z+2=16"), 7.00)

    def test_exec3_2c_plus_1_equals_19(self):
        self.assertEqual(resolve_linear_equation("2c+1=19"), 9.00)

    def test_exec4_3u_plus_8_equals_32(self):
        self.assertEqual(resolve_linear_equation("3u+8=32"), 8.00)

    def test_exec5_3c_plus_3_equals_15(self):
        self.assertEqual(resolve_linear_equation("3c+3=15"), 4.00)

    def test_exec6_2x_plus_3_equals_0(self):
        self.assertEqual(resolve_linear_equation("2x+3=0"), - 1.50)

    def test_exec7_1x_plus_1_equals_minus_3(self):
        self.assertEqual(resolve_linear_equation("1x+1=-3"), -4.00)

    def test_exec8_2x_plus_zero_equals_zero(self):
        self.assertEqual(resolve_linear_equation("2x+0=0"), 0.00)

    def test_exec9_2x_equals_zero(self):
        self.assertEqual(resolve_linear_equation("2x=0"), 0.00)

    def test_exec_010_x_plus_3_equals_3(self):
        self.assertEqual(resolve_linear_equation("x+3=3"), 0.00)

    def test_exec_011_x_plus_3_equals_3dot5(self):
        self.assertEqual(resolve_linear_equation("x+3=3.5"), 0.50)

    def test_exec_012_x_plus_3_equals_minus_3dot5(self):
        self.assertEqual(resolve_linear_equation("x+3=-3.5"), -6.50)


if __name__ == "__main__":
    unittest.main()


