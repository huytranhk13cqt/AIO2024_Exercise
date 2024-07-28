import os
import sys

import numpy as np

# add root into sys.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', '..')))

try:
    from compute_conditional_probability import compute_conditional_probability
    from create_train_dataset import create_train_data
except ModuleNotFoundError as e:
    print(f"Error importing module: {e}")
    print("Current sys.path:", sys.path)


def get_index_from_value(feature_name, list_features):
    return np.nonzero(list_features == feature_name.strip())[0][0]


if __name__ == "__main__":
    train_data = create_train_data()
    list_features = compute_conditional_probability(train_data)[1]
    feature_name = list_features[0]

    i1 = get_index_from_value("Overcast", feature_name)
    i2 = get_index_from_value("Rain", feature_name)
    i3 = get_index_from_value("Sunny", feature_name)

    print(i1, i2, i3)
