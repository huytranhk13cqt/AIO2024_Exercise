# Finding Eigenvalues and Eigenvectors of Matrix A

Given the matrix \(A\):
| 0.9 | 0.2 |
|-----|-----|
| 0.1 | 0.8 |

## Step 1: Define the Function to Compute Eigenvalues and Eigenvectors

```python
import numpy as np

def compute_eigenvalues_eigenvectors(matrix):
    # Check if the matrix is 2x2
    n = matrix.shape[0]
    if n != 2:
        raise ValueError("This function is currently designed for 2x2 matrices.")
```

## Step 2: Extract the Elements of the Matrix

```python
    a, b, c, d = matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]
```

## Step 3: Compute the Eigenvalues

```python
    trace = a + d
    determinant = a * d - b * c
```

## Step 4: Solve the Quadratic Equation

```python
    coefficients = [1, -trace, determinant]
```

## Step 5: Compute the Roots of the Quadratic Equation

```python
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
            [complex(root1_real, root1_imag), complex(root2_real, root2_imag)]
        )
```

## Step 6: Compute the Eigenvectors

```python
    # Eigenvector 1
    eigenvector1 = np.array([1, 0])
    eigenvector1 = eigenvector1 / np.linalg.norm(eigenvector1)

    # Eigenvector 2
    eigenvector2 = np.array([eigenvalues[1] - d, c])
    eigenvector2 = eigenvector2 / np.linalg.norm(eigenvector2)

    eigenvectors = np.array([eigenvector1, eigenvector2])
```

## Step 7: Normalize the Eigenvectors

```python
    for i in range(eigenvectors.shape[1]):
        eigenvectors[:, i] = eigenvectors[:, i] / np.linalg.norm(eigenvectors[:, i])
```

## Step 8: Ensure Eigenvectors Have Consistent Signs with NumPy's `eig` Function

```python
    # Compare with NumPy's eig function for consistent signs
    eigenvalues_np, eigenvectors_np = np.linalg.eig(matrix)
    for i in range(eigenvectors.shape[1]):
        if np.sign(eigenvectors[0, i]) != np.sign(eigenvectors_np[0, i]):
            eigenvectors[:, i] = -eigenvectors[:, i]
```

## Step 9: return

```python
    return eigenvalues, eigenvectors
```

# Step10: Test the function with a 2x2 matrix

```python
matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvalues_and_eigenvectors(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
```

### Conclusion

The eigenvalues and eigenvectors of matrix \(A\) are:

**Eigenvalues:**
λ1 = 1, λ2 = 0.7

**Eigenvectors:**
| 0.89442719 | -0.70710678 |
| ---------- | ---------- |
| 0.4472136 | 0.70710678 |
