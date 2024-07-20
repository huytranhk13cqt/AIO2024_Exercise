import numpy as np


# Define a function to compute the length of a vector
def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.sum(np.square(vector)))
    return len_of_vector

# Define a function to compute the dot product of two vectors


def compute_dot_product(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    return dot_product

# Define a function to perform matrix-vector multiplication


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result

# Define a function to perform matrix-matrix multiplication


def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

# Define a function to calculate the inverse of a matrix


def inverse_matrix(matrix):
    # Calculate the determinant
    det = np.linalg.det(matrix)

    # Check if the determinant is zero
    if det == 0:
        return "Matrix is not invertible"
    else:
        # Calculate the inverse if the matrix is invertible
        inv_matrix = np.linalg.inv(matrix)
        return inv_matrix


if __name__ == "__main__":
    # Test vector length
    vector = np.array([3, 4])
    vector_length = compute_vector_length(vector)
    print(f"Length of the vector {vector} is {vector_length}")

    # Test dot product
    vector1 = np.array([1, 2])
    vector2 = np.array([3, 4])
    dot_product = compute_dot_product(vector1, vector2)
    print(f"Dot product of vectors {vector1} and {vector2} is {dot_product}")

    # Test matrix-vector multiplication
    matrix = np.array([[1, 2], [3, 4]])
    vector = np.array([5, 6])
    matrix_vector_result = matrix_multi_vector(matrix, vector)
    print(
        f"Matrix-vector multiplication of {matrix} and {vector} is {matrix_vector_result}")

    # Test matrix-matrix multiplication
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    matrix_matrix_result = matrix_multi_matrix(matrix1, matrix2)
    print(
        f"Matrix-matrix multiplication of {matrix1} and {matrix2} is {matrix_matrix_result}")

    # Test matrix inverse
    matrix = np.array([[1, 2], [3, 4]])
    inverse_result = inverse_matrix(matrix)
    print(f"Inverse of the matrix {matrix} is {inverse_result}")

    # Test with a non-invertible matrix
    non_invertible_matrix = np.array([[1, 2], [2, 4]])
    non_invertible_result = inverse_matrix(non_invertible_matrix)
    print(f"Inverse of the non-invertible matrix {
          non_invertible_matrix} is {non_invertible_result}")
