import sys
input = sys.stdin.readline

n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]
total = 0

for i in range(n):
    total += abs(dots[i - 1][0] - dots[i][0]) + abs(dots[i - 1][1] - dots[i][1])

print(total)