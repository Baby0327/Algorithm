while 1:
    b, n = map(int, input().split())

    if b == n == 0:
        break

    a = int(b**(1/n))
    print(a + 1 if b - a**n > (a + 1)**n - b else a)