# General import

```python
import os
import sys

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', '..')))

try:
    from module_number.week_number.practice_exercise.python_file import (
        function,
        ...
    )
except ModuleNotFoundError as e:
    print(f"Error importing module: {e}")
    print("Current sys.path:", sys.path)
```

# Q1 - D

```python
vector = np.array([-2, 4, 9, 21])
result = compute_vector_length([vector])
print(round(result, 2))
```

# Q2 - B

```python
v1 = np.array([0, 1, -1, 2])
v2 = np.array([2, 5, 1, 0])
result = compute_dot_product(v1, v2)
print(round(result, 2))
```

# Q3 - A

```python
x = np.array([[1, 2], [3, 4]])
k = np.array([1, 2])
print('result \n', x.dot(k))
```

# Q4 - B

```python
x = np.array([[-1, 2], [3, -4]])
k = np.array([1, 2])
print('result \n', x@k)
```

# Q5 - A

```python
m = np.array([[-1, 1, 1], [0, -4, 9]])
v = np.array([0, 2, 1])
result = matrix_multi_vector(m, v)
print(result)
```

# Q6 - C

```python
m1 = np.array([[0, 1, 2], [2, -3, 1]])
m2 = np.array([[1, -3], [6, 1], [0, -1]])
result = matrix_multi_matrix(m1, m2)
print(result)
```

# Q7 - A

```python
m1 = np.eye(3)
m2 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result = m1@m2
print(result)
```

# Q8 - D

```python
m1 = np.eye(2)
m1 = np.reshape(m1, (-1, 4))[0]
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1@m2
print(result)
```

# Q9 - B

```python
m1 = np.array([[1, 2], [3, 4]])
m1 = np.reshape(m1, (-1, 4), "F")[0]
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1@m2
print(result)
```

# Q10 - A

```python
m1 = np.array([[-2, 6], [8, -4]])
result = inverse_matrix(m1)
print(result)
```

# Q11 - A

```python
matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvalues_and_eigenvectors(matrix)
print(eigenvectors)
```

# Q12 - C

```python
x = np.array([1, 2, 3, 4])
y = np.array([1, 0, 3, 0])
result = compute_cosine(x, y)
print(round(result, 3))
```
