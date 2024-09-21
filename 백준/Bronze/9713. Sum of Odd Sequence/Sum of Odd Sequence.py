"""
Sum of Odd Sequence
"""

def total(n):
    result = 0
    for i in range(1, n+1, +2):
        result += i
    return result


t = int(input())

for i in range(t):
    print(total(int(input())))