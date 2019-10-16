"""pukanie sheldona"""

def sheldon(name, n):
    for i in range(n):
        print(f'{name}!')

if __name__ == "__main__":
    user_name = input('Podaj imię: ')
    user_num = int(input('Podaj liczbę: '))
    sheldon(user_name, user_num)
