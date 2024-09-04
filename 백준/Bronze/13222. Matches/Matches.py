"""
Matches
"""

n, w, h = map(int, input().split())
length = (w**2 + h**2)**0.5

for i in range(n):
    num = int(input())

    if num <= length:
        print("YES")
    else:
        print("NO")