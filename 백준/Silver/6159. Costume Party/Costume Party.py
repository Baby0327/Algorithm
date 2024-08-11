"""
Costume Party
"""

import sys

n, s = map(int, sys.stdin.readline().split())
cow = []
result = 0

for i in range(n):
    cow.append(int(sys.stdin.readline()))

cow.sort()
start, end = 0, n-1

while start < end:
    if cow[start] + cow[end] <= s:
        result += (end - start)
        start += 1
    else:
        end -= 1

sys.stdout.write(str(result))