m, s, x1, x2 = map(int, input().split())
b = 0

for a in range(0, m):
    for c in range(0, m):
        if (a * s + c) % m == x1 and (a * x1 + c) % m == x2:
            print(a, c)
            b = 1
            break
    if b:
        break