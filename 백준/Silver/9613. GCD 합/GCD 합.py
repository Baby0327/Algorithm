"""
GCD 합
"""


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


t = int(input())

for i in range(t):
    n = list(map(int, input().split()))[1:]
    result = 0

    for j in range(len(n)):
        for k in range(j + 1, len(n)):
            result += gcd(n[j], n[k])

    print(result)