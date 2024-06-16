import math
import sys

ALPHA_ELU = 0.05


def sigmoid_calculator(x):
    # Calculate sigmoid activation
    return 1 / (1 + math.exp(-x))


def relu_calculator(x):
    # Calculate ReLU activation
    return max(0, x)


def elu_calculator(x):
    # Calculate ELU activation
    if x > 0:
        return x
    else:
        return ALPHA_ELU * (math.exp(x) - 1)


def is_number(x):
    # Check if x is a number
    try:
        float(x)
    except ValueError:
        return False
    return True


def validate_input(func_name, x):
    # Validate the input for function name and x
    if not is_number(x):
        print("x must be a number")
        return False
    if func_name not in {'sigmoid', 'relu', 'elu'}:
        print(f"{func_name} is not supported")
        return False
    return True


def activation_function_calculator(func_name, x):
    # Validate inputs and calculate the activation function result
    validation_error = validate_input(func_name, x)
    if not validation_error:
        sys.exit()

    if func_name == 'sigmoid':
        return sigmoid_calculator(x)
    elif func_name == 'relu':
        return relu_calculator(x)
    elif func_name == 'elu':
        return elu_calculator(x)

    return None


# Example usage
func_name = 'sigmoid'
x = 1.5

# Calculate and print the activation function result
result = activation_function_calculator(func_name, x)
print(f"The result of {func_name} activation for x={x} is {result}")
