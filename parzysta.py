"""Parzysta"""

def parzyste(numer):
    for i in range(numer):
        if not numer % 2 == 0:
            numer -= 1
        else:
            print(numer)
            numer -= 1

if __name__ == "__main__":
    cyfra = int(input('Podaj liczbę: '))
    parzyste(cyfra)