"""liczenie słów"""


def word_count(text):
    """Przelicz słowa"""
    text = text.strip().split(" ")
    word_dict = {}
    for word in text:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict


if __name__ == '__main__':
    user_text = input("Provide a text ")
    print(word_count(user_text))
