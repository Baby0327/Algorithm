"""
반전 요세푸스
"""

import sys
from collections import deque

input = sys.stdin.readline

n, k, m = map(int, input().split())

num = deque([i+1 for i in range(n)])
i = 0
direction = -(k - 1)

while num:
    if i % m == 0:
        if i and direction == -(k-1):
            direction = k
        else:
            direction = -(k-1)

    num.rotate(direction)
    sys.stdout.write(str(num.popleft())+"\n")
    i += 1