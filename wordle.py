from collections import defaultdict

def read_word_list(file_name = '5_letter_words.txt'):
    with open(file_name, 'r') as f:
        word_list = f.readlines()

    # cleaning up readlines, comes with \n on the end
    word_list = [w.strip("\n") for w in word_list]
    return word_list

def pick_next_word(word_list, correct_letters, misplaced_letters):
    """Selects the next word given a word list."""
    # getting word with all unique letters and no correct letters matching
    for i in range(5, 0, -1):
        for word in word_list:
            if len(set(word)) == i:
                return word

def trim_word_list(word_list, absent_letters, correct_letters, misplaced_letters):
    """Reduces the word list to match the current set of criteria.

    First, any word that contains an absent letter is ignored. Then any
    word that doesn't contain at least one instance of each present letter is ignored.
    Then any word that doesn't have the correct letters in the correct locations is
    ignored. Then any word that has a present letter in a known incorrect location is
    ignored.
    
    The valid word list is returned.
    """
    # exclude words with absent letters
    for letter in absent_letters:
        word_list = [w for w in word_list if letter not in w]

    # include words with correct letters in the right spots
    for letter, indexes in correct_letters.items():
        for index in indexes:
            word_list = [w for w in word_list if w[index] == letter]

    # exclude words with misplaced letters in the known wrong spot
    for letter, indexes in misplaced_letters.items():
        for index in indexes:
            word_list = [w for w in word_list if w[index] != letter]

    # include words with misplaced letters in unknown spots
    for letter, indexes in misplaced_letters.items():
        word_list = [w for w in word_list if letter in w]

    return word_list

def update_list_with_list(l, vals):
    l += vals
    return l

def update_dict_with_dict(d, vals):
    for key, value in vals.items():
        if key in d:
            d[key] += value
        else:
            d[key] = value
    return d

if __name__ == "__main__":
    word_list = read_word_list('5_letter_words_knuth.txt')
    absent_letters = []
    correct_letters = {}
    misplaced_letters = {}

    word = pick_next_word(word_list, correct_letters, misplaced_letters)
    print(f"Next word: {word}")

    absent_letters = ['t', 'h', 'i', 'r', 'p' ,'l', 'c', 's', 'k', 'd', 'x', 'm', 'n']
    correct_letters = {'a':[0], 'e':[3]}
    misplaced_letters = {'e':[2,4], 'a':[2]}
    word_list = trim_word_list(word_list, absent_letters, correct_letters, misplaced_letters)
    print(f"Word list len: {len(word_list)}")
    word = pick_next_word(word_list, correct_letters, misplaced_letters)
    print(f"Next word: {word}")

    print(word_list)
