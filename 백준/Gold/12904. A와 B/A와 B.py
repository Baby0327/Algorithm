"""
A와 B
"""

import sys
input = sys.stdin.readline

s = list(map(str, input().strip()))
t = list(map(str, input().strip()))

while len(s) != len(t):
    x = t.pop()

    if x == "B":
        t.reverse()

print(int(s == t))