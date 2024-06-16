import os


def count_words_in_file(file_path: str) -> dict:
    word_count = {}

    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")

    # Read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Convert to lowercase
            line = line.lower()
            words = line.split()

            # Count the words
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return word_count


# Test cases:
file_path = 'P1_data.txt'
word_counts = count_words_in_file(file_path)
print(word_counts)
