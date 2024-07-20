# Finding the Inverse of Matrix A

Given the matrix \(A\):
| -2 | 6 |
|----|----|
| 8 | -4 |

### Step 1: Calculate the Determinant of A

```python
import numpy as np

A = np.array([[-2, 6], [8, -4]])

a, b = A[0, 0], A[0, 1]
c, d = A[1, 0], A[1, 1]

det_A = a * d - b * c
```

### Step 2: Check if the Determinant is Non-zero or not

```python
if det_A != 0:
    print("Matrix A is invertible.")
else:
    print("Matrix A is not invertible.")
```

### Step 3: Calculate the Inverse of Matrix A

```python
if det_A != 0:
    A_inv = (1 / det_A) * np.array([[d, -b], [-c, a]])
    print("Inverse of Matrix A:")
    print(A_inv)
else:
    A_inv = None
    print("Matrix A does not have an inverse.")
```

### Conclusion

The inverse of matrix \(A\) is:

| 1/10 | 3/20 |
| ---- | ---- |
| 1/5  | 1/20 |
