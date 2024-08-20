"""
전체 계산 횟수
"""

n, m = map(int, input().split())
total = 0

while n != 0:
    total += n
    n //= m

print(total)