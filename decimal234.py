import decimal

def score(m, p, o):
    a = m.keys()
    b = m.values()
    c = m[f'{p}']
    srednia = 0
    j = 0
    for i in c:
        srednia += i
        j += 1
    srednia2 = srednia / j
    print("{0:.2f}".format(srednia2))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    score(student_marks, query_name, n)

    score(student_marks, query_name, n)