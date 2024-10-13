"""
5의 수난
"""

import sys
input = sys.stdin.readline

n = input().strip()
result = 0

for i in n:
    result += int(i) ** 5

print(result)