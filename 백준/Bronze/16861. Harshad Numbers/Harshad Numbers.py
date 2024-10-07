"""
Harchad Numbers
"""

n = int(input())

while True:
    num = 0

    for i in str(n):
        num += int(i)

    if not int(n) % num:
        print(n)
        break
    else:
        n += 1