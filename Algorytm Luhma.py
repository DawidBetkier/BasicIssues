"""Luhma"""

import sys


def doubledigit(n, double_flag):
    if double_flag:
        doubledigit = 2 * n
        if doubledigit >= 10 :
            total = 1 + doubledigit % 10
        else:
            total = doubledigit
    else:
        total = n
    return total


def calc_total():
    total = 0
    while True:
        prop = input("Enter how many digits you want: ")
        try:
            prop = int(prop)
            break
        except ValueError:
            print("Please enter a number", file=sys.stderr)
    for _ in range(0, prop):
        while True:
            n = input("Enter your digit: ")
            try:
                n = int(n)
                break
            except ValueError:
                print("Please enter a number", file=sys.stderr)
        while True:
            double_flag = input("Enter True or False: ").lower()
            if double_flag in ['true', 'false']:
                double_flag = double_flag == 'true'
                break
        total += doubledigit(n, double_flag)
    return total


def findx(n):
    checkdigit = 10 - n % 10
    if n == 10:
        print("Valid checksum")
    else:
        print("The check digit is", checkdigit)
        n += checkdigit
    return n


if __name__ == "__main__":
    total = calc_total()
    x = findx(total)
    print(x)