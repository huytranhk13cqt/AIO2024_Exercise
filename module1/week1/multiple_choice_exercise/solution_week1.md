# Q1. -> C

```python


def evaluate_model_f1_score(tp, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)
    return f1_score


assert round(evaluate_model_f1_score(2, 3, 5), 2) == 0.33
print(round(evaluate_model_f1_score(2, 3, 5), 2))
```

# Q2. -> B

```python


def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


assert is_number(3) == 1.0
assert is_number('-2a') == 0.0
print(is_number(1))
print(is_number('n'))
```

# Q3. -> C

```python
x = -2.0
if x < 0:
    y = 0.0
else:
    y = x
print(y)
```

# Q4. -> A

```python


def calc_sig(x):
    return 1 / (1 + math.exp(-x))


assert round(calc_sig(3), 2) == 0.95
print(round(calc_sig(2), 2))
```

# Q5. -> B

```python


def calc_elu(x):
    if x > 0:
        return x
    else:
        return 0.01 * (math.exp(x) - 1)


assert round(calc_elu(1)) == 1
print(round(calc_elu(-1), 2))
```

# Q6. -> A

```python


def calc_activation_func(x, act_name):
    if act_name == 'sigmoid':
        return 1 / (1 + math.exp(-x))
    elif act_name == 'relu':
        return max(0, x)
    elif act_name == 'elu':
        if x > 0:
            return x
        else:
            return 0.01 * (math.exp(x) - 1)
    else:
        return None


assert round(calc_activation_func(1, 'relu')) == 1
print(round(calc_activation_func(3, 'sigmoid'), 2))
```

# Q7. -> A

```python


def calc_ae(y, y_hat):
    return abs(y-y_hat)


y = 1
y_hat = 6
assert calc_ae(y, y_hat) == 5
y = 2
y_hat = 9
print(calc_ae(y, y_hat))
```

# Q8. -> A

```python


def calc_se(y, y_hat):
    return (y - y_hat) ** 2


y = 4
y_hat = 2
assert calc_se(y, y_hat) == 4
print(calc_se(2, 1))
```

# Q9. -> C

```python


def approx_cos(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i) * (x**(2*i)) / math.factorial(2*i)
    return result


assert round(approx_cos(1, 10), 2) == 0.54
print(round(approx_cos(3.14, 10), 2))
```

# Q10. -> A

```python


def approx_sin(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i) * (x**(2*i+1)) / math.factorial(2*i+1)
    return result


assert round(approx_sin(1, 10), 4) == 0.8415
print(round(approx_sin(3.14, 10), 4))
```

# Q11. -> A

```python


def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result += (x**(2*i+1)) / math.factorial(2*i+1)
    return result


assert round(approx_sinh(1, 10), 2) == 1.18
print(round(approx_sinh(3.14, 10), 2))
```

# Q12. -> A

```python


def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result += (x**(2*i)) / math.factorial(2*i)
    return result


assert round(approx_cosh(1, 10), 2) == 1.54
print(round(approx_cosh(3.14, 10), 2))
```

# Q13. -> A

```python


def md_nre_single_sample(y, y_hat, n, p):
    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / n)
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss


```
