"""
거스름돈
"""

n = 1000 - int(input())
result = 0

for i in [500, 100, 50, 10, 5, 1]:
    result += n // i
    n = n % i

print(result)