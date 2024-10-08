"""
타임 카드
"""

import sys
input  = sys.stdin.readline

def time(n):
    total = (n[3] * 3600 + n[4] * 60 + n[5]) - (n[0] * 3600 + n[1] * 60 + n[2])
    return [total // 3600, total % 3600 // 60, total % 60]

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

print(*time(a))
print(*time(b))
print(*time(c))