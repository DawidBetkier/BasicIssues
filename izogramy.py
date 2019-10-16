"""
Izogramy
"""


def is_izogram(word):
    word = word.lower()
    letters = []
    for letter in word:
        if letter in letters:
            return False
        letters.append(letter)
    return True


# def is_izogram_better(word):
# return len(word) == len(set(word))#jezeli dłogsc wyrazu jest równa do ilości literek w set to izogram


if __name__ == '__main__':
    user_word = input('Podaj słowo do sprawdzenia: ')
    if is_izogram(user_word):
        print('Word is izogram')
    else:
        print('Word is not izogram')

    # is_izogram_better(user_word)
