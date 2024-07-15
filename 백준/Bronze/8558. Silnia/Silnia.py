"""
Silnia
"""

n = int(input())
result = 1

for i in range(n):
    result *= i+1

print(str(result)[-1])