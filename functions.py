import Calculator
import math

# Functions for Basic Calculator


def basic_calculator():
    print("Basic Calculator")
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /, sqrt, ^): ")

    if operator == 'sqrt':
        result = math.sqrt(num1)
    elif operator == '^':
        exponent = float(input("Enter the exponent: "))
        result = num1 ** exponent
    else:
        num2 = float(input("Enter the second number: "))
        result = perform_basic_operation(num1, num2, operator)

    print("Result: {}".format(result))


def perform_basic_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Cannot divide by zero.")
            return None

# Functions for Matrix Calculator


def matrix_calculator():
    print("Matrix Calculator")
    rows_A, cols_A = get_matrix_dimensions("A")
    matrix_A = get_matrix_values(rows_A, cols_A, "A")

    operation = input("Choose operation (rref, multiply, inverse): ")

    if operation == 'rref':
        rref_result = rank_of_matrix(matrix_A)
        print("Row-Reduced Echelon Form (rref) Rank: {}".format(rref_result))
    elif operation == 'multiply':
        rows_B, cols_B = get_matrix_dimensions("B")
        matrix_B = get_matrix_values(rows_B, cols_B, "B")
        multiply_result = matrix_multiply(matrix_A, matrix_B)
        print("Matrix Multiplication Result:")
        print_matrix(multiply_result)
    elif operation == 'inverse':
        try:
            inverse_result = matrix_inverse(matrix_A)
            print("Matrix Inverse:")
            print_matrix(inverse_result)
        except ValueError as e:
            print("Error:", e)
    else:
        print("Invalid operation.")


def get_matrix_dimensions(matrix_name):
    rows = int(
        input("Enter the number of rows for Matrix {}: ".format(matrix_name)))
    cols = int(
        input("Enter the number of columns for Matrix {}: ".format(matrix_name)))
    return rows, cols


def get_matrix_values(rows, cols, matrix_name):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(
                input("Enter element {}[{}][{}]: ".format(matrix_name, i, j)))
            row.append(element)
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def matrix_multiply(matrix_A, matrix_B):
    rows_A, cols_A = len(matrix_A), len(matrix_A[0])
    rows_B, cols_B = len(matrix_B), len(matrix_B[0])

    if cols_A != rows_B:
        raise ValueError(
            "Number of columns in Matrix A must be equal to the number of rows in Matrix B.")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]

    return result


def matrix_inverse(matrix):
    det = determinant(matrix)

    if det == 0:
        raise ValueError("The matrix is singular and cannot be inverted.")

    adjugate_matrix = adjugate(matrix)
    inverse_matrix = scalar_multiply(adjugate_matrix, 1 / det)

    return inverse_matrix


def determinant(matrix):
    size = len(matrix)

    if size == 1:
        return matrix[0][0]

    det = 0

    for i in range(size):
        minor_matrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
        det += ((-1) ** i) * matrix[0][i] * determinant(minor_matrix)

    return det


def adjugate(matrix):
    size = len(matrix)
    adjugate_matrix = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            minor_matrix = [row[:j] + row[j + 1:]
                            for row in (matrix[:i] + matrix[i + 1:])]
            cofactor = ((-1) ** (i + j)) * determinant(minor_matrix)
            adjugate_matrix[j][i] = cofactor

    return adjugate_matrix


def scalar_multiply(matrix, scalar):
    return [[element * scalar for element in row] for row in matrix]


def rank_of_matrix(matrix):
    return len([row for row in matrix if any(element != 0 for element in row)])
