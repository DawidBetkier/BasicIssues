"""FizzBuzz"""


def fizzbuzz(nums):
    for i in range(1, nums):
        if i % 15 == 0:
            print('FIZZBUZZ')
        elif i % 3 == 0:
            print('FIZZ')
        elif i % 5 == 0:
            print('BUZZ')
        else:
            print(i)


if __name__ == '__main__':
    wprowadzenie = int(input('Wprowadz ilość cyfr od 1: '))
    fizzbuzz(wprowadzenie)
