"""Szafa"""

from collections import namedtuple


class Szafa:
    def __init__(self, wysokosc, szerokosc, glebokosc):
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        self.glebokosc = glebokosc


if __name__ == '__main__':
    szafa1 = namedtuple('Szafa', ('szer', 'wys', 'gle'))
    szafa = Szafa(2, 3, 4)

    print(szafa.szerokosc)
    print(szafa.szerokosc)
    print(szafa.glebokosc)
