# Calculating Cosine Similarity

Given vectors x:

| 1   |
| --- |
| 2   |
| 3   |
| 4   |

and y:

| 1   |
| --- |
| 0   |
| 3   |
| 0   |

```python
x = np.array([[1], [2], [3], [4]])
y = np.array([[1], [0], [3], [0]])
```

**Step 1: Calculate the dot product of `x` and `y`:**

```python
dot_product = 0
for i in range(len(x)):
    dot_product += x[i, 0] * y[i, 0]
print("Dot product:", dot_product)
```

Calculation:

```
dot_product = 1*1 + 2*0 + 3*3 + 4*0 = 1 + 0 + 9 + 0 = 10
```

**Step 2: Calculate the magnitude of vector `x`:**

```python
import numpy as np

norm_x = np.sqrt(np.sum(x ** 2))
print("Magnitude of x:", norm_x)
```

Calculation:

```
norm_x = sqrt(1^2 + 2^2 + 3^2 + 4^2) = sqrt(1 + 4 + 9 + 16) = sqrt(30)
```

**Step 3: Calculate the magnitude of vector `y`:**

```python
norm_y = np.sqrt(np.sum(y ** 2))
print("Magnitude of y:", norm_y)
```

Calculation:

```
norm_y = sqrt(1^2 + 0^2 + 3^2 + 0^2) = sqrt(1 + 0 + 9 + 0) = sqrt(10)
```

**Step 4: Calculate the Cosine similarity:**

```python
cosine_similarity = dot_product / (norm_x * norm_y)
print("Cosine similarity:", cosine_similarity)
```

Calculation:

```
cosine_similarity = 10 / (sqrt(30) * sqrt(10)) = 10 / sqrt(300) = 10 / (10*sqrt(3)) = 1 / sqrt(3) ≈ 0.577
```

In summary, the Cosine similarity between `x` and `y` is approximately 0.577.
