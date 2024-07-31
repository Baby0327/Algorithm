"""
Contest timing
"""

d, h, m = map(int, input().split())
start = 11 * 24 * 60 + 11 * 60 + 11
finish = d * 24 * 60 + h * 60 + m

print(finish - start if finish - start >= 0 else -1)