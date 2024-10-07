"""
Speed Limit
"""

import sys
input = sys.stdin.readline

while True:
    n = int(input())
    temp = 0
    result = 0

    if n == -1:
        break

    for i in range(n):
        s, t = map(int, input().split())
        result += s * (t - temp)
        temp = t

    sys.stdout.write(str(result) + " miles\n")