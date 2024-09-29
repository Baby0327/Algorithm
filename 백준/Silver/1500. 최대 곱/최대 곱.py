"""
최대 곱
"""

s, k = map(int, input().split())
num = [s // k] * (k - (s % k)) + [s // k + 1] * (s % k)
result = 1

for i in num:
    result *= i

print(result)