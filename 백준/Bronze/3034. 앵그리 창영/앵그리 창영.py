"""
앵그리 창영
"""

n, w, h = map(int, input().split())
maxi = (w**2 + h**2)**0.5

for i in range(n):
    print("DA" if int(input()) <= maxi else "NE")