import os
import sys

import numpy as np

# Thêm thư mục gốc của dự án vào sys.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', '..')))

try:
    from module2.week2.practice_exercise.cosine_similarity import compute_cosine
    from module2.week2.practice_exercise.eigenvectors_and_eigenvalues import (
        compute_eigenvalues_and_eigenvectors,
    )
    from module2.week2.practice_exercise.vector_and_matrix_operations import (
        compute_dot_product,
        compute_vector_length,
        inverse_matrix,
        matrix_multi_matrix,
        matrix_multi_vector,
    )
except ModuleNotFoundError as e:
    print(f"Error importing module: {e}")
    print("Current sys.path:", sys.path)

# 1
# vector = np.array([-2, 4, 9, 21])
# result = compute_vector_length([vector])
# print(round(result, 2))

# 2
# v1 = np.array([0, 1, -1, 2])
# v2 = np.array([2, 5, 1, 0])
# result = compute_dot_product(v1, v2)
# print(round(result, 2))

# 3
# x = np.array([[1, 2], [3, 4]])
# k = np.array([1, 2])
# print('result \n', x.dot(k))

# 4
# x = np.array([[-1, 2], [3, -4]])
# k = np.array([1, 2])
# print('result \n', x@k)

# 5
# m = np.array([[-1, 1, 1], [0, -4, 9]])
# v = np.array([0, 2, 1])
# result = matrix_multi_vector(m, v)
# print(result)

# 6
# m1 = np.array([[0, 1, 2], [2, -3, 1]])
# m2 = np.array([[1, -3], [6, 1], [0, -1]])
# result = matrix_multi_matrix(m1, m2)
# print(result)

# 7
# m1 = np.eye(3)
# m2 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
# result = m1@m2
# print(result)

# 8
# m1 = np.eye(2)
# m1 = np.reshape(m1, (-1, 4))[0]
# m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
# result = m1@m2
# print(result)

# 9
# m1 = np.array([[1, 2], [3, 4]])
# m1 = np.reshape(m1, (-1, 4), "F")[0]
# m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
# result = m1@m2
# print(result)

# 10
# m1 = np.array([[-2, 6], [8, -4]])
# result = inverse_matrix(m1)
# print(result)

# 11
# matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
# eigenvalues, eigenvectors = compute_eigenvalues_and_eigenvectors(matrix)
# print(eigenvectors)

# 12
# x = np.array([1, 2, 3, 4])
# y = np.array([1, 0, 3, 0])
# result = compute_cosine(x, y)
# print(round(result, 3))
