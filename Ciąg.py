"""Fibonaci

Wypisz ciąg Fibonacciego aż do n-tego wyrazu podanego przez użytkownika.
Ciąg Fibonacciego to ciąg liczb naturalnych, którego każdy wyraz poza dwoma
pierwszymi jest sumą dwóch wyrazów poprzednich.
Początkowe wyrazy tego ciągu to: 0 1 1 2 3 5 8 13 21. Przyjmujemy, że 0 wchodzi w skład ciągu.
Można też to zrobić przy użyciu pętli - iteracyjnie. """

def fib(x):

    if x == 0:
        return 0
    elif x == 1:
        return 1

    return fib(x -2) + fib(x - 1)

if __name__ == '__main__':
    num = int(input('Podaj liczbę początkową: '))
    print(fib(num))# nie bierzemy pod uwagę 0 więc jesli podamy liczbę 4tą to otrzymamy 3