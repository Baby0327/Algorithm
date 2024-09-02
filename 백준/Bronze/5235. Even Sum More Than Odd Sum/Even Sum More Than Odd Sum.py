"""
Even Sum More Than Odd Sum
"""

t = int(input())

for i in range(t):
    num = list(map(int, input().split()))[1:]
    even, odd = 0, 0

    for i in num:
        if i % 2 == 0:
            even += i
        else:
            odd += i

    if even > odd :
        print("EVEN")
    elif even < odd:
        print("ODD")
    else:
        print("TIE")