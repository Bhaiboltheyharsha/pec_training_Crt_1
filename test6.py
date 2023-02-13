if __name__ == '__main__':
    a = []
    b = []
    n = int(input())
    for i in range(n):
        name = input()
        score = float(input())
        a.append([name, score])
        b.append(score)
    a = sorted(a)
    b = sorted(b)
    a.sort()
    b.sort()
    print(a)
    print(b)
    for i in range(n):
        if a[i][1] == b[i]:
            print(a[i][0])
