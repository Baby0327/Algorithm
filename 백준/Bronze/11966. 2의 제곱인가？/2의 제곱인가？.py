"""
2의 제곱인가?
"""

n = int(input())

while True:
    if n % 2 != 0:
        break

    n = n // 2

print("1" if n == 1 else "0")