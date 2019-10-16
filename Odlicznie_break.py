"Start rakiety"


def odliczanie(number):
    while number:
        print(number)
        number -= 1
        if number == 5:
            break
    print('Lecimy!')


if __name__ == '__main__':
    liczba = int(input('Podaj liczbę: '))

    odliczanie(liczba)
