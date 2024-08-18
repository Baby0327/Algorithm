"""
Generations of Tribbles
"""

t = int(input())
num = [1, 1, 2, 4]

for i in range(t):
    n = int(input())
    while len(num) <= n:
        num.append(num[-4] + num[-3] + num[-2] + num[-1])

    print(num[n])