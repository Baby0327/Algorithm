"""
학생 인기도 측정
"""

import sys
input = sys.stdin.readline

n = int(input())
temp = list(input().strip().split())
name = {}

for i in temp:
    name[i] = 0

for i in range(n):
    like = list(input().strip().split())
    for j in like:
        name[j] += 1

for i, j in sorted(name.items(), key=lambda  x : (-x[1], x[0])):
    print(i, j)