"""
Oddities
"""

n = int(input())

for i in range(n):
    num = int(input())

    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")