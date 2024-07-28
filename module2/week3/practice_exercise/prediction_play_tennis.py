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
    from get_index_from_value import get_index_from_value
    from train_naive_bayes import train_naive_bayes
except ModuleNotFoundError as e:
    print(f"Error importing module: {e}")
    print("Current sys.path:", sys.path)


def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])

    # Tính xác suất hậu nghiệm cho lớp 'No' và 'Yes'
    p_no = prior_probability[0] * conditional_probability[0][0, x1] * conditional_probability[1][0,
                                                                                                 x2] * conditional_probability[2][0, x3] * conditional_probability[3][0, x4]
    p_yes = prior_probability[1] * conditional_probability[0][1, x1] * conditional_probability[1][1,
                                                                                                  x2] * conditional_probability[2][1, x3] * conditional_probability[3][1, x4]

    if p_no > p_yes:
        y_pred = 0  # 'no'
    else:
        y_pred = 1  # 'yes'
    return y_pred


if __name__ == "__main__":
    train_data = create_train_data()
    prior_probability, conditional_probability, list_x_name = train_naive_bayes(
        train_data)

    # Prediction for D11: (Sunny, Cool, High, Strong)
    X_test = ['Sunny', 'Cool', 'High', 'Strong']
    prediction = prediction_play_tennis(
        X_test, list_x_name, prior_probability, conditional_probability)

    print(f"Prediction for {X_test}: {prediction}")
