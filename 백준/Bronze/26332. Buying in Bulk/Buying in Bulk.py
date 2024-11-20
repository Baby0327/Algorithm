for i in range(int(input())):
    c, p = map(int, input().split())
    print(c, p)
    print(c * p - (c - 1) * 2 *  int(c > 1))