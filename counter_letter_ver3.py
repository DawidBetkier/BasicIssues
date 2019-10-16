"""zliczacz liter
defaultdict
"""
from collections import Counter


def counter_letter_v3(text: str) -> dict:
    return Counter(text)


if __name__ == '__main__':
    print(counter_letter_v3('Ala ma kota'))
    print(counter_letter_v3('Ala ma kota').most_common(2))
