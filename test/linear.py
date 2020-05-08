from src.linear import rslv_linear_equation, get_varname_from
import unittest


class TestLinearTestCase(unittest.TestCase):

    def test_exec1_3y_plus_1_equals_25(self):
        self.assertEqual(rslv_linear_equation("3y+1=25"), 8.00)

    def test_exec2_2z_plus_2_equals_16(self):
        self.assertEqual(rslv_linear_equation("2z+2=16"), 7.00)

    def test_exec3_2c_plus_1_equals_19(self):
        self.assertEqual(rslv_linear_equation("2c+1=19"), 9.00)

    def test_exec4_3u_plus_8_equals_32(self):
        self.assertEqual(rslv_linear_equation("3u+8=32"), 8.00)

    def test_exec5_3c_plus_3_equals_15(self):
        self.assertEqual(rslv_linear_equation("3c+3=15"), 4.00)

    def test_exec6_x_is_variable_name_in_4x(self):
        self.assertEqual(get_varname_from("4x+1=25"), "x")

    def test_exec7_c_is_variable_name_in_3c(self):
        self.assertEqual(get_varname_from("3c+1=25"), "c")

if __name__ == "__main__":
    unittest.main()


