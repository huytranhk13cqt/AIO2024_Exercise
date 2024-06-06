import math
import sys

ALPHA_ELU = 0.05


def sigmoid_calculator(x):
    return 1 / (1 + math.exp(-x))


def relu_calculator(x):
    return max(0, x)


def elu_calculator(x):
    if x > 0:
        return x
    else:
        return ALPHA_ELU * (math.exp(x) - 1)


def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


def validate_input(func_name, x):
    if not is_number(x):
        print("x must be a number")
        return False
    if not (func_name == 'sigmoid' or func_name == 'relu' or func_name == 'elu'):
        print(f"{func_name} is not supported")
        return False
    return True


def activation_function_calculator(func_name, x):
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
