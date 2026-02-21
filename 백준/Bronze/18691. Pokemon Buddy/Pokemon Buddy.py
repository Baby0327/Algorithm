for _ in range(int(input())):
    g, c, e = map(int, input().split())
    print(max((e - c) * (2 * g - 1), 0))