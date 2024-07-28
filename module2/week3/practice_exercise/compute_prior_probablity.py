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


def compute_prior_probablity(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))

    total_samples = train_data.shape[0]
    play_tennis_column = train_data[:, -1]

    for i, value in enumerate(y_unique):
        prior_probability[i] = np.sum(
            play_tennis_column == value) / total_samples

    return prior_probability


if __name__ == "__main__":
    prior_probability = compute_prior_probablity(train_data)
    print("P(play tennis = No):", prior_probability[0])
    print("P(play tennis = Yes):", prior_probability[1])
