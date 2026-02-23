import sys
input = sys.stdin.readline

p = [[0 for i in range(101)] for j in range(101)]

for b in range(2, 101):
    for m in range(1, 101):
        p[b][m] = p[b - 1][m]

        for a in range(1, b):
            if ((a**2 + b**2 + m) / (a * b)).is_integer():
                p[b][m] += 1

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(p[n - 1][m])