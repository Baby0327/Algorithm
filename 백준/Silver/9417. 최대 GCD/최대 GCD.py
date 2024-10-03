"""
최대 GCD
"""

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())

for i in range(n):
    m = sorted(list(map(int, input().split())), reverse=True)
    result = 0

    for a in range(len(m)):
        for b in range(a + 1, len(m)):
            result = max(result, gcd(m[a], m[b]))

    print(result)