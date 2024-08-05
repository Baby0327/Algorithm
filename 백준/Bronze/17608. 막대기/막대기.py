"""
막대기
"""

import sys

n = int(sys.stdin.readline())
stick = []
count = 0
maxi = 0

for i in range(n):
    stick.append(int(sys.stdin.readline()))

for i in reversed(stick):
    if i > maxi:
        maxi = i
        count += 1

sys.stdout.write(str(count))