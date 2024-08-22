"""
파인만
"""

while True:
    n = int(input())

    if not n:
        break

    total = 0

    for i in range(1, n+1):
        total += i**2

    print(total)