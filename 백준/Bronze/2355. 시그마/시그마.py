"""
시그마
"""

a, b = map(int, input().split())
result = (abs(b - a) + 1) * (a + b) // 2

print(result)