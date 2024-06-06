import sys


def validate_input(tp, fp, fn):
    for name, value in {'tp': tp, 'fp': fp, 'fn': fn}.items():
        if not isinstance(value, int):
            print(f'{name} must be int')
            return False
        if value <= 0:
            print(f'{name} must be greater than zero')
            return False
    return True


def evaluate_model_f1_score(tp, fp, fn):
    validation_error = validate_input(tp, fp, fn)
    if not validation_error:
        sys.exit()

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    return precision, recall, f1_score
