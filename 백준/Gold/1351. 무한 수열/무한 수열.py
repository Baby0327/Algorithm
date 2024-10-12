"""
무한 수열
"""

import sys
input = sys.stdin.readline

def num(n):
    if n not in dic:
        dic[n] = num(n // p) + num(n // q)
    return dic[n]

n, p, q = map(int, input().split())
dic = {0 : 1}

print(num(n))