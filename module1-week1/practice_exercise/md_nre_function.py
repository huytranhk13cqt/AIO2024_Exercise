def validate_input(y, y_hat, n, p):
    for value, name in [(y, "y"), (y_hat, "y_hat"), (n, "n"), (p, "p")]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"{name} must be numeric value")
    if n <= 0:
        raise ValueError("n must be a positive numeric value")
    if p <= 0:
        raise ValueError("p must be a positive numeric value")


def mean_difference_nth_root_error(y, y_hat, n, p):
    validate_input(y, y_hat, n, p)
    return (y ** (1 / n) - y_hat ** (1 / n)) ** p
