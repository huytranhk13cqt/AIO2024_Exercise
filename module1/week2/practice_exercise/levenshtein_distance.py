def levenshtein_distance(source: str, target: str) -> int:

    # Initialize a matrix to store distances
    source_len, target_len = len(source), len(target)
    distance_matrix = [[0] * (target_len + 1) for _ in range(source_len + 1)]

    # Transformations involving empty strings
    for i in range(source_len + 1):
        distance_matrix[i][0] = i
    for j in range(target_len + 1):
        distance_matrix[0][j] = j

    # Compute distances
    for i in range(1, source_len + 1):
        for j in range(1, target_len + 1):

            if source[i - 1] == target[j - 1]:
                subs_cost = 0
            else:
                subs_cost = 1

            # Update distance matrix
            distance_matrix[i][j] = min(
                distance_matrix[i - 1][j] + 1,       # Deletion
                distance_matrix[i][j - 1] + 1,       # Insertion
                distance_matrix[i - 1][j - 1] + subs_cost  # Substitution
            )

    return distance_matrix[source_len][target_len]


# Test cases
source = "yu"
target = "you"
print(levenshtein_distance(source, target))
