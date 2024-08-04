"""
반지
"""

word = input()
n = int(input())
result = 0

for i in range(n):
    ring = input() * 2

    if word in ring:
        result += 1

print(result)