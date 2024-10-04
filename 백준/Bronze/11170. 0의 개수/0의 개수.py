"""
0의 개수
"""

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    result = 0

    for i in range(a, b + 1):
        result += str(i).count("0")

    print(result)