"""
Cutting Corners
"""

w, h = map(int, input().split())
length = (w**2 + h**2)**0.5

print((w + h) - length)