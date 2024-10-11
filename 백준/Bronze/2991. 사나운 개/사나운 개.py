"""
사나운 개
"""

import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
p = list(map(int, input().split()))
result = [0, 0, 0]

for i in range(len(p)):
    if 0 < p[i] % (a + b) <= a:
        result[i] += 1
    if 0 < p[i] % (c + d) <= c:
        result[i] += 1

for i in result:
    print(i)