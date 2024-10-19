"""
디지털 루트
"""

while True:
    n = int(input())

    if not n:
        break

    while n >= 10:
        temp = 0
        for i in str(n):
            temp += int(i)
        n = int(temp)

    print(n)