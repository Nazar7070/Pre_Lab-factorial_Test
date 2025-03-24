import unittest
import subprocess
from matrix import add_matrices, multiply_matrices, transpose_matrix, generate_matrix, determinant

class TestMatrixOperations(unittest.TestCase):
    def setUp(self):
        self.A = [[1, 2], [3, 4]]
        self.B = [[5, 6], [7, 8]]
        self.C = [[1, 2, 3], [4, 5, 6]]
        self.D = [[7, 8], [9, 10], [11, 12]]
        self.invalid_matrix = [[1, 2]]
        self.square_matrix = [[2, 3], [1, 4]]

    def test_add_matrices(self):
        result = add_matrices(self.A, self.B)
        expected = [[6, 8], [10, 12]]
        self.assertEqual(result, expected)

    def test_multiply_matrices(self):
        result = multiply_matrices(self.A, self.B)
        expected = [[19, 22], [43, 50]]
        self.assertEqual(result, expected)

    def test_transpose_matrix(self):
        result = transpose_matrix(self.C)
        expected = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(result, expected)

    def test_invalid_addition(self):
        with self.assertRaises(ValueError):
            add_matrices(self.A, self.C)

    def test_invalid_multiplication(self):
        with self.assertRaises(ValueError):
            multiply_matrices(self.A, self.invalid_matrix)

    def test_generate_matrix(self):
        matrix = generate_matrix(3, 3, 1, 10)
        self.assertEqual(len(matrix), 3)
        self.assertEqual(len(matrix[0]), 3)

    def test_determinant(self):
        result = determinant(self.square_matrix)
        expected = (self.square_matrix[0][0] * self.square_matrix[1][1]) - (self.square_matrix[0][1] * self.square_matrix[1][0])
        self.assertEqual(result, expected)

    def test_zero_matrix_addition(self):
        zero_matrix = [[0, 0], [0, 0]]
        result = add_matrices(self.A, zero_matrix)
        self.assertEqual(result, self.A)

    def test_identity_matrix_multiplication(self):
        identity = [[1, 0], [0, 1]]
        result = multiply_matrices(self.A, identity)
        self.assertEqual(result, self.A)

    def test_transpose_square_matrix(self):
        result = transpose_matrix(self.A)
        expected = [[1, 3], [2, 4]]
        self.assertEqual(result, expected)

class TestCodeQuality(unittest.TestCase):
    def test_pylint_matrix(self):
        result = subprocess.run(["pylint", "matrix.py"], capture_output=True, text=True)
        print(result.stdout)  # Вивід результатів для перегляду
        self.assertIn("Your code has been rated at", result.stdout)

    def test_pylint_test_matrix(self):
        result = subprocess.run(["pylint", "test_matrix.py"], capture_output=True, text=True)
        print(result.stdout)
        self.assertIn("Your code has been rated at", result.stdout)

if __name__ == "__main__":
    unittest.main()
