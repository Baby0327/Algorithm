import sys
input = sys.stdin.readline

n, m = map(int, input().split())
f = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    f[a - 1] += 1
    f[b - 1] += 1

print("\n".join(map(str, f)))