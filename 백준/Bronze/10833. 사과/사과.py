"""
사과
"""

n = int(input())
result = 0

for i in range(n):
    s, a = map(int, input().split())
    result += a % s

print(result)