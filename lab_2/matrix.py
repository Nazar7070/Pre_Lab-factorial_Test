import random

def generate_matrix(n, m, min_value=1, max_value=10):
    return [[random.randint(min_value, max_value) for _ in range(m)] for _ in range(n)]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

def validate_dimensions(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Матриці повинні мати однакові розміри для додавання")

def validate_multiplication(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Кількість стовпців A має дорівнювати кількості рядків B")

def add_matrices(A, B):
    validate_dimensions(A, B)
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    validate_multiplication(A, B)
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def determinant(matrix):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    raise ValueError("Тільки 2x2 матриці підтримуються")

if __name__ == "__main__":
    n, m = 3, 3
    A = generate_matrix(n, m)
    B = generate_matrix(n, m)

    print("Матриця A:")
    print_matrix(A)
    print("Матриця B:")
    print_matrix(B)

    try:
        print("A + B:")
        print_matrix(add_matrices(A, B))
    except ValueError as e:
        print(f"Помилка при додаванні: {e}")

    try:
        print("A * B^T:")
        print_matrix(multiply_matrices(A, transpose_matrix(B)))
    except ValueError as e:
        print(f"Помилка при множенні: {e}")
