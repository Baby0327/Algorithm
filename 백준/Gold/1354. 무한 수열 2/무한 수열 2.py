"""
무한 수열 2
"""

import sys
input = sys.stdin.readline

def num(n):
    if n <= 0:
        return 1
    elif n not in dic:
        dic[n] = num(n // p - x) + num(n // q - y)
        
    return dic[n]

n, p, q, x, y = map(int, input().split())
dic = {}

print(num(n))