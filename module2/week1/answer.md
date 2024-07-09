```python
import matplotlib.image as mpimg
import numpy as np
import pandas as pd
df = pd.read_csv("advertising.csv")
data = df.to_numpy()
```

# Q1 - A

```python
arr = np.arange(0, 10, 1)
print(arr)  # [0 1 2 3 4 5 6 7 8 9]
```

---

# Q2 - D

```python
arr = np.ones((3, 3)) > 0
print(arr)  # [[True True True] [True True True] [True True True]]
arr = np.ones((3, 3), dtype=bool)
print(arr)  # [[True True True] [True True True] [True True True]]
arr = np.full((3, 3), fill_value=True, dtype=bool)
print(arr)  # [[True True True] [True True True] [True True True]]
```

---

# Q3 - A

```python
arr = np.arange(0, 10)
print(arr[arr % 2 == 1])  # [1 3 5 7 9]
```

---

# Q4 - B

```python
arr = np.arange(0, 10)
arr[arr % 2 == 1] = -1
print(arr)  # [ 0 -1  2 -1  4 -1  6 -1  8 -1]
```

---

# Q5 - B

```python
arr = np.arange(10)
arr_2d = arr.reshape(2, -1)
print(arr_2d)  # [[0 1 2 3 4] [5 6 7 8 9]]
```

---

# Q6 - A

```python
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=0)
print(" Result : \n", c)  # [[0 1 2 3 4] [5 6 7 8 9] [1 1 1 1 1] [1 1 1 1 1]]
```

---

# Q7 - C

```python
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=1)
print("C = ", c)  # [[0 1 2 3 4 1 1 1 1 1] [5 6 7 8 9 1 1 1 1 1]]
```

---

# Q8 - A

```python
arr = np.array([1, 2, 3])
print(np.repeat(arr, 3))
print(np.tile(arr, 3))  # [1 1 1 2 2 2 3 3 3] [1 2 3 1 2 3 1 2 3]
```

---

# Q9 - C

```python
a = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.where((a >= 5) & (a <= 10))
print("result", a[index])  # [6 9 10]
```

---

# Q10 - A

```python
def maxx(x, y):
    if x >= y:
        return x
    else:
        return y

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(a, b))  # [6. 7. 9. 8. 9. 7. 5.]
```

---

# Q11 - A

```python
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print("Result", np.where(a < b, b, a))  # [6 7 9 8 9 7 5]
```

---

# Q12 - A

```python
img = mpimg.imread('dog.jpeg')
gray_img_01 = (np.max(img[..., :3], axis=-1) + np.min(img[..., :3], axis=-1)) / 2
print(gray_img_01[0, 0])  # 102.5
```

---

# Q13 - B

```python
img = mpimg.imread('dog.jpeg')
gray_img_01 = np.mean(img[..., :3], axis=-1)
print(gray_img_01[0, 0])  # 107.66666666666667
```

---

# Q14 - C

```python
img = mpimg.imread('dog.jpeg')
gray_img_01 = 0.21 * img[..., 0] + 0.72 * img[..., 1] + 0.07 * img[..., 2]
print(gray_img_01[0, 0])  # 126.22999999999999
```

---

# Q15 - C

```python
max_sales = np.max(data[:, -1])
max_sales_index = np.argmax(data[:, -1])
print(f"Max: {max_sales} - Index: {max_sales_index}")  # Max: 27.0 - Index: 175
```

---

# Q16 - B

```python
mean_tv = np.mean(data[:, 0])
print(f"Mean TV: {mean_tv}")  # Mean TV: 147.0425
```

---

# Q17 - A

```python
sales_greater_than_20 = np.sum(data[:, -1] >= 20)
print(f"Sales>20: {sales_greater_than_20}")  # Sales>20: 40
```

---

# Q18 - B

```python
mean_radio = np.mean(data[data[:, -1] >= 15, 1])
print(f"Mean Radio: {mean_radio}")  # Mean Radio: 23.42727272727273
```

---

# Q19 - C

```python
total_sales = np.sum(data[data[:, 2] > np.mean(data[:, 2]), -1])
print(f"Total Sales: {total_sales}")  # Total Sales: 1405.1
```

---

# Q20 - C

```python
A = df['Sales'].mean()
scores_q20 = ['Good' if x > A else 'Bad' if x < A else 'Average' for x in df['Sales']]
print(scores_q20[7:10])  # ["Bad", "Bad", "Good"]
```

---

# Q21 - C

```python
closest_to_average = df['Sales'].iloc[(df['Sales'] - A).abs().argmin()]
scores_q21 = ['Good' if x > closest_to_average else 'Bad' if x < closest_to_average else 'Average' for x in df['Sales']]
print(scores_q21[7:10])  # ["Bad", "Bad", "Good"]
```
