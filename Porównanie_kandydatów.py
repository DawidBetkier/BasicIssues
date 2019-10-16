"""porównanie dwóch kandytatów"""


def main():
    sum_points_A = 0
    sum_points_B = 0

    if a > d:
        sum_points_A += 1
    elif a < d:
        sum_points_B += 1
    else:
        sum_points_A += 0
        sum_points_B += 0
    if b > e:
        sum_points_A += 1
    elif b < e:
        sum_points_B += 1
    else:
        sum_points_A += 0
        sum_points_B += 0
    if c > g:
        sum_points_A += 1
    elif c < g:
        sum_points_B += 1
    else:
        sum_points_A += 0
        sum_points_B += 0

    print(sum_points_A)
    print(sum_points_B)


if __name__ == '__main__':
    a, b, c = 4, 5, 6
    d, e, g = 3, 5, 7

    main()
