"""Wyznaczanie lat przystępnych"""

def czyPrzestepny(rok):

        return (rok % 4 == 0) and (rok % 100 != 0) or (rok % 400 == 0)

if __name__ == '__main__':
    year = int(input('Podaj rok'))
    czyPrzestepny(year)
