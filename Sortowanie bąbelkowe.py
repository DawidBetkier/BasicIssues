"""Sortowanie bąbelkowe"""



def sorting():

    data = [10, 3, 7, 8, 1, 6, 2, 9, 4, 5, 0]

    for i in range(len(data)):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    data.sort()
    print(data)

if __name__ == '__main__':
    sorting()