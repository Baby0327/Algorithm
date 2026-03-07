import sys
input = sys.stdin.readline

n, x, k = map(int, input().split())
b = [0] * (n + 1)
b[x] = 1

for _ in range(k):
    i, j = map(int, input().split())
    b[i], b[j] = b[j], b[i]

print(b.index(1))