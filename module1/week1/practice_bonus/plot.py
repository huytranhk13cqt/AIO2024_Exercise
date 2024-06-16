import math
import sys

import matplotlib.pyplot as plt
import numpy as np

# Constants for ELU and Swish functions
ALPHA_ELU = 0.05
BETA_SWISH = 1.0


# Sigmoid activation function
def sigmoid_calculator(x):
    return 1 / (1 + math.exp(-x))


# ReLU activation function
def relu_calculator(x):
    return max(0, x)


# ELU activation function
def elu_calculator(x):
    if x > 0:
        return x
    else:
        return ALPHA_ELU * (math.exp(x) - 1)


# Swish activation function
def swish_calculator(x):
    return x / (1 + math.exp(-x * BETA_SWISH))


# Mish activation function
def mish_calculator(x):
    return x * math.tanh(math.log1p(math.exp(x)))


# GELU activation function
def gelu_calculator(x):
    return 0.5 * x * (1 + math.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * math.pow(x, 3))))


# Check if a value is a number
def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


# Validate input for activation function calculation
def validate_input(func_name, x):
    if not is_number(x):
        print("x must be a number")
        return False
    if func_name not in {'sigmoid', 'relu', 'elu', 'swish', 'mish', 'gelu'}:
        print(f"{func_name} is not supported")
        return False
    return True


# Calculate the result of an activation function
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
    elif func_name == 'swish':
        return swish_calculator(x)
    elif func_name == 'mish':
        return mish_calculator(x)
    elif func_name == 'gelu':
        return gelu_calculator(x)

    return None


# Generate values for plotting
x_values = np.linspace(-10, 10, 10000)  # Generates 10000 values from -10 to 10
sigmoid_values = [sigmoid_calculator(x) for x in x_values]
relu_values = [relu_calculator(x) for x in x_values]
elu_values = [elu_calculator(x) for x in x_values]
swish_values = [swish_calculator(x) for x in x_values]
mish_values = [mish_calculator(x) for x in x_values]
gelu_values = [gelu_calculator(x) for x in x_values]

# Plot the activation functions
plt.figure(figsize=(20, 12))

# Plot Sigmoid
plt.subplot(2, 3, 1)
plt.plot(x_values, sigmoid_values, label="Sigmoid", color="blue")
plt.title("Sigmoid Function")
plt.xlabel("x")
plt.ylabel("sigmoid(x)")
plt.grid(True)
plt.legend()

# Plot ReLU
plt.subplot(2, 3, 2)
plt.plot(x_values, relu_values, label="ReLU", color="green")
plt.title("ReLU Function")
plt.xlabel("x")
plt.ylabel("relu(x)")
plt.grid(True)
plt.legend()

# Plot ELU
plt.subplot(2, 3, 3)
plt.plot(x_values, elu_values, label="ELU", color="red")
plt.title("ELU Function")
plt.xlabel("x")
plt.ylabel("elu(x)")
plt.grid(True)
plt.legend()

# Plot Swish
plt.subplot(2, 3, 4)
plt.plot(x_values, swish_values, label="Swish", color="purple")
plt.title("Swish Function")
plt.xlabel("x")
plt.ylabel("swish(x)")
plt.grid(True)
plt.legend()

# Plot Mish
plt.subplot(2, 3, 5)
plt.plot(x_values, mish_values, label="Mish", color="orange")
plt.title("Mish Function")
plt.xlabel("x")
plt.ylabel("mish(x)")
plt.grid(True)
plt.legend()

# Plot GELU
plt.subplot(2, 3, 6)
plt.plot(x_values, gelu_values, label="GELU", color="brown")
plt.title("GELU Function")
plt.xlabel("x")
plt.ylabel("gelu(x)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
