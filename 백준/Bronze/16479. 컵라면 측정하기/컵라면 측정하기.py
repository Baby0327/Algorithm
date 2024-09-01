"""
컵라면 측정하기
"""

k = int(input())
d = sorted(list(map(int, input().split())))

print(k**2 - ((max(d) - min(d)) / 2 )**2)