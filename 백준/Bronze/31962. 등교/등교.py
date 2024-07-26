"""
등교
"""

n, x = map(int, input().split())
result = -1

for i in range(n):
    s, t = map(int, input().split())

    if s + t <= x:
        result = max(result, s)

print(result)