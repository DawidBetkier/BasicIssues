if __name__ == '__main__':
    numbers = (1, 2, 3)  # ctrl + shift + strzałki przesuwanie całej linijki
    a, b, c = numbers
    print(a)
    print(b)
    print(c)

    a, _, _ = numbers
    print(a)

    nums = (4, 5, 6, 7, 8, 9)
    new_nums = (nums[0], nums[-1])
    print(new_nums)

    first, *rest, last = nums
    print(first)
    print(rest)
    print(last) #crtl + d powielenie zaznaczonego tekstu

    d = {
        'a': 1,
        'b': 2,
        'c': 3,
    }

    for key, value in d.items():
        print(key)
        print(value)