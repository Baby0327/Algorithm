for _ in range(int(input())):
    d = int(input())
    n = int(d**0.5)

    if n + n**2 > d:
        print(n - 1)
    else:
        print(n)