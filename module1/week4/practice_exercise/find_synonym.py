import os

import streamlit as st


def load_synonyms(file_path):
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return None

    synonyms = {}
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            word, syns = line.strip().split(':')
            synonyms[word.strip()] = [syn.strip() for syn in syns.split(',')]
    return synonyms


file_path = "data/synonyms.txt"
synonyms = load_synonyms(file_path)
if synonyms is not None:
    print("Loaded synonyms successfully.")
else:
    print("File data not exist.")


def levenshtein_distance(token1, token2):
    distances = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                distances[t1][t2] = min(a, b, c) + 1

    return distances[len(token1)][len(token2)]


def find_closest_synonym(word, syn_list):
    closest_word = None
    min_distance = float('inf')

    for syn in syn_list:
        distance = levenshtein_distance(word, syn)
        if distance < min_distance:
            min_distance = distance
            closest_word = syn

    return closest_word, min_distance


def main():
    st.title("Synonym Finder using Levenshtein Distance")
    keyword = st.text_input('Enter a keyword (e.g., "happy", "sad"):')
    word = st.text_input('Enter a word to find the closest synonym:')

    if st.button("Find Synonym"):
        if keyword in synonyms:
            closest_word, distance = find_closest_synonym(
                word, synonyms[keyword])
            if closest_word:
                st.write(f'The closest synonym for "{word}" in the list of "{
                         keyword}" is: {closest_word} (Distance: {distance})')
            else:
                st.write('No synonyms found.')
        else:
            st.write('Keyword not found in the synonyms list.')

    st.write("Loaded Synonyms:")
    st.write(synonyms)


if __name__ == "__main__":
    main()
