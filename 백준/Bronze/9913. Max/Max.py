import sys
input = sys.stdin.readline

f = {}

for _ in range(int(input())):
    n = int(input())
    f[n] = f.get(n, 0) + 1

print(sorted(f.values())[-1])