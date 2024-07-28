import os
import sys

import numpy as np

# add root into sys.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', '..')))

try:
    from compute_conditional_probability import compute_conditional_probability
    from compute_prior_probablity import compute_prior_probablity
    from create_train_dataset import create_train_data
except ModuleNotFoundError as e:
    print(f"Error importing module: {e}")
    print("Current sys.path:", sys.path)


def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_features = compute_conditional_probability(
        train_data)

    return prior_probability, conditional_probability, list_features


if __name__ == "__main__":
    train_data = create_train_data()
    prior_probability, conditional_probability, list_features = train_naive_bayes(
        train_data)

    print("Prior Probability:", prior_probability)
    print("Conditional Probabilities:")
    for i, prob in enumerate(conditional_probability):
        print(f"Feature {i + 1}:")
        print(prob)

    print("\nList of Unique Feature Values:")
    for i, names in enumerate(list_features):
        print(f"Feature {i + 1}: {names}")
