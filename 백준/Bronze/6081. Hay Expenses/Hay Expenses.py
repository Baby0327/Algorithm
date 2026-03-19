import sys
input = sys.stdin.readline

n, q = map(int, input().split())
h = [int(input()) for _ in range(n)]
s = [0, h[0]]

for i in range(1, n):
    s.append(s[-1] + h[i])

for _ in range(q):
    a, b = map(int, input().split())
    print(s[b] - s[a - 1])