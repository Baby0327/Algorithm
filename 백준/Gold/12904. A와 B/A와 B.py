"""
A와 B
"""

s = list(input())
t = list(input())

while len(s) != len(t):
    x = t.pop()

    if x == "B":
        t.reverse()

print(int(s == t))