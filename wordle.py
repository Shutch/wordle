from collections import defaultdict

def read_word_list(file_name = '5_letter_words.txt'):
    with open(file_name, 'r') as f:
        word_list = f.readlines()

    # cleaning up readlines, comes with \n on the end
    word_list = [w.strip("\n") for w in word_list]
    return word_list

def pick_next_word(word_list, correct_letters, misplaced_letters):
    """Selects the next word given a word list.

    Scores all words in the word list based on the following:
    Each unique letter: +2
    Each misplaced letter: -1
    Each correct letter: -2
    """
    # getting word with all unique letters and no correct letters matching
    # for i in range(5, 0, -1):
    max_score = 0
    max_word = None
    for word in word_list:
        # unique letters
        score = len(set(word)) * 2

        # correct_letters
        for letter, indexes in correct_letters.items():
            for index in indexes:
                if word[index] == letter:
                    score -= 2

        # misplaced letters
        for letter, indexes in misplaced_letters.items():
            if letter in word:
                score -= 1

        if score > max_score:
            max_score = score
            max_word = word

    print(f"Word: {max_word}, Score {max_score}")
    return max_word

def trim_word_list(word_list, absent_letters, correct_letters, misplaced_letters):
    """Reduces the word list to match the current set of criteria.

    First, any word that contains an absent letter is ignored. Then any
    word that doesn't contain at least one instance of each present letter is ignored.
    Then any word that doesn't have the correct letters in the correct locations is
    ignored. Then any word that has a present letter in a known incorrect location is
    ignored.
    
    The valid word list is returned.
    """
    print(f"Word list len: {len(word_list)}")

    # absent letters
    for letter in absent_letters:
        word_list = [w for w in word_list if letter not in w]
    print(f"Word list len: {len(word_list)}")

    for letter, indexes in correct_letters.items():
        for index in indexes:
            word_list = [w for w in word_list if w[index] == letter]
    print(f"Word list len: {len(word_list)}")

    for letter, indexes in misplaced_letters.items():
        for index in indexes:
            word_list = [w for w in word_list if w[index] != letter]
    print(f"Word list len: {len(word_list)}")

    for letter, indexes in misplaced_letters.items():
        word_list = [w for w in word_list if letter in w]
    print(f"Word list len: {len(word_list)}")

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


    absent_letters = ['r', 'i', 's', 'e', 'c', 'u', 'l', 'd', 'h', 'r', 'w']
    correct_letters = {'o':[3]}
    misplaced_letters = {'a':[1], 'o':[1], 't':[0]}
    word_list = trim_word_list(word_list, absent_letters, correct_letters, misplaced_letters)
    word = pick_next_word(word_list, correct_letters, misplaced_letters)
    print(f"Next word: {word}")

    print(word_list)
