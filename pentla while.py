"""wykorzystanie pentli while"""

def odliczanie(com1, number, com2):
    print(com1)
    while number:
        print(number)
        number -= 1
    print(com2)

if __name__ == '__main__':
    user_start = input('Podaj komendę startową: ')
    user_num = int(input('Podaj liczbę początkową: '))
    user_stop = input('Podaj komendę końcową: ')
    odliczanie(user_start, user_num, user_stop)
