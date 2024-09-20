"""
10!
"""

n = int(input())
total = 1

for i in range(1, n + 1):
    total *= i

print(total // (60 * 60 * 24 * 7))