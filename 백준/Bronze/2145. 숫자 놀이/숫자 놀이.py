"""
숫자 놀이
"""

while True:
    n = int(input())

    if not n:
        break

    while n >= 10:
        temp = 0

        for i in str(n):
            temp += int(i)

        n = temp

    print(n)