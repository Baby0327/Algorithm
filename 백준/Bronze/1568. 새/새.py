"""
새
"""

n = int(input())
i = 1
result = 0

while n:
    if i <= n:
        n -= i
        i += 1
    else:
        n -= 1
        i = 2
    result += 1

print(result)