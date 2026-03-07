import sys
input = sys.stdin.readline

n, x, k = map(int, input().split())

for _ in range(k):
    i, j = map(int, input().split())

    if i == x:
        x = j
    elif j == x:
        x = i

print(x)