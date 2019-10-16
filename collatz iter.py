"""Collatz Algorithm solutio"""

def collatz(x):
    """Iterative version"""
    while True:
        print(x)
        if x == 1:
            break #po break zakończy ale wykona ostatnią funkcję a po return zakańcza i jużnic nie wykonuje
        elif x % 2 != 0:
            x = x * 3 + 1
        else:
            x = x // 2

    print('Zakończyłem')

if __name__ =='__main__':
    number = int(input('Provide number: '))
    collatz(number)