import math
import random


def valid_input():
    number_samples_input = input("Enter the number of samples: ")
    if not number_samples_input.isnumeric():
        print("Number of samples must be an integer.")
        return False

    num_samples = int(number_samples_input)

    loss_name = input("Enter the loss name (MAE/MSE/RMSE): ")
    if loss_name not in {'MAE', 'MSE', 'RMSE'}:
        print(f"{loss_name} is not supported.")
        return False

    print(f"Input number of samples (integer): {num_samples}")
    print(f"Input loss name: {loss_name}")

    return num_samples, loss_name


def loss_regression_calculator():
    validation_error = valid_input()
    if not validation_error:
        return
    else:
        values = valid_input()

    num_samples, loss_name = values
    loss = 0

    for _ in range(num_samples):
        y_true = random.uniform(0, 10)
        y_pred = random.uniform(0, 10)
        if loss_name == 'MAE':
            loss += abs(y_true - y_pred)
        elif loss_name in {'MSE', 'RMSE'}:
            loss += (y_true - y_pred) ** 2

    if loss_name == 'MAE':
        loss /= num_samples
    elif loss_name == 'MSE':
        loss /= num_samples
    elif loss_name == 'RMSE':
        loss = math.sqrt(loss / num_samples)

    print("Loss:", loss)


loss_regression_calculator()
