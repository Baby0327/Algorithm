import sys
input = sys.stdin.readline

n = int(input())
c = [int(input())]

for i in range(n):
    s, e = map(int, input().split())
    c.append(c[-1] + s - e)

print(max(c) if min(c) >= 0 else 0)