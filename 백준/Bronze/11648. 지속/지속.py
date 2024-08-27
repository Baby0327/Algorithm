"""
지속
"""

n = input()
count = 0

while len(n) > 1:
    temp = 1

    for i in n:
        temp *= int(i)

    n = str(temp)
    count += 1

print(count)