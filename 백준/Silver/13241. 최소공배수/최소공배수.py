import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


num = list(map(int, sys.stdin.readline().rstrip().split()))
num.sort(reverse=True)
print(num[0] * num[1] // gcd(num[0], num[1]))