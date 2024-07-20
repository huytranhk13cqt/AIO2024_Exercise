import numpy as np


def compute_eigenvalues_eigenvectors(matrix):
    # Step 1: Check if the matrix is 2x2
    n = matrix.shape[0]
    if n != 2:
        raise ValueError(
            "This function is currently designed for 2x2 matrices.")

    # Step 2: Extract the elements of the matrix
    a, b, c, d = matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]

    # Step 3: Compute the eigenvalues
    trace = a + d
    determinant = a * d - b * c

    # Step 4: Solve the quadratic equation
    coefficients = [1, -trace, determinant]

    # Step 5: Compute the roots of the quadratic equation
    a, b, c = coefficients
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        eigenvalues = np.array([root1, root2])
    else:
        root1_real = -b / (2*a)
        root1_imag = np.sqrt(-discriminant) / (2*a)
        root2_real = root1_real
        root2_imag = -root1_imag
        eigenvalues = np.array(
            [complex(root1_real, root1_imag), complex(root2_real, root2_imag)])

    # Step 6: Compute the eigenvectors

    # Eigenvector 1
    eigenvector1 = np.array([1, 0])
    eigenvector1 = eigenvector1 / np.linalg.norm(eigenvector1)

    # Eigenvector 2
    eigenvector2 = np.array([eigenvalues[1] - d, c])
    eigenvector2 = eigenvector2 / np.linalg.norm(eigenvector2)

    eigenvectors = np.array([eigenvector1, eigenvector2])

    return eigenvalues, eigenvectors


if __name__ == "__main__":
    # Test the function with a 2x2 matrix
    matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
    eigenvalues = compute_eigenvalues_eigenvectors(matrix)
    print("Eigenvalues:", eigenvalues)
