"""
경기 결과
"""

import sys

n = int(sys.stdin.readline())
A = 0
B = 0

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if a > b:
        A += 1
    elif a < b:
        B += 1

print(A, B)