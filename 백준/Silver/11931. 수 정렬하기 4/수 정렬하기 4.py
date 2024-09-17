"""
수 정렬하기 4
"""

import sys

n = int(sys.stdin.readline())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))

num.sort(reverse=True)

for i in num:
    sys.stdout.write(str(i) + "\n")