import os
import sys

import numpy as np

# add root into sys.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', '..')))

try:
    from create_train_dataset import create_train_data
except ModuleNotFoundError as e:
    print(f"Error importing module: {e}")
    print("Current sys.path:", sys.path)


train_data = create_train_data()


def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []

    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))

        for j, y_value in enumerate(y_unique):
            for k, x_value in enumerate(x_unique):
                x_and_y = np.sum((train_data[:, i] == x_value) & (
                    train_data[:, -1] == y_value))
                y_count = np.sum(train_data[:, -1] == y_value)
                x_conditional_probability[j, k] = x_and_y / y_count

        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name


if __name__ == "__main__":
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)

    print("Conditional Probabilities:")
    for i, prob in enumerate(conditional_probability):
        print(f"Feature {i + 1}:")
        print(prob)

    print("\nList of Unique Feature Values:")
    for i, names in enumerate(list_x_name):
        print(f"Feature {i + 1}: {names}")
