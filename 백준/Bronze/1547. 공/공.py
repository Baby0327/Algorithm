import sys

M = int(sys.stdin.readline())

now = 1
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if now == a:
        now = b
    elif now == b:
        now = a

print(now)