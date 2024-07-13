"""
2차원 배열의 합

문제 잘 읽자...
"""

import sys

n, m = map(int, sys.stdin.readline().split())
num = []

for i in range(n):
    num.append(list(map(int, sys.stdin.readline().split())))

total = [[0] * (m+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        total[i][j] = num[i-1][j-1] + total[i-1][j] + total[i][j-1] - total[i-1][j-1]

k = int(input())

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(total[x2][y2] - total[x2][y1-1] - total[x1-1][y2] + total[x1-1][y1-1])