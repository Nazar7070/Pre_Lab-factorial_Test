import unittest
from main import grade_scale, factorial

class TestGradeScale(unittest.TestCase):
    def test_A_grade(self):
        self.assertEqual(grade_scale(95), 'A')

    def test_B_grade(self):
        self.assertEqual(grade_scale(85), 'B')

    def test_C_grade(self):
        self.assertEqual(grade_scale(75), 'C')

    def test_D_grade(self):
        self.assertEqual(grade_scale(65), 'D')

class TestFactorial(unittest.TestCase):
    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_negative(self):
        self.assertEqual(factorial(-3), 'Invalid input')

if __name__ == "__main__":
    unittest.main()
