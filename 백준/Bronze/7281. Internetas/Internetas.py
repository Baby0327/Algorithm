"""
Internetas
"""

n = int(input())
num = [0]
result = 0

for i in range(n):
    a, b = map(int, input().split())

    if b:
        num.append(a)
        result = max(result, num[-1] - num[-2])

print(result)