# Data (vector x,y): x = {x1,...,xN} and y = {y1,...,yN}
# Cosine Similarity = cs(x,y) = (x dot y) / (||x||||y||) = (x1*y1 + x2*y2 + ... + xN*yN) / (sqrt(x1^2 + x2^2 + ... + xN^2) * sqrt(y1^2 + y2^2 + ... + yN^2))

# given x = [1 2 3 4]T and y = [1 0 3 0]T. Find cosine similarity between x and y

import numpy as np


def compute_cosine_manually(v1, v2):
    dot_product = 0
    x_squared = 0
    y_squared = 0
    cosine_similarity = 0

    for i in range(len(v1)):
        dot_product += v1[i, 0] * v2[i, 0]
        x_squared += v1[i, 0] ** 2
        y_squared += v2[i, 0] ** 2

    cosine_similarity = dot_product / ((x_squared ** 0.5) * (y_squared ** 0.5))

    return cosine_similarity


def compute_cosine_np(v1, v2):
    dot_product = np.dot(v1.T, v2)[0, 0]

    norm_x = np.linalg.norm(v1)
    norm_y = np.linalg.norm(v2)

    cosine_similarity = dot_product / (norm_x * norm_y)

    return cosine_similarity


def compute_cosine(v1, v2):
    dot_product = np.dot(v1, v2)

    norm_x = np.linalg.norm(v1)
    norm_y = np.linalg.norm(v2)

    cosine_similarity = dot_product / (norm_x * norm_y)

    return cosine_similarity


if __name__ == "__main__":
    # Test the functions
    x = np.array([[1], [2], [3], [4]])
    y = np.array([[1], [0], [3], [0]])

    print("Cosine similarity between x and y (manually):",
          compute_cosine_manually(x, y))
    print("Cosine similarity between x and y (numpy):", compute_cosine_np(x, y))
