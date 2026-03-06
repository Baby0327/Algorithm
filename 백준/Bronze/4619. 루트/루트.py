while 1:
    b, n = map(int, input().split())

    if b == n == 0:
        break

    a = 0

    while a ** n <= b:
        a += 1

    print(a if b - (a - 1)**n > a**n - b else a - 1)