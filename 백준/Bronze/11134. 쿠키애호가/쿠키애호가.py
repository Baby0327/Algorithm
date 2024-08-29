"""
쿠키애호가
"""

t = int(input())

for i in range(t):
    n, c = map(int, input().split())

    print((n + c - 1) // c)