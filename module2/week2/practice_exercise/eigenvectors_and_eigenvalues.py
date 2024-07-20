import numpy as np


def compute_eigenvalues_and_eigenvectors(matrix):
    """Method 1: Using the characteristic polynomial"""
    # coefficients of the characteristic polynomial
    coefficients = np.poly(matrix)
    eigenvalues = np.roots(coefficients)

    eigenvectors = []
    for eigenvalue in eigenvalues:
        # create A - λI
        matrix_minus_lambda_I = matrix - \
            eigenvalue * np.identity(matrix.shape[0])

        # SVD decomposition of A - λI
        _, _, vh = np.linalg.svd(matrix_minus_lambda_I)

        # the eigenvector is the last column of vh (or the last row of vh.T) after SVD decomposition of A - λI matrix
        eigenvector = vh[-1, :]
        eigenvectors.append(eigenvector)

    eigenvectors = np.array(eigenvectors).T

    # Normalize eigenvectors
    for i in range(eigenvectors.shape[1]):
        eigenvectors[:, i] = eigenvectors[:, i] / \
            np.linalg.norm(eigenvectors[:, i])

    # Ensure the eigenvectors have consistent signs with np.linalg.eig
    eigenvalues_np, eigenvectors_np = np.linalg.eig(matrix)
    for i in range(eigenvectors.shape[1]):
        if np.sign(eigenvectors[0, i]) != np.sign(eigenvectors_np[0, i]):
            eigenvectors[:, i] = -eigenvectors[:, i]

    # """Method 2: Using the eig function"""
    # eigenvalues, eigenvectors = np.linalg.eig(matrix)

    return eigenvalues, eigenvectors


if __name__ == "__main__":
    # test the function with a 2x2 matrix
    matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
    eigenvalues, eigenvectors = compute_eigenvalues_and_eigenvectors(matrix)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)
