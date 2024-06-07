def validate_input(y, y_hat, n, p):
    # Validate that y, y_hat, n, and p are numeric values and positive where required
    for value, name in [(y, "y"), (y_hat, "y_hat"), (n, "n"), (p, "p")]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"{name} must be a numeric value")
    if n <= 0:
        raise ValueError("n must be a positive numeric value")
    if p <= 0:
        raise ValueError("p must be a positive numeric value")


def mean_difference_nth_root_error(y, y_hat, n, p):
    # Calculate the mean difference nth root error
    validate_input(y, y_hat, n, p)
    return (y ** (1 / n) - y_hat ** (1 / n)) ** p


# Example usage
y = 27
y_hat = 8
n = 3
p = 2

# Calculate and print the error
error = mean_difference_nth_root_error(y, y_hat, n, p)
print("Mean difference nth root error:", error)
