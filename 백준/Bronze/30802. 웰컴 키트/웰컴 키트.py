"""
웰컴 키트
"""

n = int(input())
shirt = list(map(int, input().split()))
t, p = map(int, input().split())
s_count = 0

for i in shirt:
    s_count += (i + t - 1) // t

print(s_count)
print(n // p, n % p)