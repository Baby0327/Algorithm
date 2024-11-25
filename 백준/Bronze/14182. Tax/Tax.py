while 1:
    n = int(input())

    if not n:
        break

    if n > 5000000:
        n *= 0.8
    elif n > 1000000:
        n *= 0.9

    print(int(n))