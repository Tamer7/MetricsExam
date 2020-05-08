"Testing For Absolute Function"
import unittest
import math
from absolute import my_fabs



class TestMathFunction(unittest.TestCase):
    """
    Class to Test The Absolute math function
    """

    def test_correct_param(self):
        "Test for correct parameters"
        input_result = -5.63
        expected = 5.63
        self.assertEqual(math.fabs(input_result), expected)


    def test_positive_param(self):
        "Test for positive number"
        input_result = 5.2
        expected = 5.2
        self.assertEqual(math.fabs(input_result), expected)



    def test_missing_param(self):
        "Test for missing parameters"
        with self.assertRaises(TypeError):
            self.assertEqual(my_fabs(), True)
        with self.assertRaises(TypeError):
            self.assertEqual(my_fabs(''), True)


    def test_wrong_param(self):
        "Test for wrong parameters"
        with self.assertRaises(TypeError):
            my_fabs({})
        with self.assertRaises(TypeError):
            my_fabs([])
        with self.assertRaises(TypeError):
            my_fabs("Wrong String")



if __name__ == '__main__':
    unittest.main()
