def count_chars(words: str) -> dict:
    # Convert to lowercase and sort the characters
    words = words.lower()
    words = sorted(words)
    result = {}

    # Count the characters
    for i in words:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


# Test cases
dict_result = count_chars("smiles")
print(dict_result)
