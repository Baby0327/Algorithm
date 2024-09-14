"""
Yangjojang of The Year
"""

t = int(input())

for i in range(t):
    n = int(input())
    name = ""
    maxi = 0

    for j in range(n):
        s, l = input().split()
        if int(l) > maxi:
            name = s
            maxi = int(l)

    print(name)