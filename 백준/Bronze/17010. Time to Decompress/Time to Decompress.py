"""
Time to Decompress
"""

l = int(input())

for i in range(l):
    n, x = input().split()

    print(x * int(n))