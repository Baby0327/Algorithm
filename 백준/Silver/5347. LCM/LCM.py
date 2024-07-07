"""
LCM
"""

def gcd(a, b):
    while True:
        a, b = b, a % b
        if b == 0:
            return a


n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))