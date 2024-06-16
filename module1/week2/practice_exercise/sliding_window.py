def max_sliding_window(num_lst: list, size_slide_window: int) -> list:
    result = []

    # Iterate through the list
    for i in range(len(num_lst) - size_slide_window + 1):

        # Get the window
        window = num_lst[i:i + size_slide_window]

        # Append the maximum value to the result
        result.append(max(window))
    return result


# Test cases
print(max_sliding_window([3, 4, 5, 1, -44, 5, 10, 12, 33, 1], 3))
