import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
c = list(map(int, input().split()))
bp = [[0] * (sum(c) + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(sum(c) + 1):
        if j < c[i - 1]:
            bp[i][j] = bp[i - 1][j]
        else:
            bp[i][j] = max(bp[i - 1][j], bp[i - 1][j - c[i - 1]] + num[i - 1])

for i in range(len(bp[-1])):
    if bp[-1][i] >= m:
        print(i)
        break