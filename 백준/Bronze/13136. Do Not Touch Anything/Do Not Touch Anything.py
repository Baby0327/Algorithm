"""
Do Not Touch Anything
"""

r, c, n = map(int, input().split())
h = r // n + 1 if r % n else r // n
w = c // n + 1 if c % n else c // n

print(h * w)