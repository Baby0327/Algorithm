while 1:
    try:
        a, b, c = map(int, input().split())

        if b - a < c - b:
            print( c - b - 1)
        elif b - a > c - b:
            print(b - a - 1)
        elif  b - a > 0:
            print(b - a - 1)
        else:
            print(0)

    except EOFError:
        break