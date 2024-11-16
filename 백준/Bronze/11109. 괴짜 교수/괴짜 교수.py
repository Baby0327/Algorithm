for i in range(int(input())):
    d, n, s, p = map(int, input().split())

    if n * s < d + n * p:
        print("do not parallelize")
    elif n * s > d + n * p:
        print("parallelize")
    else:
        print("does not matter")