def sum23(numbers):
    """
    Simple exercise
    sum integers in given list except sections starting with 2
    and ending with 3
    Assume each 2 is followed by 3 in given data
    :param numbers:
    :return:
    """
    sum_of_numbers = 0
    can_sum = True
    for num in numbers:
        num = int(num)  # optionally we can move it out of here
        if num == 2:
            can_sum = False
        if num == 3 and not can_sum:
            can_sum = True
            continue
        if can_sum:
            sum_of_numbers += num

    return sum_of_numbers


if __name__ == '__main__':
    """
    TODO: unit test
    """
    test1 = [1, 2, 3]
    print(test1, '->', sum23(test1))

    test2 = [4, 7, 2, 2, 6, 1, 3]
    print(test2, '->', sum23(test2))

    test3 = [1, 2, 3, 7]
    print(test2, '->', sum23(test3))

    user_test = input("Provide numbers splitted by whitespace: ").split(' ')
    user_test = [int(x) for x in user_test]
    print(user_test, '->', sum23(user_test))
