"""
XMAS
"""

n = int(input())
result = [0] * n

for i in range(n):
    result[int(input()) - 1] = i + 1

for i in result:
    print(i)