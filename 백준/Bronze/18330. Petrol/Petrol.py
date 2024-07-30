"""
Petrol
"""

n = int(input())
k = int(input())
sale = 60 + k

if n <= sale:
    result = n * 1500
else:
    result = sale * 1500 + (n - sale) * 3000

print(result)