"""
鉛筆 (Pencils)
"""

n, a, b, c, d = map(int, input().split())
result1 = b * (n // a) if n % a == 0 else b * (n // a + 1)
result2 = d * (n // c) if n % c == 0 else d * (n // c + 1)

print(min(result1, result2))